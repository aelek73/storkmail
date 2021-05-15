## StorkMail

Simple mail forwarder in Python

Currently supported:
- IMAP over TLS with port 143 
- SMTP over SSL with port 465
- One IMAP and SMTP connection
- Mark forwarded mail as `SEEN`

ToDo:
- IMAP SSL
- SMTP TLS
- Custom ports
- Multiple configuration managing
- Logging
- Forwarded mails marking
- Use one SMTP for more IMAP connection

## Usage
1. Rename `config_example.yaml` to `config.yaml` and edit configuration.
2. Start Storkmail with `./main.py` command
