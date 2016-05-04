from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import csv


class Network(object):
	def __init__(self, input_size, output_size):
		# two inputs, three hidden and a single output neuron.
		self.net = buildNetwork(input_size, 3, output_size, bias=True)
		self.input_size = input_size
		self.output_size = output_size

	def train(self, filedir):
		# initialize the data set 
		self.ds = SupervisedDataSet(self.input_size, self.output_size)
		
		# train on data 
		with open(filedir, 'rt') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				# format data
				input_data = tuple(map(float, row[:self.input_size]))
				output_data = tuple(map(float, row[self.input_size:]))

				# add to dataset
				self.ds.addSample(input_data, output_data)

		# uses backpropegation to create a trainer 
		trainer = BackpropTrainer(self.net, self.ds)  
		trainer.train()
		# Trains until convergance...whatever that means
		# trainer.trainUntilConvergence()

	def query(self, input_data):
		return self.net.activate(input_data)

def main():
	network = Network(3,2)
	network.train("Network_Data/test.csv")
	print(network.query([1,5,7]))

if __name__ == "__main__":
	main()



		# self.ds = SupervisedDataSet(self.input_size, self.output_size)  # 2 input, 1 output

		# # for each example in the file 
		# for line in open(filedir,"r").read().split('\n'):
		# 	line_list = line.split(',')

		# 	input_data = tuple(line_list[self.input_size+1:])
		# 	output_data = tuple(line_list[:self.input_size]) 
		# 	self.ds.addSample(input_data, output_data)


# initiallize a default network

# net = buildNetwork(3, 3, 1)

# # it has random values so it can already be used!
# print(net.activate([20000,1, 1]))

# # run data through the network s 
# net.activate([20000,1, 1])

# # inspect different layers of the network
# print(net['in'])
# net['hidden0']
# net['out']

# there are different types of layers, by default it is uses the sigmoid squashing function
# from pybrain.structure import TanhLayer
# net = buildNetwork(2, 3, 1, hiddenclass=TanhLayer)

# # from pybrain.structure import SoftmaxLayer
# # net = buildNetwork(2, 3, 2, hiddenclass=TanhLayer, outclass=SoftmaxLayer)

# # building dataset


# # adding samples
# ds.addSample((0, 0), (0,1))
# ds.addSample((0, 1), (1,))
# ds.addSample((1, 0), (1,))
# ds.addSample((1, 1), (0,))

# len(ds)  # they have lengths

# # and can be iterated through
# for inpt, target in ds:
#     print(inpt, target)

# # clearing dataset
# ds.clear()

# # Training
# from pybrain.supervised.trainers 

# # use trainer to link dataset and network
# net = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)
# trainer = BackpropTrainer(net, ds)  # uses backpropegation

# # train!
# trainer.train()


