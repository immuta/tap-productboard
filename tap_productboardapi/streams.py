"""Stream type classes for tap-productboardapi."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_productboardapi.client import ProductboardAPIStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class FeatureStream(ProductboardAPIStream):
    """Define custom stream."""
    name = "feature"
    path = "/features"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "feature.json"

class FeatureStatusStream(ProductboardAPIStream):
    name = "feature_status"
    path = "/feature-statuses"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "feature_status.json"

class NoteStream(ProductboardAPIStream):
    name = "note"
    path = "/notes"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "note.json"
    
class TextCustomFieldsStream(ProductboardAPIStream):
    name = "text_custom_fields"
    path = "/hierarchy-entities/custom-fields-values"
    primary_keys = ["value"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "text_custom_fields.json"

class CustomDescriptionCustomFieldsStream(ProductboardAPIStream):
    name = "custom_description_custom_fields"
    path = "/hierarchy-entities/custom-fields-values"
    primary_keys = ["value"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "custom_description_custom_fields.json"

class NumberCustomFieldsStream(ProductboardAPIStream):
    name = "number_custom_fields"
    path = "/hierarchy-entities/custom-fields-values"
    primary_keys = ["value"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "number_custom_fields.json"

class DropdownCustomFieldsStream(ProductboardAPIStream):
    name = "dropdown_custom_fields"
    path = "/hierarchy-entities/custom-fields-values"
    primary_keys = ["value"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "dropdown_custom_fields.json"

class MultiDropdownCustomFieldsStream(ProductboardAPIStream):
    name = "multi_dropdown_custom_fields"
    path = "/hierarchy-entities/custom-fields-values"
    primary_keys = ["value"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "multi_dropdown_custom_fields.json"

class MemberCustomFieldsStream(ProductboardAPIStream):
    name = "member_custom_fields"
    path = "/hierarchy-entities/custom-fields-values"
    primary_keys = ["value"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "member_custom_fields.json"

class MemberCustomFieldNamesStream(ProductboardAPIStream):
    name = "member_custom_field_names"
    path = "/hierarchy-entities/custom-fields"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "member_custom_field_names.json"

class MultiDropdownCustomFieldNamesStream(ProductboardAPIStream):
    name = "multi_dropdown_custom_field_names"
    path = "/hierarchy-entities/custom-fields"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "multi_dropdown_custom_field_names.json"

class DropdownCustomFieldNamesStream(ProductboardAPIStream):
    name = "dropdown_custom_field_names"
    path = "/hierarchy-entities/custom-fields"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "dropdown_custom_field_names.json"

class NumberCustomFieldNamesStream(ProductboardAPIStream):
    name = "number_custom_field_names"
    path = "/hierarchy-entities/custom-fields"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "number_custom_field_names.json"

class CustomDescriptionCustomFieldNamesStream(ProductboardAPIStream):
    name = "custom_description_custom_field_names"
    path = "/hierarchy-entities/custom-fields"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "custom_description_custom_field_names.json"

class TextCustomFieldNamesStream(ProductboardAPIStream):
    name = "text_custom_field_names"
    path = "/hierarchy-entities/custom-fields"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "text_custom_field_names.json"

class UserStream(ProductboardAPIStream):
    name = "user"
    path = "/users"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "user.json"

class CompanyStream(ProductboardAPIStream):
    name = "company"
    path = "/companies"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "company.json"
