## Overview
1. This PR fixes part of #26838.
2. This PR does the following:

This PR migrates the `site-moderator/check-recent-feedback-messages` acceptance test suite from Puppeteer to Playwright as part of Oppia's ongoing test suite modernization.

In particular, it rewrites the site moderator acceptance test verifying recent feedback messages using Playwright role-based actions, removes the obsolete Puppeteer spec, and registers the suite under Playwright in `core/tests/ci-test-suite-configs/acceptance.json`.

**Key Implementation Decisions & Tricky Points:**
- **Moderator Role Implementation**: Created `Moderator` user class and factory in `core/tests/playwright-acceptance-tests/utilities/user/moderator.ts` and registered `ROLES.MODERATOR` in `user-factory.ts`.
- **Datetime Parsing**: Implemented `parseLocaleAbbreviatedDatetimeString` in `playwright-utils.ts` to reliably handle localized abbreviated datetime strings displayed in the moderator feedback table.
- **Feedback Submission Helper**: Added `giveFeedback` helper method in `LoggedOutUser` to streamline submitting feedback on the exploration player page.
- **Baseline Snapshots**: Updated Desktop and Mobile dev and prod baseline snapshots to match the exact Playwright CI viewport renderings.

## Essential Checklist

Please follow the [instructions for making a code change](https://github.com/oppia/oppia/wiki/Make-a-pull-request).

- [x] I have referenced the issue(s) that this PR fixes or fixes part of on line 1 above. Once I open the PR, I will check that any issues this PR fully fixes are listed in the "Development" section of the sidebar.
- [x] I have checked the "Files Changed" tab and confirmed that the changes are what I want to make.
- [x] I have written tests for my code.
- [x] The **PR title** starts with "Fix #bugnum: " or "Fix part of #bugnum: ...", followed by a short, clear summary of the changes.
- [x] I have assigned the correct reviewers to this PR (or will leave a comment with the phrase "@{{reviewer_username}} PTAL" if I can't assign them directly).

## Proof that changes are correct

**200-Run Stress Test (100 Desktop + 100 Mobile):** https://github.com/abdulhamid999/oppia/actions/runs/42498974451 (Passed 100% — 203/203 jobs completed with 0 failures)

**Single Verification Run (Desktop & Mobile):** https://github.com/abdulhamid999/oppia/actions/runs/42497871340 (Passed 100% — both Desktop and Mobile green)

### Video Recordings Proof (100% Green Run):
- **Desktop Artifact:** [Desktop Video Artifact](https://github.com/abdulhamid999/oppia/actions/runs/42559793875/artifacts/13649003804)
- **Mobile Artifact:** [Mobile Video Artifact](https://github.com/abdulhamid999/oppia/actions/runs/42559793875/artifacts/13648354681)
- **Full Video Workflow Run:** https://github.com/abdulhamid999/oppia/actions/runs/42559793875

## PR Pointers

- Never force push! If you do, your PR will be closed.
- To reply to reviewers, follow these instructions: https://github.com/oppia/oppia/wiki/Rules-for-making-PRs#step-5-address-review-comments-until-all-reviewers-approve
- Some acceptance tests are flaky, and can fail for reasons unrelated to your PR. We are working on fixing this, but in the meantime, if you need to restart the tests, please check the ["If your build fails" wiki page](https://github.com/oppia/oppia/wiki/If-CI-checks-fail-on-your-PR).
- See the [Code Owner's wiki page](https://github.com/oppia/oppia/wiki/Oppia's-code-owners-and-checks-to-be-carried-out-by-developers) for what code owners will expect.
