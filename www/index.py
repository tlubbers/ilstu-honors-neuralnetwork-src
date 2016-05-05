#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgi
import cgitb
cgitb.enable()


# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
county_name = form.getvalue('county_name')
state_name  = form.getvalue('state_name')
if form.getvalue('party'):
	party = form.getvalue('party')
else:
	party = "No party yet"
print ('''
  <head><meta http-equiv="refresh" content="0;URL='main.html'" /></head>
''')

#print "Content-type:text/html\r\n\r\n"
#print
#"""<html>
#	<head>
#		<title>Predict county election results.</title>
#	</head>
#   <body>
#"""
#print "<h2>County, State, Party: %s %s %s</h2>" % (county_name, state_name, party)
#print """<form action="index.py" method="POST">
#		County:<input type="text" name="county_name"><br />
#		State: <input type="text" name="state_name" /><br />
#		<input type="radio" name="party" value="Republican" /> Republican
#		<input type="radio" name="party" value="Democrat" /> Democrat
#		<input type="submit" value="Submit" />
#		</form>
#"""
#print "</body></html>"
