from io import open_code
import numpy as np

# ------------------------------------------------------------------------------------
# Based on Question 7 in Tutorial 7 - Batch Version of Oja's Learning Rule:

def main(weight, learning_rate, x, y, epochs):

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculating zero-mean data:
    feature_vectors = []

    for x_val, y_val in zip(x, y):

        x_val = x_val - x_mean
        y_val = y_val - y_mean
        feature_vectors.append([x_val, y_val])

    epoch = 1

    print("Initial weights = {}.".format(weight))
    
    # # loop for the number of epochs:
    
    while True:


        # this for loop is going through each instance of the dataset (row):
        correct_counter = 0
        update_tracker = []

        print("w value being used for Epoch {} is {}.".format(epoch, weight))

        for i in range(len(feature_vectors)):

            # Weight to use for this epoch. If first epoch than use given parameters in question:
            wx = np.dot(np.array(feature_vectors[i]), weight)

            # Calculating y = wx:
            yw = np.dot(wx, weight)

            # Finding update value for inside bracket -> x^t - yw
            bracket_update = feature_vectors[i] - yw

            # Calculating update for this feature vector:
            update = learning_rate * wx * bracket_update

            # Appending update value to update tracker. It is then summed together once the 
            # algorithm has gone through all the feature vectors in the epoch:
            update_tracker.append(update)
        
        # summing together updates associated with each feature vector for the epoch:
        total_weight_change = np.sum(update_tracker, 0)

        # Doing Batch Oja's Learning Rule weight update:
        weight = weight + total_weight_change
        
        epoch += 1

        # Stopping learning once requested number of epochs has been reached:
        if epoch == epochs:
            print("Learning has converged.")
            break

if __name__ == '__main__':
    
    # Input parameters as given in the question -> CHECK THESE BEFORE ANSWERING QUESTIONS

    x = [0, 3, 5, 5, 8, 9]  # x values of feature vectors given in question
    y = [1, 5, 4, 6, 7, 7]  # y values of feature vectors given in question

    main(weight = [-1, 0], learning_rate = 0.01, x = x, y = y, epochs = 8)




 


