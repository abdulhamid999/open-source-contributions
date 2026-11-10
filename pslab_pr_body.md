Relates to #3348

## Changes
- **Universal Semantics for MultimeterKnob**: Previously, `MultimeterKnob` returned `_buildDial()` on non-desktop platforms (`if (!_isDesktopOrWeb) return _buildDial();`), meaning mobile users (TalkBack on Android and VoiceOver on iOS) had zero accessibility semantics for the multimeter dial.
- **Localized Semantic Labels**: Wrapped the dial with `Semantics` across all platforms and added `label: appLocalizations.multimeter` so screen readers announce both the control identity and current channel marker (e.g. "Multimeter: CH1, adjustable").
- **Preserved Desktop Shortcuts**: Maintained `FocusableActionDetector` on desktop platforms for keyboard arrow navigation.
- **Widget & Accessibility Test**: Added `test/multimeter_knob_accessibility_test.dart` to verify localized semantics (`en` and `hi`), accessibility labels, values, and `SemanticsAction.increase` / `decrease` mode switching.

## Screenshots / Recordings
> N/A (Accessibility semantics enhancement and test coverage)

**Checklist**:
- [x] **No hard coding**: Used localized strings from `appLocalizations`.
- [x] **No end of file edits**: No modifications at end of resource files.
- [x] **Code reformatting**: Formatted using `dart format`.
- [x] **Code analysis**: Passes `flutter analyze` with 0 issues and all 38 tests pass in `flutter test`.

