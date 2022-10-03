<a name="__pageTop"></a>
# neurovault_sdk.apis.tags.atlases_api.AtlasesApi

All URIs are relative to *https://neurovault.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**atlases_atlas_query_region_retrieve**](#atlases_atlas_query_region_retrieve) | **get** /api/atlases/atlas_query_region/ | 
[**atlases_atlas_query_voxel_retrieve**](#atlases_atlas_query_voxel_retrieve) | **get** /api/atlases/atlas_query_voxel/ | 
[**atlases_datatable_retrieve**](#atlases_datatable_retrieve) | **get** /api/atlases/{id}/datatable/ | 
[**atlases_destroy**](#atlases_destroy) | **delete** /api/atlases/{id}/ | 
[**atlases_list**](#atlases_list) | **get** /api/atlases/ | 
[**atlases_partial_update**](#atlases_partial_update) | **patch** /api/atlases/{id}/ | 
[**atlases_regions_table_retrieve**](#atlases_regions_table_retrieve) | **get** /api/atlases/{id}/regions_table/ | 
[**atlases_retrieve**](#atlases_retrieve) | **get** /api/atlases/{id}/ | 
[**atlases_update**](#atlases_update) | **put** /api/atlases/{id}/ | 

# **atlases_atlas_query_region_retrieve**
<a name="atlases_atlas_query_region_retrieve"></a>
> Atlas atlases_atlas_query_region_retrieve()



Returns a dictionary containing a list of voxels that match the searched term (or related searches) in the specified atlas.  Parameters: region, collection, atlas  Example: '/api/atlases/atlas_query_region/?region=middle frontal gyrus&collection=Harvard-Oxford cortical and subcortical structural atlases&atlas=HarvardOxford cort maxprob thr25 1mm'

### Example

```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from neurovault_sdk.model.atlas import Atlas
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.atlases_atlas_query_region_retrieve()
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_atlas_query_region_retrieve: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#atlases_atlas_query_region_retrieve.ApiResponseFor200) | 

#### atlases_atlas_query_region_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **atlases_atlas_query_voxel_retrieve**
<a name="atlases_atlas_query_voxel_retrieve"></a>
> Atlas atlases_atlas_query_voxel_retrieve()



Returns the region name that matches specified coordinates in the specified atlas.  Parameters: x, y, z, collection, atlas  Example: '/api/atlases/atlas_query_voxel/?x=30&y=30&z=30&collection=Harvard-Oxford cortical and subcortical structural atlases&atlas=HarvardOxford cort maxprob thr25 1mm'

### Example

```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from neurovault_sdk.model.atlas import Atlas
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.atlases_atlas_query_voxel_retrieve()
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_atlas_query_voxel_retrieve: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#atlases_atlas_query_voxel_retrieve.ApiResponseFor200) | 

#### atlases_atlas_query_voxel_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **atlases_datatable_retrieve**
<a name="atlases_datatable_retrieve"></a>
> Atlas atlases_datatable_retrieve(id)



A wrapper around standard retrieve() request that formats the object for the Datatables plugin.

### Example

```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from neurovault_sdk.model.atlas import Atlas
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.atlases_datatable_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_datatable_retrieve: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#atlases_datatable_retrieve.ApiResponseFor200) | 

#### atlases_datatable_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **atlases_destroy**
<a name="atlases_destroy"></a>
> atlases_destroy(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = neurovault_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.atlases_destroy(
            path_params=path_params,
        )
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_destroy: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#atlases_destroy.ApiResponseFor204) | No response body

#### atlases_destroy.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **atlases_list**
<a name="atlases_list"></a>
> PaginatedAtlasList atlases_list()



### Example

```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from neurovault_sdk.model.paginated_atlas_list import PaginatedAtlasList
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 1,
        'offset': 1,
    }
    try:
        api_response = api_instance.atlases_list(
            query_params=query_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#atlases_list.ApiResponseFor200) | 

#### atlases_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedAtlasList**](../../models/PaginatedAtlasList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **atlases_partial_update**
<a name="atlases_partial_update"></a>
> Atlas atlases_partial_update(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from neurovault_sdk.model.patched_atlas import PatchedAtlas
from neurovault_sdk.model.atlas import Atlas
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = neurovault_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.atlases_partial_update(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_partial_update: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    body = PatchedAtlas(
        url="url_example",
        id=1,
        file="file_example",
        collection="collection_example",
        collection_id=1,
        file_size=1,
        label_description_file="label_description_file_example",
        name="name_example",
        description="description_example",
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
        is_valid=True,
        surface_left_file="surface_left_file_example",
        surface_right_file="surface_right_file_example",
        data_origin=None,
        target_template_image=None,
        subject_species="subject_species_example",
        figure="figure_example",
        handedness=None,
        age=3.14,
        gender=None,
        race=None,
        ethnicity=None,
        bmi=3.14,
        fat_percentage=3.14,
        waist_hip_ratio=3.14,
        mean_pds_score=3.14,
        tanner_stage=None,
        days_since_menstruation=3.14,
        hours_since_last_meal=3.14,
        bis_bas_score=3.14,
        spsrq_score=3.14,
        bis11_score=3.14,
        thumbnail="thumbnail_example",
        reduced_representation="reduced_representation_example",
        data=dict(
            "key": None,
        ),
    )
    try:
        api_response = api_instance.atlases_partial_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_partial_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded, SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedAtlas**](../../models/PatchedAtlas.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedAtlas**](../../models/PatchedAtlas.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedAtlas**](../../models/PatchedAtlas.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#atlases_partial_update.ApiResponseFor200) | 

#### atlases_partial_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **atlases_regions_table_retrieve**
<a name="atlases_regions_table_retrieve"></a>
> Atlas atlases_regions_table_retrieve(id)



A wrapper around standard retrieve() request that formats the object for the regions_table plugin.

### Example

```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from neurovault_sdk.model.atlas import Atlas
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.atlases_regions_table_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_regions_table_retrieve: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#atlases_regions_table_retrieve.ApiResponseFor200) | 

#### atlases_regions_table_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **atlases_retrieve**
<a name="atlases_retrieve"></a>
> Atlas atlases_retrieve(id)



### Example

```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from neurovault_sdk.model.atlas import Atlas
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.atlases_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_retrieve: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#atlases_retrieve.ApiResponseFor200) | 

#### atlases_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **atlases_update**
<a name="atlases_update"></a>
> Atlas atlases_update(idatlas)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import atlases_api
from neurovault_sdk.model.atlas import Atlas
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = neurovault_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = atlases_api.AtlasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = Atlas(
        url="url_example",
        id=1,
        file="file_example",
        collection="collection_example",
        collection_id=1,
        file_size=1,
        label_description_file="label_description_file_example",
        name="name_example",
        description="description_example",
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
        is_valid=True,
        surface_left_file="surface_left_file_example",
        surface_right_file="surface_right_file_example",
        data_origin=None,
        target_template_image=None,
        subject_species="subject_species_example",
        figure="figure_example",
        handedness=None,
        age=3.14,
        gender=None,
        race=None,
        ethnicity=None,
        bmi=3.14,
        fat_percentage=3.14,
        waist_hip_ratio=3.14,
        mean_pds_score=3.14,
        tanner_stage=None,
        days_since_menstruation=3.14,
        hours_since_last_meal=3.14,
        bis_bas_score=3.14,
        spsrq_score=3.14,
        bis11_score=3.14,
        thumbnail="thumbnail_example",
        reduced_representation="reduced_representation_example",
        data=dict(
            "key": None,
        ),
    )
    try:
        api_response = api_instance.atlases_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling AtlasesApi->atlases_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded, SchemaForRequestBodyMultipartFormData] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#atlases_update.ApiResponseFor200) | 

#### atlases_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Atlas**](../../models/Atlas.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

