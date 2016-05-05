from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import csv


class Network(object):
	def __init__(self, input_size, output_size, number_of_layers=3, size_of_hidden_layers=3, type_of_hidden_layer='sigmoid', net_bias=False):
		self.net = FeedForwardNetwork()

		# set up layers of the network
		layers = []

		for i in range(number_of_layers):
			if i == 0:
				layers.append(LinearLayer(input_size))
				self.net.addInputModule(layers[i])
			elif i == (number_of_layers-1):
				layers.append(LinearLayer(output_size))
				self.net.addOutputModule(layers[i])
				self.net.addConnection(FullConnection(layers[i-1], layers[i]))
			else:
				if type_of_hidden_layer == 'linear':
					layers.append(LinearLayer(output_size))
				elif type_of_hidden_layer == 'sigmoid':
					layers.append(SigmoidLayer(output_size))
				elif type_of_hidden_layer == 'tanh':
					layers.append(TanhLayer(output_size))	
				self.net.addModule(layers[i])
				self.net.addConnection(FullConnection(layers[i-1], layers[i]))

		self.net.sortModules()

		# self.net = buildNetwork(input_size, 3, output_size, bias=net_bias)
		self.input_size = input_size
		self.output_size = output_size

	def train(self, filedir, convergance):
		# initialize the data set 
		self.ds = SupervisedDataSet(self.input_size, self.output_size)
		
		# train on data 
		with open(filedir, 'rt') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			# reader.pop()
			for row in reader:
				# format data
				input_data = tuple(map(float, row[2:(self.input_size+2)]))
				output_data = tuple(map(float, row[(self.input_size+2):((self.input_size+2)+self.output_size)]))

				# add to dataset
				self.ds.addSample(input_data, output_data)

		# uses backpropegation to create a trainer 
		trainer = BackpropTrainer(self.net, self.ds)  
		if convergance:
			trainer.trainUntilConvergence()
		else:
			trainer.train()


	def query(self, input_data):
		return self.net.activate(input_data)

def main():
	network = Network(input_size=69, output_size=10,number_of_layers=3, net_bias=True)
	network.train("Network_Data/final_rep.csv", False)
	print(network.query([50756,37,14613,19347,5876,1947,49584,18,476,191,26030,7,9,96,31,175,10,10,65,37,60,4,88,2969,24132,8,116,3,367,1156,109,29938,9923,264,235,15980,17577,13.7,1310,15064,1261,979,811,835,1139,905,1089,964,931,1661,1950,2760,1317,825,605,256,14597,1553,53081,11.2,54571,10900,91.8,26569,28002,42154,9643,232,474]))

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


