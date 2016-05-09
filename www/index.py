#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgi
import cgitb
import csv
from honors_net import Network
import sys
sys.stderr = sys.stdout

cgitb.enable()
ready_to_predict = False
form = cgi.FieldStorage()


def main():
  content = load_values()
  print(content)

def initCountyLookup(filedir, input_size, county):
	with open(filedir, 'rt') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		input_data = ()
		for row in reader:
			if row[0].lower() == county.lower():
				input_data = tuple(map(float, row[1:(input_size+1)]))
				return input_data
		return input_data


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


	if county != "" and state != "":
		ready_to_predict = True
		data = initCountyLookup("./final_data_nostates_normalized.csv", 69, county+ ", " + state)

		if len(data) > 0:
			pathToDemXml = "./demNetwork"
			demNetwork = Network(input_size=69, output_size=4,number_of_layers=3, net_bias=True)
			demNetwork.load(pathToDemXml)
			pathToRepubXML = "./repNetwork"
			repNetwork = Network(input_size=69, output_size=4,number_of_layers=3, net_bias=True)
			repNetwork.load(pathToRepubXML)      

			demOut = demNetwork.query(data)
			repOut = repNetwork.query(data)
			clinton = demOut[0]*100
			sanders = demOut[1]*100
			trump = repOut[0]*100
			cruz = repOut[1]*100
			rubio = repOut[2]*100
			carson = repOut[3]*100
			kasich = repOut[4]*100
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



