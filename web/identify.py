# Load the model

import os
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
from PIL import Image 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("model1.h5")

image_size = (100, 100)

image_path = os.path.join("all_100", "70033.jpeg") # 4933.jpeg
img = image.load_img(image_path, target_size=image_size)
plt.imshow(img)

# Preprocess image for model prediction
# This step handles scaling and normalization for VGG19
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)
x_ques = x.astype("float32")/255.0
x_quest = x_ques.reshape(x_ques.shape[0], x_ques.shape[1],x_ques.shape[2],3)

x_quest.shape

model.predict(x_quest).round()

print(f"Predicted class: {model.predict_classes(x_quest)}")