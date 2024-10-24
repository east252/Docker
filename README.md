# Docker 

Docker w/o Composer 
Run, naming, first. 

```docker run -ti --rm -name <Container Name> <Image> ```

7D w/ a folder, container named 7Days with ports. 
```docker run -ti -v 7D2D:/app/saves/:z -u 0 -p 26900:26900 -p 26901:26901 -p 26902:26902 --rm --name 7Days a7e6dff822dd /bin/bash```

Pull an image 
`Sudo docker pull <imageName> `

Run an image, interactive, that del the container when done. 
`sudo docker run -ti --rm <imageName> /bin/bash`

Show containers 
`sudo docker ps (also: docker ps --size to show the sizes) `

Show images 
`sudo docker images `

Remove images 
`sudo docker rmi <imageName> `

Save to a new image 
`sudo docker commit -p <Container ID> <New Name> `

Attach a storage 
`sudo docker run -ti --rm -v ~/Docker_Share:/data ubuntu /bin/bash `

Clean up / Delete unused containers, images, networks, etc. 
`sudo docker system prune `

Exit the docker container session. 
`CTRL+P then CTRL+Q `

Enter the docker container session. 
`sudo docker exec -it <Container Name> /bin/bash `

Kill a docker 
`Sudo docker container kill <id> `



# Docker Compose 
Edit a compose.yml to use the commands against. 

Pull an image 
`docker compose pull `

Up - Bring the docker up (detached / in the background) 
`docker compose up -d `

Launch including file location 
`docker compose -f /etc/opt/compose.yml up `

Down - Bring the docker down 
`docker compose down `

# Docker Build
`docker build -t <image name>:<tag> <path>`  
Example (if in same folder): `docker build -t ubuntu:latest . `  
Tag your docker for upload: `docker tag myapp:1.0-ubuntu east252prg/myapp:1.0-ubuntu`


