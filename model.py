from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Input
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.optimizer_v1 import Adam
import tensorflow as tf

def create_model():
    model = Sequential(
        [
            Input(shape=(None,11)),
            Dense(units=256, activation="relu", name="L1"),
            Dense(units=128, activation="relu", name="L2"),
            Dense(units=3, name="Output")
        ]
    )

    model.compile(optimizer=Adam(learning_rate=0.001), loss=tf.keras.losses.mean_squared_error)

    return model