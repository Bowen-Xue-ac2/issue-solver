# issue-solver 0.1 scope

A portable skill workbench for a bounded issue, CI failure, code defect,
security alert, or an explicitly authorized server-configuration question.
The common path is scope/routing → evidence/reproduction → minimal repair →
targeted verification → delivery. A normal bug does not trigger a security audit.

The entrypoint selects debugging, ordinary review, or algorithm/boundary
properties as needed. Security work adds best-practice checks, attack-path
reasoning, false-positive checks, differential review, or a requested threat
model only when relevant. Prefer installed capabilities; optional references
have immutable source pins and verified licenses. No third-party skill text is
vendored and no network installation is required.

This release provides instructions, references, examples, a report template,
and a standard-library helper for explicit local installation and discovery.
It has no issue executor, scanner wrapper, database, queue, background service,
automatic remediation, or network configuration. Trivy is optional; Lynis,
remote servers, and offensive tests remain scoped authorization interfaces.
Runtime reports, source snapshots, and sensitive logs are not release content.

Acceptance: an isolated local consumer can install/discover the skill and use
it on an ordinary bug, CI failure, confirmed security flaw, false positive,
and unavailable optional tool. Tests must observe behavior, not merely find
words in Markdown. Publish on a separate branch; do not merge.

## Protection and hardware increment

Keep the 0.1 workbench, installer/discovery interface and existing references.
Add two peer routes in the same entrypoint: defensive **virus protect** and
**hardware inspection, diagnosis and repair guidance**. Each has one focused
reference, optional report fields and examples. No scanner wrapper, dependency,
background service or automatic remediation is added.

Protection covers platform/protection status, existing alert and scan reports,
coverage/freshness/failure distinctions, false-positive evidence, and guidance
for quarantine, restoration or removal. Hardware covers OS/device context,
disk SMART/NVMe evidence, memory, temperature/power symptoms, competing software
causes, least disruptive repair proposals and symptom-specific rechecks.
Windows, Linux and macOS are routed separately; vendor-specific evidence does
not become a universal threshold or command.

Default to supplied, redacted reports. Distinguish read-only inspection,
proposed repair and actions requiring an authorized operator. This increment
must not execute live scans, invasive tests, cleanup/repair, firmware writes,
stress tests, privilege elevation or security/network changes, or create
credentials. It must not claim host activation or real-device validation.

Before selecting optional references, verify provenance, license, maintenance,
dependencies and an immutable revision; record adoption/rejection reasons.
Acceptance uses four harmless offline report/symptom fixtures and one independent
consumer of a real temporary install, combined with incremental diff review.
Preserve the old acceptance history; verify new packaged references and reuse
unchanged CLI evidence. Continue the isolated checkout/extension branch and
leave the BowenX_WS repository and global Git configuration unchanged.

