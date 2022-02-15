import numpy as np


class NeuralNetwork:
    def __init__(self, inputs, hidden, output, weightsIH, weightsHO, bias1, bias2):
        self.inputs = inputs
        self.hidden = hidden
        self.output = output

        self.weightsIH = np.array(weightsIH)
        self.weightsHO = np.array(weightsHO)

        self.bias1 = bias1
        self.bias2 = bias2

        self.X = None

    def predict(self, metrics):

        self.X = np.array(metrics) / 500

        self.Z1 = np.dot(self.weightsIH.T, self.X) + self.bias1
        self.A1 = 1 / (1 + np.exp(-self.Z1))

        self.Z2 = np.dot(self.weightsHO.T, self.A1) + self.bias2
        self.A2 = 1 / (1 + np.exp(-self.Z2))

        return self.A2
