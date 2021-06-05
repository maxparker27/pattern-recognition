import numpy as np

def normalize(beta, gamma, value, mean, variance, epsilon):
    
    normalize = beta + gamma * ((value - mean)/np.sqrt(variance + epsilon))
    
    return normalize

def main(x_1, x_2, x_3, x_4, beta, gamma, epsilon, number_samples):

    normalised_X_1, normalised_X_2, normalised_X_3, normalised_X_4 = [], [], [], []
    

    for sample_1, sample_2, sample_3, sample_4 in zip(x_1, x_2, x_3, x_4):
        norm_x_1, norm_x_2, norm_x_3, norm_x_4 = [], [], [], []


        for neuron_1, neuron_2, neuron_3, neuron_4 in zip(sample_1, sample_2, sample_3, sample_4):

            ex_mean = (neuron_1 + neuron_2 + neuron_3 + neuron_4) / number_samples
            variance = ((neuron_1 - ex_mean) ** 2 + (neuron_2 -ex_mean) ** 2 + (neuron_3 - ex_mean) ** 2 + (neuron_4 - ex_mean) ** 2) / number_samples

            norm_x_1.append(normalize(beta, gamma, neuron_1, ex_mean, variance, epsilon))
            norm_x_2.append(normalize(beta, gamma, neuron_2, ex_mean, variance, epsilon))
            norm_x_3.append(normalize(beta, gamma, neuron_3, ex_mean, variance, epsilon))
            norm_x_4.append(normalize(beta, gamma, neuron_4, ex_mean, variance, epsilon))

        normalised_X_1.append(norm_x_1)
        normalised_X_2.append(norm_x_2)
        normalised_X_3.append(norm_x_3)
        normalised_X_4.append(norm_x_4)


    print("Normalised Sample X_1 = {}\n".format(normalised_X_1))
    print("Normalised Sample X_2 = {}\n".format(normalised_X_2))
    print("Normalised Sample X_3 = {}\n".format(normalised_X_3))
    print("Normalised Sample X_4 = {}\n".format(normalised_X_4))


    print("End of script.")

if __name__ == "__main__":

    x_1 = [[1, 0.5, 0.2], [-1, -0.5, -0.2], [0.1, -0.1, 0]]
    x_2 = [[1, -1, 0.1], [0.5, -0.5, -0.1], [0.2, -0.2, 0]]
    x_3 = [[0.5, -0.5, -0.1], [0, -0.4, 0], [0.5, 0.5, 0.2]]
    x_4 = [[0.2, 1, -0.2], [-1, -0.6, -0.1], [0.1, 0, 0.1]]


    main(x_1, x_2, x_3, x_4, beta = 0, gamma = 1, epsilon = 0.1, number_samples = 4)



