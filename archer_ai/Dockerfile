# Use the latest Ubuntu base image
FROM ubuntu:latest

# Create a working directory 
WORKDIR /app

# Copy the entry point script into the image
COPY entry.sh /app/entry.sh

# Update packages and install necessary utilities
RUN apt update && apt upgrade -y \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt install -y iputils-ping cron nano curl wget tzdata openssh-server unzip \
    && rm -rf /var/lib/apt/lists/*

# Set timezone
RUN ln -fs /usr/share/zoneinfo/America/Chicago /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

# Install Python
RUN apt update && apt install -y python3 python3-pip

# Install Ollama (assuming there's an official Ubuntu package or using a script)
# If Ollama provides a specific install script, you might add it here
RUN curl -fsSL https://ollama.com/install.sh | sh

# Allow root SSH login and enable password authentication
RUN grep -qxF 'PermitRootLogin yes' /etc/ssh/sshd_config || echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config \
    && grep -qxF 'PasswordAuthentication yes' /etc/ssh/sshd_config || echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Set root password
RUN echo 'root:myArcherDocker2024!' | chpasswd

# Make sure the entry script is executable
RUN chmod +x /app/entry.sh

# Expose port 51434
EXPOSE 51434

# Set the entry point to the script that starts services
ENTRYPOINT ["/app/entry.sh"]

# BUILD
# docker build -t archer_ai:v1 .
