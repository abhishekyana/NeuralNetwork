"""
Neural Networks class where the desired number of data can be predicted out
dated:20july2017
"""
import numpy
class NeuralNetwork_model(object):

    def __init__(self,input_size=0,no_H_layers=0,hidden_size=0,output_size=0):
        import numpy
        self.input_size=input_size
        self.output_size=output_size
        self.no_H_layers=no_H_layers
        self.hidden_size=hidden_size
        self.all_layers=self.no_H_layers+2
    def sigmoid(data=numpy.array([]),weights=numpy.array([])):
        return 1/(1+numpy.exp(-1*(numpy.matmul(weights,data))))

    def gen_neurons():
        self.layers=numpy.array([])

    #def give_output(self,data=np.array([])):
     #       for i in range(0,self.all_layers):

