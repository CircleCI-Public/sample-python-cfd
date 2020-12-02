# Sample Python App - Flask Server

[![CircleCI Build Status](https://circleci.com/gh/CircleCI-Public/sample-python-cfd.svg?style=shield)](https://circleci.com/gh/CircleCI-Public/sample-python-cfd) [![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CircleCI-Public/sample-python-cfd/main/LICENSE)

## Description

The sample python flask app here is designed to demonstrate a typical python CI workflow may look on CircleCI.

You can see the CI pipelines for this application running [live on CircleCI](https://app.circleci.com/pipelines/github/CircleCI-Public/sample-python-cfd?branch=main).

In this sample config, we have a single workflow `build-and-test` which will install and cache our required python packages, and then run tests with `pytest`, a common python testing framework. This config makes use of the [Python orb](https://circleci.com/developer/orbs/orb/circleci/python), a package for CircleCI's config language, which makes writing our config shorter, and easier.

## Getting Started

If you would like to copy the [config.yml](https://github.com/CircleCI-public/sample-python-cfd/blob/main/.circleci/config.yml) and adapt it to your project, be sure to read the comments in the config file to ensure it works for your project. For more details, see the [CircleCI configuration reference](https://circleci.com/docs/2.0/configuration-reference/).

## About This App

This sample application is a flask REST server written in python, and utilizes the connexion framework which allows us build and run the service from an [OpenAPI/Swagger specification](https://swagger.io/specification/).

### Continuous Food Delivery

When you start up the service, you can open [this page](http://localhost:8080/CFD/1.0.0/ui/) in your browser to view the available API endpoints.

[![Swagger UI Screenshot](https://raw.githubusercontent.com/CircleCI-Public/sample-python-cfd/main/.github/img/preview.png)]

### Front-End

CFD(Continuous Food Delivery) is a sample application that relies on a separate UI framework. If you would like to run this project locally with a complete UI, you can use a valid CFD front-end, such as one of the following sample projects:

| Language |  GitHub | Description |
|---|---|---|
|  Javascript (Vue.js) | [Link](https://github.com/CircleCI-Public/sample-javascript-cfd)  | A Javascript Front-End for CFD |

## Run and Test Locally

If you would like to try this application out locally, you can find runtime instructions below.

### Requirements

Python 3.5.2+ OR Docker

### Run Local Server

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t sample-flask .

# starting up a container
docker run -p 8080:8080 sample-flask
```

If not using docker, to run the server, please execute the following from the root directory:

```
pip3 install -r run-requirements.txt
python3 -m openapi_server
```

### Tests

To launch the integration tests, use pytest:

```
pip3 install -r requirements.txt
pytest
```

## Additional Resources

* [CircleCI Docs](https://circleci.com/docs/) - The official CircleCI Documentation website.
* [CircleCI Configuration Reference](https://circleci.com/docs/2.0/configuration-reference/#section=configuration) - From CircleCI Docs, the configuration reference page is one of the most useful pages we have.


## License

This repository is licensed under the MIT license.
The license can be found [here](./LICENSE).

