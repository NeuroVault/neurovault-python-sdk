# coding: utf-8

"""
    Neurovault API

    All ur images r belong to us  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from neurovault_sdk.paths.api_atlases_atlas_query_region_.get import AtlasesAtlasQueryRegionRetrieve
from neurovault_sdk.paths.api_atlases_atlas_query_voxel_.get import AtlasesAtlasQueryVoxelRetrieve
from neurovault_sdk.paths.api_atlases_id_datatable_.get import AtlasesDatatableRetrieve
from neurovault_sdk.paths.api_atlases_id_.delete import AtlasesDestroy
from neurovault_sdk.paths.api_atlases_.get import AtlasesList
from neurovault_sdk.paths.api_atlases_id_.patch import AtlasesPartialUpdate
from neurovault_sdk.paths.api_atlases_id_regions_table_.get import AtlasesRegionsTableRetrieve
from neurovault_sdk.paths.api_atlases_id_.get import AtlasesRetrieve
from neurovault_sdk.paths.api_atlases_id_.put import AtlasesUpdate


class AtlasesApi(
    AtlasesAtlasQueryRegionRetrieve,
    AtlasesAtlasQueryVoxelRetrieve,
    AtlasesDatatableRetrieve,
    AtlasesDestroy,
    AtlasesList,
    AtlasesPartialUpdate,
    AtlasesRegionsTableRetrieve,
    AtlasesRetrieve,
    AtlasesUpdate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass