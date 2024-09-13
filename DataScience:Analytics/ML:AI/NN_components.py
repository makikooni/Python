
#---------------Activation Function ------------------------------

import numpy as np

# ReLU activation function

def relu(x):

    return np.maximum(0, x)

# Sigmoid activation function

def sigmoid(x):

    return 1 / (1 + np.exp(-x))

# Exercise 1

inputs = np.array([-1, 0, 2, -3, 4])

relu_output = relu(inputs)

print("ReLU Output:", relu_output)

# Exercise 2

inputs = np.array([-1, 0, 1, 2])

sigmoid_output = sigmoid(inputs)

print("Sigmoid Output:", np.round(sigmoid_output, 3))


#-----------------Loss function-----------------------
# Mean Squared Error (MSE) loss function

def mse_loss(predicted, actual):

    return np.mean((predicted - actual) ** 2)

# Cross Entropy loss function

def cross_entropy_loss(predicted_probs, actual_labels):

    return -np.mean(actual_labels * np.log(predicted_probs) + (1 - actual_labels) * np.log(1 - predicted_probs))

# Exercise 3

predicted_values = np.array([3, 4, 5, 6])

actual_values = np.array([2, 5, 4, 8])

mse = mse_loss(predicted_values, actual_values)

print("MSE Loss:", mse)

# Exercise 4

predicted_probs = np.array([0.2, 0.7, 0.9, 0.4])

actual_labels = np.array([0, 1, 1, 0])

cross_entropy = cross_entropy_loss(predicted_probs, actual_labels)

print("Cross Entropy Loss:", round(cross_entropy, 3))




#------------Optimisation function ----------
# Gradient Descent optimizer

def gradient_descent(weights, gradients, learning_rate):

    return weights - learning_rate * gradients

# Adam optimizer

def adam_optimizer(weights, gradients, learning_rate, beta1=0.9, beta2=0.999, epsilon=1e-8):

    m = 0

    v = 0

    t = 0

    t += 1

    m = beta1 * m + (1 - beta1) * gradients

    v = beta2 * v + (1 - beta2) * (gradients ** 2)

    m_hat = m / (1 - beta1 ** t)

    v_hat = v / (1 - beta2 ** t)

    weights -= learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)

    return weights

# Exercise 5

initial_weights = np.array([0.5, -0.3, 0.1])

gradients = np.array([0.2, -0.1, 0.3])

learning_rate = 0.01

updated_weights_gd = gradient_descent(initial_weights, gradients, learning_rate)

print("Updated weights (Gradient Descent):", updated_weights_gd)

# Exercise 6

initial_weights = np.array([0.2, -0.1, 0.3])

gradients = np.array([0.1, -0.05, 0.2])

learning_rate = 0.001

updated_weights_adam = adam_optimizer(initial_weights, gradients, learning_rate)

print("Updated weights (Adam):", updated_weights_adam)
