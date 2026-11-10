## Description

Fix #5264

`SpecifiedSplitter.split()` previously created index arrays `np.array(self.valid_indices)` and `np.array(self.test_indices)` without specifying `dtype=int`. When `valid_indices` or `test_indices` was omitted or empty (`[]`), NumPy created an array with `dtype=float64`. When `train_valid_test_split()` subsequently calls `dataset.select(...)`, NumPy threw an `IndexError: arrays used as indices must be of integer (or boolean) type`. Similarly, when all elements were assigned to validation/test sets, `train_indices` was empty and triggered the same crash. In addition, `split()` was mutating `self.valid_indices` and `self.test_indices` directly on the instance.

This PR fixes the issue by:
1. Using local variables for `valid_indices` and `test_indices` to avoid mutating instance attributes.
2. Explicitly returning `np.array(..., dtype=int)` for `train_indices`, `valid_indices`, and `test_indices`.
3. Adding comprehensive regression tests in `test_splitter.py` covering omitted indices, empty index lists, and empty train sets.

## Type of change

- [x] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentations (modification for documents)

## Checklist

- [x] My code follows the style guidelines of this project
- [x] I have performed a self-review of my own code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] New unit tests pass locally with my changes
- [x] I have checked my code and corrected any misspellings

