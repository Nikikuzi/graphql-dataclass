# graphql-dataclass Release Update

## Release notes version: 1.0.6

Release date: Oct. 21, 2024

Changes

* Added inheritance from `str` to `Enum`-inherited classes. Before - `class Status(Enum):` now - `class Status(str, Enum):`. It is enhancing dataclass to dict formatting for json 

## Release notes version: 1.0.5

Release date: Oct. 7, 2024

Changes

* clean-py replaced with autoflake, isort and black

## Release notes version: 1.0.0

Release date: Mar. 19, 2024

Changes

* Removed graphql mutation/queries generation
* Added proper dataclasses generation without extra dependencies
* Added code cleanup of generated files to have(mostly automatic unused imports remove)