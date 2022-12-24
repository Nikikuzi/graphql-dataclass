from pygqlmap import GQLQuery
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class codeOfConduct(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      key: str ##NON NULL

   _args: Args


   type: CodeOfConduct

class codesOfConduct(GQLQuery):
   type: list[CodeOfConduct]

class enterprise(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      slug: str ##NON NULL
      invitationToken: str

   _args: Args


   type: Enterprise

class enterpriseAdministratorInvitation(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      userLogin: str ##NON NULL
      enterpriseSlug: str ##NON NULL
      role: EnterpriseAdministratorRole ##NON NULL

   _args: Args


   type: EnterpriseAdministratorInvitation

class enterpriseAdministratorInvitationByToken(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      invitationToken: str ##NON NULL

   _args: Args


   type: EnterpriseAdministratorInvitation

class license(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      key: str ##NON NULL

   _args: Args


   type: License

class licenses(GQLQuery):
   type: License ##NON NULL

class marketplaceCategories(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      includeCategories: list[str] ##NON NULL
      excludeEmpty: bool
      excludeSubcategories: bool

   _args: Args


   type: MarketplaceCategory ##NON NULL

class marketplaceCategory(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      slug: str ##NON NULL
      useTopicAliases: bool

   _args: Args


   type: MarketplaceCategory

class marketplaceListing(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      slug: str ##NON NULL

   _args: Args


   type: MarketplaceListing

class marketplaceListings(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      categorySlug: str
      useTopicAliases: bool
      viewerCanAdmin: bool
      adminId: ID
      organizationId: ID
      allStates: bool
      slugs: list[str]
      primaryCategoryOnly: bool
      withFreeTrialsOnly: bool

   _args: Args


   type: MarketplaceListingConnection ##NON NULL

class meta(GQLQuery):
   type: GitHubMetadata ##NON NULL

class node(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Node

class nodes(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: Node ##NON NULL

class organization(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: Args


   type: Organization

class rateLimit(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      dryRun: bool

   _args: Args


   type: RateLimit

class relay(GQLQuery):
   type: Query ##NON NULL

class repository(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      owner: str ##NON NULL
      name: str ##NON NULL
      followRenames: bool

   _args: Args


   type: Repository

class repositoryOwner(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: Args


   type: RepositoryOwner

class resource(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      url: URI ##NON NULL

   _args: Args


   type: UniformResourceLocatable

class search(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      query: str ##NON NULL
      type: SearchType ##NON NULL

   _args: Args


   type: SearchResultItemConnection ##NON NULL

class securityAdvisories(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      orderBy: SecurityAdvisoryOrder
      identifier: SecurityAdvisoryIdentifierFilter
      publishedSince: DateTime
      updatedSince: DateTime
      classifications: list[SecurityAdvisoryClassification] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args


   type: SecurityAdvisoryConnection ##NON NULL

class securityAdvisory(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      ghsaId: str ##NON NULL

   _args: Args


   type: SecurityAdvisory

class securityVulnerabilities(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      orderBy: SecurityVulnerabilityOrder
      ecosystem: SecurityAdvisoryEcosystem
      package: str
      severities: list[SecurityAdvisorySeverity] ##NON NULL
      classifications: list[SecurityAdvisoryClassification] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args


   type: SecurityVulnerabilityConnection ##NON NULL

class sponsorables(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorableOrder
      onlyDependencies: bool
      orgLoginForDependencies: str
      dependencyEcosystem: SecurityAdvisoryEcosystem
      ecosystem: DependencyGraphEcosystem

   _args: Args


   type: SponsorableItemConnection ##NON NULL

class topic(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      name: str ##NON NULL

   _args: Args


   type: Topic

class user(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: Args


   type: User

class viewer(GQLQuery):
   type: User ##NON NULL


class Queries(Enum):
   codeOfConduct = codeOfConduct
   codesOfConduct = codesOfConduct
   enterprise = enterprise
   enterpriseAdministratorInvitation = enterpriseAdministratorInvitation
   enterpriseAdministratorInvitationByToken = enterpriseAdministratorInvitationByToken
   license = license
   licenses = licenses
   marketplaceCategories = marketplaceCategories
   marketplaceCategory = marketplaceCategory
   marketplaceListing = marketplaceListing
   marketplaceListings = marketplaceListings
   meta = meta
   node = node
   nodes = nodes
   organization = organization
   rateLimit = rateLimit
   relay = relay
   repository = repository
   repositoryOwner = repositoryOwner
   resource = resource
   search = search
   securityAdvisories = securityAdvisories
   securityAdvisory = securityAdvisory
   securityVulnerabilities = securityVulnerabilities
   sponsorables = sponsorables
   topic = topic
   user = user
   viewer = viewer
