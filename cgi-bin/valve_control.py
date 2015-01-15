import cgi
import cgitb; cgitb.enable(display=0, logdir="/path/to/logdir")
import sys
import RPi.GPIO as io
from time import sleep
io.setmode(io.BCM)

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print """
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="Description" content="Site for the auto bartender">
    <link rel="stylesheet" type="text/css" href="../style.css">
"""
# Create instance of FieldStorage 
form = cgi.FieldStorage()
order = form.getvalue('drink')

print "<title>WikiBot Results</title>"
print "</head>"
print "<body>"

print """
    <div style="margin-left:40px; margin-right:5%%; font-size:18px; font-family:Hoefler Text, 'Times New Roman';">
        <p>Your order %s is now being made!<p>
    <div>
""" % order

print "</body>"
print "</html>"

v1 = 18

io.setup(v1, io.OUT)

io.output(v1, True)

