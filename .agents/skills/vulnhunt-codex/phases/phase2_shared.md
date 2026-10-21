# Shared tracing rules and gates

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

Read actual production function bodies. Follow all uses, dispatch targets, stores, readers, transforms, and callers until the data reaches a sink, exits the declared scope, or is effectively constrained. Leaving scope is an unresolved boundary unless the safety argument is complete. Return/log operations can be disclosure sinks. At each defense verify the implementation and context; names, comments, schema shape, transport encoding, and inferred framework defaults are insufficient. If implementation or relevant behavior is unavailable, record an unresolved assumption. Do not assume the defense succeeds or fails.

For every input examine its absence: does omission bypass validation or identity binding? Enumerate alternative auth branches and co-parameters separately. Trace all writers before declaring stored state trusted. Continue past the first candidate to independent sinks. Check early-return guards before alleging reachability, and inspect all transitive callers before declaring a sink universally protected or dead.

Apply these gates in order to each candidate, with cited evidence:

0. **Intended behavior and boundary:** State the protected invariant. Deliberate caller-serving functionality is not itself a defect; an intended feature does not exempt broken authorization, omitted validation, or memory safety.
1. **Production reachability:** Show a real entry point and transitive call chain. Include exported APIs, FFI and callbacks. Development-only and test-only paths require evidence; route names do not establish isolation.
2. **Control and defense:** (a) Identify who can control each relevant value, directly or through stores. (b) Identify every defense, guard, type constraint, size limit, and applicable context. Cite verified implementation or record unknowns. Encoding for one parser does not establish safety for another.
3. **New capability:** State the concrete outcome beyond the attacker's prerequisites: unauthorized access/modification, code execution, memory corruption, cross-context disclosure, or attacker-induced exhaustion of a protected resource. A suspicious mechanism without demonstrated outcome stays potential or a quality observation. Cite any claimed equivalent baseline capability; do not excuse missing auth by treating all currently exposed operations as authorized.

Each candidate record includes ID, inventory IDs, class/CWE, proposed severity and rationale, entry point, source-to-sink file:line chain, all gate results, defense evidence, attacker prerequisites, root cause, expected secure behavior, concrete impact, evidence state, and remaining proof obligations. Severity follows demonstrated impact and prerequisites; do not assign a fixed floor based only on API category or missing source. Unknown controls are explicitly unknown.

Inventory dispositions: `CANDIDATE`, `PROTECTED` with cited context-matched defense, `DESIGN-INTENT` with invariant rationale, `NO RELEVANT SINK` within completed tracing, or `NOT REVIEWED` with gap. These are coverage dispositions, separate from candidate evidence states. Every declared input needs a disposition per relevant class. A finding is never disproved merely because a dependency is unavailable.
