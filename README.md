# task-C
## Dockerise task A and B

//


// List all running containers
       docker ps

       // list all containers
       docker ps -a
       
       // list all docker images
       docker images
       
       // build the docker image
       docker build -t <imageName:version> dockerFilePath
       docker build -t task-c .
       
       // run the docker container in daemon mode with ports exposed
       docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>
       docker run -itdp 80:5000 task-c

       // access the following url in your browser http://localhost
       #LoveYourCodies

