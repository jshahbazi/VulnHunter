# Phase 3c: Proposed fixes

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

Describe remediation without modifying production source. Address the root cause at the correct trust boundary, all callers and sibling paths, fail-closed behavior, and compatibility constraints. Prefer context-correct parameter binding, per-resource authorization, field allowlists, checked size arithmetic and validated buffer contracts over payload blacklists.

For every proposal name affected interfaces and regression checks that would demonstrate the protected invariant. Explain unresolved dependencies or behavior changes. Do not claim a proposed fix eliminates the defect before it is implemented and verified against actual source. Keep unrelated cleanup and hardening separate from required remediation. Output per-candidate strategies in `phase3_output.md`.
