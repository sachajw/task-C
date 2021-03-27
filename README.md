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
I used VS Code for these tasks so all extensions and so on are referenced for VS Code.

### Static Code Analyzer
After comparing [Tox](https://tox.readthedocs.io/en/latest/index.html) and [Nox](https://nox.thea.codes/en/stable/).
I choose Nox because it uses the Python language to configure its tests. You can find the cmd line [here](https://nox.thea.codes/en/stable/usage.html)
I created '''noxfile.py''' with two sessions, one for linting using [Flake8](https://flake8.pycqa.org/en/latest/) and [Black](https://pypi.org/project/black/), and one for testing using [Pytest](https://docs.pytest.org/en/stable/contents.html).
I created a '''requirements-test.txt''' file for all the neccessary plugins to be installed for [Pytest](https://docs.pytest.org/en/stable/contents.html).
I created a '''requirements.txt''' file for all the neccessary dependencies to be installed for the [Python](https://www.python.org/) application ```bubble-sort.py'''
This allows me to seperate dependencies for the application and testing and speeds up the [Docker](https://www.docker.com/) container build.

## Running pytest can result in six different exit codes:

**Exit code 0**
All tests were collected and passed successfully

**Exit code 1**
Tests were collected and run but some of the tests failed

**Exit code 2**
Test execution was interrupted by the user

**Exit code 3**
Internal error happened while executing tests

**Exit code 4**
pytest command line usage error

**Exit code 5**
No tests were collected

#### Bubble Sort
Lets describe the Python file bubble-sort.py.

* I used [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/) and [Swagger UI](https://swagger.io/) to generate the API
* Swagger is API development for all the people, in other words Open API and Open Source.
* Please refer to requirements.txt for all required dependencies to run this task.

**List all running containers**
docker ps

**list all containers**
docker ps -a
    
**list all docker images**
docker images
       
**build the docker image**
docker build -t <imageName:version> dockerFilePath
docker build -t task-c .
       
**run the docker container in daemon mode with ports exposed**
docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>
docker run -itdp 80:5000 task-c

**access the following url in your browser** http://localhost

**:heartpulse:LoveYourCodies**

