import csv
from honors_net import Network

def initCountyLookup(filedir, input_size, county):
	with open(filedir, 'rt') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		input_data = ()
		for row in reader:
			# format data
			if row[0].lower() == county.lower():
				input_data = tuple(map(float, row[1:(input_size+1)]))
				return input_data
		return input_data

def main(county, dirPath, isDemocrat):
	data = initCountyLookup(dirPath, 69, county)
	if len(data) == 0:
		print "Invalid County"
	else:
		if isDemocrat:
			PathToDemXML = "/Users/ducatirx8/Documents/AINeuralNetwork/ilstu-honors-neuralnetwork-src/demNetwork"
			network = Network(input_size=69, output_size=4,number_of_layers=3, net_bias=True)
			network.load(PathToDemXML)
			output = network.query(data)
			print data
		else:
			PathToRepubXML = ""
			network = Network(input_size=69, output_size=4,number_of_layers=3, net_bias=True)
			network.load(PathToRepubXML)
			output = network.query(data)
		print output


if __name__ == "__main__":
	main("Baldwin, AL", "/Users/ducatirx8/Documents/AINeuralNetwork/ilstu-honors-neuralnetwork-src/final_data.csv", True)




