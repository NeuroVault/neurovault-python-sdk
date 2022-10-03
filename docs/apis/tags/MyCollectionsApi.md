<a name="__pageTop"></a>
# neurovault_sdk.apis.tags.my_collections_api.MyCollectionsApi

All URIs are relative to *https://neurovault.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**my_collections_atlases_create**](#my_collections_atlases_create) | **post** /api/my_collections/{id}/atlases/ | 
[**my_collections_atlases_retrieve**](#my_collections_atlases_retrieve) | **get** /api/my_collections/{id}/atlases/ | 
[**my_collections_create**](#my_collections_create) | **post** /api/my_collections/ | 
[**my_collections_datatable_retrieve**](#my_collections_datatable_retrieve) | **get** /api/my_collections/{id}/datatable/ | 
[**my_collections_destroy**](#my_collections_destroy) | **delete** /api/my_collections/{id}/ | 
[**my_collections_images_create**](#my_collections_images_create) | **post** /api/my_collections/{id}/images/ | 
[**my_collections_images_retrieve**](#my_collections_images_retrieve) | **get** /api/my_collections/{id}/images/ | 
[**my_collections_list**](#my_collections_list) | **get** /api/my_collections/ | 
[**my_collections_nidm_results_create**](#my_collections_nidm_results_create) | **post** /api/my_collections/{id}/nidm_results/ | 
[**my_collections_nidm_results_retrieve**](#my_collections_nidm_results_retrieve) | **get** /api/my_collections/{id}/nidm_results/ | 
[**my_collections_partial_update**](#my_collections_partial_update) | **patch** /api/my_collections/{id}/ | 
[**my_collections_retrieve**](#my_collections_retrieve) | **get** /api/my_collections/{id}/ | 
[**my_collections_update**](#my_collections_update) | **put** /api/my_collections/{id}/ | 

# **my_collections_atlases_create**
<a name="my_collections_atlases_create"></a>
> Collection my_collections_atlases_create(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_atlases_create(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_atlases_create: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    body = Collection(
        id=1,
        url="url_example",
        download_url="download_url_example",
        owner=1,
        contributors="contributors_example",
        owner_name="owner_name_example",
        number_of_images=1,
        name="name_example",
        doi="doi_example",
        authors="authors_example",
        paper_url="paper_url_example",
        journal_name="journal_name_example",
        description="description_example",
        full_dataset_url="full_dataset_url_example",
        private=None,
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
        doi_add_date="1970-01-01T00:00:00.00Z",
        type_of_design=None,
        number_of_imaging_runs=-2147483648,
        number_of_experimental_units=-2147483648,
        length_of_runs=3.14,
        length_of_blocks=3.14,
        length_of_trials="length_of_trials_example",
        optimization=True,
        optimization_method="optimization_method_example",
        subject_age_mean=3.14,
        subject_age_min=3.14,
        subject_age_max=3.14,
        handedness=None,
        proportion_male_subjects=0.0,
        inclusion_exclusion_criteria="inclusion_exclusion_criteria_example",
        number_of_rejected_subjects=-2147483648,
        group_comparison=True,
        group_description="group_description_example",
        scanner_make="scanner_make_example",
        scanner_model="scanner_model_example",
        field_strength=3.14,
        pulse_sequence="pulse_sequence_example",
        parallel_imaging="parallel_imaging_example",
        field_of_view=3.14,
        matrix_size=-2147483648,
        slice_thickness=3.14,
        skip_distance=3.14,
        acquisition_orientation="acquisition_orientation_example",
        order_of_acquisition=None,
        repetition_time=3.14,
        echo_time=3.14,
        flip_angle=3.14,
        software_package="software_package_example",
        software_version="software_version_example",
        order_of_preprocessing_operations="order_of_preprocessing_operations_example",
        quality_control="quality_control_example",
        used_b0_unwarping=True,
        b0_unwarping_software="b0_unwarping_software_example",
        used_slice_timing_correction=True,
        slice_timing_correction_software="slice_timing_correction_software_example",
        used_motion_correction=True,
        motion_correction_software="motion_correction_software_example",
        motion_correction_reference="motion_correction_reference_example",
        motion_correction_metric="motion_correction_metric_example",
        motion_correction_interpolation="motion_correction_interpolation_example",
        used_motion_susceptibiity_correction=True,
        used_intersubject_registration=True,
        intersubject_registration_software="intersubject_registration_software_example",
        intersubject_transformation_type=None,
        nonlinear_transform_type="nonlinear_transform_type_example",
        transform_similarity_metric="transform_similarity_metric_example",
        interpolation_method="interpolation_method_example",
        object_image_type="object_image_type_example",
        functional_coregistered_to_structural=True,
        functional_coregistration_method="functional_coregistration_method_example",
        coordinate_space=None,
        target_template_image="target_template_image_example",
        target_resolution=3.14,
        used_smoothing=True,
        smoothing_type="smoothing_type_example",
        smoothing_fwhm=3.14,
        resampled_voxel_size=3.14,
        intrasubject_model_type="intrasubject_model_type_example",
        intrasubject_estimation_type="intrasubject_estimation_type_example",
        intrasubject_modeling_software="intrasubject_modeling_software_example",
        hemodynamic_response_function="hemodynamic_response_function_example",
        used_temporal_derivatives=True,
        used_dispersion_derivatives=True,
        used_motion_regressors=True,
        used_reaction_time_regressor=True,
        used_orthogonalization=True,
        orthogonalization_description="orthogonalization_description_example",
        used_high_pass_filter=True,
        high_pass_filter_method="high_pass_filter_method_example",
        autocorrelation_model="autocorrelation_model_example",
        group_model_type="group_model_type_example",
        group_estimation_type="group_estimation_type_example",
        group_modeling_software="group_modeling_software_example",
        group_inference_type=None,
        group_model_multilevel="group_model_multilevel_example",
        group_repeated_measures=True,
        group_repeated_measures_method="group_repeated_measures_method_example",
        nutbrain_hunger_state=None,
        nutbrain_food_viewing_conditions="nutbrain_food_viewing_conditions_example",
        nutbrain_food_choice_type="nutbrain_food_choice_type_example",
        nutbrain_taste_conditions="nutbrain_taste_conditions_example",
        nutbrain_odor_conditions="nutbrain_odor_conditions_example",
        communities=[
            1
        ],
    )
    try:
        api_response = api_instance.my_collections_atlases_create(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_atlases_create: %s\n" % e)
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
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


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
200 | [ApiResponseFor200](#my_collections_atlases_create.ApiResponseFor200) | 

#### my_collections_atlases_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_atlases_retrieve**
<a name="my_collections_atlases_retrieve"></a>
> Collection my_collections_atlases_retrieve(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_atlases_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_atlases_retrieve: %s\n" % e)
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
200 | [ApiResponseFor200](#my_collections_atlases_retrieve.ApiResponseFor200) | 

#### my_collections_atlases_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_create**
<a name="my_collections_create"></a>
> Collection my_collections_create()



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only optional values
    body = Collection(
        id=1,
        url="url_example",
        download_url="download_url_example",
        owner=1,
        contributors="contributors_example",
        owner_name="owner_name_example",
        number_of_images=1,
        name="name_example",
        doi="doi_example",
        authors="authors_example",
        paper_url="paper_url_example",
        journal_name="journal_name_example",
        description="description_example",
        full_dataset_url="full_dataset_url_example",
        private=None,
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
        doi_add_date="1970-01-01T00:00:00.00Z",
        type_of_design=None,
        number_of_imaging_runs=-2147483648,
        number_of_experimental_units=-2147483648,
        length_of_runs=3.14,
        length_of_blocks=3.14,
        length_of_trials="length_of_trials_example",
        optimization=True,
        optimization_method="optimization_method_example",
        subject_age_mean=3.14,
        subject_age_min=3.14,
        subject_age_max=3.14,
        handedness=None,
        proportion_male_subjects=0.0,
        inclusion_exclusion_criteria="inclusion_exclusion_criteria_example",
        number_of_rejected_subjects=-2147483648,
        group_comparison=True,
        group_description="group_description_example",
        scanner_make="scanner_make_example",
        scanner_model="scanner_model_example",
        field_strength=3.14,
        pulse_sequence="pulse_sequence_example",
        parallel_imaging="parallel_imaging_example",
        field_of_view=3.14,
        matrix_size=-2147483648,
        slice_thickness=3.14,
        skip_distance=3.14,
        acquisition_orientation="acquisition_orientation_example",
        order_of_acquisition=None,
        repetition_time=3.14,
        echo_time=3.14,
        flip_angle=3.14,
        software_package="software_package_example",
        software_version="software_version_example",
        order_of_preprocessing_operations="order_of_preprocessing_operations_example",
        quality_control="quality_control_example",
        used_b0_unwarping=True,
        b0_unwarping_software="b0_unwarping_software_example",
        used_slice_timing_correction=True,
        slice_timing_correction_software="slice_timing_correction_software_example",
        used_motion_correction=True,
        motion_correction_software="motion_correction_software_example",
        motion_correction_reference="motion_correction_reference_example",
        motion_correction_metric="motion_correction_metric_example",
        motion_correction_interpolation="motion_correction_interpolation_example",
        used_motion_susceptibiity_correction=True,
        used_intersubject_registration=True,
        intersubject_registration_software="intersubject_registration_software_example",
        intersubject_transformation_type=None,
        nonlinear_transform_type="nonlinear_transform_type_example",
        transform_similarity_metric="transform_similarity_metric_example",
        interpolation_method="interpolation_method_example",
        object_image_type="object_image_type_example",
        functional_coregistered_to_structural=True,
        functional_coregistration_method="functional_coregistration_method_example",
        coordinate_space=None,
        target_template_image="target_template_image_example",
        target_resolution=3.14,
        used_smoothing=True,
        smoothing_type="smoothing_type_example",
        smoothing_fwhm=3.14,
        resampled_voxel_size=3.14,
        intrasubject_model_type="intrasubject_model_type_example",
        intrasubject_estimation_type="intrasubject_estimation_type_example",
        intrasubject_modeling_software="intrasubject_modeling_software_example",
        hemodynamic_response_function="hemodynamic_response_function_example",
        used_temporal_derivatives=True,
        used_dispersion_derivatives=True,
        used_motion_regressors=True,
        used_reaction_time_regressor=True,
        used_orthogonalization=True,
        orthogonalization_description="orthogonalization_description_example",
        used_high_pass_filter=True,
        high_pass_filter_method="high_pass_filter_method_example",
        autocorrelation_model="autocorrelation_model_example",
        group_model_type="group_model_type_example",
        group_estimation_type="group_estimation_type_example",
        group_modeling_software="group_modeling_software_example",
        group_inference_type=None,
        group_model_multilevel="group_model_multilevel_example",
        group_repeated_measures=True,
        group_repeated_measures_method="group_repeated_measures_method_example",
        nutbrain_hunger_state=None,
        nutbrain_food_viewing_conditions="nutbrain_food_viewing_conditions_example",
        nutbrain_food_choice_type="nutbrain_food_choice_type_example",
        nutbrain_taste_conditions="nutbrain_taste_conditions_example",
        nutbrain_odor_conditions="nutbrain_odor_conditions_example",
        communities=[
            1
        ],
    )
    try:
        api_response = api_instance.my_collections_create(
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded, SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#my_collections_create.ApiResponseFor201) | 

#### my_collections_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_datatable_retrieve**
<a name="my_collections_datatable_retrieve"></a>
> Collection my_collections_datatable_retrieve(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_datatable_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_datatable_retrieve: %s\n" % e)
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
200 | [ApiResponseFor200](#my_collections_datatable_retrieve.ApiResponseFor200) | 

#### my_collections_datatable_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_destroy**
<a name="my_collections_destroy"></a>
> my_collections_destroy(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_destroy(
            path_params=path_params,
        )
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_destroy: %s\n" % e)
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
204 | [ApiResponseFor204](#my_collections_destroy.ApiResponseFor204) | No response body

#### my_collections_destroy.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_images_create**
<a name="my_collections_images_create"></a>
> Collection my_collections_images_create(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_images_create(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_images_create: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    body = Collection(
        id=1,
        url="url_example",
        download_url="download_url_example",
        owner=1,
        contributors="contributors_example",
        owner_name="owner_name_example",
        number_of_images=1,
        name="name_example",
        doi="doi_example",
        authors="authors_example",
        paper_url="paper_url_example",
        journal_name="journal_name_example",
        description="description_example",
        full_dataset_url="full_dataset_url_example",
        private=None,
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
        doi_add_date="1970-01-01T00:00:00.00Z",
        type_of_design=None,
        number_of_imaging_runs=-2147483648,
        number_of_experimental_units=-2147483648,
        length_of_runs=3.14,
        length_of_blocks=3.14,
        length_of_trials="length_of_trials_example",
        optimization=True,
        optimization_method="optimization_method_example",
        subject_age_mean=3.14,
        subject_age_min=3.14,
        subject_age_max=3.14,
        handedness=None,
        proportion_male_subjects=0.0,
        inclusion_exclusion_criteria="inclusion_exclusion_criteria_example",
        number_of_rejected_subjects=-2147483648,
        group_comparison=True,
        group_description="group_description_example",
        scanner_make="scanner_make_example",
        scanner_model="scanner_model_example",
        field_strength=3.14,
        pulse_sequence="pulse_sequence_example",
        parallel_imaging="parallel_imaging_example",
        field_of_view=3.14,
        matrix_size=-2147483648,
        slice_thickness=3.14,
        skip_distance=3.14,
        acquisition_orientation="acquisition_orientation_example",
        order_of_acquisition=None,
        repetition_time=3.14,
        echo_time=3.14,
        flip_angle=3.14,
        software_package="software_package_example",
        software_version="software_version_example",
        order_of_preprocessing_operations="order_of_preprocessing_operations_example",
        quality_control="quality_control_example",
        used_b0_unwarping=True,
        b0_unwarping_software="b0_unwarping_software_example",
        used_slice_timing_correction=True,
        slice_timing_correction_software="slice_timing_correction_software_example",
        used_motion_correction=True,
        motion_correction_software="motion_correction_software_example",
        motion_correction_reference="motion_correction_reference_example",
        motion_correction_metric="motion_correction_metric_example",
        motion_correction_interpolation="motion_correction_interpolation_example",
        used_motion_susceptibiity_correction=True,
        used_intersubject_registration=True,
        intersubject_registration_software="intersubject_registration_software_example",
        intersubject_transformation_type=None,
        nonlinear_transform_type="nonlinear_transform_type_example",
        transform_similarity_metric="transform_similarity_metric_example",
        interpolation_method="interpolation_method_example",
        object_image_type="object_image_type_example",
        functional_coregistered_to_structural=True,
        functional_coregistration_method="functional_coregistration_method_example",
        coordinate_space=None,
        target_template_image="target_template_image_example",
        target_resolution=3.14,
        used_smoothing=True,
        smoothing_type="smoothing_type_example",
        smoothing_fwhm=3.14,
        resampled_voxel_size=3.14,
        intrasubject_model_type="intrasubject_model_type_example",
        intrasubject_estimation_type="intrasubject_estimation_type_example",
        intrasubject_modeling_software="intrasubject_modeling_software_example",
        hemodynamic_response_function="hemodynamic_response_function_example",
        used_temporal_derivatives=True,
        used_dispersion_derivatives=True,
        used_motion_regressors=True,
        used_reaction_time_regressor=True,
        used_orthogonalization=True,
        orthogonalization_description="orthogonalization_description_example",
        used_high_pass_filter=True,
        high_pass_filter_method="high_pass_filter_method_example",
        autocorrelation_model="autocorrelation_model_example",
        group_model_type="group_model_type_example",
        group_estimation_type="group_estimation_type_example",
        group_modeling_software="group_modeling_software_example",
        group_inference_type=None,
        group_model_multilevel="group_model_multilevel_example",
        group_repeated_measures=True,
        group_repeated_measures_method="group_repeated_measures_method_example",
        nutbrain_hunger_state=None,
        nutbrain_food_viewing_conditions="nutbrain_food_viewing_conditions_example",
        nutbrain_food_choice_type="nutbrain_food_choice_type_example",
        nutbrain_taste_conditions="nutbrain_taste_conditions_example",
        nutbrain_odor_conditions="nutbrain_odor_conditions_example",
        communities=[
            1
        ],
    )
    try:
        api_response = api_instance.my_collections_images_create(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_images_create: %s\n" % e)
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
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


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
200 | [ApiResponseFor200](#my_collections_images_create.ApiResponseFor200) | 

#### my_collections_images_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_images_retrieve**
<a name="my_collections_images_retrieve"></a>
> Collection my_collections_images_retrieve(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_images_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_images_retrieve: %s\n" % e)
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
200 | [ApiResponseFor200](#my_collections_images_retrieve.ApiResponseFor200) | 

#### my_collections_images_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_list**
<a name="my_collections_list"></a>
> PaginatedCollectionList my_collections_list()



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.paginated_collection_list import PaginatedCollectionList
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 1,
        'offset': 1,
    }
    try:
        api_response = api_instance.my_collections_list(
            query_params=query_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_list: %s\n" % e)
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
200 | [ApiResponseFor200](#my_collections_list.ApiResponseFor200) | 

#### my_collections_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedCollectionList**](../../models/PaginatedCollectionList.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_nidm_results_create**
<a name="my_collections_nidm_results_create"></a>
> Collection my_collections_nidm_results_create(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_nidm_results_create(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_nidm_results_create: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    body = Collection(
        id=1,
        url="url_example",
        download_url="download_url_example",
        owner=1,
        contributors="contributors_example",
        owner_name="owner_name_example",
        number_of_images=1,
        name="name_example",
        doi="doi_example",
        authors="authors_example",
        paper_url="paper_url_example",
        journal_name="journal_name_example",
        description="description_example",
        full_dataset_url="full_dataset_url_example",
        private=None,
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
        doi_add_date="1970-01-01T00:00:00.00Z",
        type_of_design=None,
        number_of_imaging_runs=-2147483648,
        number_of_experimental_units=-2147483648,
        length_of_runs=3.14,
        length_of_blocks=3.14,
        length_of_trials="length_of_trials_example",
        optimization=True,
        optimization_method="optimization_method_example",
        subject_age_mean=3.14,
        subject_age_min=3.14,
        subject_age_max=3.14,
        handedness=None,
        proportion_male_subjects=0.0,
        inclusion_exclusion_criteria="inclusion_exclusion_criteria_example",
        number_of_rejected_subjects=-2147483648,
        group_comparison=True,
        group_description="group_description_example",
        scanner_make="scanner_make_example",
        scanner_model="scanner_model_example",
        field_strength=3.14,
        pulse_sequence="pulse_sequence_example",
        parallel_imaging="parallel_imaging_example",
        field_of_view=3.14,
        matrix_size=-2147483648,
        slice_thickness=3.14,
        skip_distance=3.14,
        acquisition_orientation="acquisition_orientation_example",
        order_of_acquisition=None,
        repetition_time=3.14,
        echo_time=3.14,
        flip_angle=3.14,
        software_package="software_package_example",
        software_version="software_version_example",
        order_of_preprocessing_operations="order_of_preprocessing_operations_example",
        quality_control="quality_control_example",
        used_b0_unwarping=True,
        b0_unwarping_software="b0_unwarping_software_example",
        used_slice_timing_correction=True,
        slice_timing_correction_software="slice_timing_correction_software_example",
        used_motion_correction=True,
        motion_correction_software="motion_correction_software_example",
        motion_correction_reference="motion_correction_reference_example",
        motion_correction_metric="motion_correction_metric_example",
        motion_correction_interpolation="motion_correction_interpolation_example",
        used_motion_susceptibiity_correction=True,
        used_intersubject_registration=True,
        intersubject_registration_software="intersubject_registration_software_example",
        intersubject_transformation_type=None,
        nonlinear_transform_type="nonlinear_transform_type_example",
        transform_similarity_metric="transform_similarity_metric_example",
        interpolation_method="interpolation_method_example",
        object_image_type="object_image_type_example",
        functional_coregistered_to_structural=True,
        functional_coregistration_method="functional_coregistration_method_example",
        coordinate_space=None,
        target_template_image="target_template_image_example",
        target_resolution=3.14,
        used_smoothing=True,
        smoothing_type="smoothing_type_example",
        smoothing_fwhm=3.14,
        resampled_voxel_size=3.14,
        intrasubject_model_type="intrasubject_model_type_example",
        intrasubject_estimation_type="intrasubject_estimation_type_example",
        intrasubject_modeling_software="intrasubject_modeling_software_example",
        hemodynamic_response_function="hemodynamic_response_function_example",
        used_temporal_derivatives=True,
        used_dispersion_derivatives=True,
        used_motion_regressors=True,
        used_reaction_time_regressor=True,
        used_orthogonalization=True,
        orthogonalization_description="orthogonalization_description_example",
        used_high_pass_filter=True,
        high_pass_filter_method="high_pass_filter_method_example",
        autocorrelation_model="autocorrelation_model_example",
        group_model_type="group_model_type_example",
        group_estimation_type="group_estimation_type_example",
        group_modeling_software="group_modeling_software_example",
        group_inference_type=None,
        group_model_multilevel="group_model_multilevel_example",
        group_repeated_measures=True,
        group_repeated_measures_method="group_repeated_measures_method_example",
        nutbrain_hunger_state=None,
        nutbrain_food_viewing_conditions="nutbrain_food_viewing_conditions_example",
        nutbrain_food_choice_type="nutbrain_food_choice_type_example",
        nutbrain_taste_conditions="nutbrain_taste_conditions_example",
        nutbrain_odor_conditions="nutbrain_odor_conditions_example",
        communities=[
            1
        ],
    )
    try:
        api_response = api_instance.my_collections_nidm_results_create(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_nidm_results_create: %s\n" % e)
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
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


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
200 | [ApiResponseFor200](#my_collections_nidm_results_create.ApiResponseFor200) | 

#### my_collections_nidm_results_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_nidm_results_retrieve**
<a name="my_collections_nidm_results_retrieve"></a>
> Collection my_collections_nidm_results_retrieve(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_nidm_results_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_nidm_results_retrieve: %s\n" % e)
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
200 | [ApiResponseFor200](#my_collections_nidm_results_retrieve.ApiResponseFor200) | 

#### my_collections_nidm_results_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_partial_update**
<a name="my_collections_partial_update"></a>
> Collection my_collections_partial_update(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.patched_collection import PatchedCollection
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_partial_update(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_partial_update: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    body = PatchedCollection(
        id=1,
        url="url_example",
        download_url="download_url_example",
        owner=1,
        contributors="contributors_example",
        owner_name="owner_name_example",
        number_of_images=1,
        name="name_example",
        doi="doi_example",
        authors="authors_example",
        paper_url="paper_url_example",
        journal_name="journal_name_example",
        description="description_example",
        full_dataset_url="full_dataset_url_example",
        private=None,
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
        doi_add_date="1970-01-01T00:00:00.00Z",
        type_of_design=None,
        number_of_imaging_runs=-2147483648,
        number_of_experimental_units=-2147483648,
        length_of_runs=3.14,
        length_of_blocks=3.14,
        length_of_trials="length_of_trials_example",
        optimization=True,
        optimization_method="optimization_method_example",
        subject_age_mean=3.14,
        subject_age_min=3.14,
        subject_age_max=3.14,
        handedness=None,
        proportion_male_subjects=0.0,
        inclusion_exclusion_criteria="inclusion_exclusion_criteria_example",
        number_of_rejected_subjects=-2147483648,
        group_comparison=True,
        group_description="group_description_example",
        scanner_make="scanner_make_example",
        scanner_model="scanner_model_example",
        field_strength=3.14,
        pulse_sequence="pulse_sequence_example",
        parallel_imaging="parallel_imaging_example",
        field_of_view=3.14,
        matrix_size=-2147483648,
        slice_thickness=3.14,
        skip_distance=3.14,
        acquisition_orientation="acquisition_orientation_example",
        order_of_acquisition=None,
        repetition_time=3.14,
        echo_time=3.14,
        flip_angle=3.14,
        software_package="software_package_example",
        software_version="software_version_example",
        order_of_preprocessing_operations="order_of_preprocessing_operations_example",
        quality_control="quality_control_example",
        used_b0_unwarping=True,
        b0_unwarping_software="b0_unwarping_software_example",
        used_slice_timing_correction=True,
        slice_timing_correction_software="slice_timing_correction_software_example",
        used_motion_correction=True,
        motion_correction_software="motion_correction_software_example",
        motion_correction_reference="motion_correction_reference_example",
        motion_correction_metric="motion_correction_metric_example",
        motion_correction_interpolation="motion_correction_interpolation_example",
        used_motion_susceptibiity_correction=True,
        used_intersubject_registration=True,
        intersubject_registration_software="intersubject_registration_software_example",
        intersubject_transformation_type=None,
        nonlinear_transform_type="nonlinear_transform_type_example",
        transform_similarity_metric="transform_similarity_metric_example",
        interpolation_method="interpolation_method_example",
        object_image_type="object_image_type_example",
        functional_coregistered_to_structural=True,
        functional_coregistration_method="functional_coregistration_method_example",
        coordinate_space=None,
        target_template_image="target_template_image_example",
        target_resolution=3.14,
        used_smoothing=True,
        smoothing_type="smoothing_type_example",
        smoothing_fwhm=3.14,
        resampled_voxel_size=3.14,
        intrasubject_model_type="intrasubject_model_type_example",
        intrasubject_estimation_type="intrasubject_estimation_type_example",
        intrasubject_modeling_software="intrasubject_modeling_software_example",
        hemodynamic_response_function="hemodynamic_response_function_example",
        used_temporal_derivatives=True,
        used_dispersion_derivatives=True,
        used_motion_regressors=True,
        used_reaction_time_regressor=True,
        used_orthogonalization=True,
        orthogonalization_description="orthogonalization_description_example",
        used_high_pass_filter=True,
        high_pass_filter_method="high_pass_filter_method_example",
        autocorrelation_model="autocorrelation_model_example",
        group_model_type="group_model_type_example",
        group_estimation_type="group_estimation_type_example",
        group_modeling_software="group_modeling_software_example",
        group_inference_type=None,
        group_model_multilevel="group_model_multilevel_example",
        group_repeated_measures=True,
        group_repeated_measures_method="group_repeated_measures_method_example",
        nutbrain_hunger_state=None,
        nutbrain_food_viewing_conditions="nutbrain_food_viewing_conditions_example",
        nutbrain_food_choice_type="nutbrain_food_choice_type_example",
        nutbrain_taste_conditions="nutbrain_taste_conditions_example",
        nutbrain_odor_conditions="nutbrain_odor_conditions_example",
        communities=[
            1
        ],
    )
    try:
        api_response = api_instance.my_collections_partial_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_partial_update: %s\n" % e)
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
[**PatchedCollection**](../../models/PatchedCollection.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedCollection**](../../models/PatchedCollection.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedCollection**](../../models/PatchedCollection.md) |  | 


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
200 | [ApiResponseFor200](#my_collections_partial_update.ApiResponseFor200) | 

#### my_collections_partial_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_retrieve**
<a name="my_collections_retrieve"></a>
> Collection my_collections_retrieve(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_retrieve: %s\n" % e)
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
200 | [ApiResponseFor200](#my_collections_retrieve.ApiResponseFor200) | 

#### my_collections_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **my_collections_update**
<a name="my_collections_update"></a>
> Collection my_collections_update(id)



### Example

* Bearer Authentication (bearerAuth):
```python
import neurovault_sdk
from neurovault_sdk.apis.tags import my_collections_api
from neurovault_sdk.model.collection import Collection
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
    api_instance = my_collections_api.MyCollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.my_collections_update(
            path_params=path_params,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_update: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    body = Collection(
        id=1,
        url="url_example",
        download_url="download_url_example",
        owner=1,
        contributors="contributors_example",
        owner_name="owner_name_example",
        number_of_images=1,
        name="name_example",
        doi="doi_example",
        authors="authors_example",
        paper_url="paper_url_example",
        journal_name="journal_name_example",
        description="description_example",
        full_dataset_url="full_dataset_url_example",
        private=None,
        add_date="1970-01-01T00:00:00.00Z",
        modify_date="1970-01-01T00:00:00.00Z",
        doi_add_date="1970-01-01T00:00:00.00Z",
        type_of_design=None,
        number_of_imaging_runs=-2147483648,
        number_of_experimental_units=-2147483648,
        length_of_runs=3.14,
        length_of_blocks=3.14,
        length_of_trials="length_of_trials_example",
        optimization=True,
        optimization_method="optimization_method_example",
        subject_age_mean=3.14,
        subject_age_min=3.14,
        subject_age_max=3.14,
        handedness=None,
        proportion_male_subjects=0.0,
        inclusion_exclusion_criteria="inclusion_exclusion_criteria_example",
        number_of_rejected_subjects=-2147483648,
        group_comparison=True,
        group_description="group_description_example",
        scanner_make="scanner_make_example",
        scanner_model="scanner_model_example",
        field_strength=3.14,
        pulse_sequence="pulse_sequence_example",
        parallel_imaging="parallel_imaging_example",
        field_of_view=3.14,
        matrix_size=-2147483648,
        slice_thickness=3.14,
        skip_distance=3.14,
        acquisition_orientation="acquisition_orientation_example",
        order_of_acquisition=None,
        repetition_time=3.14,
        echo_time=3.14,
        flip_angle=3.14,
        software_package="software_package_example",
        software_version="software_version_example",
        order_of_preprocessing_operations="order_of_preprocessing_operations_example",
        quality_control="quality_control_example",
        used_b0_unwarping=True,
        b0_unwarping_software="b0_unwarping_software_example",
        used_slice_timing_correction=True,
        slice_timing_correction_software="slice_timing_correction_software_example",
        used_motion_correction=True,
        motion_correction_software="motion_correction_software_example",
        motion_correction_reference="motion_correction_reference_example",
        motion_correction_metric="motion_correction_metric_example",
        motion_correction_interpolation="motion_correction_interpolation_example",
        used_motion_susceptibiity_correction=True,
        used_intersubject_registration=True,
        intersubject_registration_software="intersubject_registration_software_example",
        intersubject_transformation_type=None,
        nonlinear_transform_type="nonlinear_transform_type_example",
        transform_similarity_metric="transform_similarity_metric_example",
        interpolation_method="interpolation_method_example",
        object_image_type="object_image_type_example",
        functional_coregistered_to_structural=True,
        functional_coregistration_method="functional_coregistration_method_example",
        coordinate_space=None,
        target_template_image="target_template_image_example",
        target_resolution=3.14,
        used_smoothing=True,
        smoothing_type="smoothing_type_example",
        smoothing_fwhm=3.14,
        resampled_voxel_size=3.14,
        intrasubject_model_type="intrasubject_model_type_example",
        intrasubject_estimation_type="intrasubject_estimation_type_example",
        intrasubject_modeling_software="intrasubject_modeling_software_example",
        hemodynamic_response_function="hemodynamic_response_function_example",
        used_temporal_derivatives=True,
        used_dispersion_derivatives=True,
        used_motion_regressors=True,
        used_reaction_time_regressor=True,
        used_orthogonalization=True,
        orthogonalization_description="orthogonalization_description_example",
        used_high_pass_filter=True,
        high_pass_filter_method="high_pass_filter_method_example",
        autocorrelation_model="autocorrelation_model_example",
        group_model_type="group_model_type_example",
        group_estimation_type="group_estimation_type_example",
        group_modeling_software="group_modeling_software_example",
        group_inference_type=None,
        group_model_multilevel="group_model_multilevel_example",
        group_repeated_measures=True,
        group_repeated_measures_method="group_repeated_measures_method_example",
        nutbrain_hunger_state=None,
        nutbrain_food_viewing_conditions="nutbrain_food_viewing_conditions_example",
        nutbrain_food_choice_type="nutbrain_food_choice_type_example",
        nutbrain_taste_conditions="nutbrain_taste_conditions_example",
        nutbrain_odor_conditions="nutbrain_odor_conditions_example",
        communities=[
            1
        ],
    )
    try:
        api_response = api_instance.my_collections_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurovault_sdk.ApiException as e:
        print("Exception when calling MyCollectionsApi->my_collections_update: %s\n" % e)
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
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


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
200 | [ApiResponseFor200](#my_collections_update.ApiResponseFor200) | 

#### my_collections_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

