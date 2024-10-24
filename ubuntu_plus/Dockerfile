# Use the latest Ubuntu base image
FROM ubuntu:latest

# Create a working directory
WORKDIR /app

# Copy the entry point script into the image
COPY entry.sh /app/entry.sh

# Update packages and install necessary utilities
RUN apt update && apt upgrade -y \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt install -y iputils-ping cron nano git curl wget tzdata openssh-server

# Set timezone
RUN ln -fs /usr/share/zoneinfo/America/Chicago /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

# Allow root SSH login and enable password authentication
RUN grep -qxF 'PermitRootLogin yes' /etc/ssh/sshd_config || echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config \
    && grep -qxF 'PasswordAuthentication yes' /etc/ssh/sshd_config || echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Set root password
RUN echo 'root:myDocker2024!' | chpasswd

# Make sure the entry script is executable
RUN chmod +x /app/entry.sh

# Set the entry point to the script that starts services
ENTRYPOINT ["/app/entry.sh"]
