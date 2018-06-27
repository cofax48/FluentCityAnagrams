This a Full-Stack Web app that is built with Docker, Nginx, Flask, Postgres, React,
html/css

## Usage

1. Initialize the Postgres Database in shell
$ docker-compose up -d db

2. Gather all needed libraries and load data from csv to db
$ docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"

3. Bring up the cluster
$ docker-compose up -d

4. Bring online
$ docker-compose up

5. The app runs at http://localhost:8080/

 **This project can be accessed at http://localhost:8080/**

 **Dockerization/Orchestration/Containerization**
  The project uses Docker since I wanted to build an offline version that could host a DB, pull data
  from my txt file, could run my Flask server and handle NGINX proxying.
  I used Docker-Compose to handle my multiple containers and services and wanted a
  one liner to bring up my all containers. I opted against including anything fancier
  like swarm or Kubernetes since there is only one host.
  Docker: Docker, Orchestration: docker-compose.yml NGINX: conf.d/flaskapp.conf

 **The Data Initialization:**
  BackEnd ETL: The project began with downloading the dictionary in txt format.
  When running the second step: Docker-Compose, scripts in database.py run which
  use pandas to parse the data, sqlalchemy to initialize the DB with SQL,
  host it in a Postgres Docker Container and to extract the data from csv,
  transform into the proper format, and load into the container.
  This process can be found in: database.py

 **Server:**
  If I'm writing a server geared for AWS or Heroku, I'll use Django. If I'm building
  a server for Docker I'll opt for Flask (built on NGINX), especially if I'm not dealing with OAuth/CSRF/XSS etc,
  have only one connection, one html page, and a handful of APIs
  The Flask app is found in app.py
