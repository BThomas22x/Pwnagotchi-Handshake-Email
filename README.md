# Pwnagotchi-Plugins
Custom plugins I've created for Pwnagotchi

NOTE: Handymail will email you after every captured handshake.  I still have to test if it will send converted files after they've been converted, or if the next time it sends, if it'll send them then.  Feel free to edit any of these to suit your needs.

Handymail script<br>
edit your config.toml file with these settings:<br>

main.plugins.email_handshakes.enabled = true<br>
main.plugins.email_handshakes.to_addr = 'recipient@example.com' (Put your own address in here to email to yourself.  Or to another email if you need to send to another for some reason.)<br>
main.plugins.email_handshakes.from_addr = 'your_email@example.com'<br>
main.plugins.email_handshakes.smtp_server = 'smtp.example.com' (eg. smtp.google.com)<br>
main.plugins.email_handshakes.smtp_port = 587 (This can be changed if necessary)<br>
main.plugins.email_handshakes.smtp_user = 'your_email@example.com'<br>
main.plugins.email_handshakes.smtp_pass = 'your_password'<br>


