from gqlTypes import GQLConnection, GQLEdges
from .country import countryNode

class countries(GQLConnection):
    
    def __init__(self):
        super().__init__(GQLEdges(countryNode())) 
    