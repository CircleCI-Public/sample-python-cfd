import connexion

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.database import models
from sqlalchemy.exc import SQLAlchemyError


def add_image():  # noqa: E501
    """Add an image to the restaraunt

    Creates an image. Duplicates are allowed. Returns the image id # noqa: E501

    :param file_name:
    :type file_name: str

    :rtype: InlineResponse200
    """
    uploaded_file = connexion.request.files["fileName"]
    # save the file to the path and then save the path to the 'db'

    try:
        image = models.Image.add(uploaded_file.read())
        return InlineResponse200(image_id=image.id)
    except (SQLAlchemyError, TypeError):
        models.db.session.rollback()
        return Error(400), 400


def delete_image(image_id):  # noqa: E501
    """Remove image

    The imageId must exist  # noqa: E501

    :param image_id: The imageId to delete
    :type image_id: int

    :rtype: None
    """
    try:
        models.Image.delete_image(image_id)
    except (SQLAlchemyError, TypeError):
        models.db.session.rollback()
        return Error(400), 400


def get_image(image_id):  # noqa: E501
    """Get image

    Returns the image as image/png  # noqa: E501

    :param image_id: The imageId of the image to retrieve
    :type image_id: int

    :rtype: file
    """
    if not (image := models.Image.get_image(image_id)):
        return Error(404, "image not found"), 404
    return image.data
