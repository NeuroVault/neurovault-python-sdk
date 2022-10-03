<a name="__pageTop"></a>
# neurovault_sdk.apis.tags.user_api.UserApi

All URIs are relative to *https://neurovault.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_retrieve**](#user_retrieve) | **get** /api/user/ | 

# **user_retrieve**
<a name="user_retrieve"></a>
> User user_retrieve()



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import user_api
from neurovault_sdk.model.user import User
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.user_retrieve()
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling UserApi->user_retrieve: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_retrieve.ApiResponseFor200) | 

#### user_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**User**](../../models/User.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

