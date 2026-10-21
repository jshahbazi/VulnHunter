# Phase 3d: Root-cause sweep

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

For each surviving root cause, search analogous sinks, sibling implementations, alternative data sources, shared body types, mappers, guards and call sites within declared scope. Track every discovered instance with source location and disposition. Route new candidates through gates, adversarial verification and mode-appropriate reproduction. Pattern matches alone are neither confirmed findings nor disprovals.

Output `phase3d_output.md` with root cause, search scope, query/approach, total instances, candidate IDs, protected/disproved instances with evidence, and unresolved/unreviewed instances. Counts must reconcile exactly. If no root causes survive, state sweep not applicable and retain the earlier general sink coverage pass. If the pilot budget prevents a broad sweep, record the precise omitted scope.
