# Dockerfile

# Stage 1: Use a reliable Python base image
# We use a slim version to keep the final image small
FROM python:3.13-slim

# Install the system dependency: PortAudio development files
# This is the step that fixes your build error.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        portaudio19-dev \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory for the application
WORKDIR /app

# Copy the requirements file first to leverage Docker layer caching
# Changes to your code won't trigger a re-install of requirements
COPY requirements.txt .

# Install Python dependencies
# This command will now succeed because portaudio19-dev is installed
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Define the command to run the application
# You MUST replace 'main.py' with the actual entry point of your script
CMD ["python", "code.py"]
