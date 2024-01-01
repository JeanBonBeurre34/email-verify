# SMTP Email Verification Script

## Description

This Python script verifies the existence of an email address using the SMTP `VRFY` command. It establishes a connection to an SMTP server and sends a verification request for a specified email address. 

Please note that the effectiveness of this script is dependent on the SMTP server's configuration and its response to the `VRFY` command. Some servers may not respond or may provide limited information as a spam prevention measure.

## Requirements

- Python 3.x
- Internet connection
- Access to an SMTP server

## Installation

No additional installation is required, as the script uses Python's standard libraries.

## Usage

Run the script from the command line, providing the SMTP server, port, and email address as arguments:

```bash
python script_name.py --server <smtp_server_address> --port <smtp_server_port> --email <email_address_to_verify>
````
