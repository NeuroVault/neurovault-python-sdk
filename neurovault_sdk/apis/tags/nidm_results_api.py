# coding: utf-8

"""
    Neurovault API

    All ur images r belong to us  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from neurovault_sdk.paths.api_nidm_results_id_.delete import NidmResultsDestroy
from neurovault_sdk.paths.api_nidm_results_.get import NidmResultsList
from neurovault_sdk.paths.api_nidm_results_id_.patch import NidmResultsPartialUpdate
from neurovault_sdk.paths.api_nidm_results_id_.get import NidmResultsRetrieve
from neurovault_sdk.paths.api_nidm_results_id_.put import NidmResultsUpdate


class NidmResultsApi(
    NidmResultsDestroy,
    NidmResultsList,
    NidmResultsPartialUpdate,
    NidmResultsRetrieve,
    NidmResultsUpdate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
