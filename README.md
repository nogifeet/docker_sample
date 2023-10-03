# Cross-Container Communication with Docker and Flask

This repository demonstrates how to set up cross-container communication using Docker containers running MySQL and a Flask web application. Follow the steps below to get started.

## Prerequisites

- [Docker](https://www.docker.com/get-started)

## Step 1: Create a Docker Network

Create a Docker network to enable communication between containers:

```bash
docker network create mysqlApp
```

## Step 2: Pull the latest MySQL docker image from docker hub

```bash
docker pull mysql:latest
```

## Step 3: Run Mysql Container With Configurations 

```bash
docker run -d --rm -it --name mysql-container --network mysqlApp \
    -e MYSQL_ROOT_PASSWORD=helloWorld123 -e MYSQL_DATABASE=test \
    mysql:latest
```

## Step 4: Create Flask image from the backend/Dockerfile

```bash
docker build -t flaskapp:latest ./backend/.
```

## Step 5: Run Flask Container With Configurations

```bash
docker run -d --rm -it --name flask-container \
    -e FLASK_HOST=0.0.0.0 -e FLASK_PORT=8080 \
    -p 4000:8080 --network mysqlApp \
    -v flaskAppLogData:/app/logs/ flaskapp:latest
```

## Step 6: Interact with the API using Postman 

```bash
# Insert Some dummy records
http://0.0.0.0:4000/store
```

```json
{
    "name": "test1",
    "age" : 12,
    "email" : "test@123.com",
    "country" : "India"
}

{
    "name": "test2",
    "age" : 22,
    "email" : "test@456.com",
    "country" : "Japan"
}

{
    "name": "test3",
    "age" : 32,
    "email" : "test@789.com",
    "country" : "South Korea"
}
```

```bash
# View Inserted records
http://0.0.0.0:4000/customers
```




