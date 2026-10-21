# Phase 3: Reproduce and test

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

For each surviving candidate produce the smallest useful reproducible evidence: entry point, prerequisites, controlled input, expected secure result, alleged actual result, and source chain. In static mode supply a static trace and optional proposed local test; label execution NOT RUN. Keep test payloads and source-bound artifacts private. Do not run target code merely because the shell is available.

In authorized execution mode inspect the proposed command and harness first. Use an isolated temporary checkout, pinned local dependencies, bounded time/memory, synthetic inputs and permitted local targets. Exercise the actual target implementation and original caller path; stubs, copied functions, arithmetic models and sanitizer probes can establish only their limited behavior. Do not introduce persistent services, external targets, dependency installs, credentials or uncontrolled exhaustion.

Record exact commands, checkout revision/patch state, toolchain and dependency versions, test/harness hashes, exit status, assertion outcome and sanitized aggregate observations. Avoid forbidden content and exception dumps. A zero exit code alone is not proof: the assertion must observe the unauthorized outcome or violated invariant. A compile failure, skipped test, unavailable GPU/model or inconclusive result is BLOCKED/NOT RUN/INCONCLUSIVE, never PASS. Test failure disproves a candidate only if it tests the relevant exploit conditions and establishes the defense.

Use CONFIRMED-EXECUTED only when the actual target test demonstrates the concrete security outcome. Everything source-supported but unexecuted remains STATIC-POTENTIAL, with explicit conditions. Execute no remediation as part of scanning. Store useful PoCs under the private run directory (`poc/`, `exploit_tests/`) and summarize in `phase3_output.md`; in a read-only sandbox return equivalent report sections instead.
