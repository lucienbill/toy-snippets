const assert = require("assert");
const addg = require("../addg").addg;

describe("Unit tests for addg", function () {
  describe("Basic tests", () => {
    const tests = [
      // in, expected out
      ["addg()", undefined],
      ["addg(undefined)", undefined],
      ["addg(4)()", 4],
      ["addg(2)(2)()", 4],
      ["addg(2)(-2)()", 0],
      ["addg(3)(4)(0)()", 7],
      ["addg(2.5)()", 2.5],
      ["addg(0)(-2.5)()", -2.5],
      ['addg("b")("a")(0)()', "ba0"],
      ['addg(0)("a")("b")()', "0ab"],
      ['addg("b")("a")(-2)()', "ba-2"],
      ['addg("b")("a")(NaN)("a")()', "baNaNa"],
      ['addg("Hello")()', "Hello"],
    ];

    tests.forEach((el) => {
      it(`Sould return ${el[1]} when called like this : ${el[0]}`, function () {
        // const res = addg(el[0])
        const res = eval(el[0]);
        assert.strictEqual(res, el[1]);
      });
    });
  });

  describe("crash tests", () => {
    // crash
    const crashTest = ["addg()()", "addg(7)(7)()(7)"];

    crashTest.forEach((el) => {
      it(`should crash when called like this : ${el}`, function () {
        try {
          const res = eval(el);
          assert(false, `The call to ${el} did not crash`);
        } catch (error) {
          assert(true);
        }
      });
    });
  });

  describe("cases where it returns a function", () => {
    const fctTest = ["addg(2)", "addg(null)", "addg(2)(2)"];

    fctTest.forEach((el) => {
      it(`should return a function when called like this : ${el}`, function () {
        const res = eval(el);
        assert.equal(typeof res, "function");
      });
    });
  });

  describe("random sums", () => {
    randomSumGenerator = (n) => {
      let str = "addg(";
      let expected = 0;

      while (n > 0) {
        const r = Math.floor(Math.random() * 10000);
        n -= 1;

        str += `${r})(`;
        expected += r;
      }

      str += ")";

      return [str, expected];
    };

    let randomSums = [];
    for (let i = 0; i < 10; i++) {
      randomSums.push(randomSumGenerator(Math.floor(Math.random() * 10) + 1));
    }

    randomSums.forEach((el) => {
      it(`should return ${el[1]} when called like this : ${el[0]}`, function () {
        const res = eval(el[0]);
        assert.equal(res, el[1]);
      });
    });
  });
});
