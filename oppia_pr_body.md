## Overview
1. This PR fixes part of #26831.
2. This PR does the following:

This PR migrates the `lesson-creator/save-and-publish-the-exploration` acceptance test suite from Puppeteer to Playwright as part of Oppia's ongoing test suite modernization.

In particular, it rewrites the 3 exploration authoring workflows (saving/discarding draft changes, configuring the initial card and previewing states, and deleting an exploration state via the state graph) using Playwright role-based actions, removes the obsolete Puppeteer spec, and registers the suite under Playwright in `core/tests/ci-test-suite-configs/acceptance.json`.

**Key Implementation Decisions & Tricky Points:**
- **Mobile Navbar Interactions**: Added dropdown state validation and safe retry handling in `openMobileNavbarDropdown()` to prevent intermittent backdrop click interception on mobile viewports.
- **Autosave Debounce Handling**: Added network idle and save response waiting in `selectFirstCard()` to ensure backend state synchronization before navigation.
- **Graph Element Interaction**: Scoped graph node selection to modal overlays on mobile viewports to ensure accurate node deletion in state graph tests.

## Essential Checklist

Please follow the [instructions for making a code change](https://github.com/oppia/oppia/wiki/Make-a-pull-request).

- [x] I have referenced the issue(s) that this PR fixes or fixes part of on line 1 above. Once I open the PR, I will check that any issues this PR fully fixes are listed in the "Development" section of the sidebar.
- [x] I have checked the "Files Changed" tab and confirmed that the changes are what I want to make.
- [x] I have written tests for my code.
- [x] The **PR title** starts with "Fix #bugnum: " or "Fix part of #bugnum: ...", followed by a short, clear summary of the changes.
- [x] I have assigned the correct reviewers to this PR (or will leave a comment with the phrase "@{{reviewer_username}} PTAL" if I can't assign them directly).

## Proof that changes are correct

**200-Run Stress Test :** https://github.com/abdulhamid999/oppia/actions/runs/42481033309 (Passed 100% — 203/203 jobs completed with 0 failures)

**Single Verification Run (Desktop & Mobile) :** https://github.com/abdulhamid999/oppia/actions/runs/42479992070 (Passed 100%)

### Video Recordings Proof:
- **Desktop :** [Desktop Video Artifact](https://github.com/abdulhamid999/oppia/actions/runs/42487329890/artifacts/3860012217)
- **Mobile :** [Mobile Video Artifact](https://github.com/abdulhamid999/oppia/actions/runs/42487329890/artifacts/3860046556)
- **Full Video Workflow Run :** https://github.com/abdulhamid999/oppia/actions/runs/42487329890

## PR Pointers

- Never force push! If you do, your PR will be closed.
- To reply to reviewers, follow these instructions: https://github.com/oppia/oppia/wiki/Rules-for-making-PRs#step-5-address-review-comments-until-all-reviewers-approve
- Some acceptance tests are flaky, and can fail for reasons unrelated to your PR. We are working on fixing this, but in the meantime, if you need to restart the tests, please check the ["If your build fails" wiki page](https://github.com/oppia/oppia/wiki/If-CI-checks-fail-on-your-PR).
- See the [Code Owner's wiki page](https://github.com/oppia/oppia/wiki/Oppia's-code-owners-and-checks-to-be-carried-out-by-developers) for what code owners will expect.
