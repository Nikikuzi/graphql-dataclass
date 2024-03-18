# graphql-dataclass

A python library to generate dataclasses for graphql schema.

## Introduction

This library generates dataclasses which corresponding python code convention. Library is not working as client for graphql, only dataclasses mappers for GraphQL types

This document contains a quick overview of the functionalities, for more details and options you can read here:

* [Code Generation](https://github.com/nikikuzi/graphql-dataclass/blob/develop/codegen/README.MD)

The package using [clean-py](https://github.com/samhardyhey/clean-py) library for generateed code formatting and also python 3 (3.10+) standard libraries.


## Usage in a nutshell

### Installation

Available in PyPI, the following command will install the library:

```
pip install graphql-dataclass
```


### Generate python code from schema

To generate the code execute the following command:

```
gqldataclass generate ./pathToOutputFolder -apiArgs ./<pathToArgsFile>/generatorArgs.json
```

This command requires a json file containing the parameters needed to get the GraphQL schema

![image](https://github.com/nikikuzi/graphql-dataclass/blob/develop/docs/cli_args_nutshell.png)

A sample is available in the main folder ['cli_args.json'](https://github.com/nikikuzi/graphql-dataclass/blob/develop/cli_args.json).

The following python files will be generated:

* scalars.py -> GraphQL scalar types as python type aliases
* enums.py -> GraphQL enum types as Enum classes
* gql_types.py -> GraphQL object types as classes
* gql_simple_types.py -> GraphQL object types as classes not using other object types
* unions.py -> GraphQL Unions as python Unions
* gql_forward_reference.py -> file with types forward references, [dacite](https://github.com/konradhalas/dacite)-compatible
* ${class_name}.py -> GraphQL object types as classes, which affected by circular dependencies

These links show code generated using the library [Github GraphQL API](https://github.com/nikikuzi/graphql-dataclass/blob/develop/tests/output/github), and [GeoDBCities API](https://github.com/nikikuzi/graphql-dataclass/blob/develop/tests/output/gdbc)

More command options are available [here](https://github.com/nikikuzi/graphql-dataclass/blob/develop/codegen/README.MD#usage-via-command-line)
