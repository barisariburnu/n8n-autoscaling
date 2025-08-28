# Use an official Python runtime as a parent image
FROM python:3.9-slim AS builder

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gnupg \
    lsb-release \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add Docker's official GPG key and repository
RUN mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker CLI
RUN apt-get update && \
    apt-get install -y --no-install-recommends docker-ce-cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Install Docker Compose v2
RUN DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d'"' -f4) && \
    mkdir -p ~/.docker/cli-plugins/ && \
    curl -SL "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-linux-x86_64" -o ~/.docker/cli-plugins/docker-compose && \
    chmod +x ~/.docker/cli-plugins/docker-compose

# Copy requirements first to leverage Docker cache
COPY autoscaler/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.9-slim
WORKDIR /app

# Install jq for JSON processing
RUN apt-get update && \
    apt-get install -y --no-install-recommends jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy from builder
COPY --from=builder /usr/bin/docker /usr/bin/docker
COPY --from=builder /root/.docker/cli-plugins/ /usr/local/lib/docker/cli-plugins/
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Ensure docker compose plugin is in PATH
ENV PATH="/usr/local/lib/docker/cli-plugins:${PATH}"

# Copy application files
COPY autoscaler/autoscaler.py .
COPY docker-compose.yml .
COPY Dockerfile .

# Specify the command to run on container start
CMD ["python", "-u", "autoscaler.py"]