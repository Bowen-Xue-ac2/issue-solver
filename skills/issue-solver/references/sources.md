# Optional sources

Verified 2026-11-06 against the immutable raw files and license texts linked below.
The version for each entry is its full Git commit, not an assumed release tag.
These are references to optional upstream capabilities, not installed dependencies
or copied skill text. Core guidance and tests work offline.

| Capability | Pinned source | License at that commit |
| --- | --- | --- |
| Debugging | [wshobson/agents: debugging-strategies](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/developer-essentials/skills/debugging-strategies/SKILL.md) | [MIT](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/LICENSE) |
| Ordinary review | [getsentry/skills: code-review](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/skills/code-review/SKILL.md) | [Apache-2.0](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/LICENSE) |
| Property testing | [trailofbits/skills: property-based-testing](https://github.com/trailofbits/skills/blob/470419e16f97e112d01fc32f4898aea1755015d9/plugins/property-based-testing/skills/property-based-testing/SKILL.md) | [CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/470419e16f97e112d01fc32f4898aea1755015d9/LICENSE) |
| Secure code | [openai/skills: security-best-practices](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices/SKILL.md) | [Apache-2.0, per skill](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices/LICENSE.txt) |
| Requested threat model | [openai/skills: security-threat-model](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/SKILL.md) | [Apache-2.0, per skill](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/LICENSE.txt) |

Prefer a suitable installed version. A discovered name is not a version/provenance
check: inspect its source and applicable instructions. For optional manual
acquisition, use the pinned commit and retain the upstream license/notices and any
required sibling references. No repository-wide upstream license is assumed from
a skill name. Recheck path, license, and behavior when updating a pin.

Attack-path analysis, false-positive checks, and differential review in 0.1 are
short local procedures in [security.md](security.md), not additional bundled
plugins. Trivy and Lynis are not dependencies; this release neither installs them
nor claims version-specific command compatibility.

## Protection and hardware references

Checked 2026-11-06 through the authenticated GitHub connector: repository metadata,
release, tag-resolved commit, and the pinned README/license/build/manual files
below. These are documentation pins, **not installed versions or dependencies**.
All four repositories were non-archived. The observed pushes indicate activity,
not support guarantees, vulnerability clearance or real-device compatibility.

| Official upstream / release | Immutable commit | Release date / observed last push (UTC) | Decision |
| --- | --- | --- | --- |
| [Cisco-Talos/clamav, clamav-1.5.4](https://github.com/Cisco-Talos/clamav/releases/tag/clamav-1.5.4) | `fa59fca15872bb8a914ba4c68188bcc8a502cbdf` | 2026-08-07 / 2026-10-22 | Adopt optional defensive scan/report semantics; no engine or database installation. |
| [smartmontools/smartmontools, RELEASE_7_5](https://github.com/smartmontools/smartmontools/releases/tag/RELEASE_7_5) | `f276b249fdc84019403491303479485030ac7c80` | 2025-05-12 / 2026-11-05 | Adopt supplied SMART report interpretation and scoped read-only query reference; no device execution. |
| [linux-nvme/nvme-cli, v3.2](https://github.com/linux-nvme/nvme-cli/releases/tag/v3.2) | `ce55132af26607e1904a0f449f94eeae028cfee5` | 2026-10-30 / 2026-11-06 | Do not integrate: platform/device-specific tooling, destructive commands and default discovery daemon exceed report interpretation needs. Keep a specialist reference only. |
| [memtest86plus/memtest86plus, v9.00](https://github.com/memtest86plus/memtest86plus/releases/tag/v9.00) | `d130a7bf66ffd093be4334ed96f5f5b538f6837a` | 2026-10-15 / 2026-11-04 | Do not integrate execution: boot/restart and extended testing require a separate operator plan. Keep an optional memory-test reference only. |

License and dependency decisions at these pins:

- **ClamAV:** [COPYING.txt](https://github.com/Cisco-Talos/clamav/blob/fa59fca15872bb8a914ba4c68188bcc8a502cbdf/COPYING.txt)
  is GPLv2; [README](https://github.com/Cisco-Talos/clamav/blob/fa59fca15872bb8a914ba4c68188bcc8a502cbdf/README.md)
  identifies components with other terms, including UnRAR restrictions. Do not
  label the entire tree with one license. [INSTALL](https://github.com/Cisco-Talos/clamav/blob/fa59fca15872bb8a914ba4c68188bcc8a502cbdf/INSTALL.md)
  requires CMake 3.17+, C/Rust toolchains and libraries such as OpenSSL, zlib,
  bzip2, libxml2, PCRE2 and json-c; FreshClam adds curl. Runtime scanning requires
  signature databases. The pinned [clamscan manual](https://github.com/Cisco-Talos/clamav/blob/fa59fca15872bb8a914ba4c68188bcc8a502cbdf/docs/man/clamscan.1.in)
  establishes exit semantics, not successful scanning here.
- **smartmontools:** [README](https://github.com/smartmontools/smartmontools/blob/f276b249fdc84019403491303479485030ac7c80/smartmontools/README)
  states GPL-2.0-or-later; [COPYING](https://github.com/smartmontools/smartmontools/blob/f276b249fdc84019403491303479485030ac7c80/smartmontools/COPYING)
  supplies the license. [INSTALL](https://github.com/smartmontools/smartmontools/blob/f276b249fdc84019403491303479485030ac7c80/smartmontools/INSTALL)
  uses C++/make and, for repository builds, autoconf 2.64+ and automake 1.10+.
  Actual access also depends on device/controller support and permissions.
  [smartctl manual](https://github.com/smartmontools/smartmontools/blob/f276b249fdc84019403491303479485030ac7c80/smartmontools/smartctl.8.in)
  documents the exit bitmask and limited overall-health assessment. This release
  uses the `smartmontools/` source prefix; later branch layouts may differ.
- **nvme-cli:** [meson.build](https://github.com/linux-nvme/nvme-cli/blob/ce55132af26607e1904a0f449f94eeae028cfee5/meson.build)
  declares CLI GPL-2.0-only and integrated libnvme LGPL-2.1-or-later; the top-level
  [LICENSE](https://github.com/linux-nvme/nvme-cli/blob/ce55132af26607e1904a0f449f94eeae028cfee5/LICENSE)
  does not describe every component. [BUILDING](https://github.com/linux-nvme/nvme-cli/blob/ce55132af26607e1904a0f449f94eeae028cfee5/Documentation/BUILDING.md)
  requires GCC/Clang, Meson 1.0+ and Ninja; json-c is optional but needed for JSON
  output. Version 3.x integrates libnvme in-tree; the Linux path requires Linux
  4.15+ sysfs interfaces. v3.2 also adds FreeBSD PCIe support; neither platform
  was tested here. It installs `nvme-discoverd` by default, another reason
  not to add this platform for a lightweight interpretation route.
- **Memtest86+:** [README](https://github.com/memtest86plus/memtest86plus/blob/d130a7bf66ffd093be4334ed96f5f5b538f6837a/README.md)
  and [LICENSE](https://github.com/memtest86plus/memtest86plus/blob/d130a7bf66ffd093be4334ed96f5f5b538f6837a/LICENSE)
  specify GPLv2. Builds use GNU GCC/cross-GCC, binutils and make; use requires an
  appropriate boot image, architecture and restart. v9.00 covers more than x86,
  including ARM64/LoongArch; this is not a claim of support for every device.
  Do not disable Secure Boot to make this optional reference usable.

No upstream code, binaries, definitions, skill text or license text is copied.
These decisions add no runtime/build dependencies to issue-solver. Updating a pin
requires rechecking its source, component licenses, dependencies and semantics.

Official dynamic documentation, read 2026-11-06 (not immutable pins):

- [Windows virus and threat protection](https://support.microsoft.com/en-us/windows/security/threat-malware-protection/virus-and-threat-protection-in-the-windows-security-app)
  and [Protection History](https://support.microsoft.com/en-us/windows/security/windows-security/protection-history-in-the-windows-security-app):
  provider status, detections/quarantine and remediation; offline scans reboot.
- [Apple malware protection](https://support.apple.com/en-lamr/guide/security/-sec469d47bd8/web):
  Gatekeeper, notarization and XProtect have distinct roles.
- [Apple Diagnostics](https://support.apple.com/en-gb/guide/mac-help/mh35727/mac):
  model-specific hardware assistance, excluding external/third-party hardware
  and macOS software conflicts.
- [Windows memory diagnostic guidance](https://support.microsoft.com/en-us/windows/experience/performance-optimization/how-to-fix-error-0xa-irql-not-less-or-equal):
  memory testing is a restart-based operator step; a crash code alone is not a RAM diagnosis.
- [ClamAV scanning](https://docs.clamav.net/manual/Usage/Scanning.html) and
  [signature management](https://docs.clamav.net/manual/Usage/SignatureManagement.html):
  on-demand scanning and database maintenance are distinct; automatic removal
  can destroy false-positive files.
