# coding: utf-8

"""
    Neurovault API

    All ur images r belong to us  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from neurovault_sdk import schemas  # noqa: F401


class PatchedImage(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            url = schemas.StrSchema
            id = schemas.IntSchema
            file = schemas.StrSchema
            collection = schemas.StrSchema
            collection_id = schemas.IntSchema
            file_size = schemas.IntSchema
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 200
            description = schemas.StrSchema
            add_date = schemas.DateTimeSchema
            modify_date = schemas.DateTimeSchema
            is_valid = schemas.BoolSchema
            __annotations__ = {
                "url": url,
                "id": id,
                "file": file,
                "collection": collection,
                "collection_id": collection_id,
                "file_size": file_size,
                "name": name,
                "description": description,
                "add_date": add_date,
                "modify_date": modify_date,
                "is_valid": is_valid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection"]) -> MetaOapg.properties.collection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_id"]) -> MetaOapg.properties.collection_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["add_date"]) -> MetaOapg.properties.add_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modify_date"]) -> MetaOapg.properties.modify_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_valid"]) -> MetaOapg.properties.is_valid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", "id", "file", "collection", "collection_id", "file_size", "name", "description", "add_date", "modify_date", "is_valid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> typing.Union[MetaOapg.properties.file, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection"]) -> typing.Union[MetaOapg.properties.collection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_id"]) -> typing.Union[MetaOapg.properties.collection_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_size"]) -> typing.Union[MetaOapg.properties.file_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["add_date"]) -> typing.Union[MetaOapg.properties.add_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modify_date"]) -> typing.Union[MetaOapg.properties.modify_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_valid"]) -> typing.Union[MetaOapg.properties.is_valid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", "id", "file", "collection", "collection_id", "file_size", "name", "description", "add_date", "modify_date", "is_valid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        file: typing.Union[MetaOapg.properties.file, str, schemas.Unset] = schemas.unset,
        collection: typing.Union[MetaOapg.properties.collection, str, schemas.Unset] = schemas.unset,
        collection_id: typing.Union[MetaOapg.properties.collection_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        file_size: typing.Union[MetaOapg.properties.file_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        add_date: typing.Union[MetaOapg.properties.add_date, str, datetime, schemas.Unset] = schemas.unset,
        modify_date: typing.Union[MetaOapg.properties.modify_date, str, datetime, schemas.Unset] = schemas.unset,
        is_valid: typing.Union[MetaOapg.properties.is_valid, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PatchedImage':
        return super().__new__(
            cls,
            *args,
            url=url,
            id=id,
            file=file,
            collection=collection,
            collection_id=collection_id,
            file_size=file_size,
            name=name,
            description=description,
            add_date=add_date,
            modify_date=modify_date,
            is_valid=is_valid,
            _configuration=_configuration,
            **kwargs,
        )
