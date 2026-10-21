# Phase 2b: Adversarial verification

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

Before reporting, build a flat manifest of every candidate from every class and partition. Try to disprove each against actual source, using fresh reads and the entire relevant codebase, including shared defenses. If a fresh worker is available use one; disclose sequential same-context verification otherwise. Agreement among workers is not a substitute for evidence.

Re-answer missing gates. Search all transitive sink callers, all property writers and store consumers, development/production selectors, early guards, actual dependency behavior, and cross-partition defenses. Check sanitizer context, co-parameters, absent-input paths, auth helper omissions and alternative credential branches. For a defense not inspectable in the permitted environment, keep the relevant uncertainty; never convert unavailable evidence into confirmation or elimination.

Reassess impact and prerequisites. Mechanism-only PoCs, tautological tests, tests of copied logic and mere crashes cannot establish a stronger target outcome. Do not infer deployment reachability, privilege, remote exposure, cryptographic checks or ownership delegation from comments, naming or dependency imports. Missing auth in a deliberately local library needs a concrete host boundary before it is an exploitable defect.

Spot-check protected inputs nearest sinks and perform sink/source coverage gap searches within scope. New candidates join the manifest and receive the complete pipeline. Maintain distinct source/sink instances even when sharing a root cause; any presentation grouping must list every member and disposition explicitly.

Output `phase2b_output.md`: one verdict row per candidate, gate evidence, all-callers coverage, defenses, impact, evidence state, severity rationale, and unresolved obligations. DISPROVED requires a cited defeating fact; incomplete investigation is NOT REVIEWED or STATIC-POTENTIAL. Reconcile candidate count against verdict rows before proceeding. No survivor means zero confirmed findings, with coverage limitations retained.
