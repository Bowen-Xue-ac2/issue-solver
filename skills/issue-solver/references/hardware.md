# Hardware inspection, diagnosis and repair guidance

Start with supplied reports. Identify OS/version, device/model, physical vs
virtual machine, storage interface/controller/USB bridge, symptom/timing,
recent changes and backup state. A guest or blocked bridge may expose no physical
health data. Keep device identifiers private; no arbitrary disk-wide collection.

## Separate the action levels

| Level | Work and boundary |
| --- | --- |
| Read-only inspection | Interpret existing SMART/NVMe, OS/driver, memory, thermal/power reports and vendor diagnostics. A live query needs a known target, supported tool/permissions and applicable authorization; even querying may wake a disk. Missing access is a gap, not permission to elevate. |
| Repair advice | Give an evidence-linked, least disruptive proposal with operator, risk, recovery and symptom-specific recheck. State that nothing has been applied. |
| Operator / additional authorization | Reboots, offline/extended self-tests, stress or destructive tests, filesystem repair, driver/OS changes, firmware, BIOS/security settings and physical work need an explicit plan and authorization. This skill does not perform them. |

For important unbacked data plus read errors, reduce unnecessary use and discuss
data preservation/recovery before further tests or writes. Backing up also reads
the disk; severe failure or irreplaceable data may need professional recovery
before repeated copying. Burning smell, swollen battery or electrical damage
calls for stopping use and qualified service, not stress testing or disassembly.

## Route by platform

| Platform | Evidence / later operator path |
| --- | --- |
| Windows | Supplied storage/driver and system error reports; supported vendor drive diagnostics; Windows Memory Diagnostic is a separate rebooting test, not a read-only query. |
| Linux | Supplied kernel I/O/hardware error reports and supported smartmontools output; NVMe-specific logs where available. Sensor/control paths depend on hardware and drivers. |
| macOS | Supplied system/panic reports and Apple Diagnostics results for the model; Apple Diagnostics does not cover external/third-party devices or macOS software conflicts. Do not prescribe Linux device paths or universal boot keys. |

See [sources](sources.md#protection-and-hardware-references) for optional pinned
tools and official platform paths. Tool presence, permission, controller support
and model compatibility are distinct prerequisites. There is no mandatory install.

## Weigh evidence and competing causes

| Area | Evidence to connect to the symptom |
| --- | --- |
| SATA/SAS storage | Overall status plus error/self-test logs, pending/uncorrectable or reallocation trends, interface errors and OS I/O events. Raw attributes/thresholds are vendor-specific; link/cable errors and media failure are different hypotheses. A USB bridge may hide data. |
| NVMe storage | Critical warnings, media/data-integrity errors, available spare, percentage used, temperature and error history, interpreted for that controller. Lifetime counters alone do not date the current fault; ATA attributes are not NVMe fields. |
| Memory | Actual memory-test/ECC evidence, crashes, reproducibility and software/driver alternatives. Memory pressure or an out-of-memory event does not establish faulty RAM; a clean or short test does not exclude intermittent failure. |
| Heat / power | Model-specific operating limits, sensor validity, workload, ambient conditions, throttling, power/charging events and symptom timing. A warm case, one temperature or a reset alone cannot distinguish cooling, battery/adapter, driver or board faults. |

`SMART PASSED` is a limited overall assessment, not a warranty of disk health.
The pinned `smartctl` manual describes an **ATA exit bitmask** (some bits also
apply to SCSI): bits 0–2 concern invocation, access or SMART-read problems;
3–5 concern health/threshold history; 6–7 concern error/self-test logs. A nonzero
status can carry multiple findings, including historical ones. Decode using the
actual version and protocol; do not transplant the ATA table to NVMe. An aborted
test is incomplete, not passed. Do not invent universal SMART or temperature limits.

## Propose a repair and prove its scope

Rank plausible causes with supporting and conflicting evidence. Choose the next
small observation that distinguishes them. Prefer reviewing an existing log or
operator-reported comparison before suggesting an intrusive diagnostic.

For a recent driver/peripheral change, a documented vendor-supported rollback or
one-at-a-time peripheral comparison may be a reversible operator proposal after
data protection and authorization. Physical cable reseating/replacement needs
safe power-off procedures and a qualified operator; never open a PSU or battery.
Media errors are not repaired by dismissing SMART warnings or automatically
running filesystem repair. Firmware and stress tests are not default next steps.

Specify recheck conditions **before** the proposed change: same symptom/normal
workload, observation interval appropriate to original recurrence, comparable
logs/counters and acceptable outcome. Track one change at a time when feasible;
if several changed together, keep causation uncertain. No recurrence for a short
window is only that observation, not verified repair. Persistent errors, unsafe
conditions or insufficient access lead to an explicit service/evidence handoff.
Record findings, hypotheses, advice and actual operator results separately in
the [report template](../assets/report.md).
