from neurovault_sdk.paths.api_atlases_id_.get import ApiForget
from neurovault_sdk.paths.api_atlases_id_.put import ApiForput
from neurovault_sdk.paths.api_atlases_id_.delete import ApiFordelete
from neurovault_sdk.paths.api_atlases_id_.patch import ApiForpatch


class ApiAtlasesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
