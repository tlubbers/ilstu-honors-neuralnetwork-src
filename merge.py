import csv

def main():
	rep = open("republicans.csv", "rt")
	dem = open("democrats.csv", "rt")

	final = open("normalized_final_data.csv", "rt")

	final_rep = open ("final_rep.csv", "wt")
	final_dem = open ("final_dem.csv", "wt")
	final_unvoted = open ("final_unvoted.csv", "wt")


	final_reader = list(csv.reader(final, delimiter=','))
	rep_reader = list(csv.reader(rep, delimiter=','))
	dem_reader = list(csv.reader(dem, delimiter=','))

	for i in final_reader:	
		rep_switcher = False
		dem_switcher = False

		for j in rep_reader: 
			# this county has voted 
			if i[0] == j[0]:
				rep_switcher = True
				mylist = i + j[1:]
				final_rep.write("\"" + mylist[0] + "\"")
				del mylist[0] 
				for s in mylist:
					final_rep.write(s+",")
				final_rep.write("\n")
		for k in dem_reader:
			# this county has voted 
			if i[0] == k[0]:
				dem_switcher = False
				mylist = i + k[1:]
				final_dem.write("\"" + mylist[0] + "\"")
				del mylist[0] 
				for s in mylist:
					final_dem.write(','+s)
				final_dem.write("\n")
	
		# not in either, not voted for yet 
		if rep_switcher == False and dem_switcher == False:
			final_unvoted.write("\"" + i[0] + "\"")
			del i[0] 
			for s in i:
				final_unvoted.write(','+s)
			final_unvoted.write("\n")

	final_dem.close()
	final_rep.close()
	final_unvoted.close()

if __name__ == "__main__":
	main()