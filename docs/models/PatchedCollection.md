# neurovault_sdk.model.patched_collection.PatchedCollection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**download_url** | str,  | str,  |  | [optional] 
**owner** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**contributors** | str,  | str,  |  | [optional] 
**owner_name** | str,  | str,  |  | [optional] 
**number_of_images** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**DOI** | None, str,  | NoneClass, str,  | Required if you want your maps to be archived in Stanford Digital Repository | [optional] 
**authors** | None, str,  | NoneClass, str,  |  | [optional] 
**paper_url** | None, str,  | NoneClass, str,  |  | [optional] 
**journal_name** | None, str,  | NoneClass, str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**full_dataset_url** | None, str,  | NoneClass, str,  | Link to an external dataset the maps in this collection have been generated from (for example: \&quot;https://openfmri.org/dataset/ds000001\&quot; or \&quot;http://dx.doi.org/10.15387/fcp_indi.corr.mpg1\&quot;) | [optional] 
**[private](#private)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**add_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**modify_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**doi_add_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**[type_of_design](#type_of_design)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Blocked, event-related, hybrid, or other | [optional] 
**number_of_imaging_runs** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Number of imaging runs acquired | [optional] 
**number_of_experimental_units** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Number of blocks, trials or experimental units per imaging run | [optional] 
**length_of_runs** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Length of each imaging run in seconds | [optional] value must be a 64 bit float
**length_of_blocks** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | For blocked designs, length of blocks in seconds | [optional] value must be a 64 bit float
**length_of_trials** | None, str,  | NoneClass, str,  | Length of individual trials in seconds. If length varies across trials, enter &#x27;variable&#x27;.  | [optional] 
**optimization** | None, bool,  | NoneClass, BoolClass,  | Was the design optimized for efficiency | [optional] 
**optimization_method** | None, str,  | NoneClass, str,  | What method was used for optimization? | [optional] 
**subject_age_mean** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Mean age of subjects | [optional] value must be a 64 bit float
**subject_age_min** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Minimum age of subjects | [optional] value must be a 64 bit float
**subject_age_max** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Maximum age of subjects | [optional] value must be a 64 bit float
**[handedness](#handedness)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Handedness of subjects | [optional] 
**proportion_male_subjects** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The proportion (not percentage) of subjects who were male | [optional] value must be a 64 bit float
**inclusion_exclusion_criteria** | None, str,  | NoneClass, str,  | Additional inclusion/exclusion criteria, if any (including specific sampling strategies that limit inclusion to a specific group, such as laboratory members) | [optional] 
**number_of_rejected_subjects** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Number of subjects scanned but rejected from analysis | [optional] 
**group_comparison** | None, bool,  | NoneClass, BoolClass,  | Was this study a comparison between subject groups? | [optional] 
**group_description** | None, str,  | NoneClass, str,  | A description of the groups being compared | [optional] 
**scanner_make** | None, str,  | NoneClass, str,  | Manufacturer of MRI scanner | [optional] 
**scanner_model** | None, str,  | NoneClass, str,  | Model of MRI scanner | [optional] 
**field_strength** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Field strength of MRI scanner (in Tesla) | [optional] value must be a 64 bit float
**pulse_sequence** | None, str,  | NoneClass, str,  | Description of pulse sequence used for fMRI | [optional] 
**parallel_imaging** | None, str,  | NoneClass, str,  | Description of parallel imaging method and parameters | [optional] 
**field_of_view** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Imaging field of view in millimeters | [optional] value must be a 64 bit float
**matrix_size** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Matrix size for MRI acquisition | [optional] 
**slice_thickness** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Distance between slices (includes skip or distance factor) in millimeters | [optional] value must be a 64 bit float
**skip_distance** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The size of the skipped area between slices in millimeters | [optional] value must be a 64 bit float
**acquisition_orientation** | None, str,  | NoneClass, str,  | The orientation of slices | [optional] 
**[order_of_acquisition](#order_of_acquisition)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Order of acquisition of slices (ascending, descending, or interleaved) | [optional] 
**repetition_time** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Repetition time (TR) in milliseconds | [optional] value must be a 64 bit float
**echo_time** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Echo time (TE) in milliseconds | [optional] value must be a 64 bit float
**flip_angle** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Flip angle in degrees | [optional] value must be a 64 bit float
**software_package** | None, str,  | NoneClass, str,  | If a single software package was used for all analyses, specify that here | [optional] 
**software_version** | None, str,  | NoneClass, str,  | Version of software package used | [optional] 
**order_of_preprocessing_operations** | None, str,  | NoneClass, str,  | Specify order of preprocessing operations | [optional] 
**quality_control** | None, str,  | NoneClass, str,  | Describe quality control measures | [optional] 
**used_b0_unwarping** | None, bool,  | NoneClass, BoolClass,  | Was B0 distortion correction used? | [optional] 
**b0_unwarping_software** | None, str,  | NoneClass, str,  | Specify software used for distortion correction if different from the main package | [optional] 
**used_slice_timing_correction** | None, bool,  | NoneClass, BoolClass,  | Was slice timing correction used? | [optional] 
**slice_timing_correction_software** | None, str,  | NoneClass, str,  | Specify software used for slice timing correction if different from the main package | [optional] 
**used_motion_correction** | None, bool,  | NoneClass, BoolClass,  | Was motion correction used? | [optional] 
**motion_correction_software** | None, str,  | NoneClass, str,  | Specify software used for motion correction if different from the main package | [optional] 
**motion_correction_reference** | None, str,  | NoneClass, str,  | Reference scan used for motion correction | [optional] 
**motion_correction_metric** | None, str,  | NoneClass, str,  | Similarity metric used for motion correction | [optional] 
**motion_correction_interpolation** | None, str,  | NoneClass, str,  | Interpolation method used for motion correction | [optional] 
**used_motion_susceptibiity_correction** | None, bool,  | NoneClass, BoolClass,  | Was motion-susceptibility correction used? | [optional] 
**used_intersubject_registration** | None, bool,  | NoneClass, BoolClass,  | Were subjects registered to a common stereotactic space? | [optional] 
**intersubject_registration_software** | None, str,  | NoneClass, str,  | Specify software used for intersubject registration if different from main package | [optional] 
**[intersubject_transformation_type](#intersubject_transformation_type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Was linear or nonlinear registration used? | [optional] 
**nonlinear_transform_type** | None, str,  | NoneClass, str,  | If nonlinear registration was used, describe transform method | [optional] 
**transform_similarity_metric** | None, str,  | NoneClass, str,  | Similarity metric used for intersubject registration | [optional] 
**interpolation_method** | None, str,  | NoneClass, str,  | Interpolation method used for intersubject registration | [optional] 
**object_image_type** | None, str,  | NoneClass, str,  | What type of image was used to determine the transformation to the atlas? (e.g. T1, T2, EPI) | [optional] 
**functional_coregistered_to_structural** | None, bool,  | NoneClass, BoolClass,  | Were the functional images coregistered to the subject&#x27;s structural image? | [optional] 
**functional_coregistration_method** | None, str,  | NoneClass, str,  | Method used to coregister functional to structural images | [optional] 
**[coordinate_space](#coordinate_space)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Name of coordinate space for registration target | [optional] 
**target_template_image** | None, str,  | NoneClass, str,  | Name of target template image | [optional] 
**target_resolution** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Voxel size of target template in millimeters | [optional] value must be a 64 bit float
**used_smoothing** | None, bool,  | NoneClass, BoolClass,  | Was spatial smoothing applied? | [optional] 
**smoothing_type** | None, str,  | NoneClass, str,  | Describe the type of smoothing applied | [optional] 
**smoothing_fwhm** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The full-width at half-maximum of the smoothing kernel in millimeters | [optional] value must be a 64 bit float
**resampled_voxel_size** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Voxel size in mm of the resampled, atlas-space images | [optional] value must be a 64 bit float
**intrasubject_model_type** | None, str,  | NoneClass, str,  | Type of model used (e.g., regression) | [optional] 
**intrasubject_estimation_type** | None, str,  | NoneClass, str,  | Estimation method used for model (e.g., OLS, generalized least squares) | [optional] 
**intrasubject_modeling_software** | None, str,  | NoneClass, str,  | Software used for intrasubject modeling if different from overall package | [optional] 
**hemodynamic_response_function** | None, str,  | NoneClass, str,  | Nature of HRF model | [optional] 
**used_temporal_derivatives** | None, bool,  | NoneClass, BoolClass,  | Were temporal derivatives included? | [optional] 
**used_dispersion_derivatives** | None, bool,  | NoneClass, BoolClass,  | Were dispersion derivatives included? | [optional] 
**used_motion_regressors** | None, bool,  | NoneClass, BoolClass,  | Were motion regressors included? | [optional] 
**used_reaction_time_regressor** | None, bool,  | NoneClass, BoolClass,  | Was a reaction time regressor included? | [optional] 
**used_orthogonalization** | None, bool,  | NoneClass, BoolClass,  | Were any regressors specifically orthogonalized with respect to others? | [optional] 
**orthogonalization_description** | None, str,  | NoneClass, str,  | If orthogonalization was used, describe here | [optional] 
**used_high_pass_filter** | None, bool,  | NoneClass, BoolClass,  | Was high pass filtering applied? | [optional] 
**high_pass_filter_method** | None, str,  | NoneClass, str,  | Describe method used for high pass filtering | [optional] 
**autocorrelation_model** | None, str,  | NoneClass, str,  | What autocorrelation model was used (or &#x27;none&#x27; of none was used) | [optional] 
**group_model_type** | None, str,  | NoneClass, str,  | Type of group model used (e.g., regression) | [optional] 
**group_estimation_type** | None, str,  | NoneClass, str,  | Estimation method used for group model (e.g., OLS, generalized least squares) | [optional] 
**group_modeling_software** | None, str,  | NoneClass, str,  | Software used for group modeling if different from overall package | [optional] 
**[group_inference_type](#group_inference_type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Type of inference for group model | [optional] 
**group_model_multilevel** | None, str,  | NoneClass, str,  | If more than 2-levels, describe the levels and assumptions of the model (e.g. are variances assumed equal between groups) | [optional] 
**group_repeated_measures** | None, bool,  | NoneClass, BoolClass,  | Was this a repeated measures design at the group level? | [optional] 
**group_repeated_measures_method** | None, str,  | NoneClass, str,  | If multiple measurements per subject, list method to account for within subject correlation, exact assumptions made about correlation/variance | [optional] 
**[nutbrain_hunger_state](#nutbrain_hunger_state)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**nutbrain_food_viewing_conditions** | None, str,  | NoneClass, str,  | Image categories | [optional] 
**nutbrain_food_choice_type** | None, str,  | NoneClass, str,  | Choice conditions/image types | [optional] 
**nutbrain_taste_conditions** | None, str,  | NoneClass, str,  |  | [optional] 
**nutbrain_odor_conditions** | None, str,  | NoneClass, str,  |  | [optional] 
**[communities](#communities)** | list, tuple,  | tuple,  | Is this collection part of any special Community? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# private

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PrivateEnum](PrivateEnum.md) | [**PrivateEnum**](PrivateEnum.md) | [**PrivateEnum**](PrivateEnum.md) |  | 

# type_of_design

Blocked, event-related, hybrid, or other

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Blocked, event-related, hybrid, or other | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TypeOfDesignEnum](TypeOfDesignEnum.md) | [**TypeOfDesignEnum**](TypeOfDesignEnum.md) | [**TypeOfDesignEnum**](TypeOfDesignEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# handedness

Handedness of subjects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Handedness of subjects | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CollectionHandednessEnum](CollectionHandednessEnum.md) | [**CollectionHandednessEnum**](CollectionHandednessEnum.md) | [**CollectionHandednessEnum**](CollectionHandednessEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# order_of_acquisition

Order of acquisition of slices (ascending, descending, or interleaved)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Order of acquisition of slices (ascending, descending, or interleaved) | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[OrderOfAcquisitionEnum](OrderOfAcquisitionEnum.md) | [**OrderOfAcquisitionEnum**](OrderOfAcquisitionEnum.md) | [**OrderOfAcquisitionEnum**](OrderOfAcquisitionEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# intersubject_transformation_type

Was linear or nonlinear registration used?

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Was linear or nonlinear registration used? | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[IntersubjectTransformationTypeEnum](IntersubjectTransformationTypeEnum.md) | [**IntersubjectTransformationTypeEnum**](IntersubjectTransformationTypeEnum.md) | [**IntersubjectTransformationTypeEnum**](IntersubjectTransformationTypeEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# coordinate_space

Name of coordinate space for registration target

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Name of coordinate space for registration target | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CoordinateSpaceEnum](CoordinateSpaceEnum.md) | [**CoordinateSpaceEnum**](CoordinateSpaceEnum.md) | [**CoordinateSpaceEnum**](CoordinateSpaceEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# group_inference_type

Type of inference for group model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Type of inference for group model | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[GroupInferenceTypeEnum](GroupInferenceTypeEnum.md) | [**GroupInferenceTypeEnum**](GroupInferenceTypeEnum.md) | [**GroupInferenceTypeEnum**](GroupInferenceTypeEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# nutbrain_hunger_state

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NutbrainHungerStateEnum](NutbrainHungerStateEnum.md) | [**NutbrainHungerStateEnum**](NutbrainHungerStateEnum.md) | [**NutbrainHungerStateEnum**](NutbrainHungerStateEnum.md) |  | 
[BlankEnum](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) | [**BlankEnum**](BlankEnum.md) |  | 
[NullEnum](NullEnum.md) | [**NullEnum**](NullEnum.md) | [**NullEnum**](NullEnum.md) |  | 

# communities

Is this collection part of any special Community?

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Is this collection part of any special Community? | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

