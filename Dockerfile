FROM python:3.8-slim

WORKDIR /app

# Copy files to the container
COPY my-tflite-model /app/ 
COPY requirements.txt /app/
COPY run_model.py /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "run_model.py"]

