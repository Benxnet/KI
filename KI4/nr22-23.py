from builtins import print
from itertools import product

import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split


def NN1():
    return tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])


def NN2():
    return tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(16),
        tf.keras.layers.Dense(16),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])


def NN3():
    return tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(128),
        tf.keras.layers.Dense(64),
        tf.keras.layers.Dense(32),
        tf.keras.layers.Dense(16),
        tf.keras.layers.Dense(8),
        tf.keras.layers.Dense(4),
        tf.keras.layers.Dense(8),
        tf.keras.layers.Dense(16),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])


def NN2Activations():
    return tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(16, activation="sigmoid"),
        tf.keras.layers.Dense(16, activation="tanh"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])


def main():
    mnist = tf.keras.datasets.mnist

    # Laden des Datensatzes und konvertierung von int zu floats bzw von 0-255 zu 0-1 und aufteilung zu 1:3
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x = np.concatenate((x_train, x_test))
    y = np.concatenate((y_train, y_test))

    train_size = 3 / 4
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=train_size)

    print(len(x_train))
    print(len(x_test))

    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Erstellung des Sequential model
    model = NN1()

    # Für jedes Beispiel gibt das model ein vektor von logits oder log-odds zurück
    predictions = model(x_train[:1]).numpy()

    # Konvertierung von allen logits zu wahrscheinlichkeiten und eine Lost-funktion wird definiert
    tf.nn.softmax(predictions).numpy()
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn(y_train[:1], predictions).numpy()

    # Kompiliert das model mit Keras, setzt einen optimizer und eine loss funktion. Definiert die metrik
    model.compile(
        optimizer='adam',
        loss=loss_fn,
        metrics=['accuracy']
    )

    # Train and evaluate your model Use the Model.fit method to adjust your model parameters and minimize the loss:
    # Trainieren des NNs und passt die model Daten an und minimiert den Verlust
    model.fit(x_train, y_train, epochs=5)

    # 22
    # Evaluiert das generierte model nach den Testdaten und
    # wrapped das generierte model mit Softmax() in ein neues model zur darstellung von Wahrscheinlichkeiten
    model.evaluate(x_test, y_test, verbose=2)
    probability_model = tf.keras.Sequential([
        model,
        tf.keras.layers.Softmax()
    ])
    # Gibt das erste element von y_test aus
    print(y_test[:1])
    # Setzt Ausgangsdaten als wahrscheinlichkeit
    probability_model(x_test[:1])


if __name__ == "__main__":
    main()
