# INJ: Injection

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

Trace inputs into SQL/query languages (LDAP, XPath, GraphQL, service filters), shell/process execution, code/template evaluation, XML parsers, file/network filesystem paths, uploads, URLs and headers, HTML/markup/email rendering, redirects and navigation. Adapt APIs to the actual stack. Raw argument execution and shell interpretation have different semantics; prepared statements and context-matched binding require inspecting the actual call.

Verify traversal, canonicalization, symlink and base-directory enforcement against the supported threat model. A caller intentionally selecting its own local file is not automatically arbitrary file access across a protected boundary. Check archive extraction names, total expansion and recursion. For URLs, distinguish scheme/authority control, path/query injection, and credentials forwarded to a changed destination. A hardcoded hostname alone does not prevent reaching unauthorized paths or injecting query parameters.

Inspect exact sanitizer behavior on characters meaningful to the sink. HTML escaping is insufficient for SQL, shell, URLs, and LDAP. URL transport encoding is insufficient for the query language parsed after decoding. In static mode read implementations; record proposed tests without executing. Missing dependency source leaves validation unresolved. Do not treat any unsanitized cross-service value as automatically exploitable: identify the downstream parser and protected outcome or retain STATIC-POTENTIAL.

Trace attacker-controlled outbound responses onward into rendering, navigation, deserialization, or file sinks. For navigation distinguish open redirect from executable schemes only when actual browser/sink semantics support that impact; missing an allowlist alone does not prove script execution. Compare prefix checks, protocol-relative URLs, decoding and multiple transformations. Flag outbound identity/security headers for NAV analysis.
