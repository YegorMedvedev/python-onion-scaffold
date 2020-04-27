# python-onion-scaffold
Simple clean code architecture application based on Python.
Application split on different layers as classic Onion structure describes.


## How To?
### Preconditions
Since `.env` files are not committed, expects that the following format for that file is gonna be used:
```
ENV="development" // environment
PORT=5000 // used port
NAME="python-onion-scaffold" // project name
POSTGRESQL_URL="postgresql://localhost:5432/postgres" // database
``` 

I also believe, that `python` installed on your computer with version 3.8+

Since, I use `postgres`, please ensure that it is installed as well. Basic setup with `public` schema should be more that enough.  

### Local Deploy (Docker)
You have to be sure that Docker is installed and running on your local machine.
The following command will build and run an image:
```shell script
$ docker build -t python-onion-scaffold:latest .
$ docker run \
    --name=python-onion-scaffold \
    -d \
    -v ./config/:/usr/src/app/config/ \
    python-onion-scaffold:latest 
```

Meanwhile, if you are going to use docker-compose, please consider the following script:
```yaml
version: '3'
services:
  python-onion-scaffold:
    image: 'python-onion-scaffold:latest'
    env_file:
     - ./config/.env
    environment:
     - PORT="${PORT}"
```

## Layers Description
### API Layer
Public API layer which is responsible for the client client interactions.
Ideally that layer only validates request and follows response contracts, however, it also makes a decision what service should resolve a request.
Contracts between API and Service are defined in Core.  


### Core Layer (Domain)
Internal layer which is visible across all the application layers. 
Is responsible for contract between layers or inside the layers.

**Beware! Implementation is not a part of this layer!**

- domain entity interfaces (between layers interfaces)
- data access interfaces (interfaces for domain entity repositories)
- business logic interfaces (interface between service layer interactors)


### Services (Use cases)
Business logic is here, as simple as that :)


### Infrastructure
Dirty work layer. Is responsible for data access, meanwhile also defines some common infrastructure utilities (DI, logger, config, etc)