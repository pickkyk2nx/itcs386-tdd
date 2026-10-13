# Part B: Reflection

1. I wrote 10 test functions in `test_kitchen.py` for Part A. `kitchen.py` has 41 nonblank lines of production code (59 lines including blank lines), so the ratio is 10 tests to 41 nonblank production lines, or about 1 test for every 4.1 lines.

2. The mixed-unit addition test in A7 stayed red the longest. It first failed because `Converter` had no `add_rate` method, and after adding that interface it still failed because the sum used raw amounts and returned 201 instead of 228. Fixing it required conversion rates to reach both operands during reduction.

3. I used Fake It in A6 by making `plus` return the expected `grams(500)` directly. I triangulated in A2 with multiplication tests for 3 and 2, which showed that a hard-coded result could not work. I used an obvious implementation for `Quantity.times` once those examples established the rule: multiply the amount and preserve the unit. Each strategy fit its step: the addition fake got the first test green, triangulation exposed the general multiplication rule, and the multiplication implementation was small enough to write directly.

4. All seven items on the Part A test list are checked off. There is no listed behavior left to implement or remove as speculation. If I extended the exercise, I would next test unsupported conversion pairs and additional conversion directions; those are useful follow-up cases but were outside the given list.

5. I would not have designed `Quantity.reduce(converter, unit)` and `Sum.reduce(converter, unit)` in advance. The tests led to an unevaluated `Sum`, then the mixed-unit case showed that reduction needed both the requested unit and the converter's rates. Passing the converter into reduction let both quantities and sums use the same interface without putting conversion-rate knowledge in `Sum`.

6. Part 0 felt like checking tests against code that was already provided. In Part A, writing tests first made each failing example show what the design could not yet express. The immutability test led multiplication to return a new quantity, the different-unit equality test led `Quantity` to store its unit, and mixed-unit addition led to deferred sums and converter-aware reduction.
