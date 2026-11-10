var B = class {
  constructor(components) {
    const { getHasher } = components;
    this.fn = () => getHasher("sha2-256");
  }
};
var b = new B({ getHasher: (x) => x });
console.log("Result:", b.fn());

