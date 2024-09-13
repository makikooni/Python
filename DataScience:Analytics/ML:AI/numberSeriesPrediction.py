import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf

# Define the series of numbers
series = np.array([2.37, 4.85, 1.97, 4.17, 1.39, 4.66, 1.26, 4.40, 0.46, 5.54, 1.34, 5.80, 1.61])

# Prepare the training data
X_train = []
y_train = []
window_size = 3

for i in range(len(series) - window_size):
    X_train.append(series[i:i+window_size])
    y_train.append(series[i+window_size])

X_train = np.array(X_train)
y_train = np.array(y_train)

# Define the neural network architecture with increased complexity
model = Sequential([
    Dense(16, input_shape=(window_size,), activation='relu'),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1)
])

# Compile the model with a custom learning rate
learning_rate = 0.003
optimizer = tf.keras.optimizers.legacy.Adam(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss='mean_squared_error')

# Train the model with adjusted number of epochs and batch size
epochs = 850  
batch_size = 9
model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=2)



# Predict the next values in the time series
next_input = np.array([[1.34, 5.80, 1.61]])  # Taking the last three numbers as input
predicted_output = model.predict(next_input)
print("Predicted x14 in the time series:", predicted_output[0][0])

# Predict the next value after x14
next_input = np.array([[5.80, 1.61, predicted_output[0][0]]])  # Using predicted x14 as input
predicted_output = model.predict(next_input)
print("Predicted x15 in the time series:", predicted_output[0][0])

"""
    learning_rate = 0.01
    epochs = 1000
    batch_size = 8
    
    Predicted x14 in the time series: 5.5641556
    Predicted x15 in the time series: 1.5156677
    
    +
    -> learning rate = 0.001
    Predicted x14 in the time series: 5.801531
    Predicted x15 in the time series: 1.3429432
    
    -
    ---> learning rate = 0.0001
    Predicted x14 in the time series: 2.062175
Predicted x15 in the time series: 0.97700423


---->
epochs = 700
batch_size = 13
Predicted x14 in the time series: 5.9718423
Predicted x15 in the time series: 1.2663904


Last check:
1/1 [==============================] - 0s 29ms/step
Predicted x14 in the time series: 5.9266615
1/1 [==============================] - 0s 6ms/step
Predicted x15 in the time series: 1.5964717
    
"""