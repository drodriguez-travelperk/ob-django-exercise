## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Tests](#tests)


## Prerequisites

Before you get started, make sure you have the following prerequisites in place:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose)

## Usage

1. **Start Docker Compose**:

   Open a terminal window and from the project's root directory run:

   ```bash
   docker-compose up
   ```

2. **Access to the API docs**:

   Open a web browser and navigate to [Swagger doccumentation](http://127.0.0.1:8000/api/docs)

## Tests

1. **Run tests from container**
   
   Execute the following command:

   ```bash
   docker-compose run --rm app sh -c "python manage.py test"
   ```

   This command starts a temporary container from the app service and execute a Django test suite and remove the container once the tests are completed 