# Focused security maintenance

Begin with the authorized code/path and specific alert or security question.
Record attacker-controlled input, entry point, relevant data/control flow,
guards, sensitive operation, and consequence. Confirm the supported deployment
assumptions; a package match alone does not establish reachable impact.

Use one disposition per finding:

| Disposition | Required basis |
| --- | --- |
| Confirmed | A reachable path plus source evidence and a safe reproduction or equivalent decisive evidence |
| False positive | A traced guard, binding, unreachable path, or incorrect assumption that defeats the reported path; show why |
| Needs evidence | An unresolved reachability/configuration assumption or blocked reproduction; name the missing fact |

For a SQL alert, compare parameter binding with string interpolation. Exercise a
local, synthetic database with an injection string and legitimate quoted input.
Do not treat escaping by appearance as proof of safety. If the existing binding
keeps the input literal, report the scoped false positive without changing code.

Repair the responsible boundary and test both the abuse case and legitimate
behavior. A differential review compares the vulnerable/fixed paths and callers;
look for bypasses of the same root cause, not unrelated findings. For unfamiliar
frameworks, prefer their maintained security guidance. The optional OpenAI
`security-best-practices` skill at the pinned revision covers Python,
JavaScript/TypeScript and Go; do not imply coverage for other stacks.

## Threat model / attack path

When a boundary is ambiguous, sketch only what resolves it: asset → actor/input
→ trust boundary → sensitive operation → existing control → remaining question.
A full threat model is separate requested work. Respect an optional module's
own trigger; do not invoke it simply because a normal fix touches authentication.

## Optional Trivy

0.1 does not run or download Trivy. Discovery only observes a binary on PATH;
it does not establish a runnable version, cached database, successful scan, or
security result. For an explicitly requested local dependency/configuration scan,
check the installed version/help, authorized path, scanner selection, and database
availability before forming the command. A database update may access the network;
keep it within the current authority. Distinguish unavailable tool, scan failure,
findings, and successful scan with its actual coverage. Never translate a nonzero
exit or empty output into “no vulnerabilities.”

## Server / Lynis / offensive-tool interface

No such tool is executed by the helper. Before any actual server connection,
scan, or mutation, establish from current authorization: exact target(s), owner,
permitted operations, credential source, time/scope limits, and recovery plan for
changes. Existing specific authorization is reusable; a broad maintenance request
or this template is not an allowlist. If these facts are missing, work from supplied
redacted configuration and prepare a reviewable command/change plan. Do not access
other hosts, create credentials, weaken network controls, or run exploits merely
because a capability is installed. Live scanning needs explicit authorization for
that target and action. Host permissions still apply.
