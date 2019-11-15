========================
PyLadies Docker Workshop
========================

Welcome everyone! 🐍 🌈

The purpose of this workshop is to provide an interactive introduction to `Docker`_.

This repository contains a configurable ``Hello World`` web server application. The goal
of this exercise is to containerize the application and run it as an image.

Prerequisites
=============

- Docker
- Git

Instructions
============

The application code is located within the `/helloworld`_ directory. This is a simple Flask
application which takes in one environment variable, ``NAME`` and runs a web server on
port 5000.

Complete the Dockerfile
-----------------------

An empty Dockerfile_ has been provided has been provided, to complete this:

1. Choose a base image

2. Add your project files

3. Install project with pip

4. Configure the ``ENTRYPOINT`` to run the project

Run your container
------------------

1. Build the container with a tag, replacing <IMAGE-TAG> with ``hello-world:latest``::

   $ docker build -t <IMAGE-TAG>

2. Run the container::

   $ docker run 5000:5000 --env NAME=<YOUR NAME> <IMAGE-TAG>

3. Go to https://localhost:5000

4. List the running docker processes::

   $ docker ps

5. View the logs of the container::

   $ docker logs <CONTAINER-ID>

6. Stop the container::

   $ docker stop <IMAGE-TAG>


**Optional**: Docker Compose
----------------------------

`Docker Compose`_ is a tool which can be used to define and run multiple docker containers.
An empty `docker-compose`_ file has been provided for you to fill in.

Complete the docker-compose file
--------------------------------

Provide the version of ``Compose`` to use::

    version: "3"

Define the container, giving it a name ``hello-world``, and providing an image tag with
version ``latest`` to use::

    services:
      hello-world:
        image: hello-world:latest

Map port ``5000`` on the container to port ``5000`` on the host machine::

        ports:
          - "5000:5000"

Define your environment variable::

        environment:
          NAME: <YOUR NAME>

Use docker-compose!
-------------------

To run::

  $ docker-compose up

To stop::

  $ docker-compose down


.. _Docker: https://www.docker.com/
.. _/helloworld: ./helloworld
.. _Dockerfile: ./helloworld/Dockerfile
.. _Docker Compose: https://docs.docker.com/compose/
.. _docker-compose: docker-compose.yaml
