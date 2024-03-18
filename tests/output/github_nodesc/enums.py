from enum import Enum


class ActorType(Enum):

    TEAM = "TEAM"  # Indicates a team actor.
    USER = "USER"  # Indicates a user actor.


class AuditLogOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order audit log entries by timestamp


class CheckAnnotationLevel(Enum):

    FAILURE = "FAILURE"  # An annotation indicating an inescapable error.
    NOTICE = "NOTICE"  # An annotation indicating some information.
    WARNING = "WARNING"  # An annotation indicating an ignorable error.


class CheckConclusionState(Enum):

    ACTION_REQUIRED = "ACTION_REQUIRED"  # The check suite or run requires action.
    CANCELLED = "CANCELLED"  # The check suite or run has been cancelled.
    FAILURE = "FAILURE"  # The check suite or run has failed.
    NEUTRAL = "NEUTRAL"  # The check suite or run was neutral.
    SKIPPED = "SKIPPED"  # The check suite or run was skipped.
    STALE = "STALE"  # The check suite or run was marked stale by GitHub. Only GitHub can use this conclusion.
    STARTUP_FAILURE = "STARTUP_FAILURE"  # The check suite or run has failed at startup.
    SUCCESS = "SUCCESS"  # The check suite or run has succeeded.
    TIMED_OUT = "TIMED_OUT"  # The check suite or run has timed out.


class CheckRunState(Enum):

    ACTION_REQUIRED = "ACTION_REQUIRED"  # The check run requires action.
    CANCELLED = "CANCELLED"  # The check run has been cancelled.
    COMPLETED = "COMPLETED"  # The check run has been completed.
    FAILURE = "FAILURE"  # The check run has failed.
    IN_PROGRESS = "IN_PROGRESS"  # The check run is in progress.
    NEUTRAL = "NEUTRAL"  # The check run was neutral.
    PENDING = "PENDING"  # The check run is in pending state.
    QUEUED = "QUEUED"  # The check run has been queued.
    SKIPPED = "SKIPPED"  # The check run was skipped.
    STALE = "STALE"  # The check run was marked stale by GitHub. Only GitHub can use this conclusion.
    STARTUP_FAILURE = "STARTUP_FAILURE"  # The check run has failed at startup.
    SUCCESS = "SUCCESS"  # The check run has succeeded.
    TIMED_OUT = "TIMED_OUT"  # The check run has timed out.
    WAITING = "WAITING"  # The check run is in waiting state.


class CheckRunType(Enum):

    ALL = "ALL"  # Every check run available.
    LATEST = "LATEST"  # The latest check run.


class CheckStatusState(Enum):

    COMPLETED = "COMPLETED"  # The check suite or run has been completed.
    IN_PROGRESS = "IN_PROGRESS"  # The check suite or run is in progress.
    PENDING = "PENDING"  # The check suite or run is in pending state.
    QUEUED = "QUEUED"  # The check suite or run has been queued.
    REQUESTED = "REQUESTED"  # The check suite or run has been requested.
    WAITING = "WAITING"  # The check suite or run is in waiting state.


class CollaboratorAffiliation(Enum):

    ALL = "ALL"  # All collaborators the authenticated user can see.
    DIRECT = "DIRECT"  # All collaborators with permissions to an organization-owned subject, regardless of organization membership status.
    OUTSIDE = "OUTSIDE"  # All outside collaborators of an organization-owned subject.


class CommentAuthorAssociation(Enum):

    COLLABORATOR = (
        "COLLABORATOR"  # Author has been invited to collaborate on the repository.
    )
    CONTRIBUTOR = "CONTRIBUTOR"  # Author has previously committed to the repository.
    FIRST_TIMER = "FIRST_TIMER"  # Author has not previously committed to GitHub.
    FIRST_TIME_CONTRIBUTOR = "FIRST_TIME_CONTRIBUTOR"  # Author has not previously committed to the repository.
    MANNEQUIN = "MANNEQUIN"  # Author is a placeholder for an unclaimed user.
    MEMBER = (
        "MEMBER"  # Author is a member of the organization that owns the repository.
    )
    NONE = "NONE"  # Author has no association with the repository.
    OWNER = "OWNER"  # Author is the owner of the repository.


class CommentCannotUpdateReason(Enum):

    ARCHIVED = "ARCHIVED"  # Unable to create comment because repository is archived.
    DENIED = "DENIED"  # You cannot update this comment
    INSUFFICIENT_ACCESS = "INSUFFICIENT_ACCESS"  # You must be the author or have write access to this repository to update this comment.
    LOCKED = "LOCKED"  # Unable to create comment because issue is locked.
    LOGIN_REQUIRED = "LOGIN_REQUIRED"  # You must be logged in to update this comment.
    MAINTENANCE = "MAINTENANCE"  # Repository is under maintenance.
    VERIFIED_EMAIL_REQUIRED = "VERIFIED_EMAIL_REQUIRED"  # At least one email address must be verified to update this comment.


class CommitContributionOrderField(Enum):

    COMMIT_COUNT = (
        "COMMIT_COUNT"  # Order commit contributions by how many commits they represent.
    )
    OCCURRED_AT = "OCCURRED_AT"  # Order commit contributions by when they were made.


class ComparisonStatus(Enum):

    AHEAD = "AHEAD"  # The head ref is ahead of the base ref.
    BEHIND = "BEHIND"  # The head ref is behind the base ref.
    DIVERGED = "DIVERGED"  # The head ref is both ahead and behind of the base ref, indicating git history has diverged.
    IDENTICAL = "IDENTICAL"  # The head ref and base ref are identical.


class ContributionLevel(Enum):

    FIRST_QUARTILE = "FIRST_QUARTILE"  # Lowest 25% of days of contributions.
    FOURTH_QUARTILE = "FOURTH_QUARTILE"  # Highest 25% of days of contributions. More contributions than the third quartile.
    NONE = "NONE"  # No contributions occurred.
    SECOND_QUARTILE = "SECOND_QUARTILE"  # Second lowest 25% of days of contributions. More contributions than the first quartile.
    THIRD_QUARTILE = "THIRD_QUARTILE"  # Second highest 25% of days of contributions. More contributions than second quartile, less than the fourth quartile.


class DefaultRepositoryPermissionField(Enum):

    ADMIN = "ADMIN"  # Can read, write, and administrate repos by default
    NONE = "NONE"  # No access
    READ = "READ"  # Can read repos by default
    WRITE = "WRITE"  # Can read and write repos by default


class DependencyGraphEcosystem(Enum):

    ACTIONS = "ACTIONS"  # GitHub Actions
    COMPOSER = "COMPOSER"  # PHP packages hosted at packagist.org
    GO = "GO"  # Go modules
    MAVEN = "MAVEN"  # Java artifacts hosted at the Maven central repository
    NPM = "NPM"  # JavaScript packages hosted at npmjs.com
    NUGET = "NUGET"  # .NET packages hosted at the NuGet Gallery
    PIP = "PIP"  # Python packages hosted at PyPI.org
    PUB = "PUB"  # Dart packages hosted at pub.dev
    RUBYGEMS = "RUBYGEMS"  # Ruby gems hosted at RubyGems.org
    RUST = "RUST"  # Rust crates
    SWIFT = "SWIFT"  # Swift packages


class DeploymentOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order collection by creation time


class DeploymentProtectionRuleType(Enum):

    REQUIRED_REVIEWERS = "REQUIRED_REVIEWERS"  # Required reviewers
    WAIT_TIMER = "WAIT_TIMER"  # Wait timer


class DeploymentReviewState(Enum):

    APPROVED = "APPROVED"  # The deployment was approved.
    REJECTED = "REJECTED"  # The deployment was rejected.


class DeploymentState(Enum):

    ABANDONED = "ABANDONED"  # The pending deployment was not updated after 30 minutes.
    ACTIVE = "ACTIVE"  # The deployment is currently active.
    DESTROYED = "DESTROYED"  # An inactive transient deployment.
    ERROR = "ERROR"  # The deployment experienced an error.
    FAILURE = "FAILURE"  # The deployment has failed.
    INACTIVE = "INACTIVE"  # The deployment is inactive.
    IN_PROGRESS = "IN_PROGRESS"  # The deployment is in progress.
    PENDING = "PENDING"  # The deployment is pending.
    QUEUED = "QUEUED"  # The deployment has queued
    SUCCESS = "SUCCESS"  # The deployment was successful.
    WAITING = "WAITING"  # The deployment is waiting.


class DeploymentStatusState(Enum):

    ERROR = "ERROR"  # The deployment experienced an error.
    FAILURE = "FAILURE"  # The deployment has failed.
    INACTIVE = "INACTIVE"  # The deployment is inactive.
    IN_PROGRESS = "IN_PROGRESS"  # The deployment is in progress.
    PENDING = "PENDING"  # The deployment is pending.
    QUEUED = "QUEUED"  # The deployment is queued
    SUCCESS = "SUCCESS"  # The deployment was successful.
    WAITING = "WAITING"  # The deployment is waiting.


class DiffSide(Enum):

    LEFT = "LEFT"  # The left side of the diff.
    RIGHT = "RIGHT"  # The right side of the diff.


class DiscussionCloseReason(Enum):

    DUPLICATE = "DUPLICATE"  # The discussion is a duplicate of another
    OUTDATED = "OUTDATED"  # The discussion is no longer relevant
    RESOLVED = "RESOLVED"  # The discussion has been resolved


class DiscussionOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order discussions by creation time.
    UPDATED_AT = "UPDATED_AT"  # Order discussions by most recent modification time.


class DiscussionPollOptionOrderField(Enum):

    AUTHORED_ORDER = "AUTHORED_ORDER"  # Order poll options by the order that the poll author specified when creating the poll.
    VOTE_COUNT = "VOTE_COUNT"  # Order poll options by the number of votes it has.


class DiscussionState(Enum):

    CLOSED = "CLOSED"  # A discussion that has been closed
    OPEN = "OPEN"  # A discussion that is open


class DiscussionStateReason(Enum):

    DUPLICATE = "DUPLICATE"  # The discussion is a duplicate of another
    OUTDATED = "OUTDATED"  # The discussion is no longer relevant
    REOPENED = "REOPENED"  # The discussion was reopened
    RESOLVED = "RESOLVED"  # The discussion has been resolved


class DismissReason(Enum):

    FIX_STARTED = "FIX_STARTED"  # A fix has already been started
    INACCURATE = "INACCURATE"  # This alert is inaccurate or incorrect
    NOT_USED = "NOT_USED"  # Vulnerable code is not actually used
    NO_BANDWIDTH = "NO_BANDWIDTH"  # No bandwidth to fix this
    TOLERABLE_RISK = "TOLERABLE_RISK"  # Risk is tolerable to this project


class EnterpriseAdministratorInvitationOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order enterprise administrator member invitations by creation time


class EnterpriseAdministratorRole(Enum):

    BILLING_MANAGER = (
        "BILLING_MANAGER"  # Represents a billing manager of the enterprise account.
    )
    OWNER = "OWNER"  # Represents an owner of the enterprise account.


class EnterpriseAllowPrivateRepositoryForkingPolicyValue(Enum):

    ENTERPRISE_ORGANIZATIONS = "ENTERPRISE_ORGANIZATIONS"  # Members can fork a repository to an organization within this enterprise.
    ENTERPRISE_ORGANIZATIONS_USER_ACCOUNTS = "ENTERPRISE_ORGANIZATIONS_USER_ACCOUNTS"  # Members can fork a repository to their enterprise-managed user account or an organization inside this enterprise.
    EVERYWHERE = "EVERYWHERE"  # Members can fork a repository to their user account or an organization, either inside or outside of this enterprise.
    SAME_ORGANIZATION = "SAME_ORGANIZATION"  # Members can fork a repository only within the same organization (intra-org).
    SAME_ORGANIZATION_USER_ACCOUNTS = "SAME_ORGANIZATION_USER_ACCOUNTS"  # Members can fork a repository to their user account or within the same organization.
    USER_ACCOUNTS = (
        "USER_ACCOUNTS"  # Members can fork a repository to their user account.
    )


class EnterpriseDefaultRepositoryPermissionSettingValue(Enum):

    ADMIN = "ADMIN"  # Organization members will be able to clone, pull, push, and add new collaborators to all organization repositories.
    NONE = "NONE"  # Organization members will only be able to clone and pull public repositories.
    NO_POLICY = "NO_POLICY"  # Organizations in the enterprise choose base repository permissions for their members.
    READ = "READ"  # Organization members will be able to clone and pull all organization repositories.
    WRITE = "WRITE"  # Organization members will be able to clone, pull, and push all organization repositories.


class EnterpriseEnabledDisabledSettingValue(Enum):

    DISABLED = (
        "DISABLED"  # The setting is disabled for organizations in the enterprise.
    )
    ENABLED = "ENABLED"  # The setting is enabled for organizations in the enterprise.
    NO_POLICY = (
        "NO_POLICY"  # There is no policy set for organizations in the enterprise.
    )


class EnterpriseEnabledSettingValue(Enum):

    ENABLED = "ENABLED"  # The setting is enabled for organizations in the enterprise.
    NO_POLICY = (
        "NO_POLICY"  # There is no policy set for organizations in the enterprise.
    )


class EnterpriseMemberOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order enterprise members by creation time
    LOGIN = "LOGIN"  # Order enterprise members by login


class EnterpriseMembersCanCreateRepositoriesSettingValue(Enum):

    ALL = "ALL"  # Members will be able to create public and private repositories.
    DISABLED = (
        "DISABLED"  # Members will not be able to create public or private repositories.
    )
    NO_POLICY = "NO_POLICY"  # Organization owners choose whether to allow members to create repositories.
    PRIVATE = "PRIVATE"  # Members will be able to create only private repositories.
    PUBLIC = "PUBLIC"  # Members will be able to create only public repositories.


class EnterpriseMembersCanMakePurchasesSettingValue(Enum):

    DISABLED = (
        "DISABLED"  # The setting is disabled for organizations in the enterprise.
    )
    ENABLED = "ENABLED"  # The setting is enabled for organizations in the enterprise.


class EnterpriseMembershipType(Enum):

    ADMIN = "ADMIN"  # Returns all enterprises in which the user is an admin.
    ALL = "ALL"  # Returns all enterprises in which the user is a member, admin, or billing manager.
    BILLING_MANAGER = "BILLING_MANAGER"  # Returns all enterprises in which the user is a billing manager.
    ORG_MEMBERSHIP = "ORG_MEMBERSHIP"  # Returns all enterprises in which the user is a member of an org that is owned by the enterprise.


class EnterpriseOrderField(Enum):

    NAME = "NAME"  # Order enterprises by name


class EnterpriseServerInstallationOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order Enterprise Server installations by creation time
    CUSTOMER_NAME = (
        "CUSTOMER_NAME"  # Order Enterprise Server installations by customer name
    )
    HOST_NAME = "HOST_NAME"  # Order Enterprise Server installations by host name


class EnterpriseServerUserAccountEmailOrderField(Enum):

    EMAIL = "EMAIL"  # Order emails by email


class EnterpriseServerUserAccountOrderField(Enum):

    LOGIN = "LOGIN"  # Order user accounts by login
    REMOTE_CREATED_AT = "REMOTE_CREATED_AT"  # Order user accounts by creation time on the Enterprise Server installation


class EnterpriseServerUserAccountsUploadOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order user accounts uploads by creation time


class EnterpriseServerUserAccountsUploadSyncState(Enum):

    FAILURE = "FAILURE"  # The synchronization of the upload failed.
    PENDING = "PENDING"  # The synchronization of the upload is pending.
    SUCCESS = "SUCCESS"  # The synchronization of the upload succeeded.


class EnterpriseUserAccountMembershipRole(Enum):

    MEMBER = "MEMBER"  # The user is a member of an organization in the enterprise.
    OWNER = "OWNER"  # The user is an owner of an organization in the enterprise.
    UNAFFILIATED = "UNAFFILIATED"  # The user is not an owner of the enterprise, and not a member or owner of any organizations in the enterprise; only for EMU-enabled enterprises.


class EnterpriseUserDeployment(Enum):

    CLOUD = "CLOUD"  # The user is part of a GitHub Enterprise Cloud deployment.
    SERVER = "SERVER"  # The user is part of a GitHub Enterprise Server deployment.


class EnvironmentOrderField(Enum):

    NAME = "NAME"  # Order environments by name.


class FileViewedState(Enum):

    DISMISSED = "DISMISSED"  # The file has new changes since last viewed.
    UNVIEWED = "UNVIEWED"  # The file has not been marked as viewed.
    VIEWED = "VIEWED"  # The file has been marked as viewed.


class FundingPlatform(Enum):

    BUY_ME_A_COFFEE = "BUY_ME_A_COFFEE"  # Buy Me a Coffee funding platform.
    COMMUNITY_BRIDGE = "COMMUNITY_BRIDGE"  # Community Bridge funding platform.
    CUSTOM = "CUSTOM"  # Custom funding platform.
    GITHUB = "GITHUB"  # GitHub funding platform.
    ISSUEHUNT = "ISSUEHUNT"  # IssueHunt funding platform.
    KO_FI = "KO_FI"  # Ko-fi funding platform.
    LFX_CROWDFUNDING = "LFX_CROWDFUNDING"  # LFX Crowdfunding funding platform.
    LIBERAPAY = "LIBERAPAY"  # Liberapay funding platform.
    OPEN_COLLECTIVE = "OPEN_COLLECTIVE"  # Open Collective funding platform.
    PATREON = "PATREON"  # Patreon funding platform.
    POLAR = "POLAR"  # Polar funding platform.
    TIDELIFT = "TIDELIFT"  # Tidelift funding platform.


class GistOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order gists by creation time
    PUSHED_AT = "PUSHED_AT"  # Order gists by push time
    UPDATED_AT = "UPDATED_AT"  # Order gists by update time


class GistPrivacy(Enum):

    ALL = "ALL"  # Gists that are public and secret
    PUBLIC = "PUBLIC"  # Public
    SECRET = "SECRET"  # Secret


class GitSignatureState(Enum):

    BAD_CERT = "BAD_CERT"  # The signing certificate or its chain could not be verified
    BAD_EMAIL = "BAD_EMAIL"  # Invalid email used for signing
    EXPIRED_KEY = "EXPIRED_KEY"  # Signing key expired
    GPGVERIFY_ERROR = (
        "GPGVERIFY_ERROR"  # Internal error - the GPG verification service misbehaved
    )
    GPGVERIFY_UNAVAILABLE = "GPGVERIFY_UNAVAILABLE"  # Internal error - the GPG verification service is unavailable at the moment
    INVALID = "INVALID"  # Invalid signature
    MALFORMED_SIG = "MALFORMED_SIG"  # Malformed signature
    NOT_SIGNING_KEY = "NOT_SIGNING_KEY"  # The usage flags for the key that signed this don't allow signing
    NO_USER = "NO_USER"  # Email used for signing not known to GitHub
    OCSP_ERROR = (
        "OCSP_ERROR"  # Valid signature, though certificate revocation check failed
    )
    OCSP_PENDING = (
        "OCSP_PENDING"  # Valid signature, pending certificate revocation checking
    )
    OCSP_REVOKED = "OCSP_REVOKED"  # One or more certificates in chain has been revoked
    UNKNOWN_KEY = "UNKNOWN_KEY"  # Key used for signing not known to GitHub
    UNKNOWN_SIG_TYPE = "UNKNOWN_SIG_TYPE"  # Unknown signature type
    UNSIGNED = "UNSIGNED"  # Unsigned
    UNVERIFIED_EMAIL = "UNVERIFIED_EMAIL"  # Email used for signing unverified on GitHub
    VALID = "VALID"  # Valid signature and verified by GitHub


class IdentityProviderConfigurationState(Enum):

    CONFIGURED = "CONFIGURED"  # Authentication with an identity provider is configured but not enforced.
    ENFORCED = "ENFORCED"  # Authentication with an identity provider is configured and enforced.
    UNCONFIGURED = (
        "UNCONFIGURED"  # Authentication with an identity provider is not configured.
    )


class IpAllowListEnabledSettingValue(Enum):

    DISABLED = "DISABLED"  # The setting is disabled for the owner.
    ENABLED = "ENABLED"  # The setting is enabled for the owner.


class IpAllowListEntryOrderField(Enum):

    ALLOW_LIST_VALUE = (
        "ALLOW_LIST_VALUE"  # Order IP allow list entries by the allow list value.
    )
    CREATED_AT = "CREATED_AT"  # Order IP allow list entries by creation time.


class IpAllowListForInstalledAppsEnabledSettingValue(Enum):

    DISABLED = "DISABLED"  # The setting is disabled for the owner.
    ENABLED = "ENABLED"  # The setting is enabled for the owner.


class IssueClosedStateReason(Enum):

    COMPLETED = "COMPLETED"  # An issue that has been closed as completed
    NOT_PLANNED = "NOT_PLANNED"  # An issue that has been closed as not planned


class IssueCommentOrderField(Enum):

    UPDATED_AT = "UPDATED_AT"  # Order issue comments by update time


class IssueOrderField(Enum):

    COMMENTS = "COMMENTS"  # Order issues by comment count
    CREATED_AT = "CREATED_AT"  # Order issues by creation time
    UPDATED_AT = "UPDATED_AT"  # Order issues by update time


class IssueState(Enum):

    CLOSED = "CLOSED"  # An issue that has been closed
    OPEN = "OPEN"  # An issue that is still open


class IssueStateReason(Enum):

    COMPLETED = "COMPLETED"  # An issue that has been closed as completed
    NOT_PLANNED = "NOT_PLANNED"  # An issue that has been closed as not planned
    REOPENED = "REOPENED"  # An issue that has been reopened


class IssueTimelineItemsItemType(Enum):

    ADDED_TO_PROJECT_EVENT = "ADDED_TO_PROJECT_EVENT"  # Represents a 'added_to_project' event on a given issue or pull request.
    ASSIGNED_EVENT = (
        "ASSIGNED_EVENT"  # Represents an 'assigned' event on any assignable object.
    )
    CLOSED_EVENT = "CLOSED_EVENT"  # Represents a 'closed' event on any `Closable`.
    COMMENT_DELETED_EVENT = "COMMENT_DELETED_EVENT"  # Represents a 'comment_deleted' event on a given issue or pull request.
    CONNECTED_EVENT = "CONNECTED_EVENT"  # Represents a 'connected' event on a given issue or pull request.
    CONVERTED_NOTE_TO_ISSUE_EVENT = "CONVERTED_NOTE_TO_ISSUE_EVENT"  # Represents a 'converted_note_to_issue' event on a given issue or pull request.
    CONVERTED_TO_DISCUSSION_EVENT = "CONVERTED_TO_DISCUSSION_EVENT"  # Represents a 'converted_to_discussion' event on a given issue.
    CROSS_REFERENCED_EVENT = "CROSS_REFERENCED_EVENT"  # Represents a mention made by one issue or pull request to another.
    DEMILESTONED_EVENT = "DEMILESTONED_EVENT"  # Represents a 'demilestoned' event on a given issue or pull request.
    DISCONNECTED_EVENT = "DISCONNECTED_EVENT"  # Represents a 'disconnected' event on a given issue or pull request.
    ISSUE_COMMENT = "ISSUE_COMMENT"  # Represents a comment on an Issue.
    LABELED_EVENT = "LABELED_EVENT"  # Represents a 'labeled' event on a given issue or pull request.
    LOCKED_EVENT = (
        "LOCKED_EVENT"  # Represents a 'locked' event on a given issue or pull request.
    )
    MARKED_AS_DUPLICATE_EVENT = "MARKED_AS_DUPLICATE_EVENT"  # Represents a 'marked_as_duplicate' event on a given issue or pull request.
    MENTIONED_EVENT = "MENTIONED_EVENT"  # Represents a 'mentioned' event on a given issue or pull request.
    MILESTONED_EVENT = "MILESTONED_EVENT"  # Represents a 'milestoned' event on a given issue or pull request.
    MOVED_COLUMNS_IN_PROJECT_EVENT = "MOVED_COLUMNS_IN_PROJECT_EVENT"  # Represents a 'moved_columns_in_project' event on a given issue or pull request.
    PINNED_EVENT = (
        "PINNED_EVENT"  # Represents a 'pinned' event on a given issue or pull request.
    )
    REFERENCED_EVENT = "REFERENCED_EVENT"  # Represents a 'referenced' event on a given `ReferencedSubject`.
    REMOVED_FROM_PROJECT_EVENT = "REMOVED_FROM_PROJECT_EVENT"  # Represents a 'removed_from_project' event on a given issue or pull request.
    RENAMED_TITLE_EVENT = "RENAMED_TITLE_EVENT"  # Represents a 'renamed' event on a given issue or pull request
    REOPENED_EVENT = (
        "REOPENED_EVENT"  # Represents a 'reopened' event on any `Closable`.
    )
    SUBSCRIBED_EVENT = (
        "SUBSCRIBED_EVENT"  # Represents a 'subscribed' event on a given `Subscribable`.
    )
    TRANSFERRED_EVENT = "TRANSFERRED_EVENT"  # Represents a 'transferred' event on a given issue or pull request.
    UNASSIGNED_EVENT = (
        "UNASSIGNED_EVENT"  # Represents an 'unassigned' event on any assignable object.
    )
    UNLABELED_EVENT = "UNLABELED_EVENT"  # Represents an 'unlabeled' event on a given issue or pull request.
    UNLOCKED_EVENT = "UNLOCKED_EVENT"  # Represents an 'unlocked' event on a given issue or pull request.
    UNMARKED_AS_DUPLICATE_EVENT = "UNMARKED_AS_DUPLICATE_EVENT"  # Represents an 'unmarked_as_duplicate' event on a given issue or pull request.
    UNPINNED_EVENT = "UNPINNED_EVENT"  # Represents an 'unpinned' event on a given issue or pull request.
    UNSUBSCRIBED_EVENT = "UNSUBSCRIBED_EVENT"  # Represents an 'unsubscribed' event on a given `Subscribable`.
    USER_BLOCKED_EVENT = (
        "USER_BLOCKED_EVENT"  # Represents a 'user_blocked' event on a given user.
    )


class LabelOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order labels by creation time
    NAME = "NAME"  # Order labels by name


class LanguageOrderField(Enum):

    SIZE = "SIZE"  # Order languages by the size of all files containing the language


class LockReason(Enum):

    OFF_TOPIC = "OFF_TOPIC"  # The issue or pull request was locked because the conversation was off-topic.
    RESOLVED = "RESOLVED"  # The issue or pull request was locked because the conversation was resolved.
    SPAM = "SPAM"  # The issue or pull request was locked because the conversation was spam.
    TOO_HEATED = "TOO_HEATED"  # The issue or pull request was locked because the conversation was too heated.


class MannequinOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order mannequins why when they were created.
    LOGIN = "LOGIN"  # Order mannequins alphabetically by their source login.


class MergeCommitMessage(Enum):

    BLANK = "BLANK"  # Default to a blank commit message.
    PR_BODY = "PR_BODY"  # Default to the pull request's body.
    PR_TITLE = "PR_TITLE"  # Default to the pull request's title.


class MergeCommitTitle(Enum):

    MERGE_MESSAGE = "MERGE_MESSAGE"  # Default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).
    PR_TITLE = "PR_TITLE"  # Default to the pull request's title.


class MergeQueueEntryState(Enum):

    AWAITING_CHECKS = (
        "AWAITING_CHECKS"  # The entry is currently waiting for checks to pass.
    )
    LOCKED = "LOCKED"  # The entry is currently locked.
    MERGEABLE = "MERGEABLE"  # The entry is currently mergeable.
    QUEUED = "QUEUED"  # The entry is currently queued.
    UNMERGEABLE = "UNMERGEABLE"  # The entry is currently unmergeable.


class MergeQueueMergingStrategy(Enum):

    ALLGREEN = "ALLGREEN"  # Entries only allowed to merge if they are passing.
    HEADGREEN = "HEADGREEN"  # Failing Entires are allowed to merge if they are with a passing entry.


class MergeStateStatus(Enum):

    BEHIND = "BEHIND"  # The head ref is out of date.
    BLOCKED = "BLOCKED"  # The merge is blocked.
    CLEAN = "CLEAN"  # Mergeable and passing commit status.
    DIRTY = "DIRTY"  # The merge commit cannot be cleanly created.
    HAS_HOOKS = (
        "HAS_HOOKS"  # Mergeable with passing commit status and pre-receive hooks.
    )
    UNKNOWN = "UNKNOWN"  # The state cannot currently be determined.
    UNSTABLE = "UNSTABLE"  # Mergeable with non-passing commit status.


class MergeableState(Enum):

    CONFLICTING = (
        "CONFLICTING"  # The pull request cannot be merged due to merge conflicts.
    )
    MERGEABLE = "MERGEABLE"  # The pull request can be merged.
    UNKNOWN = (
        "UNKNOWN"  # The mergeability of the pull request is still being calculated.
    )


class MigrationSourceType(Enum):

    AZURE_DEVOPS = "AZURE_DEVOPS"  # An Azure DevOps migration source.
    BITBUCKET_SERVER = "BITBUCKET_SERVER"  # A Bitbucket Server migration source.
    GITHUB_ARCHIVE = "GITHUB_ARCHIVE"  # A GitHub Migration API source.


class MigrationState(Enum):

    FAILED = "FAILED"  # The migration has failed.
    FAILED_VALIDATION = "FAILED_VALIDATION"  # The migration has invalid credentials.
    IN_PROGRESS = "IN_PROGRESS"  # The migration is in progress.
    NOT_STARTED = "NOT_STARTED"  # The migration has not started.
    PENDING_VALIDATION = (
        "PENDING_VALIDATION"  # The migration needs to have its credentials validated.
    )
    QUEUED = "QUEUED"  # The migration has been queued.
    SUCCEEDED = "SUCCEEDED"  # The migration has succeeded.


class MilestoneOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order milestones by when they were created.
    DUE_DATE = "DUE_DATE"  # Order milestones by when they are due.
    NUMBER = "NUMBER"  # Order milestones by their number.
    UPDATED_AT = "UPDATED_AT"  # Order milestones by when they were last updated.


class MilestoneState(Enum):

    CLOSED = "CLOSED"  # A milestone that has been closed.
    OPEN = "OPEN"  # A milestone that is still open.


class NotificationRestrictionSettingValue(Enum):

    DISABLED = "DISABLED"  # The setting is disabled for the owner.
    ENABLED = "ENABLED"  # The setting is enabled for the owner.


class OIDCProviderType(Enum):

    AAD = "AAD"  # Azure Active Directory


class OauthApplicationCreateAuditEntryState(Enum):

    ACTIVE = (
        "ACTIVE"  # The OAuth application was active and allowed to have OAuth Accesses.
    )
    PENDING_DELETION = (
        "PENDING_DELETION"  # The OAuth application was in the process of being deleted.
    )
    SUSPENDED = "SUSPENDED"  # The OAuth application was suspended from generating OAuth Accesses due to abuse or security concerns.


class OperationType(Enum):

    ACCESS = "ACCESS"  # An existing resource was accessed
    AUTHENTICATION = "AUTHENTICATION"  # A resource performed an authentication event
    CREATE = "CREATE"  # A new resource was created
    MODIFY = "MODIFY"  # An existing resource was modified
    REMOVE = "REMOVE"  # An existing resource was removed
    RESTORE = "RESTORE"  # An existing resource was restored
    TRANSFER = (
        "TRANSFER"  # An existing resource was transferred between multiple resources
    )


class OrderDirection(Enum):

    ASC = "ASC"  # Specifies an ascending order for a given `orderBy` argument.
    DESC = "DESC"  # Specifies a descending order for a given `orderBy` argument.


class OrgAddMemberAuditEntryPermission(Enum):

    ADMIN = "ADMIN"  # Can read, clone, push, and add collaborators to repositories.
    READ = "READ"  # Can read and clone repositories.


class OrgCreateAuditEntryBillingPlan(Enum):

    BUSINESS = "BUSINESS"  # Team Plan
    BUSINESS_PLUS = "BUSINESS_PLUS"  # Enterprise Cloud Plan
    FREE = "FREE"  # Free Plan
    TIERED_PER_SEAT = "TIERED_PER_SEAT"  # Tiered Per Seat Plan
    UNLIMITED = "UNLIMITED"  # Legacy Unlimited Plan


class OrgEnterpriseOwnerOrderField(Enum):

    LOGIN = "LOGIN"  # Order enterprise owners by login.


class OrgRemoveBillingManagerAuditEntryReason(Enum):

    SAML_EXTERNAL_IDENTITY_MISSING = (
        "SAML_EXTERNAL_IDENTITY_MISSING"  # SAML external identity missing
    )
    SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY = "SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY"  # SAML SSO enforcement requires an external identity
    TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE = "TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE"  # The organization required 2FA of its billing managers and this user did not have 2FA enabled.


class OrgRemoveMemberAuditEntryMembershipType(Enum):

    ADMIN = "ADMIN"  # Organization owners have full access and can change several settings, including the names of repositories that belong to the Organization and Owners team membership. In addition, organization owners can delete the organization and all of its repositories.
    BILLING_MANAGER = "BILLING_MANAGER"  # A billing manager is a user who manages the billing settings for the Organization, such as updating payment information.
    DIRECT_MEMBER = "DIRECT_MEMBER"  # A direct member is a user that is a member of the Organization.
    OUTSIDE_COLLABORATOR = "OUTSIDE_COLLABORATOR"  # An outside collaborator is a person who isn't explicitly a member of the Organization, but who has Read, Write, or Admin permissions to one or more repositories in the organization.
    SUSPENDED = "SUSPENDED"  # A suspended member.
    UNAFFILIATED = "UNAFFILIATED"  # An unaffiliated collaborator is a person who is not a member of the Organization and does not have access to any repositories in the Organization.


class OrgRemoveMemberAuditEntryReason(Enum):

    SAML_EXTERNAL_IDENTITY_MISSING = (
        "SAML_EXTERNAL_IDENTITY_MISSING"  # SAML external identity missing
    )
    SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY = "SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY"  # SAML SSO enforcement requires an external identity
    TWO_FACTOR_ACCOUNT_RECOVERY = "TWO_FACTOR_ACCOUNT_RECOVERY"  # User was removed from organization during account recovery
    TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE = "TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE"  # The organization required 2FA of its billing managers and this user did not have 2FA enabled.
    USER_ACCOUNT_DELETED = "USER_ACCOUNT_DELETED"  # User account has been deleted


class OrgRemoveOutsideCollaboratorAuditEntryMembershipType(Enum):

    BILLING_MANAGER = "BILLING_MANAGER"  # A billing manager is a user who manages the billing settings for the Organization, such as updating payment information.
    OUTSIDE_COLLABORATOR = "OUTSIDE_COLLABORATOR"  # An outside collaborator is a person who isn't explicitly a member of the Organization, but who has Read, Write, or Admin permissions to one or more repositories in the organization.
    UNAFFILIATED = "UNAFFILIATED"  # An unaffiliated collaborator is a person who is not a member of the Organization and does not have access to any repositories in the organization.


class OrgRemoveOutsideCollaboratorAuditEntryReason(Enum):

    SAML_EXTERNAL_IDENTITY_MISSING = (
        "SAML_EXTERNAL_IDENTITY_MISSING"  # SAML external identity missing
    )
    TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE = "TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE"  # The organization required 2FA of its billing managers and this user did not have 2FA enabled.


class OrgUpdateDefaultRepositoryPermissionAuditEntryPermission(Enum):

    ADMIN = "ADMIN"  # Can read, clone, push, and add collaborators to repositories.
    NONE = "NONE"  # No default permission value.
    READ = "READ"  # Can read and clone repositories.
    WRITE = "WRITE"  # Can read, clone and push to repositories.


class OrgUpdateMemberAuditEntryPermission(Enum):

    ADMIN = "ADMIN"  # Can read, clone, push, and add collaborators to repositories.
    READ = "READ"  # Can read and clone repositories.


class OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility(Enum):

    ALL = (
        "ALL"  # All organization members are restricted from creating any repositories.
    )
    INTERNAL = "INTERNAL"  # All organization members are restricted from creating internal repositories.
    NONE = "NONE"  # All organization members are allowed to create any repositories.
    PRIVATE = "PRIVATE"  # All organization members are restricted from creating private repositories.
    PRIVATE_INTERNAL = "PRIVATE_INTERNAL"  # All organization members are restricted from creating private or internal repositories.
    PUBLIC = "PUBLIC"  # All organization members are restricted from creating public repositories.
    PUBLIC_INTERNAL = "PUBLIC_INTERNAL"  # All organization members are restricted from creating public or internal repositories.
    PUBLIC_PRIVATE = "PUBLIC_PRIVATE"  # All organization members are restricted from creating public or private repositories.


class OrganizationInvitationRole(Enum):

    ADMIN = "ADMIN"  # The user is invited to be an admin of the organization.
    BILLING_MANAGER = "BILLING_MANAGER"  # The user is invited to be a billing manager of the organization.
    DIRECT_MEMBER = "DIRECT_MEMBER"  # The user is invited to be a direct member of the organization.
    REINSTATE = "REINSTATE"  # The user's previous role will be reinstated.


class OrganizationInvitationSource(Enum):

    MEMBER = "MEMBER"  # The invitation was created from the web interface or from API
    SCIM = "SCIM"  # The invitation was created from SCIM
    UNKNOWN = "UNKNOWN"  # The invitation was sent before this feature was added


class OrganizationInvitationType(Enum):

    EMAIL = "EMAIL"  # The invitation was to an email address.
    USER = "USER"  # The invitation was to an existing user.


class OrganizationMemberRole(Enum):

    ADMIN = "ADMIN"  # The user is an administrator of the organization.
    MEMBER = "MEMBER"  # The user is a member of the organization.


class OrganizationMembersCanCreateRepositoriesSettingValue(Enum):

    ALL = "ALL"  # Members will be able to create public and private repositories.
    DISABLED = (
        "DISABLED"  # Members will not be able to create public or private repositories.
    )
    INTERNAL = "INTERNAL"  # Members will be able to create only internal repositories.
    PRIVATE = "PRIVATE"  # Members will be able to create only private repositories.


class OrganizationMigrationState(Enum):

    FAILED = "FAILED"  # The Octoshift migration has failed.
    FAILED_VALIDATION = (
        "FAILED_VALIDATION"  # The Octoshift migration has invalid credentials.
    )
    IN_PROGRESS = "IN_PROGRESS"  # The Octoshift migration is in progress.
    NOT_STARTED = "NOT_STARTED"  # The Octoshift migration has not started.
    PENDING_VALIDATION = "PENDING_VALIDATION"  # The Octoshift migration needs to have its credentials validated.
    POST_REPO_MIGRATION = "POST_REPO_MIGRATION"  # The Octoshift migration is performing post repository migrations.
    PRE_REPO_MIGRATION = "PRE_REPO_MIGRATION"  # The Octoshift migration is performing pre repository migrations.
    QUEUED = "QUEUED"  # The Octoshift migration has been queued.
    REPO_MIGRATION = "REPO_MIGRATION"  # The Octoshift org migration is performing repository migrations.
    SUCCEEDED = "SUCCEEDED"  # The Octoshift migration has succeeded.


class OrganizationOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order organizations by creation time
    LOGIN = "LOGIN"  # Order organizations by login


class PackageFileOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order package files by creation time


class PackageOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order packages by creation time


class PackageType(Enum):

    DEBIAN = "DEBIAN"  # A debian package.
    PYPI = "PYPI"  # A python package.


class PackageVersionOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order package versions by creation time


class PatchStatus(Enum):

    ADDED = "ADDED"  # The file was added. Git status 'A'.
    CHANGED = "CHANGED"  # The file's type was changed. Git status 'T'.
    COPIED = "COPIED"  # The file was copied. Git status 'C'.
    DELETED = "DELETED"  # The file was deleted. Git status 'D'.
    MODIFIED = "MODIFIED"  # The file's contents were changed. Git status 'M'.
    RENAMED = "RENAMED"  # The file was renamed. Git status 'R'.


class PinnableItemType(Enum):

    GIST = "GIST"  # A gist.
    ISSUE = "ISSUE"  # An issue.
    ORGANIZATION = "ORGANIZATION"  # An organization.
    PROJECT = "PROJECT"  # A project.
    PULL_REQUEST = "PULL_REQUEST"  # A pull request.
    REPOSITORY = "REPOSITORY"  # A repository.
    TEAM = "TEAM"  # A team.
    USER = "USER"  # A user.


class PinnedDiscussionGradient(Enum):

    BLUE_MINT = "BLUE_MINT"  # A gradient of blue to mint
    BLUE_PURPLE = "BLUE_PURPLE"  # A gradient of blue to purple
    PINK_BLUE = "PINK_BLUE"  # A gradient of pink to blue
    PURPLE_CORAL = "PURPLE_CORAL"  # A gradient of purple to coral
    RED_ORANGE = "RED_ORANGE"  # A gradient of red to orange


class PinnedDiscussionPattern(Enum):

    CHEVRON_UP = "CHEVRON_UP"  # An upward-facing chevron pattern
    DOT = "DOT"  # A hollow dot pattern
    DOT_FILL = "DOT_FILL"  # A solid dot pattern
    HEART_FILL = "HEART_FILL"  # A heart pattern
    PLUS = "PLUS"  # A plus sign pattern
    ZAP = "ZAP"  # A lightning bolt pattern


class ProjectCardArchivedState(Enum):

    ARCHIVED = "ARCHIVED"  # A project card that is archived
    NOT_ARCHIVED = "NOT_ARCHIVED"  # A project card that is not archived


class ProjectCardState(Enum):

    CONTENT_ONLY = "CONTENT_ONLY"  # The card has content only.
    NOTE_ONLY = "NOTE_ONLY"  # The card has a note only.
    REDACTED = "REDACTED"  # The card is redacted.


class ProjectColumnPurpose(Enum):

    DONE = "DONE"  # The column contains cards which are complete
    IN_PROGRESS = (
        "IN_PROGRESS"  # The column contains cards which are currently being worked on
    )
    TODO = "TODO"  # The column contains cards still to be worked on


class ProjectOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order projects by creation time
    NAME = "NAME"  # Order projects by name
    UPDATED_AT = "UPDATED_AT"  # Order projects by update time


class ProjectState(Enum):

    CLOSED = "CLOSED"  # The project is closed.
    OPEN = "OPEN"  # The project is open.


class ProjectTemplate(Enum):

    AUTOMATED_KANBAN_V2 = "AUTOMATED_KANBAN_V2"  # Create a board with v2 triggers to automatically move cards across To do, In progress and Done columns.
    AUTOMATED_REVIEWS_KANBAN = "AUTOMATED_REVIEWS_KANBAN"  # Create a board with triggers to automatically move cards across columns with review automation.
    BASIC_KANBAN = (
        "BASIC_KANBAN"  # Create a board with columns for To do, In progress and Done.
    )
    BUG_TRIAGE = "BUG_TRIAGE"  # Create a board to triage and prioritize bugs with To do, priority, and Done columns.


class ProjectV2CustomFieldType(Enum):

    DATE = "DATE"  # Date
    NUMBER = "NUMBER"  # Number
    SINGLE_SELECT = "SINGLE_SELECT"  # Single Select
    TEXT = "TEXT"  # Text


class ProjectV2FieldOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order project v2 fields by creation time
    NAME = "NAME"  # Order project v2 fields by name
    POSITION = "POSITION"  # Order project v2 fields by position


class ProjectV2FieldType(Enum):

    ASSIGNEES = "ASSIGNEES"  # Assignees
    DATE = "DATE"  # Date
    ITERATION = "ITERATION"  # Iteration
    LABELS = "LABELS"  # Labels
    LINKED_PULL_REQUESTS = "LINKED_PULL_REQUESTS"  # Linked Pull Requests
    MILESTONE = "MILESTONE"  # Milestone
    NUMBER = "NUMBER"  # Number
    REPOSITORY = "REPOSITORY"  # Repository
    REVIEWERS = "REVIEWERS"  # Reviewers
    SINGLE_SELECT = "SINGLE_SELECT"  # Single Select
    TEXT = "TEXT"  # Text
    TITLE = "TITLE"  # Title
    TRACKED_BY = "TRACKED_BY"  # Tracked by
    TRACKS = "TRACKS"  # Tracks


class ProjectV2ItemFieldValueOrderField(Enum):

    POSITION = "POSITION"  # Order project v2 item field values by the their position in the project


class ProjectV2ItemOrderField(Enum):

    POSITION = "POSITION"  # Order project v2 items by the their position in the project


class ProjectV2ItemType(Enum):

    DRAFT_ISSUE = "DRAFT_ISSUE"  # Draft Issue
    ISSUE = "ISSUE"  # Issue
    PULL_REQUEST = "PULL_REQUEST"  # Pull Request
    REDACTED = "REDACTED"  # Redacted Item


class ProjectV2OrderField(Enum):

    CREATED_AT = "CREATED_AT"  # The project's date and time of creation
    NUMBER = "NUMBER"  # The project's number
    TITLE = "TITLE"  # The project's title
    UPDATED_AT = "UPDATED_AT"  # The project's date and time of update


class ProjectV2Roles(Enum):

    ADMIN = "ADMIN"  # The collaborator can view, edit, and maange the settings of the project
    NONE = "NONE"  # The collaborator has no direct access to the project
    READER = "READER"  # The collaborator can view the project
    WRITER = "WRITER"  # The collaborator can view and edit the project


class ProjectV2SingleSelectFieldOptionColor(Enum):

    BLUE = "BLUE"  # BLUE
    GRAY = "GRAY"  # GRAY
    GREEN = "GREEN"  # GREEN
    ORANGE = "ORANGE"  # ORANGE
    PINK = "PINK"  # PINK
    PURPLE = "PURPLE"  # PURPLE
    RED = "RED"  # RED
    YELLOW = "YELLOW"  # YELLOW


class ProjectV2State(Enum):

    CLOSED = "CLOSED"  # A project v2 that has been closed
    OPEN = "OPEN"  # A project v2 that is still open


class ProjectV2ViewLayout(Enum):

    BOARD_LAYOUT = "BOARD_LAYOUT"  # Board layout
    ROADMAP_LAYOUT = "ROADMAP_LAYOUT"  # Roadmap layout
    TABLE_LAYOUT = "TABLE_LAYOUT"  # Table layout


class ProjectV2ViewOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order project v2 views by creation time
    NAME = "NAME"  # Order project v2 views by name
    POSITION = "POSITION"  # Order project v2 views by position


class ProjectV2WorkflowsOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # The date and time of the workflow creation
    NAME = "NAME"  # The name of the workflow
    NUMBER = "NUMBER"  # The number of the workflow
    UPDATED_AT = "UPDATED_AT"  # The date and time of the workflow update


class PullRequestBranchUpdateMethod(Enum):

    MERGE = "MERGE"  # Update branch via merge
    REBASE = "REBASE"  # Update branch via rebase


class PullRequestMergeMethod(Enum):

    MERGE = "MERGE"  # Add all commits from the head branch to the base branch with a merge commit.
    REBASE = "REBASE"  # Add all commits from the head branch onto the base branch individually.
    SQUASH = "SQUASH"  # Combine all commits from the head branch into a single commit in the base branch.


class PullRequestOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order pull_requests by creation time
    UPDATED_AT = "UPDATED_AT"  # Order pull_requests by update time


class PullRequestReviewCommentState(Enum):

    PENDING = "PENDING"  # A comment that is part of a pending review
    SUBMITTED = "SUBMITTED"  # A comment that is part of a submitted review


class PullRequestReviewDecision(Enum):

    APPROVED = "APPROVED"  # The pull request has received an approving review.
    CHANGES_REQUESTED = (
        "CHANGES_REQUESTED"  # Changes have been requested on the pull request.
    )
    REVIEW_REQUIRED = (
        "REVIEW_REQUIRED"  # A review is required before the pull request can be merged.
    )


class PullRequestReviewEvent(Enum):

    APPROVE = "APPROVE"  # Submit feedback and approve merging these changes.
    COMMENT = "COMMENT"  # Submit general feedback without explicit approval.
    DISMISS = "DISMISS"  # Dismiss review so it now longer effects merging.
    REQUEST_CHANGES = (
        "REQUEST_CHANGES"  # Submit feedback that must be addressed before merging.
    )


class PullRequestReviewState(Enum):

    APPROVED = "APPROVED"  # A review allowing the pull request to merge.
    CHANGES_REQUESTED = (
        "CHANGES_REQUESTED"  # A review blocking the pull request from merging.
    )
    COMMENTED = "COMMENTED"  # An informational review.
    DISMISSED = "DISMISSED"  # A review that has been dismissed.
    PENDING = "PENDING"  # A review that has not yet been submitted.


class PullRequestReviewThreadSubjectType(Enum):

    FILE = "FILE"  # A comment that has been made against the file of a pull request
    LINE = "LINE"  # A comment that has been made against the line of a pull request


class PullRequestState(Enum):

    CLOSED = "CLOSED"  # A pull request that has been closed without being merged.
    MERGED = "MERGED"  # A pull request that has been closed by being merged.
    OPEN = "OPEN"  # A pull request that is still open.


class PullRequestTimelineItemsItemType(Enum):

    ADDED_TO_MERGE_QUEUE_EVENT = "ADDED_TO_MERGE_QUEUE_EVENT"  # Represents an 'added_to_merge_queue' event on a given pull request.
    ADDED_TO_PROJECT_EVENT = "ADDED_TO_PROJECT_EVENT"  # Represents a 'added_to_project' event on a given issue or pull request.
    ASSIGNED_EVENT = (
        "ASSIGNED_EVENT"  # Represents an 'assigned' event on any assignable object.
    )
    AUTOMATIC_BASE_CHANGE_FAILED_EVENT = "AUTOMATIC_BASE_CHANGE_FAILED_EVENT"  # Represents a 'automatic_base_change_failed' event on a given pull request.
    AUTOMATIC_BASE_CHANGE_SUCCEEDED_EVENT = "AUTOMATIC_BASE_CHANGE_SUCCEEDED_EVENT"  # Represents a 'automatic_base_change_succeeded' event on a given pull request.
    AUTO_MERGE_DISABLED_EVENT = "AUTO_MERGE_DISABLED_EVENT"  # Represents a 'auto_merge_disabled' event on a given pull request.
    AUTO_MERGE_ENABLED_EVENT = "AUTO_MERGE_ENABLED_EVENT"  # Represents a 'auto_merge_enabled' event on a given pull request.
    AUTO_REBASE_ENABLED_EVENT = "AUTO_REBASE_ENABLED_EVENT"  # Represents a 'auto_rebase_enabled' event on a given pull request.
    AUTO_SQUASH_ENABLED_EVENT = "AUTO_SQUASH_ENABLED_EVENT"  # Represents a 'auto_squash_enabled' event on a given pull request.
    BASE_REF_CHANGED_EVENT = "BASE_REF_CHANGED_EVENT"  # Represents a 'base_ref_changed' event on a given issue or pull request.
    BASE_REF_DELETED_EVENT = "BASE_REF_DELETED_EVENT"  # Represents a 'base_ref_deleted' event on a given pull request.
    BASE_REF_FORCE_PUSHED_EVENT = "BASE_REF_FORCE_PUSHED_EVENT"  # Represents a 'base_ref_force_pushed' event on a given pull request.
    CLOSED_EVENT = "CLOSED_EVENT"  # Represents a 'closed' event on any `Closable`.
    COMMENT_DELETED_EVENT = "COMMENT_DELETED_EVENT"  # Represents a 'comment_deleted' event on a given issue or pull request.
    CONNECTED_EVENT = "CONNECTED_EVENT"  # Represents a 'connected' event on a given issue or pull request.
    CONVERTED_NOTE_TO_ISSUE_EVENT = "CONVERTED_NOTE_TO_ISSUE_EVENT"  # Represents a 'converted_note_to_issue' event on a given issue or pull request.
    CONVERTED_TO_DISCUSSION_EVENT = "CONVERTED_TO_DISCUSSION_EVENT"  # Represents a 'converted_to_discussion' event on a given issue.
    CONVERT_TO_DRAFT_EVENT = "CONVERT_TO_DRAFT_EVENT"  # Represents a 'convert_to_draft' event on a given pull request.
    CROSS_REFERENCED_EVENT = "CROSS_REFERENCED_EVENT"  # Represents a mention made by one issue or pull request to another.
    DEMILESTONED_EVENT = "DEMILESTONED_EVENT"  # Represents a 'demilestoned' event on a given issue or pull request.
    DEPLOYED_EVENT = (
        "DEPLOYED_EVENT"  # Represents a 'deployed' event on a given pull request.
    )
    DEPLOYMENT_ENVIRONMENT_CHANGED_EVENT = "DEPLOYMENT_ENVIRONMENT_CHANGED_EVENT"  # Represents a 'deployment_environment_changed' event on a given pull request.
    DISCONNECTED_EVENT = "DISCONNECTED_EVENT"  # Represents a 'disconnected' event on a given issue or pull request.
    HEAD_REF_DELETED_EVENT = "HEAD_REF_DELETED_EVENT"  # Represents a 'head_ref_deleted' event on a given pull request.
    HEAD_REF_FORCE_PUSHED_EVENT = "HEAD_REF_FORCE_PUSHED_EVENT"  # Represents a 'head_ref_force_pushed' event on a given pull request.
    HEAD_REF_RESTORED_EVENT = "HEAD_REF_RESTORED_EVENT"  # Represents a 'head_ref_restored' event on a given pull request.
    ISSUE_COMMENT = "ISSUE_COMMENT"  # Represents a comment on an Issue.
    LABELED_EVENT = "LABELED_EVENT"  # Represents a 'labeled' event on a given issue or pull request.
    LOCKED_EVENT = (
        "LOCKED_EVENT"  # Represents a 'locked' event on a given issue or pull request.
    )
    MARKED_AS_DUPLICATE_EVENT = "MARKED_AS_DUPLICATE_EVENT"  # Represents a 'marked_as_duplicate' event on a given issue or pull request.
    MENTIONED_EVENT = "MENTIONED_EVENT"  # Represents a 'mentioned' event on a given issue or pull request.
    MERGED_EVENT = (
        "MERGED_EVENT"  # Represents a 'merged' event on a given pull request.
    )
    MILESTONED_EVENT = "MILESTONED_EVENT"  # Represents a 'milestoned' event on a given issue or pull request.
    MOVED_COLUMNS_IN_PROJECT_EVENT = "MOVED_COLUMNS_IN_PROJECT_EVENT"  # Represents a 'moved_columns_in_project' event on a given issue or pull request.
    PINNED_EVENT = (
        "PINNED_EVENT"  # Represents a 'pinned' event on a given issue or pull request.
    )
    PULL_REQUEST_COMMIT = (
        "PULL_REQUEST_COMMIT"  # Represents a Git commit part of a pull request.
    )
    PULL_REQUEST_COMMIT_COMMENT_THREAD = "PULL_REQUEST_COMMIT_COMMENT_THREAD"  # Represents a commit comment thread part of a pull request.
    PULL_REQUEST_REVIEW = (
        "PULL_REQUEST_REVIEW"  # A review object for a given pull request.
    )
    PULL_REQUEST_REVIEW_THREAD = "PULL_REQUEST_REVIEW_THREAD"  # A threaded list of comments for a given pull request.
    PULL_REQUEST_REVISION_MARKER = "PULL_REQUEST_REVISION_MARKER"  # Represents the latest point in the pull request timeline for which the viewer has seen the pull request's commits.
    READY_FOR_REVIEW_EVENT = "READY_FOR_REVIEW_EVENT"  # Represents a 'ready_for_review' event on a given pull request.
    REFERENCED_EVENT = "REFERENCED_EVENT"  # Represents a 'referenced' event on a given `ReferencedSubject`.
    REMOVED_FROM_MERGE_QUEUE_EVENT = "REMOVED_FROM_MERGE_QUEUE_EVENT"  # Represents a 'removed_from_merge_queue' event on a given pull request.
    REMOVED_FROM_PROJECT_EVENT = "REMOVED_FROM_PROJECT_EVENT"  # Represents a 'removed_from_project' event on a given issue or pull request.
    RENAMED_TITLE_EVENT = "RENAMED_TITLE_EVENT"  # Represents a 'renamed' event on a given issue or pull request
    REOPENED_EVENT = (
        "REOPENED_EVENT"  # Represents a 'reopened' event on any `Closable`.
    )
    REVIEW_DISMISSED_EVENT = "REVIEW_DISMISSED_EVENT"  # Represents a 'review_dismissed' event on a given issue or pull request.
    REVIEW_REQUESTED_EVENT = "REVIEW_REQUESTED_EVENT"  # Represents an 'review_requested' event on a given pull request.
    REVIEW_REQUEST_REMOVED_EVENT = "REVIEW_REQUEST_REMOVED_EVENT"  # Represents an 'review_request_removed' event on a given pull request.
    SUBSCRIBED_EVENT = (
        "SUBSCRIBED_EVENT"  # Represents a 'subscribed' event on a given `Subscribable`.
    )
    TRANSFERRED_EVENT = "TRANSFERRED_EVENT"  # Represents a 'transferred' event on a given issue or pull request.
    UNASSIGNED_EVENT = (
        "UNASSIGNED_EVENT"  # Represents an 'unassigned' event on any assignable object.
    )
    UNLABELED_EVENT = "UNLABELED_EVENT"  # Represents an 'unlabeled' event on a given issue or pull request.
    UNLOCKED_EVENT = "UNLOCKED_EVENT"  # Represents an 'unlocked' event on a given issue or pull request.
    UNMARKED_AS_DUPLICATE_EVENT = "UNMARKED_AS_DUPLICATE_EVENT"  # Represents an 'unmarked_as_duplicate' event on a given issue or pull request.
    UNPINNED_EVENT = "UNPINNED_EVENT"  # Represents an 'unpinned' event on a given issue or pull request.
    UNSUBSCRIBED_EVENT = "UNSUBSCRIBED_EVENT"  # Represents an 'unsubscribed' event on a given `Subscribable`.
    USER_BLOCKED_EVENT = (
        "USER_BLOCKED_EVENT"  # Represents a 'user_blocked' event on a given user.
    )


class PullRequestUpdateState(Enum):

    CLOSED = "CLOSED"  # A pull request that has been closed without being merged.
    OPEN = "OPEN"  # A pull request that is still open.


class ReactionContent(Enum):

    CONFUSED = "CONFUSED"  # Represents the `:confused:` emoji.
    EYES = "EYES"  # Represents the `:eyes:` emoji.
    HEART = "HEART"  # Represents the `:heart:` emoji.
    HOORAY = "HOORAY"  # Represents the `:hooray:` emoji.
    LAUGH = "LAUGH"  # Represents the `:laugh:` emoji.
    ROCKET = "ROCKET"  # Represents the `:rocket:` emoji.
    THUMBS_DOWN = "THUMBS_DOWN"  # Represents the `:-1:` emoji.
    THUMBS_UP = "THUMBS_UP"  # Represents the `:+1:` emoji.


class ReactionOrderField(Enum):

    CREATED_AT = (
        "CREATED_AT"  # Allows ordering a list of reactions by when they were created.
    )


class RefOrderField(Enum):

    ALPHABETICAL = "ALPHABETICAL"  # Order refs by their alphanumeric name
    TAG_COMMIT_DATE = "TAG_COMMIT_DATE"  # Order refs by underlying commit date if the ref prefix is refs/tags/


class ReleaseOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order releases by creation time
    NAME = "NAME"  # Order releases alphabetically by name


class RepoAccessAuditEntryVisibility(Enum):

    INTERNAL = (
        "INTERNAL"  # The repository is visible only to users in the same business.
    )
    PRIVATE = "PRIVATE"  # The repository is visible only to those with explicit access.
    PUBLIC = "PUBLIC"  # The repository is visible to everyone.


class RepoAddMemberAuditEntryVisibility(Enum):

    INTERNAL = (
        "INTERNAL"  # The repository is visible only to users in the same business.
    )
    PRIVATE = "PRIVATE"  # The repository is visible only to those with explicit access.
    PUBLIC = "PUBLIC"  # The repository is visible to everyone.


class RepoArchivedAuditEntryVisibility(Enum):

    INTERNAL = (
        "INTERNAL"  # The repository is visible only to users in the same business.
    )
    PRIVATE = "PRIVATE"  # The repository is visible only to those with explicit access.
    PUBLIC = "PUBLIC"  # The repository is visible to everyone.


class RepoChangeMergeSettingAuditEntryMergeType(Enum):

    MERGE = "MERGE"  # The pull request is added to the base branch in a merge commit.
    REBASE = "REBASE"  # Commits from the pull request are added onto the base branch individually without a merge commit.
    SQUASH = "SQUASH"  # The pull request's commits are squashed into a single commit before they are merged to the base branch.


class RepoCreateAuditEntryVisibility(Enum):

    INTERNAL = (
        "INTERNAL"  # The repository is visible only to users in the same business.
    )
    PRIVATE = "PRIVATE"  # The repository is visible only to those with explicit access.
    PUBLIC = "PUBLIC"  # The repository is visible to everyone.


class RepoDestroyAuditEntryVisibility(Enum):

    INTERNAL = (
        "INTERNAL"  # The repository is visible only to users in the same business.
    )
    PRIVATE = "PRIVATE"  # The repository is visible only to those with explicit access.
    PUBLIC = "PUBLIC"  # The repository is visible to everyone.


class RepoRemoveMemberAuditEntryVisibility(Enum):

    INTERNAL = (
        "INTERNAL"  # The repository is visible only to users in the same business.
    )
    PRIVATE = "PRIVATE"  # The repository is visible only to those with explicit access.
    PUBLIC = "PUBLIC"  # The repository is visible to everyone.


class ReportedContentClassifiers(Enum):

    ABUSE = "ABUSE"  # An abusive or harassing piece of content
    DUPLICATE = "DUPLICATE"  # A duplicated piece of content
    OFF_TOPIC = "OFF_TOPIC"  # An irrelevant piece of content
    OUTDATED = "OUTDATED"  # An outdated piece of content
    RESOLVED = "RESOLVED"  # The content has been resolved
    SPAM = "SPAM"  # A spammy piece of content


class RepositoryAffiliation(Enum):

    COLLABORATOR = "COLLABORATOR"  # Repositories that the user has been added to as a collaborator.
    ORGANIZATION_MEMBER = "ORGANIZATION_MEMBER"  # Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on.
    OWNER = "OWNER"  # Repositories that are owned by the authenticated user.


class RepositoryContributionType(Enum):

    COMMIT = "COMMIT"  # Created a commit
    ISSUE = "ISSUE"  # Created an issue
    PULL_REQUEST = "PULL_REQUEST"  # Created a pull request
    PULL_REQUEST_REVIEW = "PULL_REQUEST_REVIEW"  # Reviewed a pull request
    REPOSITORY = "REPOSITORY"  # Created the repository


class RepositoryInteractionLimit(Enum):

    COLLABORATORS_ONLY = "COLLABORATORS_ONLY"  # Users that are not collaborators will not be able to interact with the repository.
    CONTRIBUTORS_ONLY = "CONTRIBUTORS_ONLY"  # Users that have not previously committed to a repository’s default branch will be unable to interact with the repository.
    EXISTING_USERS = "EXISTING_USERS"  # Users that have recently created their account will be unable to interact with the repository.
    NO_LIMIT = "NO_LIMIT"  # No interaction limits are enabled.


class RepositoryInteractionLimitExpiry(Enum):

    ONE_DAY = "ONE_DAY"  # The interaction limit will expire after 1 day.
    ONE_MONTH = "ONE_MONTH"  # The interaction limit will expire after 1 month.
    ONE_WEEK = "ONE_WEEK"  # The interaction limit will expire after 1 week.
    SIX_MONTHS = "SIX_MONTHS"  # The interaction limit will expire after 6 months.
    THREE_DAYS = "THREE_DAYS"  # The interaction limit will expire after 3 days.


class RepositoryInteractionLimitOrigin(Enum):

    ORGANIZATION = (
        "ORGANIZATION"  # A limit that is configured at the organization level.
    )
    REPOSITORY = "REPOSITORY"  # A limit that is configured at the repository level.
    USER = "USER"  # A limit that is configured at the user-wide level.


class RepositoryInvitationOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order repository invitations by creation time


class RepositoryLockReason(Enum):

    BILLING = "BILLING"  # The repository is locked due to a billing related reason.
    MIGRATING = "MIGRATING"  # The repository is locked due to a migration.
    MOVING = "MOVING"  # The repository is locked due to a move.
    RENAME = "RENAME"  # The repository is locked due to a rename.
    TRADE_RESTRICTION = "TRADE_RESTRICTION"  # The repository is locked due to a trade controls related reason.
    TRANSFERRING_OWNERSHIP = "TRANSFERRING_OWNERSHIP"  # The repository is locked due to an ownership transfer.


class RepositoryMigrationOrderDirection(Enum):

    ASC = "ASC"  # Specifies an ascending order for a given `orderBy` argument.
    DESC = "DESC"  # Specifies a descending order for a given `orderBy` argument.


class RepositoryMigrationOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order mannequins why when they were created.


class RepositoryOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order repositories by creation time
    NAME = "NAME"  # Order repositories by name
    PUSHED_AT = "PUSHED_AT"  # Order repositories by push time
    STARGAZERS = "STARGAZERS"  # Order repositories by number of stargazers
    UPDATED_AT = "UPDATED_AT"  # Order repositories by update time


class RepositoryPermission(Enum):

    ADMIN = "ADMIN"  # Can read, clone, and push to this repository. Can also manage issues, pull requests, and repository settings, including adding collaborators
    MAINTAIN = "MAINTAIN"  # Can read, clone, and push to this repository. They can also manage issues, pull requests, and some repository settings
    READ = "READ"  # Can read and clone this repository. Can also open and comment on issues and pull requests
    TRIAGE = "TRIAGE"  # Can read and clone this repository. Can also manage issues and pull requests
    WRITE = "WRITE"  # Can read, clone, and push to this repository. Can also manage issues and pull requests


class RepositoryPrivacy(Enum):

    PRIVATE = "PRIVATE"  # Private
    PUBLIC = "PUBLIC"  # Public


class RepositoryRuleOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order repository rules by created time
    TYPE = "TYPE"  # Order repository rules by type
    UPDATED_AT = "UPDATED_AT"  # Order repository rules by updated time


class RepositoryRuleType(Enum):

    AUTHORIZATION = "AUTHORIZATION"  # Authorization
    BRANCH_NAME_PATTERN = "BRANCH_NAME_PATTERN"  # Branch name pattern
    COMMITTER_EMAIL_PATTERN = "COMMITTER_EMAIL_PATTERN"  # Committer email pattern
    COMMIT_AUTHOR_EMAIL_PATTERN = (
        "COMMIT_AUTHOR_EMAIL_PATTERN"  # Commit author email pattern
    )
    COMMIT_MESSAGE_PATTERN = "COMMIT_MESSAGE_PATTERN"  # Commit message pattern
    CREATION = (
        "CREATION"  # Only allow users with bypass permission to create matching refs.
    )
    DELETION = (
        "DELETION"  # Only allow users with bypass permissions to delete matching refs.
    )
    LOCK_BRANCH = "LOCK_BRANCH"  # Branch is read-only. Users cannot push to the branch.
    MAX_REF_UPDATES = "MAX_REF_UPDATES"  # Max ref updates
    MERGE_QUEUE = "MERGE_QUEUE"  # Merges must be performed via a merge queue.
    MERGE_QUEUE_LOCKED_REF = "MERGE_QUEUE_LOCKED_REF"  # Merge queue locked ref
    NON_FAST_FORWARD = (
        "NON_FAST_FORWARD"  # Prevent users with push access from force pushing to refs.
    )
    PULL_REQUEST = "PULL_REQUEST"  # Require all commits be made to a non-target branch and submitted via a pull request before they can be merged.
    REQUIRED_DEPLOYMENTS = "REQUIRED_DEPLOYMENTS"  # Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule.
    REQUIRED_LINEAR_HISTORY = "REQUIRED_LINEAR_HISTORY"  # Prevent merge commits from being pushed to matching refs.
    REQUIRED_REVIEW_THREAD_RESOLUTION = "REQUIRED_REVIEW_THREAD_RESOLUTION"  # When enabled, all conversations on code must be resolved before a pull request can be merged into a branch that matches this rule.
    REQUIRED_SIGNATURES = "REQUIRED_SIGNATURES"  # Commits pushed to matching refs must have verified signatures.
    REQUIRED_STATUS_CHECKS = "REQUIRED_STATUS_CHECKS"  # Choose which status checks must pass before the ref is updated. When enabled, commits must first be pushed to another ref where the checks pass.
    REQUIRED_WORKFLOW_STATUS_CHECKS = "REQUIRED_WORKFLOW_STATUS_CHECKS"  # Require all commits be made to a non-target branch and submitted via a pull request and required workflow checks to pass before they can be merged.
    SECRET_SCANNING = "SECRET_SCANNING"  # Secret scanning
    TAG = "TAG"  # Tag
    TAG_NAME_PATTERN = "TAG_NAME_PATTERN"  # Tag name pattern
    UPDATE = (
        "UPDATE"  # Only allow users with bypass permission to update matching refs.
    )
    WORKFLOWS = "WORKFLOWS"  # Require all changes made to a targeted branch to pass the specified workflows before they can be merged.
    WORKFLOW_UPDATES = "WORKFLOW_UPDATES"  # Workflow files cannot be modified.


class RepositoryRulesetBypassActorBypassMode(Enum):

    ALWAYS = "ALWAYS"  # The actor can always bypass rules
    PULL_REQUEST = "PULL_REQUEST"  # The actor can only bypass rules via a pull request


class RepositoryRulesetTarget(Enum):

    BRANCH = "BRANCH"  # Branch
    TAG = "TAG"  # Tag


class RepositoryVisibility(Enum):

    INTERNAL = (
        "INTERNAL"  # The repository is visible only to users in the same business.
    )
    PRIVATE = "PRIVATE"  # The repository is visible only to those with explicit access.
    PUBLIC = "PUBLIC"  # The repository is visible to everyone.


class RepositoryVulnerabilityAlertDependencyScope(Enum):

    DEVELOPMENT = "DEVELOPMENT"  # A dependency that is only used in development
    RUNTIME = "RUNTIME"  # A dependency that is leveraged during application runtime


class RepositoryVulnerabilityAlertState(Enum):

    AUTO_DISMISSED = (
        "AUTO_DISMISSED"  # An alert that has been automatically closed by Dependabot.
    )
    DISMISSED = "DISMISSED"  # An alert that has been manually closed by a user.
    FIXED = "FIXED"  # An alert that has been resolved by a code change.
    OPEN = "OPEN"  # An alert that is still open.


class RequestableCheckStatusState(Enum):

    COMPLETED = "COMPLETED"  # The check suite or run has been completed.
    IN_PROGRESS = "IN_PROGRESS"  # The check suite or run is in progress.
    PENDING = "PENDING"  # The check suite or run is in pending state.
    QUEUED = "QUEUED"  # The check suite or run has been queued.
    WAITING = "WAITING"  # The check suite or run is in waiting state.


class RoleInOrganization(Enum):

    DIRECT_MEMBER = (
        "DIRECT_MEMBER"  # A user who is a direct member of the organization.
    )
    OWNER = "OWNER"  # A user with full administrative access to the organization.
    UNAFFILIATED = "UNAFFILIATED"  # A user who is unaffiliated with the organization.


class RuleEnforcement(Enum):

    ACTIVE = "ACTIVE"  # Rules will be enforced
    DISABLED = "DISABLED"  # Do not evaluate or enforce rules
    EVALUATE = "EVALUATE"  # Allow admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise).


class SamlDigestAlgorithm(Enum):

    SHA1 = "SHA1"  # SHA1
    SHA256 = "SHA256"  # SHA256
    SHA384 = "SHA384"  # SHA384
    SHA512 = "SHA512"  # SHA512


class SamlSignatureAlgorithm(Enum):

    RSA_SHA1 = "RSA_SHA1"  # RSA-SHA1
    RSA_SHA256 = "RSA_SHA256"  # RSA-SHA256
    RSA_SHA384 = "RSA_SHA384"  # RSA-SHA384
    RSA_SHA512 = "RSA_SHA512"  # RSA-SHA512


class SavedReplyOrderField(Enum):

    UPDATED_AT = "UPDATED_AT"  # Order saved reply by when they were updated.


class SearchType(Enum):

    DISCUSSION = "DISCUSSION"  # Returns matching discussions in repositories.
    ISSUE = "ISSUE"  # Returns results matching issues in repositories.
    REPOSITORY = "REPOSITORY"  # Returns results matching repositories.
    USER = "USER"  # Returns results matching users and organizations on GitHub.


class SecurityAdvisoryClassification(Enum):

    GENERAL = "GENERAL"  # Classification of general advisories.
    MALWARE = "MALWARE"  # Classification of malware advisories.


class SecurityAdvisoryEcosystem(Enum):

    ACTIONS = "ACTIONS"  # GitHub Actions
    COMPOSER = "COMPOSER"  # PHP packages hosted at packagist.org
    ERLANG = "ERLANG"  # Erlang/Elixir packages hosted at hex.pm
    GO = "GO"  # Go modules
    MAVEN = "MAVEN"  # Java artifacts hosted at the Maven central repository
    NPM = "NPM"  # JavaScript packages hosted at npmjs.com
    NUGET = "NUGET"  # .NET packages hosted at the NuGet Gallery
    PIP = "PIP"  # Python packages hosted at PyPI.org
    PUB = "PUB"  # Dart packages hosted at pub.dev
    RUBYGEMS = "RUBYGEMS"  # Ruby gems hosted at RubyGems.org
    RUST = "RUST"  # Rust crates
    SWIFT = "SWIFT"  # Swift packages


class SecurityAdvisoryIdentifierType(Enum):

    CVE = "CVE"  # Common Vulnerabilities and Exposures Identifier.
    GHSA = "GHSA"  # GitHub Security Advisory ID.


class SecurityAdvisoryOrderField(Enum):

    PUBLISHED_AT = "PUBLISHED_AT"  # Order advisories by publication time
    UPDATED_AT = "UPDATED_AT"  # Order advisories by update time


class SecurityAdvisorySeverity(Enum):

    CRITICAL = "CRITICAL"  # Critical.
    HIGH = "HIGH"  # High.
    LOW = "LOW"  # Low.
    MODERATE = "MODERATE"  # Moderate.


class SecurityVulnerabilityOrderField(Enum):

    UPDATED_AT = "UPDATED_AT"  # Order vulnerability by update time


class SocialAccountProvider(Enum):

    FACEBOOK = "FACEBOOK"  # Social media and networking website.
    GENERIC = "GENERIC"  # Catch-all for social media providers that do not yet have specific handling.
    HOMETOWN = "HOMETOWN"  # Fork of Mastodon with a greater focus on local posting.
    INSTAGRAM = (
        "INSTAGRAM"  # Social media website with a focus on photo and video sharing.
    )
    LINKEDIN = "LINKEDIN"  # Professional networking website.
    MASTODON = "MASTODON"  # Open-source federated microblogging service.
    NPM = "NPM"  # JavaScript package registry.
    REDDIT = "REDDIT"  # Social news aggregation and discussion website.
    TWITCH = "TWITCH"  # Live-streaming service.
    TWITTER = "TWITTER"  # Microblogging website.
    YOUTUBE = "YOUTUBE"  # Online video platform.


class SponsorAndLifetimeValueOrderField(Enum):

    LIFETIME_VALUE = "LIFETIME_VALUE"  # Order results by how much money the sponsor has paid in total.
    SPONSOR_LOGIN = "SPONSOR_LOGIN"  # Order results by the sponsor's login (username).
    SPONSOR_RELEVANCE = (
        "SPONSOR_RELEVANCE"  # Order results by the sponsor's relevance to the viewer.
    )


class SponsorOrderField(Enum):

    LOGIN = "LOGIN"  # Order sponsorable entities by login (username).
    RELEVANCE = "RELEVANCE"  # Order sponsors by their relevance to the viewer.


class SponsorableOrderField(Enum):

    LOGIN = "LOGIN"  # Order sponsorable entities by login (username).


class SponsorsActivityAction(Enum):

    CANCELLED_SPONSORSHIP = (
        "CANCELLED_SPONSORSHIP"  # The activity was cancelling a sponsorship.
    )
    NEW_SPONSORSHIP = "NEW_SPONSORSHIP"  # The activity was starting a sponsorship.
    PENDING_CHANGE = (
        "PENDING_CHANGE"  # The activity was scheduling a downgrade or cancellation.
    )
    REFUND = "REFUND"  # The activity was funds being refunded to the sponsor or GitHub.
    SPONSOR_MATCH_DISABLED = "SPONSOR_MATCH_DISABLED"  # The activity was disabling matching for a previously matched sponsorship.
    TIER_CHANGE = "TIER_CHANGE"  # The activity was changing the sponsorship tier, either directly by the sponsor or by a scheduled/pending change.


class SponsorsActivityOrderField(Enum):

    TIMESTAMP = "TIMESTAMP"  # Order activities by when they happened.


class SponsorsActivityPeriod(Enum):

    ALL = "ALL"  # Don't restrict the activity to any date range, include all activity.
    DAY = "DAY"  # The previous calendar day.
    MONTH = "MONTH"  # The previous thirty days.
    WEEK = "WEEK"  # The previous seven days.


class SponsorsCountryOrRegionCode(Enum):

    AD = "AD"  # Andorra
    AE = "AE"  # United Arab Emirates
    AF = "AF"  # Afghanistan
    AG = "AG"  # Antigua and Barbuda
    AI = "AI"  # Anguilla
    AL = "AL"  # Albania
    AM = "AM"  # Armenia
    AO = "AO"  # Angola
    AQ = "AQ"  # Antarctica
    AR = "AR"  # Argentina
    AS = "AS"  # American Samoa
    AT = "AT"  # Austria
    AU = "AU"  # Australia
    AW = "AW"  # Aruba
    AX = "AX"  # Åland
    AZ = "AZ"  # Azerbaijan
    BA = "BA"  # Bosnia and Herzegovina
    BB = "BB"  # Barbados
    BD = "BD"  # Bangladesh
    BE = "BE"  # Belgium
    BF = "BF"  # Burkina Faso
    BG = "BG"  # Bulgaria
    BH = "BH"  # Bahrain
    BI = "BI"  # Burundi
    BJ = "BJ"  # Benin
    BL = "BL"  # Saint Barthélemy
    BM = "BM"  # Bermuda
    BN = "BN"  # Brunei Darussalam
    BO = "BO"  # Bolivia
    BQ = "BQ"  # Bonaire, Sint Eustatius and Saba
    BR = "BR"  # Brazil
    BS = "BS"  # Bahamas
    BT = "BT"  # Bhutan
    BV = "BV"  # Bouvet Island
    BW = "BW"  # Botswana
    BY = "BY"  # Belarus
    BZ = "BZ"  # Belize
    CA = "CA"  # Canada
    CC = "CC"  # Cocos (Keeling) Islands
    CD = "CD"  # Congo (Kinshasa)
    CF = "CF"  # Central African Republic
    CG = "CG"  # Congo (Brazzaville)
    CH = "CH"  # Switzerland
    CI = "CI"  # Côte d'Ivoire
    CK = "CK"  # Cook Islands
    CL = "CL"  # Chile
    CM = "CM"  # Cameroon
    CN = "CN"  # China
    CO = "CO"  # Colombia
    CR = "CR"  # Costa Rica
    CV = "CV"  # Cape Verde
    CW = "CW"  # Curaçao
    CX = "CX"  # Christmas Island
    CY = "CY"  # Cyprus
    CZ = "CZ"  # Czech Republic
    DE = "DE"  # Germany
    DJ = "DJ"  # Djibouti
    DK = "DK"  # Denmark
    DM = "DM"  # Dominica
    DO = "DO"  # Dominican Republic
    DZ = "DZ"  # Algeria
    EC = "EC"  # Ecuador
    EE = "EE"  # Estonia
    EG = "EG"  # Egypt
    EH = "EH"  # Western Sahara
    ER = "ER"  # Eritrea
    ES = "ES"  # Spain
    ET = "ET"  # Ethiopia
    FI = "FI"  # Finland
    FJ = "FJ"  # Fiji
    FK = "FK"  # Falkland Islands
    FM = "FM"  # Micronesia
    FO = "FO"  # Faroe Islands
    FR = "FR"  # France
    GA = "GA"  # Gabon
    GB = "GB"  # United Kingdom
    GD = "GD"  # Grenada
    GE = "GE"  # Georgia
    GF = "GF"  # French Guiana
    GG = "GG"  # Guernsey
    GH = "GH"  # Ghana
    GI = "GI"  # Gibraltar
    GL = "GL"  # Greenland
    GM = "GM"  # Gambia
    GN = "GN"  # Guinea
    GP = "GP"  # Guadeloupe
    GQ = "GQ"  # Equatorial Guinea
    GR = "GR"  # Greece
    GS = "GS"  # South Georgia and South Sandwich Islands
    GT = "GT"  # Guatemala
    GU = "GU"  # Guam
    GW = "GW"  # Guinea-Bissau
    GY = "GY"  # Guyana
    HK = "HK"  # Hong Kong
    HM = "HM"  # Heard and McDonald Islands
    HN = "HN"  # Honduras
    HR = "HR"  # Croatia
    HT = "HT"  # Haiti
    HU = "HU"  # Hungary
    ID = "ID"  # Indonesia
    IE = "IE"  # Ireland
    IL = "IL"  # Israel
    IM = "IM"  # Isle of Man
    IN = "IN"  # India
    IO = "IO"  # British Indian Ocean Territory
    IQ = "IQ"  # Iraq
    IR = "IR"  # Iran
    IS = "IS"  # Iceland
    IT = "IT"  # Italy
    JE = "JE"  # Jersey
    JM = "JM"  # Jamaica
    JO = "JO"  # Jordan
    JP = "JP"  # Japan
    KE = "KE"  # Kenya
    KG = "KG"  # Kyrgyzstan
    KH = "KH"  # Cambodia
    KI = "KI"  # Kiribati
    KM = "KM"  # Comoros
    KN = "KN"  # Saint Kitts and Nevis
    KR = "KR"  # Korea, South
    KW = "KW"  # Kuwait
    KY = "KY"  # Cayman Islands
    KZ = "KZ"  # Kazakhstan
    LA = "LA"  # Laos
    LB = "LB"  # Lebanon
    LC = "LC"  # Saint Lucia
    LI = "LI"  # Liechtenstein
    LK = "LK"  # Sri Lanka
    LR = "LR"  # Liberia
    LS = "LS"  # Lesotho
    LT = "LT"  # Lithuania
    LU = "LU"  # Luxembourg
    LV = "LV"  # Latvia
    LY = "LY"  # Libya
    MA = "MA"  # Morocco
    MC = "MC"  # Monaco
    MD = "MD"  # Moldova
    ME = "ME"  # Montenegro
    MF = "MF"  # Saint Martin (French part)
    MG = "MG"  # Madagascar
    MH = "MH"  # Marshall Islands
    MK = "MK"  # Macedonia
    ML = "ML"  # Mali
    MM = "MM"  # Myanmar
    MN = "MN"  # Mongolia
    MO = "MO"  # Macau
    MP = "MP"  # Northern Mariana Islands
    MQ = "MQ"  # Martinique
    MR = "MR"  # Mauritania
    MS = "MS"  # Montserrat
    MT = "MT"  # Malta
    MU = "MU"  # Mauritius
    MV = "MV"  # Maldives
    MW = "MW"  # Malawi
    MX = "MX"  # Mexico
    MY = "MY"  # Malaysia
    MZ = "MZ"  # Mozambique
    NA = "NA"  # Namibia
    NC = "NC"  # New Caledonia
    NE = "NE"  # Niger
    NF = "NF"  # Norfolk Island
    NG = "NG"  # Nigeria
    NI = "NI"  # Nicaragua
    NL = "NL"  # Netherlands
    NO = "NO"  # Norway
    NP = "NP"  # Nepal
    NR = "NR"  # Nauru
    NU = "NU"  # Niue
    NZ = "NZ"  # New Zealand
    OM = "OM"  # Oman
    PA = "PA"  # Panama
    PE = "PE"  # Peru
    PF = "PF"  # French Polynesia
    PG = "PG"  # Papua New Guinea
    PH = "PH"  # Philippines
    PK = "PK"  # Pakistan
    PL = "PL"  # Poland
    PM = "PM"  # Saint Pierre and Miquelon
    PN = "PN"  # Pitcairn
    PR = "PR"  # Puerto Rico
    PS = "PS"  # Palestine
    PT = "PT"  # Portugal
    PW = "PW"  # Palau
    PY = "PY"  # Paraguay
    QA = "QA"  # Qatar
    RE = "RE"  # Reunion
    RO = "RO"  # Romania
    RS = "RS"  # Serbia
    RU = "RU"  # Russian Federation
    RW = "RW"  # Rwanda
    SA = "SA"  # Saudi Arabia
    SB = "SB"  # Solomon Islands
    SC = "SC"  # Seychelles
    SD = "SD"  # Sudan
    SE = "SE"  # Sweden
    SG = "SG"  # Singapore
    SH = "SH"  # Saint Helena
    SI = "SI"  # Slovenia
    SJ = "SJ"  # Svalbard and Jan Mayen Islands
    SK = "SK"  # Slovakia
    SL = "SL"  # Sierra Leone
    SM = "SM"  # San Marino
    SN = "SN"  # Senegal
    SO = "SO"  # Somalia
    SR = "SR"  # Suriname
    SS = "SS"  # South Sudan
    ST = "ST"  # Sao Tome and Principe
    SV = "SV"  # El Salvador
    SX = "SX"  # Sint Maarten (Dutch part)
    SZ = "SZ"  # Swaziland
    TC = "TC"  # Turks and Caicos Islands
    TD = "TD"  # Chad
    TF = "TF"  # French Southern Lands
    TG = "TG"  # Togo
    TH = "TH"  # Thailand
    TJ = "TJ"  # Tajikistan
    TK = "TK"  # Tokelau
    TL = "TL"  # Timor-Leste
    TM = "TM"  # Turkmenistan
    TN = "TN"  # Tunisia
    TO = "TO"  # Tonga
    TR = "TR"  # Türkiye
    TT = "TT"  # Trinidad and Tobago
    TV = "TV"  # Tuvalu
    TW = "TW"  # Taiwan
    TZ = "TZ"  # Tanzania
    UA = "UA"  # Ukraine
    UG = "UG"  # Uganda
    UM = "UM"  # United States Minor Outlying Islands
    US = "US"  # United States of America
    UY = "UY"  # Uruguay
    UZ = "UZ"  # Uzbekistan
    VA = "VA"  # Vatican City
    VC = "VC"  # Saint Vincent and the Grenadines
    VE = "VE"  # Venezuela
    VG = "VG"  # Virgin Islands, British
    VI = "VI"  # Virgin Islands, U.S.
    VN = "VN"  # Vietnam
    VU = "VU"  # Vanuatu
    WF = "WF"  # Wallis and Futuna Islands
    WS = "WS"  # Samoa
    YE = "YE"  # Yemen
    YT = "YT"  # Mayotte
    ZA = "ZA"  # South Africa
    ZM = "ZM"  # Zambia
    ZW = "ZW"  # Zimbabwe


class SponsorsGoalKind(Enum):

    MONTHLY_SPONSORSHIP_AMOUNT = "MONTHLY_SPONSORSHIP_AMOUNT"  # The goal is about getting a certain amount in USD from sponsorships each month.
    TOTAL_SPONSORS_COUNT = "TOTAL_SPONSORS_COUNT"  # The goal is about reaching a certain number of sponsors.


class SponsorsListingFeaturedItemFeatureableType(Enum):

    REPOSITORY = "REPOSITORY"  # A repository owned by the user or organization with the GitHub Sponsors profile.
    USER = "USER"  # A user who belongs to the organization with the GitHub Sponsors profile.


class SponsorsTierOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order tiers by creation time.
    MONTHLY_PRICE_IN_CENTS = (
        "MONTHLY_PRICE_IN_CENTS"  # Order tiers by their monthly price in cents
    )


class SponsorshipNewsletterOrderField(Enum):

    CREATED_AT = (
        "CREATED_AT"  # Order sponsorship newsletters by when they were created.
    )


class SponsorshipOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order sponsorship by creation time.


class SponsorshipPaymentSource(Enum):

    GITHUB = "GITHUB"  # Payment was made through GitHub.
    PATREON = "PATREON"  # Payment was made through Patreon.


class SponsorshipPrivacy(Enum):

    PRIVATE = "PRIVATE"  # Private
    PUBLIC = "PUBLIC"  # Public


class SquashMergeCommitMessage(Enum):

    BLANK = "BLANK"  # Default to a blank commit message.
    COMMIT_MESSAGES = "COMMIT_MESSAGES"  # Default to the branch's commit messages.
    PR_BODY = "PR_BODY"  # Default to the pull request's body.


class SquashMergeCommitTitle(Enum):

    COMMIT_OR_PR_TITLE = "COMMIT_OR_PR_TITLE"  # Default to the commit's title (if only one commit) or the pull request's title (when more than one commit).
    PR_TITLE = "PR_TITLE"  # Default to the pull request's title.


class StarOrderField(Enum):

    STARRED_AT = (
        "STARRED_AT"  # Allows ordering a list of stars by when they were created.
    )


class StatusState(Enum):

    ERROR = "ERROR"  # Status is errored.
    EXPECTED = "EXPECTED"  # Status is expected.
    FAILURE = "FAILURE"  # Status is failing.
    PENDING = "PENDING"  # Status is pending.
    SUCCESS = "SUCCESS"  # Status is successful.


class SubscriptionState(Enum):

    IGNORED = "IGNORED"  # The User is never notified.
    SUBSCRIBED = "SUBSCRIBED"  # The User is notified of all conversations.
    UNSUBSCRIBED = (
        "UNSUBSCRIBED"  # The User is only notified when participating or @mentioned.
    )


class TeamDiscussionCommentOrderField(Enum):

    NUMBER = "NUMBER"  # Allows sequential ordering of team discussion comments (which is equivalent to chronological ordering).


class TeamDiscussionOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Allows chronological ordering of team discussions.


class TeamMemberOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order team members by creation time
    LOGIN = "LOGIN"  # Order team members by login


class TeamMemberRole(Enum):

    MAINTAINER = (
        "MAINTAINER"  # A team maintainer has permission to add and remove team members.
    )
    MEMBER = "MEMBER"  # A team member has no administrative permissions on the team.


class TeamMembershipType(Enum):

    ALL = "ALL"  # Includes immediate and child team members for the team.
    CHILD_TEAM = "CHILD_TEAM"  # Includes only child team members for the team.
    IMMEDIATE = "IMMEDIATE"  # Includes only immediate members of the team.


class TeamNotificationSetting(Enum):

    NOTIFICATIONS_DISABLED = (
        "NOTIFICATIONS_DISABLED"  # No one will receive notifications.
    )
    NOTIFICATIONS_ENABLED = "NOTIFICATIONS_ENABLED"  # Everyone will receive notifications when the team is @mentioned.


class TeamOrderField(Enum):

    NAME = "NAME"  # Allows ordering a list of teams by name.


class TeamPrivacy(Enum):

    SECRET = "SECRET"  # A secret team can only be seen by its members.
    VISIBLE = "VISIBLE"  # A visible team can be seen and @mentioned by every member of the organization.


class TeamRepositoryOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order repositories by creation time
    NAME = "NAME"  # Order repositories by name
    PERMISSION = "PERMISSION"  # Order repositories by permission
    PUSHED_AT = "PUSHED_AT"  # Order repositories by push time
    STARGAZERS = "STARGAZERS"  # Order repositories by number of stargazers
    UPDATED_AT = "UPDATED_AT"  # Order repositories by update time


class TeamReviewAssignmentAlgorithm(Enum):

    LOAD_BALANCE = "LOAD_BALANCE"  # Balance review load across the entire team
    ROUND_ROBIN = "ROUND_ROBIN"  # Alternate reviews between each team member


class TeamRole(Enum):

    ADMIN = "ADMIN"  # User has admin rights on the team.
    MEMBER = "MEMBER"  # User is a member of the team.


class ThreadSubscriptionFormAction(Enum):

    NONE = "NONE"  # The User cannot subscribe or unsubscribe to the thread
    SUBSCRIBE = "SUBSCRIBE"  # The User can subscribe to the thread
    UNSUBSCRIBE = "UNSUBSCRIBE"  # The User can unsubscribe to the thread


class ThreadSubscriptionState(Enum):

    DISABLED = "DISABLED"  # The subscription status is currently disabled.
    IGNORING_LIST = (
        "IGNORING_LIST"  # The User is never notified because they are ignoring the list
    )
    IGNORING_THREAD = "IGNORING_THREAD"  # The User is never notified because they are ignoring the thread
    NONE = "NONE"  # The User is not recieving notifications from this thread
    SUBSCRIBED_TO_LIST = (
        "SUBSCRIBED_TO_LIST"  # The User is notified becuase they are watching the list
    )
    SUBSCRIBED_TO_THREAD = "SUBSCRIBED_TO_THREAD"  # The User is notified because they are subscribed to the thread
    SUBSCRIBED_TO_THREAD_EVENTS = "SUBSCRIBED_TO_THREAD_EVENTS"  # The User is notified because they chose custom settings for this thread.
    SUBSCRIBED_TO_THREAD_TYPE = "SUBSCRIBED_TO_THREAD_TYPE"  # The User is notified because they chose custom settings for this thread.
    UNAVAILABLE = "UNAVAILABLE"  # The subscription status is currently unavailable.


class TrackedIssueStates(Enum):

    CLOSED = "CLOSED"  # The tracked issue is closed
    OPEN = "OPEN"  # The tracked issue is open


class UserBlockDuration(Enum):

    ONE_DAY = "ONE_DAY"  # The user was blocked for 1 day
    ONE_MONTH = "ONE_MONTH"  # The user was blocked for 30 days
    ONE_WEEK = "ONE_WEEK"  # The user was blocked for 7 days
    PERMANENT = "PERMANENT"  # The user was blocked permanently
    THREE_DAYS = "THREE_DAYS"  # The user was blocked for 3 days


class UserStatusOrderField(Enum):

    UPDATED_AT = "UPDATED_AT"  # Order user statuses by when they were updated.


class VerifiableDomainOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order verifiable domains by their creation date.
    DOMAIN = "DOMAIN"  # Order verifiable domains by the domain name.


class WorkflowRunOrderField(Enum):

    CREATED_AT = "CREATED_AT"  # Order workflow runs by most recently created


class WorkflowState(Enum):

    ACTIVE = "ACTIVE"  # The workflow is active.
    DELETED = "DELETED"  # The workflow was deleted from the git repository.
    DISABLED_FORK = "DISABLED_FORK"  # The workflow was disabled by default on a fork.
    DISABLED_INACTIVITY = "DISABLED_INACTIVITY"  # The workflow was disabled for inactivity in the repository.
    DISABLED_MANUALLY = "DISABLED_MANUALLY"  # The workflow was disabled manually.
