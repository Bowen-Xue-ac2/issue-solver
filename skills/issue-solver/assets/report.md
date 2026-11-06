# Issue result

- **Result:** fixed / confirmed / false positive / guidance only / needs evidence / blocked
- **Scope:** requested target, symptom, allowed actions; relevant exclusions
- **Evidence:** reproduction or source path; actual vs expected; root cause or
  reason the alert does not apply; confidence and unresolved assumptions
- **Change:** minimal repair and affected behavior, or no change with reason

| Verification | Actual result | Coverage / limit |
| --- | --- | --- |
| `command` (cwd, relevant revision/environment) | exit / observed behavior | what this establishes |

- **Remaining gaps:** missing tool/check/input and the next useful action; omit if none
- **Delivery:** local files/commit, branch or PR if actually created; remote status

For security findings add affected boundary and concrete impact. For a requested
server operation add the exact authorized target/action and recovery plan before
execution. Keep reports concise and redact sensitive inputs; do not paste raw logs.

For **virus protection**, add OS/provider, engine/definitions/report time,
execution and coverage (complete / partial / failed / not run / unknown),
detections and confidence, actual quarantine/remediation state, and the next
authorized recheck. Zero detections and current protection are separate claims.

For **hardware**, add OS/device/interface and backup state, observed health/error
evidence, competing causes and confidence. For every proposed repair, identify
the level (read-only inspection / advice / operator or additional authorization),
target/action, responsible operator, risk/recovery and symptom-specific recheck.
State what was actually performed and what remains advice; apply these proposal
fields to protection actions too. Omit irrelevant fields, not material unknowns.
