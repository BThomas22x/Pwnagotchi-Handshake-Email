# Pwnagotchi-Plugins
Custom plugins I've created for Pwnagotchi - !!Currently in testing phase!!

NOTE: Handymail will email you after every captured handshake.  I still have to test if it will send converted files after they've been converted, or if the next time it sends, if it'll send them then.  Feel free to edit any of these to suit your needs.

<B><U>Handymail</B></U><br>
edit your config.toml file with these settings:<br>

main.plugins.Handymail.enabled = true<br>
main.plugins.Handymail.to_addr = "recipient@example.com" (Put your own address in here to email to yourself.  Or to another email if you need to send to another for some reason.)<br>
main.plugins.Handymail.from_addr = "your_email@example.com"<br>
main.plugins.Handymail.smtp_server = "smtp.example.com" (eg. smtp.gmail.com)<br>
main.plugins.Handymail.smtp_port = 587 (This can be changed if necessary - 465, 587)<br>
main.plugins.Handymail.smtp_user = "your_email@example.com"<br>
main.plugins.Handymail.smtp_pass = "your_password"<br><br>

<B><U>Pwncord</B></U><br>
for this to work, you must have hcxpcapngtool, so first do:<br>
sudo apt-get install hcxtools<br>
then do<br>
sudo chmod ug+x /usr/bin/hcxpcapngtool<br><br>

Then, you need to edit the config.toml:<br>
main.plugins.pwncord.enabled = true<br>
main.plugins.pwncord.discord_token = 'YOUR_DISCORD_BOT_TOKEN'<br>
main.plugins.pwncord.channel_id = 'YOUR_DISCORD_CHANNEL_ID'<br><br>

Then, go to the discord Developer portal, create a new application, and add a bot to it.  Copy the bot token and add it to config.toml. Then invite the bot to your server and do any and all permissions you want to do with it.  Finally, restart your pwnagotchi to load the new plugin.<br>
sudo systemctl restart pwnagotchi<br><br>




