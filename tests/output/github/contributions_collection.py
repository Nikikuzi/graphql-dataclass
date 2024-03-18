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
    """
        ContributionsCollection - A contributions collection aggregates contributions such as opened issues and commits created by a user.

        commitContributionsByRepository - Commit contributions made by the user, grouped by repository.

        contributionCalendar - A calendar of this user's contributions on GitHub.

        contributionYears - The years the user has been making contributions with the most recent year first.

        doesEndInCurrentMonth - Determine if this collection's time span ends in the current month.

        earliestRestrictedContributionDate - The date of the first restricted contribution the user made in this time
    period. Can only be non-null when the user has enabled private contribution counts.

        endedAt - The ending date and time of this collection.

        firstIssueContribution - The first issue the user opened on GitHub. This will be null if that issue was
    opened outside the collection's time range and ignoreTimeRange is false. If
    the issue is not visible but the user has opted to show private contributions,
    a RestrictedContribution will be returned.

        firstPullRequestContribution - The first pull request the user opened on GitHub. This will be null if that
    pull request was opened outside the collection's time range and
    ignoreTimeRange is not true. If the pull request is not visible but the user
    has opted to show private contributions, a RestrictedContribution will be returned.

        firstRepositoryContribution - The first repository the user created on GitHub. This will be null if that
    first repository was created outside the collection's time range and
    ignoreTimeRange is false. If the repository is not visible, then a
    RestrictedContribution is returned.

        hasActivityInThePast - Does the user have any more activity in the timeline that occurred prior to the collection's time range?

        hasAnyContributions - Determine if there are any contributions in this collection.

        hasAnyRestrictedContributions - Determine if the user made any contributions in this time frame whose details
    are not visible because they were made in a private repository. Can only be
    true if the user enabled private contribution counts.

        isSingleDay - Whether or not the collector's time span is all within the same day.

        issueContributions - A list of issues the user opened.

        issueContributionsByRepository - Issue contributions made by the user, grouped by repository.

        joinedGitHubContribution - When the user signed up for GitHub. This will be null if that sign up date
    falls outside the collection's time range and ignoreTimeRange is false.

        latestRestrictedContributionDate - The date of the most recent restricted contribution the user made in this time
    period. Can only be non-null when the user has enabled private contribution counts.

        mostRecentCollectionWithActivity - When this collection's time range does not include any activity from the user, use this
    to get a different collection from an earlier time range that does have activity.

        mostRecentCollectionWithoutActivity - Returns a different contributions collection from an earlier time range than this one
    that does not have any contributions.

        popularIssueContribution - The issue the user opened on GitHub that received the most comments in the specified
    time frame.

        popularPullRequestContribution - The pull request the user opened on GitHub that received the most comments in the
    specified time frame.

        pullRequestContributions - Pull request contributions made by the user.

        pullRequestContributionsByRepository - Pull request contributions made by the user, grouped by repository.

        pullRequestReviewContributions - Pull request review contributions made by the user. Returns the most recently
    submitted review for each PR reviewed by the user.

        pullRequestReviewContributionsByRepository - Pull request review contributions made by the user, grouped by repository.

        repositoryContributions - A list of repositories owned by the user that the user created in this time range.

        restrictedContributionsCount - A count of contributions made by the user that the viewer cannot access. Only
    non-zero when the user has chosen to share their private contribution counts.

        startedAt - The beginning date and time of this collection.

        totalCommitContributions - How many commits were made by the user in this time span.

        totalIssueContributions - How many issues the user opened.

        totalPullRequestContributions - How many pull requests the user opened.

        totalPullRequestReviewContributions - How many pull request reviews the user left.

        totalRepositoriesWithContributedCommits - How many different repositories the user committed to.

        totalRepositoriesWithContributedIssues - How many different repositories the user opened issues in.

        totalRepositoriesWithContributedPullRequestReviews - How many different repositories the user left pull request reviews in.

        totalRepositoriesWithContributedPullRequests - How many different repositories the user opened pull requests in.

        totalRepositoryContributions - How many repositories the user created.

        user - The user who made the contributions in this collection.

    """

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
