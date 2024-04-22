import os
import pathlib
import random

import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

image_height = 1920
image_width = 1080

cwd = os.getcwd()
data_path = os.path.join(cwd, "images")
model_path = os.path.join(cwd, "models")

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_path,
    subset="training",
    validation_split=0.2,
    seed=123,
    image_size=(image_height, image_width),
)
validation_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_path,
    validation_split=0.1,
    subset="validation",
    seed=123,
    image_size=(image_height, image_width),
)

class_names = train_ds.class_names
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")


num_classes = 2
model = Sequential(
    [
        layers.experimental.preprocessing.Rescaling(
            1.0 / 255, input_shape=(image_height, image_width, 3)
        ),
        layers.Conv2D(16, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(num_classes),
    ]
)


model.compile(
    optimizer="Adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)


epochs = 15
history = model.fit(train_ds, validation_data=validation_ds, epochs=epochs)

model.summary()

if model.accuracy > 0.9:
    model.save(f"{model_path}/{random.randint(0, 1000000)}.keras")
