import tensorflow as tf
import cv2
import numpy as np
import os


class HomeService:
    def __init__(self):
        self.interpreter = tf.lite.Interpreter(model_path="fruitModelYOLOv8.tflite")
        self.interpreter.allocate_tensors()

        # Get input and output tensors
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
    async def detect(self, image):
      
        input_shape = self.input_details[0]['shape']
        image = cv2.resize(image, (input_shape[2], input_shape[3]))

        # Preprocess image
        image = np.expand_dims(image, axis=0)  # Add batch dimension if needed
        image = image.astype(np.float32) / 255.0  # Normalize pixel values
        image = np.transpose(image, (0, 3, 1, 2)) 
        self.interpreter.set_tensor(self.input_details[0]['index'], image)

        # Run the inference
        self.interpreter.invoke()

        # Get the output tensor
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        print( np.argmax(output_data))
        print( np.max(output_data))
        if np.max(output_data) < 0.5:
            return "Unknown"
        
        return np.argmax(output_data)
