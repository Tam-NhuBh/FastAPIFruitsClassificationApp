import tensorflow as tf
import cv2
import numpy as np
import os


class HomeService:
    def __init__(self):
        self.interpreter = tf.lite.Interpreter(model_path="D:\\Nam 3\\HK2\\Mobile\\Final\\web\\fruitModelYOLOv8.tflite")
        self.interpreter.allocate_tensors()

        # Get input and output tensors
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
    async def detect(self, image):
        image2 = cv2.imread("D:\\Nam 3\\HK2\\Mobile\\Final\\web\\image.jpg", cv2.IMREAD_COLOR)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)  # Convert color space from BGR to RGB   
        cv2.imwrite("D:\\Nam 3\\HK2\\Mobile\\Final\\web\\image.jpg", image2)
        # Resize image to match the expected input size
        input_shape2 = self.input_details[0]['shape']
        image2 = cv2.resize(image2, (input_shape2[2], input_shape2[3]))

        # Preprocess image
        image2 = np.expand_dims(image2, axis=0)  # Add batch dimension if needed
        image2 = image2.astype(np.float32) / 255.0  # Normalize pixel values
        image2 = np.transpose(image2, (0, 3, 1, 2)) 
        # Set the input tensor
        self.interpreter.set_tensor(self.input_details[0]['index'], image2)

        # Run the inference
        self.interpreter.invoke()

        # Get the output tensor
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        print(np.argmax(output_data))
        
        
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
