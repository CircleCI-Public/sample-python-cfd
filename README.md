# Sample Python App - Flask Server

[![CircleCI Build Status](https://circleci.com/gh/dsayling/sample-flask.svg?style=shield)](https://circleci.com/gh/dsayling/sample-flask) [![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CircleCI-Public/cimg-python/master/LICENSE)

## Description

The sample app here is designed to demonstrate one of the most simple python CircleCI workflows. Here in this application we're simply installing dev python packages and then running tests with pytest.

## Getting Started

You can see this CICD pipeline running live on CircleCI: https://app.circleci.com/pipelines/github/dsayling/sample-flask?branch=main

TODO: Show config here

## Adapting your workflow

Something something about copying config file into your project
Link to convience images for other versions.
Set the expecations for the user copying the config and how they can use it.

## Build and Test Locally

If you would like to try this application out locally, you can find runtime instructions below.

### Requirements

Python 3.5.2+

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
pip3 install -r requirements.txt
python3 -m openapi_server
```

### Tests

To launch the integration tests, use tox:

```
sudo pip install tox
tox
```

## Additional Resources

[CircleCI Docs](https://circleci.com/docs/) - The official CircleCI Documentation website.
[CircleCI Configuration Reference](https://circleci.com/docs/2.0/configuration-reference/#section=configuration) - From CircleCI Docs, the configuration reference page is one of the most useful pages we have.


## License

This repository is licensed under the MIT license.
The license can be found [here](./LICENSE).

