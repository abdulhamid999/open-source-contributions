BigInt.prototype[Symbol.split] = () => ["custom"];
const res = "a1b".split(1n);
console.log("Result:", JSON.stringify(res));

