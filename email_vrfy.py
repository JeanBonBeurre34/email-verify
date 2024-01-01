import socket
import sys
import argparse

def verify_email(server, port, email):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        s.connect((server, port))

        # Receive the greeting message
        recv = s.recv(1024).decode()
        print("Server:", recv)
        if not recv.startswith('220'):
            raise Exception('220 reply not received from server.')

        # Send HELO command and print server response
        helo_command = 'HELO Alice\r\n'
        s.send(helo_command.encode())
        recv = s.recv(1024).decode()
        print("Server:", recv)
        if not recv.startswith('250'):
            raise Exception('250 reply not received from server.')

        # Send VRFY command
        vrfy_command = f'VRFY {email}\r\n'
        s.send(vrfy_command.encode())
        recv = s.recv(1024).decode()
        print("Server:", recv)

        # Close the socket
        s.close()
        
        return recv
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Verify an email address using SMTP.')
    parser.add_argument('--server', type=str, required=True, help='SMTP server address')
    parser.add_argument('--port', type=int, default=25, help='SMTP server port (default: 25)')
    parser.add_argument('--email', type=str, required=True, help='Email address to verify')

    args = parser.parse_args()

    response = verify_email(args.server, args.port, args.email)
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
