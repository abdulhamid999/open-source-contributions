## Description
Fix #3229

This PR extends `log_every_n` logging support to dataset splitters that previously accepted the argument but did not use it. Per the discussion on #3229, progress logging uses Python's standard `logger.info` with modulo checks rather than terminal progress bars like `tqdm`, keeping logs clean and reliable for non-interactive / batch environments.

Splitters updated:
- `RandomSplitter`: logs initial dataset size when `log_every_n` is set
- `SingletaskStratifiedSplitter`: logs total samples and task number
- `MolecularWeightSplitter`: logs sample progress every n calculations
- `MaxMinSplitter`: logs fingerprint generation progress every n samples
- `ButinaSplitter`: logs fingerprint generation progress every n samples and fixed logging format
- `FingerprintSplitter`: logs fingerprint generation progress every n samples

Added `test_log_every_n` in `deepchem/splits/tests/test_splitter.py` verifying that logging occurs as expected for splitters when `log_every_n` is configured.

## Type of change
- [x] New feature (non-breaking change which adds functionality)

## Checklist
- [x] My code follows the style guidelines of this project
- [x] I have performed a self-review of my own code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] New unit tests pass locally with my changes (all 27 tests passing in `test_splitter.py`)

