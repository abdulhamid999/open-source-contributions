Hi @acsses @jedel1043,

Just tested both reproduction cases on the latest `main` (commit `329e89748`):

1. **Case 1** (`class A { constructor() { const x = 1; } } new A();`): executes cleanly with no panics.
2. **Case 2** (class constructor with closure over destructured binding):
```javascript
var B = class {
  constructor(components) {
    const { getHasher } = components;
    this.fn = () => getHasher("sha2-256");
  }
};
var b = new B({ getHasher: (x) => x });
console.log("Result:", b.fn());
```
Output:
```
Result: sha2-256
```

It looks like the scope/environment refactoring in v0.22.0 has resolved this issue.

