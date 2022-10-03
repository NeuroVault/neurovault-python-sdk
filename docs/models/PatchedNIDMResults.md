# neurovault_sdk.model.patched_nidm_results.PatchedNIDMResults

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**zip_file** | str,  | str,  |  | [optional] 
**ttl_file** | str,  | str,  |  | [optional] 
**[statmaps](#statmaps)** | list, tuple,  | tuple,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**collection** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**add_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**modify_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# statmaps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Image**](Image.md) | [**Image**](Image.md) | [**Image**](Image.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

