# 1) add several models and let user to change them 2) add "game" for example user writes 10 digits and has to confirm if prediction was good or not

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from Skrypty import jpg_to_28_x_28_matrix, drawing

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# plt.imshow(x_train[0], cmap=plt.cm.binary)
# plt.show()
# print(y_train[0])
# print(x_train[0])

# Normalizing data from 0-255 to 0-1
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

"""
# Architecture of the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())  # from 28x28 to 784 vector
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)  # epochs = how many times goes through data set


val_loss, val_acc = model.evaluate(x_test, y_test)\
# print(f"Y: {y_test.size}")
# print(f"X: {x_test.size/784}")
print(val_loss, val_acc)

# saving a model
model.save("num_rec2.model")"""
new_model = tf.keras.models.load_model('D:\PythonProjekty\DigitRecognition\Skrypty\\num_rec2.model')
# create jpg
# endless loop that let's the user to draw a digit and recevie 28x28 picture as well as prediction


def funct():
    drawing.create_jpg_image()
    x_testowy = jpg_to_28_x_28_matrix.return_bit_arr()
    x_testowy = jpg_to_28_x_28_matrix.clean_arr(x_testowy)

    x = tf.constant([x_testowy], dtype=tf.float32)
    # x_testowy = tf.keras.utils.normalize(x_testowy, axis=1)
    x=tf.keras.utils.normalize(x, axis=1)
    plt.imshow(x_testowy, cmap=plt.cm.binary)
    plt.show()
    # print("STop")
    #predictions = new_model.predict(x)
    predictions = new_model.predict(x)

    a=(np.argmax(predictions[0]))
    print(a)
    # jpg_to_28_x_28_matrix.print_result_of_prediction(a)


while 1:
    funct()