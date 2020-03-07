[![Build Status](https://travis-ci.com/hyfzur/pythonSelenium.svg?branch=master)](https://travis-ci.com/hyfzur/pythonSelenium)

# About

This project contains examples of basic Selenium WebDriver usage with Python bindings.
In this project, I have made use of the Docker for creating a Selenium grid and running tests.


## Setup

* Download & install [Python](https://www.python.org/downloads/)
* Download & install [PyCharm CE](https://www.jetbrains.com/pycharm/download/#section=mac) (Feel free to use your own editor, I use this)
* Setup [Docker](https://docs.docker.com/get-started/) in the system
* Open the project root directory in a **Terminal** and run ```pip3 install -r requirements.txt```. This will install the packages mentioned in the **requirements.txt** file

## How to start Selenium Grid with Docker image
I have used a ```docker-compose.yml``` for creating the grid and nodes. Open the project root directory and run the following commands:
- To start the grid: ```docker-compose -f ./docker/docker-compose.yaml up -d```
    * This command will download the docker images, if not already downloaded, and end with the below output
        * ```Creating selenium-hub ... done```
        * ```Creating docker_chrome_1  ... done```
        * ```Creating docker_firefox_1 ... done```

- To stop the grid: ```docker-compose -f ./docker/docker-compose.yaml down```
    * Below output would be displayed on the terminal if the grid is started successfully
        * ```Stopping docker_chrome_1  ... done```
        * ```Stopping docker_firefox_1 ... done```
        * ```Stopping selenium-hub     ... done```
        * ```Removing docker_chrome_1  ... done```
        * ```Removing docker_firefox_1 ... done```
        * ```Removing selenium-hub     ... done```
        * ```Removing network docker_default```

- To check if the grid is running, click [here](http://localhost:4444/grid/console)

**P.S.**: The ```docker-compose.yml``` contents have been taken from [this](https://github.com/SeleniumHQ/docker-selenium#version-3) page.

## How to run the tests
* Each test should be run individually
* Right-click within the file or on the filename -> click ```Run``` (or run from the terminal, if you prefer)

**Note**: This execution would not be visual. If they need to be looked at while executing, stop the docker grid, start a local grid, add a browser node. The existing ```hubUrl``` should work as it is. Change if required.
