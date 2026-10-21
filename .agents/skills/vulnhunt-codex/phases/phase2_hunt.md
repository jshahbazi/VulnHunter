# Phase 2: Hunting and dispatch

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

For every partition create a work packet containing its input IDs, production file scope, shared infrastructure, cross-partition edges, threat model, mode, and output destination. Analyze INJ, NAV, and LOG as separate passes using `phase2_shared.md` and the corresponding class file. Batch tasks within actual available capacity; sequential execution is valid when documented. A pilot may narrow partitions and inputs, but must apply all relevant class checks to its declared inputs.

Input-driven tracing is primary. Follow assignments, transformations, all call targets, all consumers of stored state, and all branches. A safe path does not clear an unsafe sibling path. At every outbound call inspect all security-relevant arguments, not only the variable that led there: IDs, scopes, credentials, overrides, hardcoded wildcards, and response mappers may reveal an independent issue. Attacker-selected response origins taint returned bytes; attacker-selected resource IDs require tracing sensitive response fields through mappers to the caller.

After the input passes, perform a sink-driven coverage pass across declared scope. Find dangerous sinks omitted from the inventory and trace all transitive callers back to entry points. Inspect all source flows at each sink. Add discovered input paths to the inventory and re-run relevant class checks. Do not replace the systematic input pass with searches for familiar suspicious APIs.

Output per-partition/class results with each input disposition, candidate gate records, exact source-to-sink citations, unresolved assumptions, and gaps. Aggregate a flat candidate manifest before verification. Candidate IDs must be globally unique; root causes may be grouped for discussion while distinct sources/sinks and impacts retain separate tracked instances.
