date: 2021-03-26
title: "Task-C"
linkTitle: "Task-C"
author: Sacha Wharton
---

*Contributed by Sacha Wharton* 

@sachajw

<div>
<img src="./images/ufo-abduct-cow.jpg" alt="task-c" height="192px" width="192x" />
</div>
<p></p>

# task-C
## Dockerise task A + B = C

### IDE ---> VS Code 
* I used VS Code for these tasks so all extensions and so on are referenced for VS Code.

### Static Code Analyzer
* I opted for the extension from Microsoft called Pylance which can be searched for and installed by clicking on the extensions icon which looks like a flat rubix cube.
* Fast, feature-rich language support for Python. Pylance is an extension that works alongside Python in Visual Studio Code to provide performant language support. Under the hood, Pylance is powered by Pyright, Microsoft's static type checking tool. Using Pyright, Pylance has the ability to supercharge your Python IntelliSense experience with rich type information, helping you write better code faster.

The Pylance name is a small ode to Monty Python's Lancelot who was the first knight to answer the bridgekeeper's questions in the Holy Grail.

### Bubble Sort
Lets describe the Python file bubble-sort.py.

* I used [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/) and [Swagger UI](https://swagger.io/) to generate the API
* Swagger is API development for all the people, in other words Open API and Open Source.
* Please refer to requirements.txt for all required dependencies to run this task.

### List all running containers
docker ps

### list all containers
docker ps -a
    
### list all docker images
docker images
       
### build the docker image
docker build -t <imageName:version> dockerFilePath
docker build -t task-c .
       
### run the docker container in daemon mode with ports exposed
docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>
docker run -itdp 80:5000 task-c

### access the following url in your browser http://localhost

# LoveYourCodies

