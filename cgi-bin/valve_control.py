#!/usr/bin/python

import cgi
import cgitb; cgitb.enable(display=0, logdir="/path/to/logdir")
import sys
import pigpio
import json
from time import sleep

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

file = open("busy.json")
busy = json.load(file)

print "<title>Auto-Bartender</title>"
print "</head>"
print "<body>"

if busy["busy"] == "true":
	print """
    <div style="margin-left:40px; margin-right:5%%; font-size:18px; font-family:Hoefler Text, 'Times New Roman';">
        <p>The auto-bartender is already making an order! Please re-order when it is not busy!<p>
    <div>
	"""
else:
	print """
		<div style="margin-left:40px; margin-right:5%%; font-size:18px; font-family:Hoefler Text, 'Times New Roman';">
			<p>Your order is now complete!<p>
		<div>
	"""

print "</body>"
print "</html>"


if busy["busy"] == "false":
	busy["busy"] = "true"
	json.dump(busy, file)
	
	io = pigpio.pi()
	io.write(18, 1)
	sleep(2)
	io.write(18, 0)
	busy["busy"] = "false":
	json.dump(busy, file)
	file.close()


