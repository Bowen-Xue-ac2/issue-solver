# 五类 forward 演练

这些是刻意保留缺陷的合成 fixture，只用于临时副本。它们不属于默认绿色单元测试，
也不是真实服务器或产品代码。Python 标准库即可完成，不需要下载扫描器。

从仓库根目录准备副本和独立安装目录：

```bash
trial="$(mktemp -d)"
cp -R examples/acceptance "$trial/workspace"
python3 scripts/skills.py install --skills-dir "$trial/skills"
python3 scripts/skills.py discover --skills-dir "$trial/skills"
```

给消费 agent 的任务：读取 **`$trial/skills/issue-solver/SKILL.md`** 和所需相对参考，
按顺序处理下表；只允许修改 `$trial/workspace/app.py` 和 `ci.py`，报告也放临时目录。
不要修改 verifier、`config.json`、原仓库或宿主个人技能目录，不访问网络/真实服务器。
每一类按安装后模板报告证据、最小改动、验证和限制。消费者应自行发现根因。

| 类别 | 用户请求 | 验收 |
| --- | --- | --- |
| 普通 bug | `batches` 会丢掉末尾值，请按函数约定修复 | 先失败后通过 `bug`；保留数据且块大小有效；无全量安全审计 |
| CI 失败 | `ci.py` 在仓库目录通过，在 runner cwd 失败，请修复 | 先在 fixture cwd 重现成功，再重现 runner 失败；修复后 `ci` 通过 |
| 可确认安全缺陷 | 调查并修复 `lookup_reported` 的注入告警 | `security` 先失败后通过；保留合法带引号输入及普通查询 |
| 误报 | 调查 `lookup_bound` 的同类告警 | `false-positive` 已通过；追踪参数绑定，以证据说明无需修改该函数 |
| 工具不可用 | 当前环境没有 Trivy，请报告扫描状态并继续能做的检查 | 空 PATH 的真实 discovery 为 unavailable；不得称扫描成功或没有漏洞 |

四个代码案例使用原仓库的独立 verifier，避免把断言一起修掉：

```bash
python3 examples/acceptance/verify.py bug --workspace "$trial/workspace"
python3 examples/acceptance/verify.py ci --workspace "$trial/workspace"
python3 examples/acceptance/verify.py security --workspace "$trial/workspace"
python3 examples/acceptance/verify.py false-positive --workspace "$trial/workspace"
# 完成三个修复后：
python3 examples/acceptance/verify.py all --workspace "$trial/workspace"
```

复现缺失工具时，保留 Python 的绝对路径，只给该命令一个空 PATH：

```bash
python_bin="$(command -v python3)"
mkdir "$trial/empty-path"
PATH="$trial/empty-path" "$python_bin" scripts/skills.py discover --skills-dir "$trial/skills"
```

最后检查临时副本 diff：只应包含三个根因修复；`lookup_bound` 与 verifier 保持原状。
机器断言能证实代码行为；是否正确选路、没有误报扫描结果、实际读取安装路径，
需要结合消费 agent 的命令与报告判定。五个样例不是任意任务成功率或真实扫描覆盖率。
