# CSMM Consolidated Docker

This docker has some very key characteristics

1. Ubuntu, CSMM, MySQL, Redis - are all built in.
2. Services are set to auto launch on startup.
3. Defaults are set and ready for you to edit.
4. Persistant storage is set for MySQL. You will want to backup your final .env .

The key is to launch, edit, and keep your container in tact. Back up your .env in case you ever overwrite the container.

##### How To:

1. Using docker, pull the image (`docker pull east252prg/csmm:latest`)
2. Copy the docker compose file below.
3. Launch the docker using the compose file (in the same directory, execute in terminal: `docker compose up -d`).
4. Join the shell so you can make some edits (`docker exec -it csmm /bin/bash`).
5. Navigate to /app/7-days-to-die-server-manager/.env and edit the .env file. You need to follow instructions: [CSMM .ENV INSTRUCTIONS](https://docs.csmm.app/en/CSMM/self-host/configuration.html)
6. Un-comment the needed lines, and add the info for your API key, discord bot, etc. Be sure to update the IP address at the top.

##### Final Thoughts

1. Feel free to change all of the passwords. Using the defaults is not advised.
2. Its recommended to set up a reverse proxy and secure your connection.
3. I dont warrant anything. Its a fun project for me.
4. Open the firewall to 1337 if self hosting and forward to the host machine's IP. Users will reach it at `http://<Your IP>:1337`
5. Know where the CSMM discord is, so that you can search for solutions to problems that may come up: [Join CSMM Discord!](https://discord.com/invite/EwyDdNA)
