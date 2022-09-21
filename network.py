import numpy as np

class Network:
    def __init__(self, layers_dims, weights=None, biases=None):
        self.layers_dims = layers_dims
        self.num_layers = len(layers_dims)

        if weights:
            self.weights = weights
        else:
            self.weights = [np.random.randn(layers_dims[i+1], layers_dims[i]) 
                            for i in range(0, self.num_layers-1)]
        if biases:
            self.biases = biases                    
        else:
            self.biases = [np.random.randn(layers_dims[i], 1) 
                            for i in range(1, self.num_layers)]
    
    def _sigmoid(self, z):
        return 1/(1 + np.exp(-z))
    
    def _ReLU(self, z):
        return np.maximum(0, z)

    def forward(self, x):
        for i in range(self.num_layers-1):
            x = self.weights[i].dot(x) + self.biases[i]
            x = self._ReLU(x)
        return x

    def __repr__(self):
        return str(self.weights)
    
class NetworkFactory:
    
    def __init__(self, layers_dims):
        self.layers_dims = layers_dims
        
    def _mutate_from_base_network(self, base_network, num_mutations, amount=0.5):
        all_networks = [base_network]

        for i in range(1, num_mutations):

            weights = [weight + np.random.rand(*weight.shape) * amount
                                        for weight in base_network.weights]
            biases = [bias + np.random.rand(*bias.shape) * amount
                                        for bias in base_network.biases]
            mutated_net = Network(base_network.layers_dims, weights, biases)
            all_networks.append(mutated_net)  

        return all_networks

    def create_mutated_networks(self, num_mutations, base_network=None):
        if not base_network:
            base_network = Network(self.layers_dims)
        return self._mutate_from_base_network(base_network, num_mutations)