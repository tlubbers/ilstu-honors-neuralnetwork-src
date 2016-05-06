import sys
from honors_net import Network 

def main():

	print ("this is the test")

	if len(sys.argv) != 3:
		print ("format: <filename> <# of outputs>")
		exit() 

	filedir = sys.argv[1]
	os = int(sys.argv[2])
	output_file = open (filedir[:-4] + "_validations.csv", "wt")
	
	funct_types = ['sigmoid','tanh']

	print ("lets start")
	sys.stdout.flush()
	
	x = 10
	while x <= 100:
		print("yo")

		for t in funct_types: 
			for h in range(1,4): 
				network = Network(input_size=69, output_size=os,number_of_layers=h+2, type_of_hidden_layer=t, net_bias=True, epochs=x)
				network.prepare_trainer(filedir)
				output_file.write(t + ",")
				output_file.write(str(h))
				output_file.write(",")
				output_file.write(str(x))
				output_file.write(",")
				print ("cross validate")
				output_file.write(str(network.cross_vaildate()))
				output_file.write("\n")
				print ("tick")
				sys.stdout.flush()
			print ("tock")
		print ("tuck")
		x += 10

if __name__ == "__main__":
	main()