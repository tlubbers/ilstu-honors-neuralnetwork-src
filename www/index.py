#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgi
import cgitb
cgitb.enable()
ready_to_predict = False
form = cgi.FieldStorage()


def main():
  content = load_values()
  if ready_to_predict:
    delete_me = "Put your code here Julian"
  print(content)


def load_values():
  global county
  global state
  global party
  trump = 0.0
  cruz = 0.0
  kasich = 0.0
  rubio = 0.0
  carson = 0.0
  sanders = 0.0
  clinton = 0.0
  county = form.getvalue('county', "")
  state = form.getvalue('state', "")
  party = form.getvalue('party', "")

  if county != "" and state != "" and party != "":
    ready_to_predict = True

  return fileToStr('main.html').format(**locals())

def fileToStr(fileName):
    """Return a string containing the contents of the named file."""
    fin = open(fileName);
    contents = fin.read();
    fin.close()
    return contents


try:   # NEW
    print("Content-type: text/html\n\n")   # say generating html
    main()
except:
    cgi.print_exception()



