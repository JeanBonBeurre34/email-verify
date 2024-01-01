import socket
import sys
import argparse
import ipaddress

def is_port_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)  # Set timeout to avoid long waiting periods
        try:
            s.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False

def verify_email(server, port, email):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        s.connect((server, port))

        # Receive the greeting message
        recv = s.recv(1024).decode()
        print(f"Server ({server}):", recv)
        if not recv.startswith('220'):
            raise Exception('220 reply not received from server.')

        # Send HELO command and print server response
        helo_command = 'HELO Alice\r\n'
        s.send(helo_command.encode())
        recv = s.recv(1024).decode()
        print(f"Server ({server}):", recv)
        if not recv.startswith('250'):
            raise Exception('250 reply not received from server.')

        # Send VRFY command
        vrfy_command = f'VRFY {email}\r\n'
        s.send(vrfy_command.encode())
        recv = s.recv(1024).decode()
        print(f"Server ({server}):", recv)

        # Close the socket
        s.close()

        return recv
    except Exception as e:
        print(f"Error with server {server}: {e}")
        return None

def verify_email_in_range(cidr, port, email):
    network = ipaddress.ip_network(cidr, strict=False)
    for ip in network.hosts():
        ip_str = str(ip)
        print(f"Checking port {port} on {ip_str}...")
        if is_port_open(ip_str, port):
            print(f"Port {port} is open on {ip_str}. Verifying {email}...")
            response = verify_email(ip_str, port, email)
            if response:
                print(f"Response from {ip_str}: {response}")
        else:
            print(f"Port {port} is not open on {ip_str}. Skipping.")

def main():
    parser = argparse.ArgumentParser(description='Verify an email address across an IP range using SMTP.')
    parser.add_argument('--cidr', type=str, required=True, help='CIDR range of IPs to check (e.g., 192.168.1.1/24)')
    parser.add_argument('--port', type=int, default=25, help='SMTP server port (default: 25)')
    parser.add_argument('--email', type=str, required=True, help='Email address to verify')

    args = parser.parse_args()

    verify_email_in_range(args.cidr, args.port, args.email)

if __name__ == "__main__":
    main()
