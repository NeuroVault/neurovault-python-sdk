# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from neurovault_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_ATLASES_ = "/api/atlases/"
    API_ATLASES_ID_ = "/api/atlases/{id}/"
    API_ATLASES_ID_DATATABLE_ = "/api/atlases/{id}/datatable/"
    API_ATLASES_ID_REGIONS_TABLE_ = "/api/atlases/{id}/regions_table/"
    API_ATLASES_ATLAS_QUERY_REGION_ = "/api/atlases/atlas_query_region/"
    API_ATLASES_ATLAS_QUERY_VOXEL_ = "/api/atlases/atlas_query_voxel/"
    API_COLLECTIONS_ = "/api/collections/"
    API_COLLECTIONS_ID_ = "/api/collections/{id}/"
    API_COLLECTIONS_ID_ATLASES_ = "/api/collections/{id}/atlases/"
    API_COLLECTIONS_ID_DATATABLE_ = "/api/collections/{id}/datatable/"
    API_COLLECTIONS_ID_IMAGES_ = "/api/collections/{id}/images/"
    API_COLLECTIONS_ID_NIDM_RESULTS_ = "/api/collections/{id}/nidm_results/"
    API_IMAGES_ = "/api/images/"
    API_IMAGES_ID_ = "/api/images/{id}/"
    API_IMAGES_ID_DATATABLE_ = "/api/images/{id}/datatable/"
    API_MY_COLLECTIONS_ = "/api/my_collections/"
    API_MY_COLLECTIONS_ID_ = "/api/my_collections/{id}/"
    API_MY_COLLECTIONS_ID_ATLASES_ = "/api/my_collections/{id}/atlases/"
    API_MY_COLLECTIONS_ID_DATATABLE_ = "/api/my_collections/{id}/datatable/"
    API_MY_COLLECTIONS_ID_IMAGES_ = "/api/my_collections/{id}/images/"
    API_MY_COLLECTIONS_ID_NIDM_RESULTS_ = "/api/my_collections/{id}/nidm_results/"
    API_NIDM_RESULTS_ = "/api/nidm_results/"
    API_NIDM_RESULTS_ID_ = "/api/nidm_results/{id}/"
    API_USER_ = "/api/user/"
