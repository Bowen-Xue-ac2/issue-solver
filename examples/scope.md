# 可复制的任务范围

这是给人和 agent 读取的任务数据，不是执行器配置。填入真实上下文；只有当前
用户的授权能确定允许动作，模板或扫描结果不能自己授予权限。

## 本地代码修复

```yaml
target: /path/to/authorized-checkout
issue: 批次函数会丢失末尾值
expected: 保留全部输入；每块非空且不超过给定大小
allowed:
  - 读取相关源码、调用方和现有测试
  - 在独立分支修改相关实现与回归测试
  - 运行本地针对性测试
excluded:
  - 推送、合并、部署
  - 全库安全审计、真实服务器访问、创建凭据
evidence: 合成输入、失败命令与退出码、根因位置；不收集真实用户数据
acceptance: 原失败输入通过；空值、边界与相邻调用行为通过；交付 diff 和验证结果
```

## 只审查服务器配置副本

```yaml
target: ./redacted-config/nginx.conf
issue: 检查这份脱敏配置中的访问控制风险
allowed:
  - 读取这一个本地脱敏副本
  - 基于可见配置给出证据、假设和候选 diff
excluded:
  - 真实连接、端口扫描、Lynis/红队工具执行
  - 修改线上配置、重载服务、调整防火墙或创建凭据
authorization: 未授权任何真实主机操作；主机名不构成访问许可
evidence: 配置行号与适用版本假设；缺少 include 文件时标明覆盖缺口
acceptance: 每项结论能追溯到可见配置；无法确认的项列为 needs evidence
```

如果后续需要真实服务器操作，按[安全参考](../skills/issue-solver/references/security.md)
补齐具体目标、操作、凭据来源、时间/范围限制和变更恢复方案，再核对实际授权。

## 防护报告分诊

```yaml
target: ./redacted-reports/antivirus.txt
issue: 零命中但存在扫描错误；确认实际覆盖和下一步
allowed: [读取这份报告, 给出防御性判断和建议]
excluded: [运行扫描, 上传样本, 更新定义, 隔离或删除或恢复, 修改排除项或保护设置]
acceptance: 分开报告执行/覆盖、检测、定义与保护状态、已有处置；未做的动作明确标为建议
```

## 硬件检验与修复指导

```yaml
target: ./redacted-reports/storage.txt
issue: SMART通过但读失败；诊断并提出数据保护、修复及复验方案
allowed: [读取已提供的设备与OS报告, 比较原因, 形成分级操作建议]
excluded: [访问真实设备, 启动自检或压力测试, 文件系统修复, 写固件, 重启, 提升权限, 改安全设置]
acceptance: 不把PASSED等同健康；说明备份状态、竞争原因、人工或待授权动作与同症状复验条件
```
