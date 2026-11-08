# 随时间变化的主页横幅

README 顶部直接显示 `asset_input` 中的一张原始 GIF。所有访客看到相同场景，
按纽约时间（`America/New_York`）切换，自动适应夏令时。

| 纽约时间 | 场景 | 图片 |
| --- | --- | --- |
| 06:00–11:59 | Goldsmiths 清晨 | `goldsmiths_morning.gif` |
| 12:00–16:59 | 纽约白天 | `new_york_daytime.gif` |
| 17:00–20:59 | Cambridge 黄昏 | `cambridge_sunset.gif` |
| 21:00–次日 05:59 | 洛杉矶深夜 | `los_angeles_midnight.gif` |

城市是四个时段对应的风景，切换统一看纽约时间。时段固定，不计算季节性日出日落。
图片原尺寸均为 1200 × 400，保留原有动画和比例。

## 打字问候

时间横幅下方使用 [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg)
显示三句话。横幅图片和问候语共用一次纽约时间判断，并更新同一个标记块，
因此不会分别按不同时间计算。

| 时段 | 第一句 |
| --- | --- |
| 清晨 | `Good morning, welcome!` |
| 白天 | `Good afternoon, welcome!` |
| 黄昏 | `Good evening, welcome!` |
| 深夜 | `Hello, night owl!` |

第二、三句保持原文：

> As a hacker, a professor, a musician, a kigu...
>
> Is there anything I can do to make you code better?

三句依次打出，前面的文字保留，全部显示后停留约四秒，再一起清空并循环。
电脑上是三行；手机上将第二、三句各分成两行，完整保留原文，防止字体过小。
浅色和深色模式使用不同文字颜色，SVG 背景透明。

README 引用公共服务生成的 SVG；服务不可用时可能显示图片的替代文字。
现有 GitHub Actions 只生成图片地址，不需要安装额外软件或请求公共服务。
动画会在浏览器内循环，问候时段随原有定时任务更新。

本次本地动画预览位于 `preview/typing-greeting/index.html`，其中四张 SVG 是公共服务
的实际响应，已缓存在同目录，方便离线查看。该预览固定为生成时的时段；
之后修改 README 或切换时段，不会自动重建这份预览缓存。

## 在 GitHub 上启用

1. 将 README、四张 GIF、`scripts`、`tests` 和 `.github/workflows/update-banner.yml`
   一并提交并推送到仓库默认分支。
2. 在仓库 **Actions** 中确认 Actions 已启用。工作流名称是 **Update profile banner**。
   第一次相关推送会触发更新，也可用 **Run workflow** 手动执行。
3. 工作流使用 GitHub 内置令牌及 `contents: write` 权限，无需配置个人令牌。
   如果仓库规则限制工作流写入或默认分支禁止直接提交，需要允许该工作流更新 README。

定时检查使用 `America/New_York` 时区，随纽约夏令时自动调整：

| 场景切换点（纽约时间） | 首次计划检查 | 后续计划补查 |
| --- | --- | --- |
| 06:00 清晨 | 06:03 | 06:13、06:23 |
| 12:00 白天 | 12:03 | 12:13、12:23 |
| 17:00 黄昏 | 17:03 | 17:13、17:23 |
| 21:00 深夜 | 21:03 | 21:13、21:23 |

此外，每小时第 37 分钟再检查一次，补偿切换时段的检查全部漏跑的情况。
普通日期每天计划运行 36 次（切换时段 12 次、每小时补查 24 次），
比原先每半小时检查的 48 次更少。夏令时切换日的每小时补查次数随当天小时数变化。
每次都按实际执行时刻选择场景和问候；只有场景变化才提交 README，通常每天四次。

GitHub 的任务调度可能延迟或丢失，因此“切换后三分钟”是计划触发时间，不保证实际开始时间。
增加切换时段的补查不能消除平台调度延迟。下次检查会根据实际运行时间
选择正确场景。已打开的主页需刷新才会看到新场景，页面或图片缓存也可能延迟显示。
任务失败时，最后一张成功更新的横幅继续显示。

GitHub 对公开仓库可能在 60 天无活动后停用定时任务；若任务停用，可在 Actions 中重新启用。

## 本地运行和预览

需要 Python 3.11 或更新版本及系统时区数据库，不需要安装 Python 包。
在仓库目录运行：

```sh
python3 scripts/update_banner.py
python3 -m unittest discover -s tests -v
```

按指定时刻预览会更新本地 README。以下时间均明确包含纽约夏令时偏移：

```sh
python3 scripts/update_banner.py --at '2026-07-15T08:00:00-04:00'
python3 scripts/update_banner.py --at '2026-07-15T14:00:00-04:00'
python3 scripts/update_banner.py --at '2026-07-15T18:00:00-04:00'
python3 scripts/update_banner.py --at '2026-07-15T23:00:00-04:00'
```

预览后，运行不带 `--at` 的命令恢复当前场景。也可用 `--readme /path/to/copy.md`
更新一份 README 副本。脚本只更新 `time-banner:start` 和 `time-banner:end` 两条注释之间
的内容；请保留这对标记。标记损坏、图片丢失或时间格式错误时，脚本会报错并停止写入。

修改时段时，在 `scripts/update_banner.py` 中调整区间，并同步更新测试和上方时间表。

## 参考

- [GitHub 定时任务的触发和限制](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [GitHub README 渲染和脚本过滤](https://github.com/github/markup#github-markup)
