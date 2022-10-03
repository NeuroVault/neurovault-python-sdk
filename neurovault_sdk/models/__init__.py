# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from neurovault_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from neurovault_sdk.model.atlas import Atlas
from neurovault_sdk.model.atlas_handedness_enum import AtlasHandednessEnum
from neurovault_sdk.model.blank_enum import BlankEnum
from neurovault_sdk.model.collection import Collection
from neurovault_sdk.model.collection_handedness_enum import CollectionHandednessEnum
from neurovault_sdk.model.coordinate_space_enum import CoordinateSpaceEnum
from neurovault_sdk.model.data_origin_enum import DataOriginEnum
from neurovault_sdk.model.ethnicity_enum import EthnicityEnum
from neurovault_sdk.model.gender_enum import GenderEnum
from neurovault_sdk.model.group_inference_type_enum import GroupInferenceTypeEnum
from neurovault_sdk.model.image import Image
from neurovault_sdk.model.intersubject_transformation_type_enum import IntersubjectTransformationTypeEnum
from neurovault_sdk.model.nidm_results import NIDMResults
from neurovault_sdk.model.null_enum import NullEnum
from neurovault_sdk.model.nutbrain_hunger_state_enum import NutbrainHungerStateEnum
from neurovault_sdk.model.order_of_acquisition_enum import OrderOfAcquisitionEnum
from neurovault_sdk.model.paginated_atlas_list import PaginatedAtlasList
from neurovault_sdk.model.paginated_collection_list import PaginatedCollectionList
from neurovault_sdk.model.paginated_image_list import PaginatedImageList
from neurovault_sdk.model.paginated_nidm_results_list import PaginatedNIDMResultsList
from neurovault_sdk.model.patched_atlas import PatchedAtlas
from neurovault_sdk.model.patched_collection import PatchedCollection
from neurovault_sdk.model.patched_image import PatchedImage
from neurovault_sdk.model.patched_nidm_results import PatchedNIDMResults
from neurovault_sdk.model.private_enum import PrivateEnum
from neurovault_sdk.model.race_enum import RaceEnum
from neurovault_sdk.model.tanner_stage_enum import TannerStageEnum
from neurovault_sdk.model.target_template_image_enum import TargetTemplateImageEnum
from neurovault_sdk.model.type_of_design_enum import TypeOfDesignEnum
from neurovault_sdk.model.user import User
