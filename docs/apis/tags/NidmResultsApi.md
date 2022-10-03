<a name="__pageTop"></a>
# neurovault_sdk.apis.tags.nidm_results_api.NidmResultsApi

All URIs are relative to *https://neurovault.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nidm_results_destroy**](#nidm_results_destroy) | **delete** /api/nidm_results/{id}/ | 
[**nidm_results_list**](#nidm_results_list) | **get** /api/nidm_results/ | 
[**nidm_results_partial_update**](#nidm_results_partial_update) | **patch** /api/nidm_results/{id}/ | 
[**nidm_results_retrieve**](#nidm_results_retrieve) | **get** /api/nidm_results/{id}/ | 
[**nidm_results_update**](#nidm_results_update) | **put** /api/nidm_results/{id}/ | 

# **nidm_results_destroy**
<a name="nidm_results_destroy"></a>
> nidm_results_destroy(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import nidm_results_api
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
    api_instance = nidm_results_api.NidmResultsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.nidm_results_destroy(
            path_params=path_params,
        )
    except neurovault_sdk.ApiException as e:
        print("Exception when calling NidmResultsApi->nidm_results_destroy: %s\n" % e)
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
204 | [ApiResponseFor204](#nidm_results_destroy.ApiResponseFor204) | No response body

#### nidm_results_destroy.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nidm_results_list**
<a name="nidm_results_list"></a>
> PaginatedNIDMResultsList nidm_results_list()



### Example

```python
import neurovault_sdk
from neurovault_sdk.apis.tags import nidm_results_api
from neurovault_sdk.model.paginated_nidm_results_list import PaginatedNIDMResultsList
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nidm_results_api.NidmResultsApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 1,
        'offset': 1,
    }
    try:
        api_response = api_instance.nidm_results_list(
            query_params=query_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling NidmResultsApi->nidm_results_list: %s\n" % e)
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
200 | [ApiResponseFor200](#nidm_results_list.ApiResponseFor200) | 

#### nidm_results_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedNIDMResultsList**](../../models/PaginatedNIDMResultsList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nidm_results_partial_update**
<a name="nidm_results_partial_update"></a>
> NIDMResults nidm_results_partial_update(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import nidm_results_api
from neurovault_sdk.model.nidm_results import NIDMResults
from neurovault_sdk.model.patched_nidm_results import PatchedNIDMResults
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
    api_instance = nidm_results_api.NidmResultsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.nidm_results_partial_update(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling NidmResultsApi->nidm_results_partial_update: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    body = PatchedNIDMResults(
        id=1,
        zip_file="zip_file_example",
        ttl_file="ttl_file_example",
        statmaps=[
            Image(
                url="url_example",
                id=1,
                file="file_example",
                collection="collection_example",
                collection_id=1,
                file_size=1,
                name="name_example",
                description="description_example",
                add_date="1970-01-01T00:00:00.00Z",
                modify_date="1970-01-01T00:00:00.00Z",
                is_valid=True,
            )
        ],
        url="url_example",
        collection=1,
        name="name_example",
        description="description_example",
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.nidm_results_partial_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling NidmResultsApi->nidm_results_partial_update: %s\n" % e)
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
[**PatchedNIDMResults**](../../models/PatchedNIDMResults.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedNIDMResults**](../../models/PatchedNIDMResults.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedNIDMResults**](../../models/PatchedNIDMResults.md) |  | 


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
200 | [ApiResponseFor200](#nidm_results_partial_update.ApiResponseFor200) | 

#### nidm_results_partial_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NIDMResults**](../../models/NIDMResults.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nidm_results_retrieve**
<a name="nidm_results_retrieve"></a>
> NIDMResults nidm_results_retrieve(id)



### Example

```python
import neurovault_sdk
from neurovault_sdk.apis.tags import nidm_results_api
from neurovault_sdk.model.nidm_results import NIDMResults
from pprint import pprint
# Defining the host is optional and defaults to https://neurovault.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurovault_sdk.Configuration(
    host = "https://neurovault.org/api"
)

# Enter a context with an instance of the API client
with neurovault_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nidm_results_api.NidmResultsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.nidm_results_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling NidmResultsApi->nidm_results_retrieve: %s\n" % e)
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
200 | [ApiResponseFor200](#nidm_results_retrieve.ApiResponseFor200) | 

#### nidm_results_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NIDMResults**](../../models/NIDMResults.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nidm_results_update**
<a name="nidm_results_update"></a>
> NIDMResults nidm_results_update(idnidm_results)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import nidm_results_api
from neurovault_sdk.model.nidm_results import NIDMResults
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
    api_instance = nidm_results_api.NidmResultsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = NIDMResults(
        id=1,
        zip_file="zip_file_example",
        ttl_file="ttl_file_example",
        statmaps=[
            Image(
                url="url_example",
                id=1,
                file="file_example",
                collection="collection_example",
                collection_id=1,
                file_size=1,
                name="name_example",
                description="description_example",
                add_date="1970-01-01T00:00:00.00Z",
                modify_date="1970-01-01T00:00:00.00Z",
                is_valid=True,
            )
        ],
        url="url_example",
        collection=1,
        name="name_example",
        description="description_example",
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.nidm_results_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling NidmResultsApi->nidm_results_update: %s\n" % e)
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
[**NIDMResults**](../../models/NIDMResults.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**NIDMResults**](../../models/NIDMResults.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**NIDMResults**](../../models/NIDMResults.md) |  | 


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
200 | [ApiResponseFor200](#nidm_results_update.ApiResponseFor200) | 

#### nidm_results_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NIDMResults**](../../models/NIDMResults.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

