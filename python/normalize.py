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
			# skip the headers of each column 
			if xCounter > 0:
				for col in row:
					# Skip the countyname
					if yCounter > 0:
						if arrayOfMaxes[yCounter] < float(col):
							arrayOfMaxes[yCounter] = float(col)
						if arrayOfMins[yCounter] > float(col):
							arrayOfMins[yCounter] = float(col)
					yCounter +=1
				yCounter = 0
			xCounter += 1

		newfile = open("normalized_final_dataV2.csv", 'wt')

		yCounter = 0
		for row in allData:
			if xCounter == 0:
				for y in row:
					newfile.write(y+',')
			else:
				for col in row:
					if yCounter == 0:
						newfile.write('\"'+col+'\",')
					# Skip the countyname
					else:
						xi = (float(col) - arrayOfMins[yCounter]) / (arrayOfMaxes[yCounter] - arrayOfMins[yCounter])
						newfile.write(str(xi))
						newfile.write(",")
					yCounter +=1
				yCounter = 0
			xCounter += 1
			newfile.write('\n')
					

		newfile.close()
		# print (arrayOfMaxes)
		# print (arrayOfMins)
		

def main(filedir):
	openData(filedir)




if __name__ == "__main__":
	# main("/Users/ducatirx8/Documents/AINeuralNetwork/ilstu-honors-neuralnetwork-src/final_data.csv")
	main("final_data.csv")



