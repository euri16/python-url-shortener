# Python URL Shortener

This project is a simple URL Shortener like bit.ly or goo.gl using Python 3 with the microframework Flask.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The whole app is dockerized, you will need docker to run it:

```
You can find a detailed information for your platform in the [oficial docs](https://docs.docker.com/install/)
```

### Installing

Here are the commands you have to use in order to run it locally:

First you need to start the docker-machine:

```
docker-machine start

```

Then you run this to use the default machine:

```
eval "$(docker-machine env default)"

```
And then you build and deploy the code with this command:

```
docker-compose build [container] && docker-compose up -d
```

In order to get the local IP address in which the project is running you can check the machines with:

```
docker-machine ls
```

## Authors

* **Eury Pérez** - *Initial work* - [LinkedIn](https://www.linkedin.com/in/euryperez/)/[StackOverFlow](https://stackoverflow.com/users/5294761/eury-pérez-beltré)/[Blog](https://medium.com/@euryperez)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
