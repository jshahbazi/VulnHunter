# NAV: Authentication and authorization

Modified and condensed for Codex from VulnHunter; see [provenance](../PROVENANCE.md).

For every body type inspect all accepting entry points, every sensitive field, role-specific filtering, and actual mapper/builder behavior. Format validation is not field authorization. Compare sibling endpoints for inconsistent filtering and catch-all forwarding. Track distinct field attacks separately when their impact or fix differs.

For every resource ID and scope selector verify the authenticated principal is authorized for that exact resource. Inspect all outbound credentials and identity channels. A service credential without usable bound end-user identity may create a confused deputy; forwarded identity alone does not prove ownership enforcement. Check all IDs separately, validated values replaced by defaults/wildcards, and sensitive response fields returned through mappers.

Enumerate all authentication branches, omitted-header/cookie paths, signature verification, algorithm/audience/expiry checks, session binding, caller allowlists, and authorization helper coverage. Compare sibling handlers and check whether declared middleware actually enforces its policy. Infrastructure authentication and path names do not imply per-resource authorization. Library APIs without authentication are not automatically network services: locate the trust boundary before alleging missing auth.

Inspect identity and security-signal spoofing, explicit outbound headers, trust of forwarded IPs, mass assignment, cache scope, credential/policy issuance, CSRF under actual credential/content-type/browser behavior, and auth decisions on attacker-selectable configuration. A token/library name is not evidence of cryptographic verification. Verify delegated authorization contracts and actual bound scope before treating delegation as defense.

When auth is universally absent, assess the documented supported caller/deployment model. Keep all candidate instances in the manifest even when presenting a shared root cause. Public health endpoints and authentication initiation do not require the same policy as private resource operations; their names alone establish neither safety nor vulnerability.
