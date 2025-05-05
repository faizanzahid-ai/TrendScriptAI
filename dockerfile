# Base image with Python
FROM python:3.11.12-slim

# Set env vars (fixed format)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    curl \
    build-essential \
    && apt-get clean

# Install yt-dlp
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && \
    chmod a+rx /usr/local/bin/yt-dlp

# Set work directory
WORKDIR /app

# Copy code
COPY . /app/

# Install Python dependencies (use the correct torch package)
RUN pip install --upgrade pip && \
    pip install torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install -r requirements.txt

# Expose gRPC (50051) and Streamlit (8501)
EXPOSE 50051
EXPOSE 8501

# Default command: run both gRPC and Streamlit via a simple shell script
CMD ["bash", "start.sh"]
