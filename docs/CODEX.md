# VulnHunter scanner for Codex

This repository includes a Codex port of Capital One's VulnHunter scanner at
`.agents/skills/vulnhunt-codex/`. Codex discovers skills from `.agents/skills`.
The port covers scanning and proposed remediation; it does not include upstream's
fixer, unattended runtime, publishing, or issue creation.

Read the skill's `PROVENANCE.md` for the pinned upstream revision, source hashes,
and adaptation details. Apache 2.0 attribution and the license accompany the port.
The upstream scanner was tuned for Claude Opus. This port requires separate
validation; upstream effectiveness claims do not establish Codex effectiveness.

The [2026-10-21 validation record](CODEX_VALIDATION_2026_10_21.md) reports the
four-case smoke evaluation and the blocked Stark pilot attempt.

## Run a scan

Install a user-level symlink from this checkout for scanning another repository:

```sh
uv run --no-project python tools/install_codex_skill.py
```

The installer uses `~/.agents/skills/vulnhunt-codex`, leaves an existing different
installation untouched, and requires this checkout to remain at its current
location. Re-running it for the same checkout is safe. To remove this installation,
remove that symlink. The skill is also discoverable directly within this repository.

In Codex with the target repository open, invoke `$vulnhunt-codex`, identify the source
paths and threat boundary, and select static analysis or local reproduction.
Static analysis is the default. A bounded pilot must report unreviewed paths and
cannot claim repository-wide coverage. The report distinguishes source-backed
potential findings from findings reproduced by an executed test.

For a static CLI run with a private final report:

```sh
umask 077
scan_dir=$(mktemp -d "${TMPDIR:-/tmp}/vulnhunt.XXXXXX")
codex exec --sandbox read-only --ephemeral \
  -o "$scan_dir/report.md" \
  'Use $vulnhunt-codex for a bounded static pilot of crates/stark-score/src and crates/stark-engine/src/parameters. Follow SECURITY.md. Return the report in the final response. Do not write source or publish results. Record unreviewed paths and tests not run.'
```

Run this example command from the Stark checkout after installing the skill.
For another target, replace the scope and repository policy with that target's
actual boundaries. `--ephemeral` avoids saved CLI session
files; the final audit report remains private. A read-only sandbox cannot create
the phase artifact directories described by upstream, so the port also supports
carrying phase results in memory and returning the final report. Shell tools
used for reading source are permitted in static mode; building, installing
dependencies, and running target code are separate execution choices.

Local reproduction uses synthetic inputs in a private scratch directory. Respect
the target's toolchain and dependency rules, including Stark's Rust 1.98.1,
locked dependencies, and `uv` requirements when scanning Stark. Keep
model weights, native artifacts, inference data, and detailed findings out of
commits and public issues. Keep scan-time source hashes distinct from later code
changes. The port proposes fixes without applying them.

## Synthetic smoke validation

Generate the four-case corpus outside the tracked tree, then check its actual
behavior using the independent oracle:

```sh
uv run --no-project python tools/vulnhunt_validation.py generate /tmp/vulnhunt-cases
uv run --no-project python tools/vulnhunt_validation.py check /tmp/vulnhunt-cases
```

Generation refuses to overwrite an existing destination. The cases contain path
containment and shell argument handling implementations. The oracle checks both
ordinary input and boundary-crossing input using disposable synthetic files.
Give a fresh Codex evaluator the generated cases, the skill, and the threat model:
the caller controls only the function arguments; the base filesystem is stable
and trusted. Keep the generator, oracle, and expected results out of the
evaluator's context until it has returned its report.

This corpus checks basic workflow transfer and obvious positive/negative
discrimination. Four authored cases cannot establish production recall,
false-positive rates, equivalence with Opus, or Rust/Metal memory safety.

Official Codex references: [skill discovery](https://learn.chatgpt.com/docs/build-skills)
and [non-interactive execution](https://learn.chatgpt.com/docs/non-interactive-mode).
