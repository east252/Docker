#!/bin/bash
set -e

# Start services
service ssh start 
service cron start
service mysql start
service redis-server start  # Correcting the service name for Redis
# Wait for MySQL to fully start
sleep 10

# Start the CSMM application
cd /app/7-days-to-die-server-manager
NODE_ENV=production npm run start &

# Keep container alive
tail -f /dev/null

# Execute Entrypoint
exec "$@"
