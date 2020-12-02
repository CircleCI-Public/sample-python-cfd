# Sample Python App - Flask Server

TODO: links in this document will need updating after migration to another github organization.

[![CircleCI Build Status](https://circleci.com/gh/dsayling/sample-flask.svg?style=shield)](https://circleci.com/gh/dsayling/sample-flask) [![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/dsayling/sample-flask/main/LICENSE)

## Description

The sample app here is designed to demonstrate a simple python CircleCI pipeline. CircleCI pipelines are the top-level events that contains your workflows - they can be thought of as the triggering event, e.g. when you push a commit to a branch, and the workflows associated with that trigger event.

You can see the CI pipelines for this application running [live on CircleCI](https://app.circleci.com/pipelines/github/dsayling/sample-flask?branch=main).

The definition of the workflow is contained in the CircleCI configuration file, aka [config.yml](https://github.com/dsayling/sample-flask/blob/main/.circleci/config.yml). In this sample configuration file, we're creating a workflow to simply install our required python packages, with the [CircleCI python orb](https://circleci.com/developer/orbs/orb/circleci/python), and then run tests with `pytest`, a common python testing framework.

## Getting Started

If you would like to copy the [config.yml](https://github.com/dsayling/sample-flask/blob/main/.circleci/config.yml) and adapt it to your project, be sure to read the comments in the config file to ensure it works for your project.

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

* [CircleCI Docs](https://circleci.com/docs/) - The official CircleCI Documentation website.
* [CircleCI Configuration Reference](https://circleci.com/docs/2.0/configuration-reference/#section=configuration) - From CircleCI Docs, the configuration reference page is one of the most useful pages we have.


## License

This repository is licensed under the MIT license.
The license can be found [here](./LICENSE).

