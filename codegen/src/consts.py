
from os import path
import pathlib

CLASS_SIGNATURE = "@dataclass(kw_only=True)\nclass %s"
INTERFACE_SIGNATURE = "class %s(%s)"
ARGUED_CLASS_SIGNATURE = "class %s(%s)"
QUERY_SIGNATURE = "class %s(GQLQuery)"
MUTATION_SIGNATURE = "class %s(GQLMutation)"
ENUM_SIGNATURE = "class %s(str, Enum)"
SCALAR_SIGNATURE = "%s = %s"
TYPEVAR_SIGNATURE = "%s = TypeVar('%s', bound=%s)"
EMPTY_CLASS_SIGNATURE = "class %s(%s): pass"
GQLLIST_SIGNATURE = "class %s(list, %s): pass"
OPTIONAL_SIGNATURE = "Optional[%s] = None"
FORWARD_REFERENCE_SIGNATURE = "forward_reference={%s}"
INDENTED_IMPORT_SIGNATURE = "    from .%s import %s\n"
IMPORT_SIGNATURE = "from .%s import %s\n"

NEWTYPE_DECLARATION = "NewType('%s', GQLObject)"
TEMPLATE_FOLDER = str(pathlib.Path(path.dirname(__file__), 'templates').absolute())
IMPORT_TEMPLATE = "from .%s import %s"

SCALARS_NAME = 'scalars'
ENUMS_NAME = 'enums'
TYPES_NAME = 'gql_types'
SIMPLE_TYPES_NAME = 'gql_simple_types'
QUERIES_NAME = 'queries'
MUTATIONS_NAME = 'mutations'
TYPE_REFS_NAME = 'type_refs'
UNIONS_NAME = 'gql_unions'
FORWARD_REFERENCE_NAME = 'gql_forward_reference'

PY_EXTENSION = '.py'
OPEN_LIST = 'list['
INIT_FILE = "__init__.py"
