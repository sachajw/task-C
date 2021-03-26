# task-C
## Dockerise task A and B

 // List all running container
        docker ps

        // list all containers
        docker ps -a


        // list all docker images
        docker images

        // build a docker image
        docker build -t <imageName:version> dockerFilePath
        docker build -t task-c .
        
        // run a docker container in daemon mode with ports exposed
        docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>
        docker run -it -d -p 80:5000 task-c

        // access the following url in your browser http://localhost

