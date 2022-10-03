from neurovault_sdk.paths.api_nidm_results_id_.get import ApiForget
from neurovault_sdk.paths.api_nidm_results_id_.put import ApiForput
from neurovault_sdk.paths.api_nidm_results_id_.delete import ApiFordelete
from neurovault_sdk.paths.api_nidm_results_id_.patch import ApiForpatch


class ApiNidmResultsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
