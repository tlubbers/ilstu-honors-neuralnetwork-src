import sys
from honors_net import Network 

def main():
	print (len(sys.argv))

	if len(sys.argv) != 3:
		print ("format: <filename> <# of outputs>")
		exit() 

	filedir = sys.argv[0]
	os = int(sys.argv[1])
	output_file = open (filedir + "_validations.csv", "wt")
	
	funct_types = ['sigmoid','tanh']

	x = 100
	while x <= 1000:
		for t in funct_types: 
			for h in range(1,4): 
				network = Network(input_size=69, output_size=os,number_of_layers=h+2, type_of_hidden_layer=t, net_bias=True, epochs=x)
				network.prepare_trainer(filedir)
				output_file.write(t + "," + h + "," + e + "," + network.cross_vaildate() + "\n")
				print ("tick")
			print ("tock")
		print ("tuck")
		x += 100

if __name__ == "__main__":
	main()