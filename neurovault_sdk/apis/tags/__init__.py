# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from neurovault_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ATLASES = "atlases"
    COLLECTIONS = "collections"
    IMAGES = "images"
    MY_COLLECTIONS = "my_collections"
    NIDM_RESULTS = "nidm_results"
    USER = "user"
