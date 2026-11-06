# Issue result

- **Result:** fixed / confirmed / false positive / needs evidence / blocked
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
