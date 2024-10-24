# An entry file is what launches each time a container starts. Add its location to the CMD portion of the container creation.
#!/bin/bash
set -e

# Start services
service ssh start
service cron start

# Keep container alive
tail -f /dev/null

# Execute Entrypoint
exec "$@"
