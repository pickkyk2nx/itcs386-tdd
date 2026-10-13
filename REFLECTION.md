1. Test-to-Code Ratio: I wrote 10 test functions and 41 nonblank lines of production code, resulting in a ratio of about 1 test for every 4.1 lines.

2. Longest Red Bar: The mixed-unit addition in A7 stayed red the longest because it required adding the add_rate method and updating the reduction logic to correctly handle rates instead of raw amounts.

3. Strategies Used:

Fake It: Returned a hard-coded grams(500) in A6.

Triangulate: Used multiple test cases in A2 to force a generalized multiplication rule.

Obvious Implementation: Wrote the direct multiplication code once the pattern was established.

4. Test List Status: All 7 items on the list are completed with no speculation items left. Future extensions would include testing unsupported conversion pairs.

5. Upfront Design: Designing on paper wouldn't have naturally led to the polymorphic reduce structure; the TDD process organically drove the design.

6. Part 0 vs. Part A: Part 0 involved writing tests for existing code, whereas Part A used tests to actively drive and shape the design step-by-step.