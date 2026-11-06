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
