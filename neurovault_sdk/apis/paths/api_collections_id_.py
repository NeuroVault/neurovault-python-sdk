from neurovault_sdk.paths.api_collections_id_.get import ApiForget
from neurovault_sdk.paths.api_collections_id_.put import ApiForput
from neurovault_sdk.paths.api_collections_id_.delete import ApiFordelete
from neurovault_sdk.paths.api_collections_id_.patch import ApiForpatch


class ApiCollectionsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
