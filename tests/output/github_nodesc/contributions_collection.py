from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import Date, DateTime

if TYPE_CHECKING:
    from .user import User
    from .gql_types import CommitContributionsByRepository
    from .gql_types import ContributionCalendar
    from .gql_types import CreatedIssueContribution
    from .gql_unions import CreatedIssueOrRestrictedContribution
    from .gql_types import CreatedPullRequestContribution
    from .gql_unions import CreatedPullRequestOrRestrictedContribution
    from .gql_unions import CreatedRepositoryOrRestrictedContribution
    from .gql_types import CreatedIssueContributionConnection
    from .gql_types import IssueContributionsByRepository
    from .gql_types import JoinedGitHubContribution
    from .gql_types import CreatedPullRequestContributionConnection
    from .gql_types import PullRequestContributionsByRepository
    from .gql_types import CreatedPullRequestReviewContributionConnection
    from .gql_types import PullRequestReviewContributionsByRepository
    from .gql_types import CreatedRepositoryContributionConnection


@dataclass(kw_only=True)
class ContributionsCollection:
    commit_contributions_by_repository: list[CommitContributionsByRepository]
    contribution_calendar: ContributionCalendar
    contribution_years: list[int]
    does_end_in_current_month: bool
    earliest_restricted_contribution_date: Optional[Date] = None
    ended_at: DateTime
    first_issue_contribution: Optional[CreatedIssueOrRestrictedContribution] = None
    first_pull_request_contribution: Optional[
        CreatedPullRequestOrRestrictedContribution
    ] = None
    first_repository_contribution: Optional[
        CreatedRepositoryOrRestrictedContribution
    ] = None
    has_activity_in_the_past: bool
    has_any_contributions: bool
    has_any_restricted_contributions: bool
    is_single_day: bool
    issue_contributions: CreatedIssueContributionConnection
    issue_contributions_by_repository: list[IssueContributionsByRepository]
    joined_git_hub_contribution: Optional[JoinedGitHubContribution] = None
    latest_restricted_contribution_date: Optional[Date] = None
    most_recent_collection_with_activity: Optional["ContributionsCollection"] = None
    most_recent_collection_without_activity: Optional["ContributionsCollection"] = None
    popular_issue_contribution: Optional[CreatedIssueContribution] = None
    popular_pull_request_contribution: Optional[CreatedPullRequestContribution] = None
    pull_request_contributions: CreatedPullRequestContributionConnection
    pull_request_contributions_by_repository: list[PullRequestContributionsByRepository]
    pull_request_review_contributions: CreatedPullRequestReviewContributionConnection
    pull_request_review_contributions_by_repository: list[
        PullRequestReviewContributionsByRepository
    ]
    repository_contributions: CreatedRepositoryContributionConnection
    restricted_contributions_count: int
    started_at: DateTime
    total_commit_contributions: int
    total_issue_contributions: int
    total_pull_request_contributions: int
    total_pull_request_review_contributions: int
    total_repositories_with_contributed_commits: int
    total_repositories_with_contributed_issues: int
    total_repositories_with_contributed_pull_request_reviews: int
    total_repositories_with_contributed_pull_requests: int
    total_repository_contributions: int
    user: User
