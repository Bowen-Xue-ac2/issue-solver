# Debugging, CI, and ordinary review

Use the existing test/build system. Establish the first failing step and its
contract before changing code. A timeout, unavailable registry, absent secret,
or unsupported runner is infrastructure evidence; it is not proof of a code bug.
For CI, compare the actual command, working directory, language version, lockfile,
and environment assumptions with the successful local run. Reproduce with the
smallest local equivalent; do not weaken checks to obtain a green badge.

Follow the failing value through callers and state transitions. Test one plausible
cause at a time. The repair should cover the root cause and reachable variants
within the request, rather than add broad fallback exceptions or unrelated cleanup.

Before delivery, inspect the diff and affected callers for changed contracts,
error handling, resource lifetime, and regressions. An optional `code-review`
skill can help; its organization-specific conventions do not override this
project's rules. A separate reviewer is not mandatory for every small repair.

## When properties help

For algorithms or input boundaries, choose a meaningful invariant: round-trip,
idempotence, preservation of ordering/data, bounded output, or agreement with an
independent reference. Include empty, singleton, boundary, and malformed inputs
where the contract defines them. A small exhaustive domain or seeded standard-
library generator is enough when it answers the question. Use an existing property
testing library if installed; do not add one for a single simple assertion.

For a batching bug, assert both `flatten(chunks) == input` and
`0 < len(chunk) <= size` over inputs of lengths 0..20 and sizes 1..8.
This catches dropped values and a boundary bug without asserting the implementation.
Persist a real counterexample as a regression case. Do not test undefined behavior
or make the same algorithm compute the expected result.

If the failure cannot be reproduced, retain the symptom and uncertainty, propose
the next discriminating check, and avoid claiming a completed fix.
