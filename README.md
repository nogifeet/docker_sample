# Cross-Container Communication with Docker and Flask

This repository demonstrates how to set up cross-container communication using Docker containers running MySQL and a Flask web application. Follow the steps below to get started.

## Prerequisites

- [Docker](https://www.docker.com/get-started)

## Step 1: Create a Docker Network

Create a Docker network to enable communication between containers:

```bash
docker network create mysqlApp
```

