Relates to #3348

## Changes
- **Universal Semantics for PowerSourceKnob**: Previously, `PowerSourceKnob` rendered a `RawGestureDetector` with custom painters directly without any `Semantics` wrapper, leaving screen reader users (TalkBack on Android, VoiceOver on iOS) unable to perceive the pin identity, current output value, or adjust the voltage/current.
- **Localized Labels and Value Announcements**: Wrapped the dial in `Semantics(container: true, slider: true)` with localized labels for all pins (`PV1`, `PV2`, `PV3`, `PCS`, and `PSU`), along with the formatted current values and units (`V` or `mA`).
- **Semantic Increase and Decrease Actions**: Wired `onIncrease` and `onDecrease` callbacks to adjust the pin output by `powerSourceStateProvider.step` (clamping within allowable safe ranges).
- **Unit and Widget Tests**: Added `test/power_source_knob_accessibility_test.dart` to verify that `PowerSourceKnob` exposes the correct semantics, values, units, and increase/decrease actions across multiple locales (`en` and `hi`) for voltage pins (`PV1`) and current pins (`PCS`).

## Screenshots / Recordings
> N/A (Accessibility semantics enhancement and test coverage)

**Checklist**:
- [x] **No hard coding**: Used localized strings from `appLocalizations`.
- [x] **Code reformatting**: Formatted using `dart format`.
- [x] **Code analysis**: Passes `flutter analyze` with 0 issues and all tests pass in `flutter test`.

