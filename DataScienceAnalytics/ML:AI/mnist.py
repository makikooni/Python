import ssl
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
 

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context
 
def get_mnist():
    return mnist.load_data()
 
# Initialize your neural network parameters

w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
# weights from input to hidden layer.
# the matrix has a shape of (20, 784), indicating 20 rows and 784 columns.
#Each element in the matrix is drawn randomly from a uniform distribution between -0.5 (inclusive) and 0.5 (exclusive).

w_h_o = np.random.uniform(-0.5, 0.5, (10, 20))
#weights from hidden to output layer

b_i_h = np.zeros((20, 1))
#bias for the hidden layer, 20 rows, 1 column - > column vector

b_h_o = np.zeros((10, 1))
#bias for the output layer
 
learn_rate = 0.001
#determines the size of the steps taken during the optimization process. A smaller learning rate usually leads to slower but more stable training.
nr_correct = 0
epochs = 10
#which is the number of times the entire dataset is passed forward and backward through the neural network during training
 
# Load MNIST data
(images_train, labels_train), (images_test, labels_test) = get_mnist()
 
# Training loop
for epoch in range(epochs):
    for img, label in zip(images_train, labels_train):
        img = img.reshape(-1, 1)
        #The -1 in the reshape function means that NumPy should automatically infer the size of that dimension based on the length of the input data. The resulting shape is (num_pixels, 1), where num_pixels is the total number of pixels in the image.
        label = tf.keras.utils.to_categorical(label, 10).reshape(-1, 1)
        #This line converts the label into one-hot encoded format using to_categorical from TensorFlow's Keras utilities. The resulting shape is (num_classes, 1), where num_classes is the number of classes in your classification problem.

        # Forward propagation input -> hidden
        h_pre = b_i_h + w_i_h @ img
        #h_pre is the weighted sum of inputs to the hidden layer, including the bias term.

        h = 1 / (1 + np.exp(-np.clip(h_pre, -500, 500)))
        #h is the output of the hidden layer after applying the sigmoid activation function, with values >= =500 or <= 500 removed
        #The sigmoid function squashes the input values between 0 and 1, which is a common activation function for hidden layers in neural networks.
        
        # Forward propagation hidden -> output
        o_pre = b_h_o + w_h_o @ h
        o = 1 / (1 + np.exp(-np.clip(o_pre, -500, 500)))
 
        # Cost / Error calculation
        e = 1 / len(o) * np.sum((o - label) ** 2, axis=0)
        #  e = Mean Squared Error (MSE)
        nr_correct += int(np.argmax(o) == np.argmax(label))
 
        # Backpropagation output -> hidden (cost function derivative)
        delta_o = o - label
        w_h_o += -learn_rate * delta_o @ np.transpose(h)
        b_h_o += -learn_rate * delta_o
 
        # Backpropagation hidden -> input (activation function derivative)
        delta_h = np.transpose(w_h_o) @ delta_o * (h * (1 - h))
        w_i_h += -learn_rate * delta_h @ np.transpose(img)
        b_i_h += -learn_rate * delta_h
 
    # Show accuracy for this epoch
    print(f"Epoch {epoch + 1}, Acc: {round((nr_correct / len(images_train)) * 100, 2)}%")
    nr_correct = 0
 

# Show results
while True:
    # choose a digit from database
    index = int(input("Enter a number (0 - 9999): "))
    img = images_test[index]
    plt.imshow(img, cmap="Greys")
 
    img = img.reshape(-1, 1)
    # Forward propagation input -> hidden
    h_pre = b_i_h + w_i_h @ img
    h = 1 / (1 + np.exp(-np.clip(h_pre, -500, 500)))
    # Forward propagation hidden -> output
    o_pre = b_h_o + w_h_o @ h
    o = 1 / (1 + np.exp(-np.clip(o_pre, -500, 500)))
 
    plt.title(f"Predicted Digit: {np.argmax(o)}")
    plt.show()
