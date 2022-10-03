import typing_extensions

from neurovault_sdk.paths import PathValues
from neurovault_sdk.apis.paths.api_atlases_ import ApiAtlases
from neurovault_sdk.apis.paths.api_atlases_id_ import ApiAtlasesId
from neurovault_sdk.apis.paths.api_atlases_id_datatable_ import ApiAtlasesIdDatatable
from neurovault_sdk.apis.paths.api_atlases_id_regions_table_ import ApiAtlasesIdRegionsTable
from neurovault_sdk.apis.paths.api_atlases_atlas_query_region_ import ApiAtlasesAtlasQueryRegion
from neurovault_sdk.apis.paths.api_atlases_atlas_query_voxel_ import ApiAtlasesAtlasQueryVoxel
from neurovault_sdk.apis.paths.api_collections_ import ApiCollections
from neurovault_sdk.apis.paths.api_collections_id_ import ApiCollectionsId
from neurovault_sdk.apis.paths.api_collections_id_atlases_ import ApiCollectionsIdAtlases
from neurovault_sdk.apis.paths.api_collections_id_datatable_ import ApiCollectionsIdDatatable
from neurovault_sdk.apis.paths.api_collections_id_images_ import ApiCollectionsIdImages
from neurovault_sdk.apis.paths.api_collections_id_nidm_results_ import ApiCollectionsIdNidmResults
from neurovault_sdk.apis.paths.api_images_ import ApiImages
from neurovault_sdk.apis.paths.api_images_id_ import ApiImagesId
from neurovault_sdk.apis.paths.api_images_id_datatable_ import ApiImagesIdDatatable
from neurovault_sdk.apis.paths.api_my_collections_ import ApiMyCollections
from neurovault_sdk.apis.paths.api_my_collections_id_ import ApiMyCollectionsId
from neurovault_sdk.apis.paths.api_my_collections_id_atlases_ import ApiMyCollectionsIdAtlases
from neurovault_sdk.apis.paths.api_my_collections_id_datatable_ import ApiMyCollectionsIdDatatable
from neurovault_sdk.apis.paths.api_my_collections_id_images_ import ApiMyCollectionsIdImages
from neurovault_sdk.apis.paths.api_my_collections_id_nidm_results_ import ApiMyCollectionsIdNidmResults
from neurovault_sdk.apis.paths.api_nidm_results_ import ApiNidmResults
from neurovault_sdk.apis.paths.api_nidm_results_id_ import ApiNidmResultsId
from neurovault_sdk.apis.paths.api_user_ import ApiUser

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_ATLASES_: ApiAtlases,
        PathValues.API_ATLASES_ID_: ApiAtlasesId,
        PathValues.API_ATLASES_ID_DATATABLE_: ApiAtlasesIdDatatable,
        PathValues.API_ATLASES_ID_REGIONS_TABLE_: ApiAtlasesIdRegionsTable,
        PathValues.API_ATLASES_ATLAS_QUERY_REGION_: ApiAtlasesAtlasQueryRegion,
        PathValues.API_ATLASES_ATLAS_QUERY_VOXEL_: ApiAtlasesAtlasQueryVoxel,
        PathValues.API_COLLECTIONS_: ApiCollections,
        PathValues.API_COLLECTIONS_ID_: ApiCollectionsId,
        PathValues.API_COLLECTIONS_ID_ATLASES_: ApiCollectionsIdAtlases,
        PathValues.API_COLLECTIONS_ID_DATATABLE_: ApiCollectionsIdDatatable,
        PathValues.API_COLLECTIONS_ID_IMAGES_: ApiCollectionsIdImages,
        PathValues.API_COLLECTIONS_ID_NIDM_RESULTS_: ApiCollectionsIdNidmResults,
        PathValues.API_IMAGES_: ApiImages,
        PathValues.API_IMAGES_ID_: ApiImagesId,
        PathValues.API_IMAGES_ID_DATATABLE_: ApiImagesIdDatatable,
        PathValues.API_MY_COLLECTIONS_: ApiMyCollections,
        PathValues.API_MY_COLLECTIONS_ID_: ApiMyCollectionsId,
        PathValues.API_MY_COLLECTIONS_ID_ATLASES_: ApiMyCollectionsIdAtlases,
        PathValues.API_MY_COLLECTIONS_ID_DATATABLE_: ApiMyCollectionsIdDatatable,
        PathValues.API_MY_COLLECTIONS_ID_IMAGES_: ApiMyCollectionsIdImages,
        PathValues.API_MY_COLLECTIONS_ID_NIDM_RESULTS_: ApiMyCollectionsIdNidmResults,
        PathValues.API_NIDM_RESULTS_: ApiNidmResults,
        PathValues.API_NIDM_RESULTS_ID_: ApiNidmResultsId,
        PathValues.API_USER_: ApiUser,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_ATLASES_: ApiAtlases,
        PathValues.API_ATLASES_ID_: ApiAtlasesId,
        PathValues.API_ATLASES_ID_DATATABLE_: ApiAtlasesIdDatatable,
        PathValues.API_ATLASES_ID_REGIONS_TABLE_: ApiAtlasesIdRegionsTable,
        PathValues.API_ATLASES_ATLAS_QUERY_REGION_: ApiAtlasesAtlasQueryRegion,
        PathValues.API_ATLASES_ATLAS_QUERY_VOXEL_: ApiAtlasesAtlasQueryVoxel,
        PathValues.API_COLLECTIONS_: ApiCollections,
        PathValues.API_COLLECTIONS_ID_: ApiCollectionsId,
        PathValues.API_COLLECTIONS_ID_ATLASES_: ApiCollectionsIdAtlases,
        PathValues.API_COLLECTIONS_ID_DATATABLE_: ApiCollectionsIdDatatable,
        PathValues.API_COLLECTIONS_ID_IMAGES_: ApiCollectionsIdImages,
        PathValues.API_COLLECTIONS_ID_NIDM_RESULTS_: ApiCollectionsIdNidmResults,
        PathValues.API_IMAGES_: ApiImages,
        PathValues.API_IMAGES_ID_: ApiImagesId,
        PathValues.API_IMAGES_ID_DATATABLE_: ApiImagesIdDatatable,
        PathValues.API_MY_COLLECTIONS_: ApiMyCollections,
        PathValues.API_MY_COLLECTIONS_ID_: ApiMyCollectionsId,
        PathValues.API_MY_COLLECTIONS_ID_ATLASES_: ApiMyCollectionsIdAtlases,
        PathValues.API_MY_COLLECTIONS_ID_DATATABLE_: ApiMyCollectionsIdDatatable,
        PathValues.API_MY_COLLECTIONS_ID_IMAGES_: ApiMyCollectionsIdImages,
        PathValues.API_MY_COLLECTIONS_ID_NIDM_RESULTS_: ApiMyCollectionsIdNidmResults,
        PathValues.API_NIDM_RESULTS_: ApiNidmResults,
        PathValues.API_NIDM_RESULTS_ID_: ApiNidmResultsId,
        PathValues.API_USER_: ApiUser,
    }
)
