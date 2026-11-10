# Oppia Pull Request & Issue Claim Draft

## Issue Claim Comment (to post on https://github.com/oppia/oppia/issues/26831)

```markdown
Hi @iHamza14 @Yashbhu,

I have completed the migration of the acceptance test suite `lesson-creator/save-and-publish-the-exploration` from Puppeteer to Playwright.

- Migration commit: [`a208294`](https://github.com/abdulhamid999/oppia/commit/a208294)
- Framework configuration: Updated in `core/tests/ci-test-suite-configs/acceptance.json`
- Verification run (Desktop & Mobile): [Run #42479992070 (Passed 100%)](https://github.com/abdulhamid999/oppia/actions/runs/42479992070)
- 200-run stress test (100 Desktop + 100 Mobile): [Run #42481033309 (Passed 100% - 203/203 jobs)](https://github.com/abdulhamid999/oppia/actions/runs/42481033309)

Could you please assign this part of the issue to me? I am ready to open the pull request against `oppia:develop`. Thanks!
```

---

## Pull Request Details

### Title
`Fix part of #26831: Migrate lesson-creator/save-and-publish-the-exploration to Playwright`

### Description
```markdown
## Explanation of the changes
Part of #26831.

This PR migrates the acceptance test suite `lesson-creator/save-and-publish-the-exploration` from Puppeteer to Playwright:
1. Removed the legacy Puppeteer spec: `core/tests/puppeteer-acceptance-tests/specs/lesson-creator/save-and-publish-the-exploration.spec.ts`.
2. Created the new Playwright spec: `core/tests/playwright-acceptance-tests/specs/lesson-creator/save-and-publish-the-exploration.spec.ts`.
3. Updated `core/tests/ci-test-suite-configs/acceptance.json` to configure `lesson-creator/save-and-publish-the-exploration` with `framework: "playwright"`.
4. Ported and implemented necessary utility methods in `ExplorationEditor` (`core/tests/playwright-acceptance-tests/utilities/user/exploration-editor.ts`):
   - `discardCurrentChanges`: Handles desktop and mobile dropdown flows and confirmation modal.
   - `expectCardContentToBe`: Verifies card text with whitespace normalization.
   - `updateStateName` & `expectStateNameToBe`: Renames card state and checks container label.
   - `expectCurrentOutcomeDestinationToBe`: Checks destination node label.
   - `selectFirstCard`: Configures initial card from Settings tab.
   - `navigateToPreviewTab` & `expectPreviewCardContentToBe`: Validates state card rendering in preview mode.
   - `deleteState` & `clickOnGraphNodeElement`: Interacts with SVG exploration graph to select and remove states.

## Proof of changes
- Verification run (Desktop & Mobile): [Run #42479992070 (Passed 100%)](https://github.com/abdulhamid999/oppia/actions/runs/42479992070)
- 200-run stress test: [Run #42481033309 (Passed 100% - 203/203 jobs)](https://github.com/abdulhamid999/oppia/actions/runs/42481033309)
- CI passes across Desktop and Mobile viewports with zero flakiness.

## Checklist
- [x] The PR title starts with "Fix #bugnum: " or "Fix part of #bugnum: ...".
- [x] The PR description includes a summary of changes and reference to the parent issue.
- [x] The PR does not introduce any new lint or type errors (`npm run lint`, `npm run type-check`).
- [x] The tests pass locally and on GitHub Actions CI.
```

