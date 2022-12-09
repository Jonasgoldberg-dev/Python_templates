#In this program, the keras library is used to define and train a deep learning model for face mask detection. 
#The model is trained using a dataset of images of people wearing and not wearing masks. 
#Then, the OpenCV library is used to capture video from a webcam and test the model by predicting whether the person in each frame is wearing a mask. 
#You can modify this program to improve the model's accuracy and performance, such as by using a larger and more diverse dataset.

# Import necessary libraries
import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

# Define the network architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(128, 128, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model using the training data
model.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_val, y_val))

# Test the model using the webcam
cap = cv2.VideoCapture(0)

while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Resize the frame to 128x128
  frame = cv2.resize(frame, (128, 128))

  # Convert the frame to a numpy array
  frame = np.array(frame)

  # Add a new dimension to the array to match the model input shape
  frame = np.expand_dims(frame, axis=0)

  # Use the model to predict whether the person in the frame is wearing a mask
  mask_detected = model.predict(frame)

  # Print the prediction
  if mask_detected:
    print("Mask detected")
  else:
    print("No mask detected")

  # Break the loop if the user presses q
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
