# VulnHunter Codex port provenance

This is a modified derivative of the scanner instructions from [Capital One VulnHunter](https://github.com/capitalone/VulnHunter), pinned to commit `6d25b5c58b7820809b391ecda6a102537effe3ba`. Port prepared 2026-10-21. Upstream owner and attribution: Capital One. Upstream scanner files contain no additional copyright notices. The upstream Apache License 2.0 is preserved verbatim in [LICENSE](LICENSE); no upstream NOTICE file was present at this revision. No affiliation, endorsement, or upstream validation is implied.

## Source-bound inputs

SHA-256 hashes below identify the precise original files used to derive the port. They identify upstream inputs, not the modified port files.

| Upstream path | SHA-256 |
|---|---|
| `LICENSE` | `75efa07c4d2afb14d8226cf00b7763dd2ec1c5585a9dfe919881a3a3fef2ddac` |
| `README.md` | `3178261794d36ed3a7b2c1b9345988be27fffc796dd5e5c14d89ca092020f38d` |
| `vulnhunt/SKILL.md` | `02e3704cedf5157ed6c3bee672d218a20ccc6d415800180ef24c1dd313c50b68` |
| `vulnhunt/phases/phase1_recon.md` | `077abcb37f6d98f9212e75a5451bcdceed93a1657c37060145ac5207e5661869` |
| `vulnhunt/phases/phase2_class_inj.md` | `a543f604cf4995e6ff67adcdccc4f6dcffd390f9d2823cb30d9291267d3e68f9` |
| `vulnhunt/phases/phase2_class_log.md` | `362c82764eee2feff87a53660276b6f5e596d392ac6bc3579dd5bf9647b18573` |
| `vulnhunt/phases/phase2_class_nav.md` | `7ff1bb113dba9a23b04024af4a3f0ad38b064de554f9ba3cbac45b6327e2567b` |
| `vulnhunt/phases/phase2_hunt.md` | `394754aef2dfd9f0f72d901d5529dd857d260f1ef02bd39c13c8478f5dcac45b` |
| `vulnhunt/phases/phase2_shared.md` | `15a3b1455d4de419769a9fbb982fb2851098e75dbd8628f588ce6f2963590161` |
| `vulnhunt/phases/phase2b_verify.md` | `4fb0d2bd75cc3899613356e36fcd6e6c6a747ffbdc6d4af068222101294c1618` |
| `vulnhunt/phases/phase3_reproduce_test.md` | `3262604019d74937fda581392bfa90daa2effb6ab84b5458d8d8ad5df9fb55a1` |
| `vulnhunt/phases/phase3c_fixes.md` | `cf974538dfe4cb215bab0f4ce7c75114e1e1223f9423bd7e25a01f87ccc21bcc` |
| `vulnhunt/phases/phase3d_sweep.md` | `c9ce0ee39223b45a6c6ff2cb8af3688d8f2aa336c3e1306fb16ca704a3e1ed7e` |
| `vulnhunt/phases/phase4_report.md` | `1954d7267c8af55471f93b0a55f37af948bcaedfb35da16088ee2813612c1b03` |

## Modifications

All `SKILL.md` and `phases/*.md` instructions were rewritten and condensed for Codex. Each modified file carries an explicit modification notice. The phase filenames map to the corresponding upstream phases; the entrypoint retains reconnaissance, connected partitions, three input-driven class passes, sink coverage, gate checks, adversarial verification, reproduction, fix proposals, root-cause sweep and count reconciliation.

- Removed the Claude model gate, model-switch commands, usage slash command, Claude skill paths, fixed agent types, hardcoded agent-count minimum and Claude tool envelopes. Native delegation is bounded by available capacity with documented sequential fallback; the coordinator inspects evidence.
- Removed automatic dependency installation and source-tree result directories. Static is the default; local target execution requires authorization and isolation, preserves locks/toolchains, and cannot silently acquire dependencies or use network services. Read-only runs return their report directly.
- Added explicit bounded-pilot/full-scope distinction, unresolved coverage, per-input/class accounting, tool failures and real evidence states. Static traces and proposed tests cannot be execution-confirmed or PASS results.
- Replaced upstream missing-dependency-source-equals-ineffective-defense inference with explicit uncertainty. Removed automatic injection confirmation from unsanitized cross-service propagation, speculative downstream hostility, fixed severity floors and missing-limit-equals-DoS shortcuts. Impact requires the actual parser/consumer and protected outcome.
- Removed organization-specific gateway naming shortcuts, automatic universal-auth rollups, and heuristics treating imported names as cryptographic proof. Authentication, delegation, resource ownership and deployment reachability require verified behavior.
- Included exported library and FFI entry points rather than equating zero internal call sites with dead code. Clarified local caller capability, intended filesystem access and supported host boundaries before alleging auth bypass or remote exposure.
- Added Rust/Metal checks for allocation arithmetic, tensor metadata, alignment, buffer lifetimes, host/kernel contract, dispatch/tail bounds and synchronization; kept generic class coverage. Added single-model decision/cache contract review where relevant.
- Added privacy handling and aggregate/hash-only publication where required, no source edits/fixer execution, no external publication, prompt-injection boundaries, and evidence-preserving failure handling.

## Scope and limitations

The port includes scanner instructions only. It does not include the Claude Agent SDK runtime, web service, dependency installers, fixer, fix verifier, automation harness or upstream benchmarks. Compact references intentionally remove repetition, framework-specific mandates and unsound universal severity heuristics; this is an adapted methodology, not a byte-for-byte translation.

Structural validation verifies skill packaging only. Behavioral fixtures and the source-bound Stark pilot are recorded separately with their own hashes and actual observations; they do not establish repository-wide security, upstream benchmark parity, false-negative rates, model equivalence, or production qualification. Preserve new validation runs separately when tooling or source changes.
