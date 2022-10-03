import typing_extensions

from neurovault_sdk.apis.tags import TagValues
from neurovault_sdk.apis.tags.atlases_api import AtlasesApi
from neurovault_sdk.apis.tags.collections_api import CollectionsApi
from neurovault_sdk.apis.tags.images_api import ImagesApi
from neurovault_sdk.apis.tags.my_collections_api import MyCollectionsApi
from neurovault_sdk.apis.tags.nidm_results_api import NidmResultsApi
from neurovault_sdk.apis.tags.user_api import UserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ATLASES: AtlasesApi,
        TagValues.COLLECTIONS: CollectionsApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.MY_COLLECTIONS: MyCollectionsApi,
        TagValues.NIDM_RESULTS: NidmResultsApi,
        TagValues.USER: UserApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ATLASES: AtlasesApi,
        TagValues.COLLECTIONS: CollectionsApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.MY_COLLECTIONS: MyCollectionsApi,
        TagValues.NIDM_RESULTS: NidmResultsApi,
        TagValues.USER: UserApi,
    }
)
