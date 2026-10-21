# Codex scanner validation: 2026-10-21

## Result

The Codex scanner port passed packaging checks and a four-case synthetic forward
evaluation. The separate Stark pilot was blocked by a cybersecurity safeguard
before a completed report or coverage artifact was saved. There is no Stark
security verdict, completed coverage claim, or production qualification from
this attempt. No target source was modified.

The port is an adapted, condensed workflow. These results do not establish
equivalence with the Claude Opus scanner, general precision or recall, or
Rust/Metal security.

## Source binding

The local VulnHunter checkout and upstream source snapshot both matched commit
`6d25b5c58b7820809b391ecda6a102537effe3ba`. The fourteen original-source hashes
in the skill's `PROVENANCE.md` were independently checked against that checkout;
the copied Apache license matched byte for byte.

All twelve instruction files in the final installation match the exact bytes
evaluated by the synthetic worker. The final fourteen-file skill bundle,
including license and provenance, has SHA-256:

`df50666721f3f5e8ede4a483fc62d20258627fa80f7b9371917c12292ae14022`

Bundle hashing sorts files by relative POSIX path, then hashes each relative
path, a NUL byte, file bytes, and another NUL byte in order. The entrypoint alone
has SHA-256:

`1a84c742f1a7e43d00e76e5cd6701044dd840595801e776c4ff0795886c93dc4`

## Packaging and installation

- The official skill-creator `quick_validate.py` returned `Skill is valid!`.
  It ran with `uv` and explicitly pinned `PyYAML==6.0.3` in a temporary tool
  environment; no project dependencies or lockfiles changed.
- All local Markdown reference links resolve. No required Claude model, SDK,
  slash command, skill environment variable, or fixed agent type remains.
- The user-level symlink installer succeeded and a second run confirmed
  idempotence. It refuses to replace another installation.
- The independent fixture behavior oracle passed on Python 3.13.13 with
  `uv` 0.12.24. It uses only the standard library.

## Synthetic forward evaluation

A fresh delegated Codex worker received the skill, four source files, and the
threat model without the generator, oracle, or expected answers. The caller
controls each public function's resource/name argument; the base filesystem is
stable and trusted. The worker used original target functions and disposable
synthetic files. It performed no network access, dependency installation,
source mutation, or publication.

| Case | Execution-confirmed instances | Outcome |
|---|---:|---|
| a | 1 | Seeded filesystem boundary failure found |
| b | 0 | Corresponding containment defense verified |
| c | 1 | Seeded command interpretation boundary failure found |
| d | 0 | Corresponding literal argument defense verified |

The oracle's two positive and two negative expectations matched the worker's
verdicts. Ten structured attack/control assertions and four benign baseline
assertions passed. Defensive-control PASS rows are not additional findings.
There were five candidate hypotheses and five verification verdicts: two
execution-confirmed and three disproved. All four declared inputs received
twelve INJ/NAV/LOG dispositions; none remained unreviewed in this tiny corpus.

Reconnaissance, input-driven class passes, sink coverage, candidate falsification,
reproduction, proposed fixes, sibling sweep, and report reconciliation completed
within this declared scope. The worker used sequential fallback; its adversarial
verification reused the discovery context. This is separate from the parent
authoring context and blinded to the oracle, but is not independent verification
of each candidate. The worker recorded Python 3.15.0 and uv 0.12.24. A precise
model identifier was not recorded, limiting reproducibility.

Observed portability limitations include standalone-file Git metadata fallback,
consolidated versus separate phase reports, and portable per-child time/memory
limits. The finite synthetic harness was externally time-bounded and did not
probe resource exhaustion; it is not a general execution sandbox.

Detailed native reports, generated fixtures, and the actual-target harness
remain outside Git. Their aggregate artifact hashes are:

| Private artifact | SHA-256 |
|---|---|
| Report | `e9fb5e7820a5d608d79ff6e9a6c846695189578798dbeeac9b3e67cc2920e4b0` |
| Structured execution results | `9c50f903392222b29cb2ada2be0e3d26ffb8ec1421b03d478b71c4f2a0a95fdd` |
| Actual-target harness | `3c66bc7f1d407f7aadbf60a617b0947d3d07239556aa5ecfc662319b56874a8d` |

## Stark pilot attempt

The requested target was Stark commit
`d49e6b599ce5948f9fd90390a309cd7143b6d670`, with a bounded scope covering scorer
protocol/scoring/cache, model and safetensors loading, and directly referenced
validation. Legacy bindings, conversion tools, model weights, private inference
data, and cloud infrastructure were outside the requested pilot.

The worker reported starting reconnaissance, then terminated with a platform
cybersecurity safeguard flag. No saved pilot output directory, completed report,
coverage accounting, or execution evidence was available. The preliminary
progress message does not establish reviewed coverage. The attempt was not
retried to bypass the safeguard. Completing the Stark pilot requires a supported
authorized execution path that clears the platform restriction.

The original Stark checkout was restored to `codex/deepinfer-adoption` with a
clean working tree. Port implementation and validation documentation belong in
VulnHunter. The unrelated Stark documentation commit was preserved on its branch.
