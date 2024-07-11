<pre>
  <B>Disclaimer</B>
  Anything you do to your own pwnagotchi is on you.  I'm not responsible if you mess something up.  That said, I've personally done this script and it works.
  Also... If anyone is willing to get all this set up for a plugin and set up a zip to automatically install everything, let me know.  I'm just too lazy as I've already typed this up and accidentally deleted it, so I'm done after typing it again lol.

  Ok, so we're going to do this in steps.  Sometimes it may not make sense when I say to do something, but it'll all make sense in the end.  I just need to get there.

  <B>Step 1</B>
  So the first thing we're going to do is download the files we're going to need for this.<br>
  _________________________________________________________
  sudo apt install msmtp msmtp-mta
  sudo apt install mailutils
  sudo apt install mpack
  __________________________________________________________<br>

  Now that we have the files that we need, we're going to start setting things up to be able to use them.

  <B>Step 2</B>
  First, we need to get to the correct folder.
  __________________________________________________________
  cd /etc/
  __________________________________________________________<br>
  Then, we're going to create a file.
  __________________________________________________________
  sudo nano msmtprc
  __________________________________________________________<br>
  Now that we're in here, let's write the code.  Try to type it as close to this as you can.  I'm sure some spacing won't make too much of a difference.
  __________________________________________________________
  account          gmail
  host             smtp.gmail.com (you can use other providers here, I'll list some after this)
  port             587 (This is going to be the same for all providers)

  from             BThomas22x@gmail.com (you can put anything here, I just used my email)
  user             your-gmail-address@gmail.com (or whatever provider you're using)
  password         your-password (for gmail, you'll probably have to set up an app password. Settings, security, and search for "app password" and create one)

  #default
  account default  gmail (or whatever you set up)
  ___________________________________________________________<br>
  Hit ctrl+x to save (press y) and then hit enter to keep the name.
  
  Other providers are:
  Yahoo      smtp.mail.yahoo.com
  Outlook    smtp.office365.com
  AOL        smtp.aol.com
  Zoho       smtp.zoho.com

  I'm sure you get the idea...
  
  Now we can test it from here. Let's go home first just to get back to the start.  Usually the home folder is pi, but if you're unsure, type "cd /home" and then type "ls" and you'll see the name of your home folder.
  ___________________________________________________________
  cd /home/pi
  ___________________________________________________________
  Now that we're back home, let's go ahead and test our script to make sure we've set it up correctly.  Just type:
  ___________________________________________________________
  echo "Test message" | msmtp destination-email@gmail.com
  ___________________________________________________________
  Or, to add a subject line...
  ___________________________________________________________
  echo "Test message" | mail -s "Subject" destination-email@gmail.com 
  ___________________________________________________________<br>
  Just hit enter to send it, and wait a minute.  An email should soon be in your inbox if all goes well.

  <B>Step 3</B>
  Now that we have it set up to send the email, we can write a script to send the files.  For this, we're going to have to create a folder to store files that we've already transferred so we don't transfer them again.

  ____________________________________________________________
  cd /root
  sudo mkdir savedhs (you can name the folder anything you want, I just named it savedhs for "saved handshakes"... clever, I know.)
  ____________________________________________________________
  Now that the folder is created, we need to create the script that's going to do all the magic.  It's going to go through the handshakes folder, and email the files to your email, and then transfer the files to the new folder we just created, so they don't get transferred again.  And we're going to set it up to check for new files every 30 mintes.  You can actually make your own time table up, and I'll tell you how to do that then.  But first, we need to set up the script...

  ____________________________________________________________
  cd /home/pi/scripts (or whatever your home folder is)
  sudo nano send_files.sh (we're creating this, so the file will be empty.  Feel free to name it whatever you want, as long as it has .sh at the end)
  ____________________________________________________________
  Now that we have the editor up, let's go ahead and put our script in it...
  ____________________________________________________________
  #!/bin/bash
  #to just email all files, remove the .22000 and just leave the *
  for file in /root/handshakes/*22000; do 
  if [ -f "$file" ]; then
    mpack -s "New Handshakes" -d <(echo "A new file has been captured and sent: $(basename "$file")") "$file" destination-email@gmail.com

      if [ $? -eq 0 ]; then
        sudo mv "$file" /root/savedhs
        echo "Sent and moved: $file"
      else
        echo "Failed to send: $file"
      fi
  fi
done
___________________________________________________________________
Now just hit ctrl+x to save (press y), and hit enter to keep the name.  But since it's a bash script, we have to make it executable.
___________________________________________________________________
sudo chmod +x send_files.sh
___________________________________________________________________

Now we just have to set up the cron job and we're ready to go.  So we're going to go home again.  It's just good practice to go home again.

___________________________________________________________________
cd /home/pi
___________________________________________________________________
Now that we're home, lets set up the job.  One of the first things you need to know about cron is the format it's set up in.  It's formatted by Minute, Hour, Day of Month, Month, Day of Week, and CMD.  Each one gets a selection, or a *.  A * means it doesn't have a specific number, just any time it's set up to run. So a quick example is...
      */30**** /home/pi/scripts/send_files.sh -- The */30 means every 30 minutes.  If you just put 30, it will be every 30 minute mark.  1:30, 2:30, 3:30 etc.  The / is important for making sure it's every 30 minutes.  Or you could do **/2*** which is every two hours.  Or take away the / and it'll send every day at 2.  You get the idea on how to set it up now. So now lets go ahead and set up our job...
____________________________________________________________________
crontab -e
____________________________________________________________________
Go ahead and scroll all the way to the bottom, and under everything else, we're going to type what I typed earlier...
____________________________________________________________________
*/30**** /home/pi/scripts/send_files.sh (or whatever you named your script)
____________________________________________________________________
And that's it.  You're now set up for every half hour to email the .pcap or .22000 files to yourself, and then it'll move the files it emailed to you to the savedhs folder so they aren't deleted and you can still refer to them if need be.  Hopefully this was easy to follow, and you're now receiving the emails.  If you set it up like I did for every 30 minutes, you should recieve them at :00 and :30, so if you don't see them right away, remember, we set it up for every 30 minutes (or longer if you choose to).

If this worked for you, feel free to buy me a coffee.
<a href="paypal.me/BThomas22x">Buy me a coffee!</a>

  
</pre>
