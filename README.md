# SMTP Email Verification Script

## Description

This Python script verifies the existence of an email address across a specified IP range using the SMTP `VRFY` command. The script first checks if port 25 is open on each host within the given CIDR IP range. If the port is open, it then proceeds to verify the specified email address on that host.

Please note that the effectiveness of this script is dependent on the SMTP server's configuration and its response to the `VRFY` command. Some servers may not respond or may provide limited information as a spam prevention measure.

## Requirements

- Python 3.x
- Internet connection
- Access to SMTP servers within the specified IP range

## Installation

No additional installation is required, as the script uses Python's standard libraries.

## Usage

Run the script from the command line, providing the CIDR IP range, port, and email address as arguments:

```bash
python script_name.py --cidr <cidr_ip_range> --port <smtp_server_port> --email <email_address_to_verify>
````
