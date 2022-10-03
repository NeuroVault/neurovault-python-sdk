from neurovault_sdk.paths.api_my_collections_id_.get import ApiForget
from neurovault_sdk.paths.api_my_collections_id_.put import ApiForput
from neurovault_sdk.paths.api_my_collections_id_.delete import ApiFordelete
from neurovault_sdk.paths.api_my_collections_id_.patch import ApiForpatch


class ApiMyCollectionsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
