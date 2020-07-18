# Mailpl0it

Mailpl0it is a small utility that hunts the homepage of [exploit-db](https://www.exploit-db.com/) looking for user supplied quer(y/ies) and notifies the user via email if an exploit is found for the supplied query.

Please note that the utility has only been made for Gmail inboxes. Since the utility uses Python to send emails, so in order to receive emails on the mailbox - the user will have to toggle [this](https://myaccount.google.com/lesssecureapps) switch.

Please refer the "Points to note" section below for more details.

_________________________

Mailpl0it was made:
- To get notified only for user-specified, specific class of exploits on the mailbox.
-  Out of pure curiosity while playing around with the requests library (Already aware of exploit-db's [RSS](https://www.exploit-db.com/rss.xml) feed, still, import requests, because why not!). 


## Installation

Built on native libraries with zero dependencies.
Clone and launch!

```bash
git clone https://github.com/bad-bit/mailpl0it.git
```
## Usage

```
python mailpl0it.py -l "Remote Code Execution, Citrix, Privilege Escalation" -m mailid@gmail.com
```
![alt text](https://github.com/bad-bit/mailpl0it/blob/master/terminal.jpg?raw=true)

> OUTPUT in the mailbox.

![alt text](https://github.com/bad-bit/mailpl0it/blob/master/OP.jpg?raw=true)
___
```

> Help message:

mailpl0it.py [-h] -l WORDLIST [-s SLEEPTIME] -m EMAIL [-p PASSWORD]

optional arguments:
  -h, --help            show this help message and exit
  -l WORDLIST, --list WORDLIST
                        Comma seperated words to hunt on exploit-db. Example:
                        mailpl0it.py -l "LPR, RCE"
  -s SLEEPTIME, --sleep SLEEPTIME
                        Time to sleep in seconds before checking exploit-db
                        for new results. Default is 3600s / 1 hour.
  -m EMAIL, --email EMAIL
                        Your email-id to receive notification emails.
  -p PASSWORD, --password PASSWORD
                        Your email-id's password.
```
It is recommended to launch the utility from a tmux or a Byobu session on a VPS for a seamless experience and infinite hunting! :D

# Points to note
- Since the utility relies on the native "email.message" library, it is inevitable to avoid using password for authentication to the mailing server. 
The user will have to either pass the recipient email's password as an argument (-p) or for the more paranoid ones - hardcode the credentials of the recipient email by editing a single line (line 130) inside the script. It is recommended to create a throwaway account for this utility which you can dedicate only for this purpose without having to worry about harcoding your credentials in clear text! :D

- The utility has been tested only on Gmail. By default, Gmail doesn't allow Python to send emails to your mailbox. The user can however manually enable it by visiting [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps). This setting can't be enabled for accounts having 2FA. Again, it is recommended to create a throwaway account for this utility which you can dedicate only for this purpose without having to worry about harcoding your credentials in clear text! :D


## License
[MIT](https://choosealicense.com/licenses/mit/)
