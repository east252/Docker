#!/bin/bash
set -e

# Start services
service ssh start 
service cron start

# Keep container alive
tail -f /dev/null

# Execute Entrypoint
exec "$@"