from neurovault_sdk.paths.api_images_id_.get import ApiForget
from neurovault_sdk.paths.api_images_id_.put import ApiForput
from neurovault_sdk.paths.api_images_id_.delete import ApiFordelete
from neurovault_sdk.paths.api_images_id_.patch import ApiForpatch


class ApiImagesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
