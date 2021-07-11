FROM python:3.8.0-slim

# Make a directory for our application
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code
COPY /src .

# Run the application
CMD ["python", "SimpleCalculator.py"]