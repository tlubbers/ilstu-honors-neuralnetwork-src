from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
from pybrain.tools.validation import CrossValidator
from pybrain.tools.validation import CrossValidator
from pybrain.tools.validation import ModuleValidator

import csv
from numpy import sum, array

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

	def load(self, filedir):
		self.net = NetworkReader.readFrom(filedir)

	def save(self, filedir):
		NetworkWriter.writeToFile(self.net, filedir)

	def prepare_trainer(self, filedir):
		# initialize the data set 
		self.ds = SupervisedDataSet(self.input_size, self.output_size)
		
		# train on data 
		with open(filedir, 'rt') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')

			# reader.pop()
			for row in reader:
				print (row[(self.input_size):(self.input_size+self.output_size)])
				# print(row[1:(self.input_size+1)])
				# format data
				input_data = tuple(map(float, row[1:(self.input_size+1)]))
				output_data = tuple(map(float, row[(self.input_size):(self.input_size+self.output_size)]))

				# add to dataset
				self.ds.addSample(input_data, output_data)

		# uses backpropegation to create a trainer 
		self.trainer = BackpropTrainer(self.net, self.ds)  

	def train(self, convergance):
		if convergance:
			self.trainer.trainUntilConvergence()
		else:
			self.trainer.train()

	def query(self, input_data):
		return self.net.activate(input_data)

	def cross_vaildate(self):
		# creates a crossvalidator instance
		# print (ModuleValidator.validate(, module=self.net, dataset=self.ds))
		# print (ModuleValidator.MSE(module=self.net, dataset=self.ds))
		# cv = CrossValidator(trainer=self.trainer, dataset=self.ds, n_folds=5) 
		# print (CrossValidator.validate(cv))
		# calls the validate() function in CrossValidator to return results
		# print (ModuleValidator.MSE(module=self.net,dataset=self.ds)) 
		# creates a crossvalidator instance
		cv=CrossValidator(valfunc=self.MyValidate, trainer=self.trainer, dataset=self.ds, n_folds=5) 
		# calls the validate() function in CrossValidator to return results
		print (CrossValidator.validate(cv)) 

	def MyValidate(self, module, dataset):
		""" Abstract validate function, that is heavily used by this class.
		First, it calculates the module's output on the dataset.
		In advance, it compares the output to the target values of the dataset
		through the valfunc function and returns the result.

		:arg valfunc: A function expecting arrays for output, target and
		importance (optional). See Validator.MSE for an example.
		:arg module:  Object of any subclass of pybrain's Module type
		:arg dataset: Dataset object at least containing the fields
		'input' and 'target' (for example SupervisedDataSet)
		"""
		target = dataset.getField('target')
		output = ModuleValidator.calculateModuleOutput(module, dataset)

		return self.myClassificationPerformance(output, target)


	def myClassificationPerformance(self, output, target):
		""" Returns the hit rate of the outputs compared to the targets.

		:arg output: array of output values
		:arg target: array of target values
		"""
		output = array(output)
		target = array(target)

		assert len(output) == len(target)

		for i in range(len(output)):
			# print (output[i])
			# print (target[i])

		n_correct = sum(output == target)
		return float(n_correct) / float(len(output))

def main():
	network = Network(input_size=69, output_size=4,number_of_layers=3, net_bias=True)
	network.prepare_trainer("final_dem.csv")
	# network.cross_vaildate()


	# print(network.query([50756,37,14613,19347,5876,1947,49584,18,476,191,26030,7,9,96,31,175,10,10,65,37,60,4,88,2969,24132,8,116,3,367,1156,109,29938,9923,264,235,15980,17577,13.7,1310,15064,1261,979,811,835,1139,905,1089,964,931,1661,1950,2760,1317,825,605,256,14597,1553,53081,11.2,54571,10900,91.8,26569,28002,42154,9643,232,474]))

if __name__ == "__main__":
	main()