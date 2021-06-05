import numpy as np

# Based on Questions 2 and 5 in Tutorial 2:

def makeClassification(weight, feature_vector):

    # augmenting feature vector:
    feature_vector.insert(0, 1)
    print("Feature vector being classified is {}".format(feature_vector))
    
    weight = np.array(weight)
    feature_vector = np.array(feature_vector)

    gx = np.dot(weight, feature_vector)
    print("gx = {}.".format(gx))

    if gx > 0:
        print("Feature Vector {} is in Class 1.\n".format(feature_vector))
    else:
        print("Feature Vector {} is in Class 2.\n".format(feature_vector))


if __name__ == '__main__':

    # determine the class of the following feature vectors:
    # Change these parameters to fit the question at hand.

    # Given weights:
    at = [-3, 1, 2, 2, 2, 4]

    # Given feature vectors before augmentation:
    x_1 = [0, -1, 0, 0, 1]
    x_2 = [1, 1, 1, 1, 1]

    makeClassification(at, x_1)
    makeClassification(at, x_2)
    
