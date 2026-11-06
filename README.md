# issue-solver · 0.1

轻量的代码修复与授权安全维护工作台。统一入口处理 issue、CI 失败、代码缺陷、
安全告警和有明确授权的服务器配置问题：**范围与路由 → 证据与复现 → 最小修复
→ 针对性验证 → 交付**。普通 bug 走调试路线；安全模块按具体问题启用。

入口是 [issue-solver/SKILL.md](skills/issue-solver/SKILL.md)。内置调试、性质检查、
常规 review、安全确认/误报、验收参考和报告模板；可复用已安装的专门技能。
不需要数据库、队列、常驻服务或网络安装。唯一 helper 只做本地复制和发现，
不执行 issue、扫描器或远端命令。

## 安装与发现

需要 Python 3.10+，没有第三方 Python 依赖。先在临时目录体验：

```bash
skill_root="$(mktemp -d)/skills"
python3 scripts/skills.py install --skills-dir "$skill_root"
python3 scripts/skills.py discover --skills-dir "$skill_root"
```

`install` 复制完整 `issue-solver/` 文件夹；目标已存在就拒绝，不覆盖用户修改。
升级时先检查旧目录，再选择新目录安装或自行备份迁移。复制遇到磁盘/权限错误
可能留下未完成的目标，命令会非零退出；检查该目标后再决定清理/重试。

正式使用时，**自行选择宿主支持的技能目录**。例如 Codex 的个人目录：

```bash
python3 scripts/skills.py install --skills-dir "$HOME/.agents/skills"
```

项目范围也可以选宿主支持的 `.agents/skills`。重新载入会话后查找 `issue-solver`
或显式请求 `$issue-solver`；若宿主不支持自动发现，直接让它读取安装后的
`issue-solver/SKILL.md`。临时复制/文件发现不等于宿主已经加载，0.1 验证不修改
本机个人技能目录。也可直接从这个仓库读取入口，无需复制。

发现可选模块时可重复提供目录，目录下应直接是各技能文件夹：

```bash
python3 scripts/skills.py discover \
  --skills-dir "$HOME/.agents/skills" --skills-dir "$HOME/.codex/skills"
```

JSON 中技能值是入口路径数组，缺少时为空；同名多版本保留全部候选，由调用者
核对来源与版本。扫描只看已知技能的直接子目录，不遍历整个硬盘。
Trivy 的 `found-on-path` 仅表示 PATH 上有可执行文件；`unavailable` 表示未找到。
发现命令退出 0 只表示观察完成，**不是扫描成功或没有漏洞**。

## 使用范围

| 输入示例 | 预期路径 |
| --- | --- |
| “修复空列表分页异常” | 复现 → 根因 → 最小修复 → 边界回归，不启动安全审计 |
| “这个 CI 步骤本地通过但 runner 失败” | 对齐命令、cwd、版本和依赖；分清代码/环境故障 |
| “检查这条 SQL 注入告警并修复确认的缺陷” | 追踪输入到 SQL；本地合成数据验证；修复后保留正常输入 |
| “扫描器把参数化查询报成注入” | 检查绑定与可达性；有证据则报告误报，不制造改动 |
| “Trivy 不存在，先完成能做的检查” | 标明扫描未执行；继续有证据的人工/本地检查 |
| “审查这份服务器配置” | 可先分析提供的脱敏文件；实际连接/扫描/变更须有具体目标和操作授权 |

授权接口、可选 Trivy 和 Lynis 边界见 [安全参考](skills/issue-solver/references/security.md)。
可直接复制 [任务范围示例](examples/scope.md)，分别用于本地修复和只读脱敏配置审查。
0.1 没有远端执行器，未扫描任何真实服务器。运行记录不要提交；目标项目使用
`.issue-solver/` 前要确认它已被忽略。报告可按 [模板](skills/issue-solver/assets/report.md) 精简填写。

## 验证与来源

```bash
python3 -m unittest discover -s tests -v
```

这验证离线安装、保留已有目录、多目录发现以及工具缺失/不执行工具的行为。
[五类 forward 演练](examples/acceptance/README.md) 验证消费者实际使用技能；
[验收记录](docs/validation.md) 区分已经运行的检查和未验证的宿主/真实扫描。

[来源表](skills/issue-solver/references/sources.md) 列出所选上游技能的真实路径、
不可变 commit 和许可；仅引用，不 vendor，不强制安装。原仓库未指定整体开源
许可，0.1 不把上游许可自动套用到本仓库原创内容。
