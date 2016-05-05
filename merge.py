import csv

def main():
	rep = open("republicans.csv", "rt")
	dem = open("democrats.csv", "rt")

	final = open("final_data.csv", "rt")

	final_rep = open ("final_rep.csv", "wt")
	final_dem = open ("final_dem.csv", "wt")

	final_reader = list(csv.reader(final, delimiter=','))
	rep_reader = list(csv.reader(rep, delimiter=','))
	dem_reader = list(csv.reader(dem, delimiter=','))

	for i in final_reader:	
		for j in rep_reader: 
			# this county has voted 
			if i[0] == j[0]:
				mylist = i + j[1:]
				for s in mylist:
					final_rep.write(s+",")
				final_rep.write("\n")

		for k in dem_reader:
			# this county has voted 
			if i[0] == k[0]:
				mylist = i + k[1:]
				for s in mylist:
					final_dem.write(s+",")
				final_dem.write("\n")
	final_dem.close()
	final_rep.close()

if __name__ == "__main__":
	main()