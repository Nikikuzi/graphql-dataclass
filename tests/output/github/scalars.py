from pygqlmap.gql_types import ID

String = str  # The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.


ID = ID  # The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.


Boolean = bool  # The `Boolean` scalar type represents `true` or `false`.


Int = int  # The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.


Base64String = str  # A (potentially binary) string encoded using base64.


BigInt = str  # Represents non-fractional signed whole numeric values. Since the value may - exceed the size of a 32-bit integer, it's encoded as a string.


Float = float  # The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).


Date = str  # An ISO-8601 encoded date string.


DateTime = str  # An ISO-8601 encoded UTC date string.


GitObjectID = str  # A Git object ID.


GitRefname = str  # A fully qualified reference name (e.g. `refs/heads/master`).


GitSSHRemote = str  # Git SSH string


GitTimestamp = str  # An ISO-8601 encoded date string. Unlike the DateTime type, GitTimestamp is not converted in UTC.


HTML = str  # A string containing HTML code.


PreciseDateTime = str  # An ISO-8601 encoded UTC date string with millisecond precision.


URI = str  # An RFC 3986, RFC 3987, and RFC 6570 (level 4) compliant URI string.


X509Certificate = str  # A valid x509 certificate string
