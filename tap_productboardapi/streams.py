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