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

Install and run the application
-------------------------------

Get started with the usual approach to installing and running the application. We can
later compare this approach with how you would run the application with Docker.

.. code:: bash

   $ cd helloworld/app
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   $ pip install -e .
   $ python app.py

Navigate to http://localhost:5000/

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

   $ docker build . -t <IMAGE-TAG>

Once it's built, you can show your built images with::

   $ docker images

2. Run the container::

   $ docker run -p 5000:5000 --env NAME=<YOUR NAME> <IMAGE-TAG>

3. Go to https://localhost:5000

4. List the running docker processes, and take note of your container's ID::

   $ docker ps

5. View the logs of the container::

   $ docker logs <CONTAINER-ID>

6. Connect to the container::

   $ docker exec -it <CONTAINER-ID> sh

From within the container you can show the environment variables::

   $ echo $NAME

7. Stop the container::

   $ docker stop <CONTAINER-ID>


Image Optimisation
------------------

If you used the ``python:3.7`` base image, you will see that the image size is ~900MB when
you run::

   $ docker images

This is quite a large image, for an application of this size! The official Python base
images have ``slim`` variants with fewer system libraries installed, such
as ``python:3.7-slim``. Does using this base image have an impact on your image size?

Docker Compose
--------------

`Docker Compose`_ is a tool which can be used to define and run multiple docker containers.
An empty `docker-compose`_ file has been provided for you to fill in.

You can install it from here_.

Complete the docker-compose file
--------------------------------

**Note**: if you use Linux, you will need to install this separately from Docker, you can
find install instructions here_. For MacOS and Windows, it will already be installed.

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

From within the root directory of the repository, run::

  $ docker-compose up -d

To stop::

  $ docker-compose down

Further learning
----------------

Well done! You've just:

- Made a Dockerfile
- Built, run and explored the docker container
- Used Docker Compose

That's a lot to take in! What's next?

If you want to learn more about Docker and containers, we recommend:

- `Multi-stage`_ Docker builds
- Pushing to and pulling from Dockerhub_
- Conference talk: `Container Operator's Manual by Alice Goldfuss`_

.. _Docker: https://www.docker.com/
.. _/helloworld: ./helloworld
.. _Dockerfile: ./helloworld/app/Dockerfile
.. _Docker Compose: https://docs.docker.com/compose/
.. _docker-compose: docker-compose.yaml
.. _Dockerhub: https://docs.docker.com/docker-hub/repos/
.. _Multi-stage: https://docs.docker.com/develop/develop-images/multistage-build/
.. _Container Operator's Manual by Alice Goldfuss: https://www.youtube.com/watch?v=Fm2tDgf40ss
.. _here: https://docs.docker.com/compose/install/
