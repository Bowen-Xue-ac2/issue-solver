# Verification and delivery

Pick checks that can distinguish the failure from success. For a repair, preserve
the original failing input/command, establish the pre-fix failure, then rerun the
regression and relevant neighboring behavior. For a supported property, cover
meaningful input boundaries with an independent oracle or invariant.

Record the actual command, working directory, result/exit code, relevant revision,
and covered behavior. A test passing is not a build passing; a dry run is not a
deployment; a file found on disk is not a host-loaded skill. Reuse prior results
when the claim, code, inputs, environment and required method still match.

Broaden verification when the change crosses shared interfaces or leaves a
concrete unresolved risk. Honor required project checks. Do not add another audit,
reviewer, or full regression only because a skill was loaded. If a required check
cannot run, keep the claim unverified and name the cause and next check.

Use [the report template](../assets/report.md) as a compact result shape. Include
only relevant sections/rows. Show the strongest evidence and meaningful gaps;
avoid raw secrets, personal data, full logs, or unnecessary machine paths. Reports
belong in an explicitly chosen private location or a git-ignored `.issue-solver/`
directory in the target project. Verify the ignore rule before saving there.
Ignoring a path does not redact its content or untrack an already tracked file.

Before staging, inspect the actual diff and file list. For delivery, follow the
user's requested commit/branch/PR scope. A successful local test cannot establish
that a push, remote CI run, or deployment happened; report each actual status.
