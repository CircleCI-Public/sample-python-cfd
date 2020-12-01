# Sample Python App - Flask Server

TODO: links in this document will need updating after migration to another github organization.

[![CircleCI Build Status](https://circleci.com/gh/dsayling/sample-flask.svg?style=shield)](https://circleci.com/gh/dsayling/sample-flask) [![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/dsayling/sample-flask/main/LICENSE)

## Description

The sample app here is designed to demonstrate a simple python CircleCI workflows.

In this sample pipeline, we're simply installing dev python packages, with the [CircleCI python orb](https://circleci.com/developer/orbs/orb/circleci/python), and then running tests with pytest.

## Getting Started

You can see the CI pipeline for this application running [live on CircleCI](https://app.circleci.com/pipelines/github/dsayling/sample-flask?branch=main).

Here you can find the CircleCI configuration file, aka [config.yml](https://github.com/dsayling/sample-flask/blob/main/.circleci/config.yml).

## Adapting to your workflow

If you would like to copy the [config.yml](https://github.com/dsayling/sample-flask/blob/main/.circleci/config.yml), be sure to follow the steps below to ensure the config.yml works for your project:

* Find the definition of the executor and ensure the correct version of python is used for your application via the convenience image tag on the [CircleCI Developer Hub](https://circleci.com/developer/images/image/cimg/python).
* Find the `install-packages` command in the configuration file, here you can define an alternative `requirements.txt` file, if necessary. The application here contains two `requirements.txt`, one that defines runtime requirements and another that combines the former with the additional test requirements.
* The `install-packages` command will effective run `pip install requirements.txt` as a part of your config, while automatically caching those dependencies for faster CI runs later.
* Find the `Run Tests` step and include any additional runtime arguments necessary for `pytest` or update it to the testing tool you're using, e.g. `nosetests`.

## Build and Test Locally

If you would like to try this application out locally, you can find runtime instructions below.

### Requirements

Python 3.5.2+ OR Docker

### Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t sample-flask .

# starting up a container
docker run -p 8080:8080 sample-flask
```

### Usage

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

[CircleCI Docs](https://circleci.com/docs/) - The official CircleCI Documentation website.
[CircleCI Configuration Reference](https://circleci.com/docs/2.0/configuration-reference/#section=configuration) - From CircleCI Docs, the configuration reference page is one of the most useful pages we have.


## License

This repository is licensed under the MIT license.
The license can be found [here](./LICENSE).

