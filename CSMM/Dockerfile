# Use the latest Ubuntu base image
FROM ubuntu:latest

# Create a working directory 
WORKDIR /app

# Copy the entry point script into the image
COPY entry.sh /app/entry.sh

# Update packages and install necessary utilities
RUN apt update && apt upgrade -y \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt install -y iputils-ping cron nano git curl wget tzdata openssh-server python3-software-properties jq \
    && apt install -y nodejs npm mysql-server redis-server unzip \
    && rm -rf /var/lib/apt/lists/*

# Set timezone
RUN ln -fs /usr/share/zoneinfo/America/Chicago /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

# Allow root SSH login and enable password authentication
RUN grep -qxF 'PermitRootLogin yes' /etc/ssh/sshd_config || echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config \
    && grep -qxF 'PasswordAuthentication yes' /etc/ssh/sshd_config || echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Set root password
RUN echo 'root:myDocker2024!' | chpasswd

# Install MySQL secure installation commands and create the csmm database and user
RUN service mysql start && \
    mysql -u root -p'myDocker2024!' -e "DELETE FROM mysql.user WHERE User='';" && \
    mysql -u root -p'myDocker2024!' -e "DROP DATABASE IF EXISTS test;" && \
    mysql -u root -p'myDocker2024!' -e "FLUSH PRIVILEGES;" && \
    mysql -u root -p'myDocker2024!' -e "CREATE DATABASE csmm;" && \
    mysql -u root -p'myDocker2024!' -e "CREATE USER 'csmm'@'localhost' IDENTIFIED WITH mysql_native_password BY 'myDocker2024!';" && \
    mysql -u root -p'myDocker2024!' -e "GRANT ALL PRIVILEGES ON csmm.* TO 'csmm'@'localhost';" && \
    mysql -u root -p'myDocker2024!' -e "FLUSH PRIVILEGES;"

# Clone the CSMM repository, ensuring the directory doesn't already exist
RUN rm -rf /app/7-days-to-die-server-manager && \
    git clone https://github.com/CatalysmsServerManager/7-days-to-die-server-manager && \
    cd 7-days-to-die-server-manager && \
    npm install --only=prod

# Copy the default .env file into the cloned directory
COPY .env /app/7-days-to-die-server-manager/.env

# Make sure the entry script is executable
RUN chmod +x /app/entry.sh

# Start MySQL and wait for it to be ready
RUN service mysql start && \
    for i in {30..0}; do \
        if mysql -u root -p'myDocker2024!' -e "SELECT 1"; then \
            break; \
        fi; \
        echo 'Waiting for MySQL...' && sleep 1; \
    done && \
    cd /app/7-days-to-die-server-manager && \
    NODE_ENV=production npm run db:migrate

# Expose port 1337
EXPOSE 1337

# Set the entry point to the script that starts services
ENTRYPOINT ["/app/entry.sh"]
