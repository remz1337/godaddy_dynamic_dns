#!/usr/bin/python
import sys, argparse, logging, pif, smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

#Define constant parameters
logfile="update_ip.log"
smtpserver="gatorXYZ.hostgator.com"
smtpport=465
smtpuser="me@mydomain.com"
smtppassword="myemailpassword"
sender="me@mydomain.com"
to="me@mydomain.com"

#email function
def email_update(body):
        global smtplib
        msg = MIMEText(body)
        msg['From'] = sender
        msg['To'] = to
        msg['Subject'] = 'IP address updater'
        s = smtplib.SMTP_SSL(smtpserver,smtpport)
        s.login(smtpuser,smtppassword)
        s.sendmail(sender, to, msg.as_string())
        s.quit()

last_ip="0.0.0.0"
def read_last_ip():
        last_ip_f=open("last_ip.txt","r")
        last_ip=last_ip_f.read()
        last_ip_f.close()
        return last_ip

def write_new_ip(ip):
        new_ip_f=open("last_ip.txt","w")
        new_ip_f.write(ip)
        new_ip_f.close()

#command line arguments parsing
parser = argparse.ArgumentParser('A Python script to notify when public IP changes')
parser.add_argument('-v', '--verbose', action='store_true', help="send emails on 'no ip update required'")
args = parser.parse_args()

#start log file
logging.basicConfig(filename=logfile, format='%(asctime)s %(message)s', level=logging.INFO)

#define last IP
try:
        last_ip=read_last_ip()
except:
        logging.warning("unable to read last IP. Creating file last_ip.txt")
        write_new_ip(last_ip)

#what is my public ip?
public_ip = pif.get_public_ip()
logging.info("My ip: {0}".format(public_ip))

#Check if changed
if last_ip != public_ip:
        logging.info("Update required: old {0}, new {1}".format(last_ip, public_ip))
        updateinfo = "old " + last_ip + ", new " + public_ip
        # This will fail if you try to set the same IP as already registered!
        email_update("Need manual update OK!\n"+updateinfo)
        write_new_ip(public_ip)
else:
        logging.info('Public IP did not change.')
        if args.verbose:
                email_update('No update required.')
