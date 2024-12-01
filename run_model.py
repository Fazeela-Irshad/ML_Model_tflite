import tflite_runtime.interpreter as tflite
import numpy as np

# Load the model
interpreter = tflite.Interpreter(model_path="my-tflite-model")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Dummy input data (adjust shape/type for your model)
input_shape = input_details[0]['shape']
input_data = np.ones(input_shape, dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

# Run inference
interpreter.invoke()

# Get output data
output_data = interpreter.get_tensor(output_details[0]['index'])
print("Model Output:", output_data)
