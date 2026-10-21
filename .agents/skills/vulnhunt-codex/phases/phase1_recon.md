# Phase 1: Reconnaissance

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

Discover production files, languages, public library APIs, CLI commands, network handlers, FFI boundaries, parsers, file/model loaders, and framework-managed administration endpoints. Read build selectors and configuration to find the actual production variant; do not audit mocks as production. Tests, documentation, generated code, vendored code, and ordinary build scripts are outside finding scope by default, but may establish behavior, reachability, or defenses. Security-relevant deployment configuration is evidence when explicitly tied to the application. Read dependency implementation only where needed to verify an actual boundary; do not launch a dependency-wide audit.

Produce an input inventory with stable IDs: entry point and file:line, each parameter or body field, origin/principal, trust level, authentication and authorization enforcement, downstream users, and review status. Include absence/null behavior, attacker-controlled file contents and metadata, persisted values and all writers/readers, indirect dispatch, callbacks, selectors, and output responses. Inventory sensitive sinks before hunting to expose gaps; discovering a sink alone is no finding.

Record attacker prerequisites precisely. A local library caller is not automatically a remote attacker. Model files, token sequences, dimensions, and paths are untrusted only under a stated supported loading/calling scenario. Distinguish caller misuse from an unsafe contract or security boundary failure. Identify process privileges, resource ownership, end-user identity, service credentials, and claimed invariants without assuming uninspected host application behavior.

Construct a compact adjacency map, shared defense catalog, and partitions that keep connected entry points and sinks together. List cross-partition edges and shared middleware explicitly. Enumerate every authentication branch, promoted trust variables (for example forwarded client IP), authorization helper callers, and build-time production/development guards. An exported library API or callback can be an entry point without an internal call site; do not label it dead solely from a zero-result search.

Output `phase1_output.md`: metadata, threat assumptions, input inventory, sink inventory, shared infrastructure, partition table, and excluded/unreviewed surfaces. For a bounded pilot choose explicit inputs and explain what remains outside coverage.
