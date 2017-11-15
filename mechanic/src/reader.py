import os
import copy
import json

import yaml

OPENAPI3_FILE_KEY = "OPENAPI"
APP_NAME_KEY = "APP_NAME"
MODELS_PATH_KEY = "MODELS_PATH"
SCHEMAS_PATH_KEY = "SCHEMAS_PATH"
CONTROLLERS_PATH_KEY = "CONTROLLERS_PATH"
MODELS_NAME_PATTERN_KEY = "MODELS_NAME_PATTERN"
SCHEMAS_NAME_PATTERN_KEY = "SCHEMAS_NAME_PATTERN"
CONTROLLERS_NAME_PATTERN_KEY = "CONTROLLERS_NAME_PATTERN"
BASE_API_PATH_KEY = "BASE_API_PATH"
BASE_ITEM_CONTROLLER_KEY = "BASE_ITEM_CONTROLLER"
BASE_COLLECTION_CONTROLLER_KEY = "BASE_COLLECTION_CONTROLLER"
BASE_CONTROLLER_KEY = "BASE_CONTROLLER"
DEFAULT_NAMESPACE_KEY = "DEFAULT_NAMESPACE"
INCLUDE_KEY = "INCLUDE"
OVERRIDE_BASE_CONTROLLER_KEY = "OVERRIDE_BASE_CONTROLLER"
OVERRIDE_CONTROLLER_TYPE_KEY = "OVERRIDE_CONTROLLER_TYPE"
OVERRIDE_BASE_MODEL_KEY = "OVERRIDE_BASE_MODEL"
OVERRIDE_BASE_SCHEMA_KEY = "OVERRIDE_BASE_SCHEMA"
OVERRIDE_TABLE_NAMES_KEY = "OVERRIDE_TABLE_NAMES"
OVERRIDE_DB_SCHEMA_NAMES_KEY = "OVERRIDE_DB_SCHEMA_NAMES"
DEFAULT_BASE_MODEL_KEY = "DEFAULT_BASE_MODEL"
DEFAULT_BASE_SCHEMA_KEY = "DEFAULT_BASE_SCHEMA"
DEFAULT_BASE_MODEL_SCHEMA_KEY = "DEFAULT_BASE_MODEL_SCHEMA"
DEFAULT_BASE_CONTROLLER_KEY = "DEFAULT_BASE_CONTROLLER"
DEFAULT_BASE_COLLECTION_CONTROLLER_KEY = "DEFAULT_BASE_COLLECTION_CONTROLLER"
DEFAULT_BASE_ITEM_CONTROLLER_KEY = "DEFAULT_BASE_ITEM_CONTROLLER"
EXCLUDE_MODEL_GENERATION_KEY = "EXCLUDE_MODEL_GENERATION"
EXCLUDE_SCHEMA_GENERATION_KEY = "EXCLUDE_SCHEMA_GENERATION"
EXCLUDE_CONTROLLER_GENERATION_KEY = "EXCLUDE_CONTROLLER_GENERATION"
DATABASE_URL_KEY = "DATABASE_URL"

default_options = {
    APP_NAME_KEY: "app",
    OPENAPI3_FILE_KEY: None,
    MODELS_PATH_KEY: "models/{{namespace}}.py",
    SCHEMAS_PATH_KEY: "schemas/{{namespace}}.py",
    CONTROLLERS_PATH_KEY: "controllers/{{namespace}}.py",
    MODELS_NAME_PATTERN_KEY: "{{resource}}",
    SCHEMAS_NAME_PATTERN_KEY: "{{resource}}Schema",
    CONTROLLERS_NAME_PATTERN_KEY: "{{resource}}{{controller_type}}Controller",
    BASE_API_PATH_KEY: "/api",
    BASE_ITEM_CONTROLLER_KEY: "mechanic.base.controllers.BaseItemController",
    BASE_COLLECTION_CONTROLLER_KEY: "mechanic.base.controllers.BaseCollectionController",
    BASE_CONTROLLER_KEY: "mechanic.base.controllers.BaseController",
    DEFAULT_NAMESPACE_KEY: "default",
    INCLUDE_KEY: [],
    OVERRIDE_BASE_CONTROLLER_KEY: {},
    OVERRIDE_CONTROLLER_TYPE_KEY: {},
    OVERRIDE_BASE_MODEL_KEY: {},
    OVERRIDE_BASE_SCHEMA_KEY: {},
    OVERRIDE_TABLE_NAMES_KEY: [],
    OVERRIDE_DB_SCHEMA_NAMES_KEY: [],
    DEFAULT_BASE_MODEL_KEY: "mechanic.base.models.MechanicBaseModelMixin",
    DEFAULT_BASE_SCHEMA_KEY: "mechanic.base.schemas.MechanicBaseSchema",
    DEFAULT_BASE_MODEL_SCHEMA_KEY: "mechanic.base.schemas.MechanicBaseModelSchema",
    EXCLUDE_MODEL_GENERATION_KEY: [],
    EXCLUDE_SCHEMA_GENERATION_KEY: [],
    EXCLUDE_CONTROLLER_GENERATION_KEY: [],
    DEFAULT_BASE_CONTROLLER_KEY: "mechanic.base.controllers.MechanicBaseController",
    DEFAULT_BASE_ITEM_CONTROLLER_KEY: "mechanic.base.controllers.MechanicBaseItemController",
    DEFAULT_BASE_COLLECTION_CONTROLLER_KEY: "mechanic.base.controllers.MechanicBaseCollectionController",
    DATABASE_URL_KEY: ""
}


def read_mechanicfile(file_path):
    path = os.path.expanduser(file_path)
    custom_options = dict()

    with open(path, "r") as f:
        if file_path.endswith(".json"):
            custom_options = json.load(f)
        elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
            custom_options = yaml.load(f)
        else:
            raise SyntaxError("mechanic file is not of correct format. Must either be json or yaml")

    options = copy.deepcopy(default_options)
    for key, val in custom_options.items():
        options[key] = val

    return options
