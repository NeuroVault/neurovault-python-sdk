# neurovault_sdk.model.atlas.Atlas

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**add_date** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**file** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**collection** | str,  | str,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**modify_date** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**file_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**url** | str,  | str,  |  | 
**label_description_file** | str,  | str,  |  | 
**description** | str,  | str,  |  | [optional] 
**is_valid** | bool,  | BoolClass,  |  | [optional] 
**surface_left_file** | None, str,  | NoneClass, str,  |  | [optional] 
**surface_right_file** | None, str,  | NoneClass, str,  |  | [optional] 
**[data_origin](#data_origin)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Was this map originaly derived from volume or surface? | [optional] 
**[target_template_image](#target_template_image)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Name of target template image | [optional] 
**subject_species** | None, str,  | NoneClass, str,  |  | [optional] 
**figure** | None, str,  | NoneClass, str,  | Which figure in the corresponding paper was this map displayed in? | [optional] 
**[handedness](#handedness)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**age** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**[gender](#gender)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[race](#race)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[ethnicity](#ethnicity)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**BMI** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**fat_percentage** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**waist_hip_ratio** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**mean_PDS_score** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**[tanner_stage](#tanner_stage)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**days_since_menstruation** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**hours_since_last_meal** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**bis_bas_score** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**spsrq_score** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**bis11_score** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**thumbnail** | None, str,  | NoneClass, str,  | The orthogonal view thumbnail path of the nifti image | [optional] 
**reduced_representation** | None, str,  | NoneClass, str,  | Binary file with the vector of in brain values resampled to lower resolution | [optional] 
**[data](#data)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data_origin

Was this map originaly derived from volume or surface?

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Was this map originaly derived from volume or surface? | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[DataOriginEnum](DataOriginEnum.md) | [**DataOriginEnum**](DataOriginEnum.md) | [**DataOriginEnum**](DataOriginEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# target_template_image

Name of target template image

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Name of target template image | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TargetTemplateImageEnum](TargetTemplateImageEnum.md) | [**TargetTemplateImageEnum**](TargetTemplateImageEnum.md) | [**TargetTemplateImageEnum**](TargetTemplateImageEnum.md) |  | 

# handedness

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AtlasHandednessEnum](AtlasHandednessEnum.md) | [**AtlasHandednessEnum**](AtlasHandednessEnum.md) | [**AtlasHandednessEnum**](AtlasHandednessEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# gender

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[GenderEnum](GenderEnum.md) | [**GenderEnum**](GenderEnum.md) | [**GenderEnum**](GenderEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# race

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RaceEnum](RaceEnum.md) | [**RaceEnum**](RaceEnum.md) | [**RaceEnum**](RaceEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# ethnicity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[EthnicityEnum](EthnicityEnum.md) | [**EthnicityEnum**](EthnicityEnum.md) | [**EthnicityEnum**](EthnicityEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# tanner_stage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TannerStageEnum](TannerStageEnum.md) | [**TannerStageEnum**](TannerStageEnum.md) | [**TannerStageEnum**](TannerStageEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

