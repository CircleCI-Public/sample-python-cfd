import os
import itertools

import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server import util
from openapi_server.database import IMAGES_PATH, IMAGES

counter = itertools.count(len(IMAGES.keys()))  # this should be the next key if they're integers


def add_image():  # noqa: E501
    """Add an image to the restaraunt

    Creates an image. Duplicates are allowed. Returns the image id # noqa: E501

    :param file_name:
    :type file_name: str

    :rtype: InlineResponse200
    """
    uploaded_file = connexion.request.files['fileName']
    image_id = next(counter)
    file_path= os.path.join(IMAGES_PATH, str(image_id))
    # save the file to the path and then save the path to the 'db'
    uploaded_file.save(file_path)
    IMAGES.update({int(image_id):file_path})
    return InlineResponse200(image_id=image_id)

def delete_image(image_id):  # noqa: E501
    """Remove image

    The imageId must exist  # noqa: E501

    :param image_id: The imageId to delete
    :type image_id: int

    :rtype: None
    """
    if image_id not in IMAGES:
        return Error(404, 'image not found')
    os.remove(IMAGES.get(int(image_id)))
    del IMAGES[int(image_id)]


def get_image(image_id):  # noqa: E501
    """Get image

    Returns the image as image/png  # noqa: E501

    :param image_id: The imageId of the image to retrieve
    :type image_id: int

    :rtype: file
    """
    if image_id not in IMAGES:
        return Error(404, 'image not found')
    with open(IMAGES.get(int(image_id)), 'rb') as f:
         data = f.read()
    return data
