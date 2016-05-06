from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, TanhLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.datasettools import DataSetNormalizer
# 
# from pybrain.tools.customxml.networkwriter import NetworkWriter
# from pybrain.tools.customxml.networkreader import NetworkReader
# If you are getting no module found errors comment out the bottom 2 and try the above.

from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader


from pybrain.tools.validation import CrossValidator
from pybrain.tools.validation import CrossValidator
from pybrain.tools.validation import ModuleValidator
from pybrain.tools.validation import Validator

import csv
from numpy import sum,array, array_split, apply_along_axis, concatenate, ones, dot, delete, append, zeros, argmax
from numpy.random import permutation
import copy

class Network(object):
	def __init__(self, input_size, output_size, number_of_layers=3, size_of_hidden_layers=3, type_of_hidden_layer='sigmoid', net_bias=False, epochs=100):
		self.net = FeedForwardNetwork()
		self.num_epochs = epochs
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
					layers.append(LinearLayer((input_size + output_size) / 2))
				elif type_of_hidden_layer == 'sigmoid':
					layers.append(SigmoidLayer((input_size + output_size) / 2))
				elif type_of_hidden_layer == 'tanh':
					layers.append(TanhLayer((input_size + output_size) / 2))	
				self.net.addModule(layers[i])
				self.net.addConnection(FullConnection(layers[i-1], layers[i]))

		self.net.sortModules()
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


			for row in reader:
				# format data

				input_data = tuple(map(float, row[1:(self.input_size+1)]))
				output_data = tuple(map(float, row[(self.input_size+1):((self.input_size+1+self.output_size))]))

				# print (output_data)

				# add to dataset
				self.ds.addSample(input_data, output_data)

		# uses backpropegation to create a trainer 
		self.trainer = BackpropTrainer(self.net, self.ds)  

	def train(self, convergance):
		if convergance:
			self.trainer.trainUntilConvergence()
		else:
			self.trainer.trainEpochs(self.num_epochs)


	def query(self, input_data):
		return self.net.activate(input_data)

	def cross_vaildate(self):
		n_folds = 5
		max_epochs = self.num_epochs
		l = self.ds.getLength()
		inp = self.ds.getField("input")
		tar = self.ds.getField("target")
		indim = self.ds.indim
		outdim = self.ds.outdim
		assert l > n_folds

		perms = array_split(permutation(l), n_folds)

		perf = 0.
		for i in range(n_folds):
			# determine train indices
			train_perms_idxs = list(range(n_folds))
			train_perms_idxs.pop(i)
			temp_list = []
			for train_perms_idx in train_perms_idxs:
				temp_list.append(perms[ train_perms_idx ])
			train_idxs = concatenate(temp_list)

			# determine test indices
			test_idxs = perms[i]

			# train
			train_ds = SupervisedDataSet(indim, outdim)
			train_ds.setField("input"  , inp[train_idxs])
			train_ds.setField("target" , tar[train_idxs])
			temp_trainer = copy.deepcopy(self.trainer)
			temp_trainer.setData(train_ds)
			if not max_epochs:
				temp_trainer.train()
			else:
				temp_trainer.trainEpochs(max_epochs)

			# test
			test_ds = SupervisedDataSet(indim, outdim)
			test_ds.setField("input"  , inp[test_idxs])
			test_ds.setField("target" , tar[test_idxs])

			perf += self.myCalculatePerformance(temp_trainer, test_ds)

		perf /= n_folds
		return perf


	def myCalculatePerformance(self, trainer, dataset):
		# compute outputs 
		output = []
		for row in array(dataset.getField('input')):
			output.append(trainer.module.activate(row))
		target = array(dataset.getField('target'))

		# compute and return the mean square error
		return Validator.MSE(output=output, target=target, )


def main():
	DemNetwork = Network(input_size=69, output_size=2,number_of_layers=3, net_bias=True)
	RepNetwork = Network(input_size=69, output_size=5,number_of_layers=3, net_bias=True)

	DemNetwork.prepare_trainer("dem-weka-normalized.csv")

	DemNetwork.train(False)
	DemNetwork.save("/Users/ducatirx8/Documents/AINeuralNetwork/ilstu-honors-neuralnetwork-src/demNetwork")
	# DemNetwork.load("/Users/ducatirx8/Documents/AINeuralNetwork/ilstu-honors-neuralnetwork-src/demNetwork")
	# DemNetwork.cross_vaildate()
	# print (DemNetwork.cross_vaildate())
	# print(network.query([50756,37,14613,19347,5876,1947,49584,18,476,191,26030,7,9,96,31,175,10,10,65,37,60,4,88,2969,24132,8,116,3,367,1156,109,29938,9923,264,235,15980,17577,13.7,1310,15064,1261,979,811,835,1139,905,1089,964,931,1661,1950,2760,1317,825,605,256,14597,1553,53081,11.2,54571,10900,91.8,26569,28002,42154,9643,232,474]))

if __name__ == "__main__":
	main()