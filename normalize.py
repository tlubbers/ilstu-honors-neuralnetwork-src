import csv
import sys

def openData(filedir):
	with open(filedir, 'rt') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		input_data = ()
		arrayOfMaxes = 70*[0]
		arrayOfMins = 70*[sys.maxint]
		allData = []
		counter = 0
		for row in reader:
			# format data
			if not row[0].isupper():
				if counter > 0:
					allData.append(row)
			counter +=1
			# input_data = tuple(map(float, row[1:(input_size+1)]))
			# return input_data
		xCounter = 0
		yCounter = 0
		# print allData
		for row in allData:
			for col in row:
				# Skip the countyname
				if yCounter > 0:
					if arrayOfMaxes[yCounter] < float(col):
						arrayOfMaxes[yCounter] = col
					if arrayOfMins[yCounter] > float(col):
						arrayOfMins[yCounter] = col
				yCounter +=1
			yCounter = 0
			xCounter += 1
		print arrayOfMaxes
		print arrayOfMins
		

def main(filedir):
	openData(filedir)




if __name__ == "__main__":
	main("/Users/ducatirx8/Documents/AINeuralNetwork/ilstu-honors-neuralnetwork-src/final_data.csv")




