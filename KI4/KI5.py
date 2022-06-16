import tensorflow as tf
mnist = tf.keras.datasets.mnist
### ... (Kommentar einfügen) ...
#Load and prepare the MNIST dataset. Convert the sample data from integers to floating-point numbers:
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
### ... (Kommentar einfügen) ...
###Build a machine learning model Build a tf.keras.Sequential model by stacking layers.
model = tf.keras.models.Sequential([
tf.keras.layers.Flatten(input_shape=(28, 28)),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10)
])
### ... (Kommentar einfügen) ...
###For each example, the model returns a vector of logits or log-odds scores, one for each class.
predictions = model(x_train[:1]).numpy()
### ... (Kommentar einfügen) ...
#The tf.nn.softmax function converts these logits to probabilities for each class:
tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
### ... (Kommentar einfügen) ...
#Before you start training, configure and compile the model using Keras Model.compile.
# Set the optimizer class to adam, set the loss to the loss_fn function you defined earlier,
# and specify a metric to be evaluated for the model by setting the metrics parameter to accuracy.
model.compile(
optimizer='adam',
loss=loss_fn,
metrics=['accuracy']
)
### ... (Kommentar einfügen) ...
#Train and evaluate your model Use the Model.fit method to adjust your model parameters and minimize the loss:
#The Model.evaluate method checks the models performance, usually on a "Validation-set" or "Test-set".
model.fit(x_train, y_train, epochs=5)


### ... (Kommentar einfügen) ...
model.evaluate(x_test, y_test, verbose=2)
probability_model = tf.keras.Sequential([
model,
tf.keras.layers.Softmax()
])
### ... (Kommentar einfügen) ...
print(y_test[:1])
### ... (Kommentar einfügen) ...
probability_model(x_test[:1])
