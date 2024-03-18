# graphql-dataclass - Generator

## Introduction

This module generates automatically python dataclasses corresponding to GraphQL schema types, moreover it can download a GraphQL schema in json format.
The generator can be launched through [command line](#usage-via-command-line) or [programmatically](#usage-programmatically).


## Table of Contents

1. [Functionalities](#functionalities)
    1. [Usage programmatically](#usage-programmatically)
    2. [Usage via command line](#usage-via-command-line)
        1. [JSON args file](#json-args-file)
2. [Using the generated files](#using-the-generated-files)


## Functionalities

Two functionalities are available:

1) Downloading a schema from a GraphQL server
2) Generating python dataclasses from a schema


## Usage programmatically

The class in charge of the generation is _CodeGenerator_, which takes a json schema as input and produces python files containing the mapped GraphQL schema types.

### Download of a schema as json file

If a json version of the schema is not yet available first step is obtaining it, this can be done passing the API Url and HTTP headers to _fetch_schema_obj_ function which will query the GraphQL API server:

```python
from codegen.network import fetch_schema_obj
from codegen.queryPresets import QUERY_SCHEMA_AND_TYPES

schemaObject = fetch_schema_obj(<graphQLUrl>, <HTTPHeaders dictionary>, QUERY_SCHEMA_AND_TYPES)
```

### Generation

If json schema is already available _build_schema_ can be used:

```python
from codegen.generator import build_schema

schema_obj = build_schema(schema_json_str)
```

After the schema object obtaining the following function _CodeGenerator.generate_code_ has to be called:

```python
from codegen.generator import CodeGenerator
from codegen.queryPresets import QUERY_SCHEMA_AND_TYPES

CodeGenerator.generate_code(schema_obj, folder='test\\output\\github\\', log_progress=False, add_desc=True)
```

Required parameters:

* schema_obj: the schema as python object
* folder: the destination folder where the created python files will be saved

Optional parameters:

* log_progress: makes the generation verbose (default false)
* add_desc: boolean telling if descriptions have to be added to the generated classes (default true)
* clean_folder: boolean, if True - output folder will be wiped before output generation, if False - changed filed will be re-writed, other files will be not changed. Default False
* create_forward_reference: if True - file with forward references dictionary will be generated. File can be used for dataclass converter library like [dacite](https://github.com/konradhalas/dacite). Default False

_generate_code_ function will create the following python files containing the GraphQL schema objects as python classes:

* scalars.py -> GraphQL scalar types as python type aliases
* enums.py -> GraphQL enum types as Enum classes
* gql_types.py -> GraphQL object types as classes
* gql_simple_types.py -> GraphQL object types as classes not using other object types
* unions.py -> GraphQL Unions as python Unions
* gql_forward_reference.py -> file with types forward references, [dacite](https://github.com/konradhalas/dacite)-compatible
* ${class_name}.py -> GraphQL object types as classes, which affected by circular dependencies


## Usage via command line

### Download of a schema as json file

Example of schema retrieval command:

```
pgmcodegen download ./cmd_output/Github/schema.json -apiArgs ./downloaderArgs.json
```

This command will create the file in _./cmd_output/Github/schema.json_ containing the schema in json version using the [information](#json-args-file) given in _./downloaderArgs.json_.


A few examples can be seen [here](https://github.com/nikikuzi/graphql-dataclass/blob/develop/tests/gdbc_unittest.py#L9) and [here](https://github.com/nikikuzi/graphql-dataclass/blob/develop/tests/gh_unittest.py#L13)


### Generation

Classes can be generated alternatively using the CLI command:

```
pgmcodegen generate ./gdbc -apiArgs ./generatorArgs.json -v
```

This command will generate python files in _./gdbc/_ relative folder using the [information](#json-args-file) given in _./generatorArgs.json_.


#### JSON args file

This file is used by the generator command line interface, it contains:

```json
{
    "addDescToGeneratedFiles": true, // boolean telling if descriptions have to be added to the generated classes (strongly advised to be true)
    "cleanOutputFolder": false, // clean or not output folder before generation
    "createForwardReference": false, // create or not forward-reference file
    // USED FOR QUERYING A GRAPHQL SERVER
    "apiURL": "https://mygraphqlapi.com/v2", // URL of the GraphQL server to query
    "httpHeaders": { // HTTP Headers necessary to query the GraphQL server
        "Authorization": "bearer abcdef12345678",
        "additionalHeader-content-type": "application/json"
    },
    // USED FOR GENERATE COMMAND USING A SCHEMA FILE
    "schemaFile": "./cmd_output/rapidapi/schema.json" // location of the json version of schema file
}
```

(_apiURL_, _httpHeaders_) and _schemaFile_ are mutually exclusive.