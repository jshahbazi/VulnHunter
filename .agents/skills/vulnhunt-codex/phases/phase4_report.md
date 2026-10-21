# Phase 4: Report

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

Compile a Markdown report privately or in the final response when writes are unavailable. Include target revision/dirty state, skill revision/hash, date, static/execution mode, pilot/full scope, exact covered and excluded inputs/files, tool limits, delegation/verification independence, and threat-model assumptions. No absolute repository safety or completeness claim follows from a partial scan.

Provide:

- Aggregate counts by evidence state and calibrated severity; executed outcome counts separate from proposed tests and static traces.
- Complete declared input inventory and class dispositions, including NOT REVIEWED rows.
- Candidate manifest and one adversarial-verdict row per candidate, including DISPROVED evidence and unresolved assumptions.
- Per surviving candidate: distinct ID, source/sink file:line chain, gates, prerequisites, concrete impact, defense analysis, state, reproduction status, proposed fix, and required validation.
- Root-cause sweep with reconciled instances and explicit skipped scope.
- Quality/reliability observations separately from security findings.
- Validation limits, blocked commands, follow-up proof obligations, and private artifact hashes where appropriate.

Reconcile inventory rows, candidate/verdict rows, sweep instances and executed outcomes before finalizing. Every executed exploit outcome must map to an instance; no skipped or proposed test is counted as PASS. Preserve distinct instances under any root-cause grouping. If all candidates are disproved, say no exploitable vulnerabilities were found **within the reviewed scope**. If static candidates remain, state zero execution-confirmed findings and the number of static potentials. Avoid publishing native artifacts or sensitive details contrary to repository rules; only publish authorized aggregates and hashes.
