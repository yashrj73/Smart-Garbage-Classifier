
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
path=r"C:\Users\inspiron\Desktop\Train1"
path_=r"C:\Users\inspiron\Desktop\Test1"

#CNN
classifier = Sequential()
# Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
# Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Flattening
classifier.add(Flatten())
# Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Fitting CNN to the images
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.2,zoom_range = 0.2,horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory(path,target_size = (64, 64),batch_size = 32, class_mode = 'binary')
test_set = test_datagen.flow_from_directory(path_,target_size = (64, 64),batch_size = 32,class_mode = 'binary')
classifier.fit_generator(training_set,steps_per_epoch = 250,epochs = 20,validation_data = test_set,validation_steps = 50)

#Making new predictions
import cv2
import os
camera = cv2.VideoCapture(0)
return_value, image = camera.read()
path = r'C:\Users\Mohit Kumar\Desktop'
cv2.imwrite(os.path.join(path , 'trial.jpg'), image)

from keras.preprocessing import image
import win32com.client
import numpy as np
test_image = image.load_img(r'C:\Users\Mohit Kumar\Desktop\trial.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("This is a bio degradable object")
    
else:
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("This is a bio degradable object")

