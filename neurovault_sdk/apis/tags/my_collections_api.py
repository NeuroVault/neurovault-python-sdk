# coding: utf-8

"""
    Neurovault API

    All ur images r belong to us  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from neurovault_sdk.paths.api_my_collections_id_atlases_.post import MyCollectionsAtlasesCreate
from neurovault_sdk.paths.api_my_collections_id_atlases_.get import MyCollectionsAtlasesRetrieve
from neurovault_sdk.paths.api_my_collections_.post import MyCollectionsCreate
from neurovault_sdk.paths.api_my_collections_id_datatable_.get import MyCollectionsDatatableRetrieve
from neurovault_sdk.paths.api_my_collections_id_.delete import MyCollectionsDestroy
from neurovault_sdk.paths.api_my_collections_id_images_.post import MyCollectionsImagesCreate
from neurovault_sdk.paths.api_my_collections_id_images_.get import MyCollectionsImagesRetrieve
from neurovault_sdk.paths.api_my_collections_.get import MyCollectionsList
from neurovault_sdk.paths.api_my_collections_id_nidm_results_.post import MyCollectionsNidmResultsCreate
from neurovault_sdk.paths.api_my_collections_id_nidm_results_.get import MyCollectionsNidmResultsRetrieve
from neurovault_sdk.paths.api_my_collections_id_.patch import MyCollectionsPartialUpdate
from neurovault_sdk.paths.api_my_collections_id_.get import MyCollectionsRetrieve
from neurovault_sdk.paths.api_my_collections_id_.put import MyCollectionsUpdate


class MyCollectionsApi(
    MyCollectionsAtlasesCreate,
    MyCollectionsAtlasesRetrieve,
    MyCollectionsCreate,
    MyCollectionsDatatableRetrieve,
    MyCollectionsDestroy,
    MyCollectionsImagesCreate,
    MyCollectionsImagesRetrieve,
    MyCollectionsList,
    MyCollectionsNidmResultsCreate,
    MyCollectionsNidmResultsRetrieve,
    MyCollectionsPartialUpdate,
    MyCollectionsRetrieve,
    MyCollectionsUpdate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
