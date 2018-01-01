manual_dynamic_dns
===================

Simple Python script to update a Hostgator DNS hosted domain name, like DDNS
This script will find your real ip address, and notify you if it changed.
Thus, you have to manually edit your hostgator zone file.

You will be emailed if changed are made (or optionally (-v) any time the script
runs.)

Note: author assumes no responsibility for the Hostgator User Agreement.
You will need to figure out for yourself if this is acceptible or not.


License:
--------
See the included LICENSE file


Requirements:
-------------

- Python v2.7  (not tested in 3.x)
- The following added modules:
  logging, pif, smtplib, email.mime.text 

Installation:
-------------

- run the script from the command line,  "python update_ip.py"
  It should create a log file with output. Check to make sure all works.
- now automate as needed, using cron, or whatever your environment needs
- on Linux, you can run this without using the 'python' prefix by making
  the script executable (chmod +x). Check your python path and the file
  update_ip.py if this does not work.

Options:
--------
run  'python update_ip.py -h' to see options.

