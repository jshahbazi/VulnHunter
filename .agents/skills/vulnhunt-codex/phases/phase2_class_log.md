# LOG: Logic, cryptography, memory safety, resources

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

Inspect cryptography, key generation/storage, security-sensitive randomness, TLS verification, deserialization, dangerous merges/prototype pollution, and sensitive logging. Do not copy secrets into artifacts. Distinguish security uses from non-security hashing/randomness.

Trace checked and unchecked arithmetic into allocations, offsets, indices, loops, conversions and dispatch dimensions. Examine size/depth/count limits, request collections, decompression, regex complexity and attacker-controlled work. Lack of a cap alone does not demonstrate cross-boundary denial of service; show attainable resource amplification or a violated availability contract under the stated attacker model.

For Rust/Metal and other native code inspect unsafe preconditions, FFI pointer validity, alignment, initialization, ownership, lifetimes, aliasing, synchronization and buffer lengths. Trace external tensor shapes, dtypes, token IDs, model metadata and byte counts through host allocation and GPU dispatch. Check multiplication/addition overflow before bounds checks, narrowing integer casts, vector tail handling, threadgroup/grid dimensions, address spaces, strides, and whether kernels enforce index bounds. Host-side validation must cover every dispatch path and supported shape, including empty and malformed inputs. A Rust panic is not evidence of memory corruption; a reduced arithmetic model is not execution of the target kernel. Explicitly record unexecuted GPU behavior.

Check concurrency invariants for check-then-act, read/modify/write, asynchronous completion and cross-call TOCTOU. Assess cache/state isolation, key completeness/collisions, revocation, and model/context lifetime. For a single-model decision API inspect whole-decision serialization, consecutive-only cache reuse, context identity and failure/restart clearing where these are part of the contract. Separate integrity/reliability observations from demonstrated security consequences.

Check credential/policy permissions across branches, request-type discrimination, supplemental grants and count limits. Demonstrate the protected invariant and attacker outcome; do not dismiss a self-account exploit that bypasses an enforced scarcity or permission limit.
