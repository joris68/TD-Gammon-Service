FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn pytest httpx

# Expose the FastAPI port
EXPOSE 8000

# Command to run the application
CMD pytest test_main.py && uvicorn main:app --host 0.0.0.0 --port 8000

