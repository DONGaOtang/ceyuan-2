# 策元 · Ceyuan

**活动策划方案生成器 · Event Planning Skill**

> 把一句模糊的需求，经过「拆解 → 重建 → 发散 → 对抗 → 成型」五步，产出可落地的活动方案。
> Turn a vague request into a deliverable event plan through a 5-step pipeline: **Deconstruct → Rebuild → Diverge → Adversarial → Finalize**.

这不是一段普通提示词，而是一份**给 AI Agent 的 Skill（指令包）**。它内置了三套方法论——**第一性原理（First-principles）**、**横纵分析法（Diachronic/Synchronic Analysis）**、**对抗式审查（Red Team / Steelman）**——让 AI 不再套模板，而是像资深策划一样思考。

This is not a plain prompt — it is an **AI Agent Skill (instruction pack)**. It bakes in three methodologies: **first-principles thinking**, **diachronic/synchronic analysis**, and **red-team adversarial review (Steelman)** — so the AI thinks like a senior event planner, not a template filler.

---

## 目录 · Table of Contents

- [这是什么 · What is Ceyuan](#what-is-ceyuan)
- [为什么不一样 · Why Ceyuan is different](#why-ceyuan-is-different)
- [五步流程 · The 5-step pipeline](#the-5-step-pipeline)
- [五条铁律 · Five iron rules](#five-iron-rules)
- [文件结构 · File structure](#file-structure)
- [怎么用 · How to use](#how-to-use)
- [关键词 · Search keywords](#search-keywords)
- [许可 · License](#license)

---

## What is Ceyuan

**策元是什么** — 一个把「模糊需求」加工成「可落地活动方案」的 AI Skill，覆盖发布会、年会、路演、展览、品鉴会、私享会、团建、招商会、快闪、市集、直播带货、峰会论坛、颁奖典礼、音乐会、公益等几乎所有活动类型。

Ceyuan is an AI Skill that turns a vague request into a **deliverable event plan**, covering product launches, annual galas, roadshows, exhibitions, tastings, private salons, team-building, dealer conferences, pop-ups, markets, livestream sales, summits, awards ceremonies, concerts, charity events, and more.

它回答的不是「这个活动怎么做得热闹」，而是「这个活动**本质上要达成什么商业目的**，用哪种形式、踩中什么心理、怎么才算成功」。

It answers not "how to make the event fun", but "**what business goal this event is really for**, which format serves it, what psychology it triggers, and how success is measured".

---

## Why Ceyuan is different

**为什么它不一样** — 市面上的策划工具大多是两种：**模板填空**（给你一堆方案模板自己填）和**一问一答**（丢一个需求吐一份方案）。策元是第三种：

Most planning tools are either **template-fillers** or **one-shot Q&A generators**. Ceyuan is the third kind:

1. **活动是手段，不是目的（First-principles）** — 同是「发布会」，动机是「募资给投资人看」还是「卖货给渠道」，方案是两种物种。策元先用 5 Whys 把真实动机挖出来，再决定形式。动机错了，后面全错。

   **An event is a means, not an end.** A "product launch" driven by fundraising vs. sales-channel stocking are two different species. Ceyuan digs out the real motive with 5 Whys before choosing a format. Wrong motive → wrong everything.

2. **自己攻击自己（Red Team + Steelman）** — 每个创意先被「钢化」成最强版本，再用 15 个攻击角度（凭什么来、预算错配、维度冲突、推导路径、前提不成立……）打这个最强版，逼出那个「一戳破整个结构就塌」的根本缺陷。

   **It attacks its own ideas.** Every idea is first steelmanned to its strongest form, then attacked from 13 angles (why would anyone come, budget misallocation, false premise…) to expose the one fatal flaw that collapses the whole structure.

3. **人不点头，不往下走（Human-in-the-loop）** — 不做全自动黑箱。五步每一步结束都强制暂停，等你确认才进入下一步。宁可慢，不做错方向。

   **No auto-pilot.** Every step force-stops and waits for human confirmation. Slow is fine; wrong direction is not.

4. **轻量活动不套重流程（Complexity routing）** — 团建（L1）走精简流程，发布会（L2）走完整五步，峰会（L3）再加完整检索。不会给 30 分钟的团建套 300 万发布会的流程。

   **Complexity-aware routing.** Team-building (L1) uses a lean path, product launch (L2) the full pipeline, summit (L3) adds full research. A 30-minute team-building won't get a 3-million-yuan launch process.

5. **核心自包含 + 能力按需增强（Self-contained + enhancement）** — 策元的内置方法能独立跑通全流程；执行时还会按「能力关键词」检索你环境里已有的 Skill 做增强，检索不到就用内置兜底，绝不硬依赖。

   **Self-contained core + on-demand enhancement.** Ceyuan runs fully on its built-in methods; it also scans your environment for skills matching a "capability keyword" to enhance itself — and gracefully falls back when none exists. No hard dependency.

---

## The 5-step pipeline

**五步流程** — 每一步产出都必须过一轮对抗式审查，且必须等你确认才进入下一步。

Every step's output is adversarially reviewed, and must be confirmed before moving on.

```
Step 1 · 拆解 Deconstruct ── 5 Whys 挖真实动机 + 维度完整性枚举 + 字段拆成 Stone/Opinion
Step 2 · 重建 Rebuild    ── 第一性原理定目标 + 传导链判据（含 1 个主判据）
Step 3 · 发散 Diverge    ── 横纵双轴分析 + 心理机制推理链 → 6-10 个创意方向
Step 4 · 对抗 Adversarial ── Steelman + 15 攻击角度 → 找根本缺陷
Step 5 · 成型 Finalize   ── 七节方案 + 四层闭环图 + 三重自检 + docx 交付
```

- **拆解 Deconstruct**：用 5 Whys 把「表面需求」和「真实动机」分开（钱 / 权 / 关系 / 怕），再按三轴（目标 / 利益相关方 / 功能）做维度完整性枚举，最后把需求拆成字段表，标出哪些是「假硬约束」可挑战。

  Use 5 Whys to separate "surface request" from "real motive" (money / power / relationship / fear), enumerate dimensions across three axes (goal / stakeholder / function), then break the request into a field table and mark which "hard constraints" are actually soft.

- **重建 Rebuild**：抛开「同类活动怎么做」，回到第一性原理问三个问题——本质上达成什么？谁来、为什么来、记住什么？成功怎么判（四层传导链判据 + 1 个主判据）？

  Put aside "what peers do" and ask from first principles — what must it achieve? who comes, why, and what will they remember? how is success measured (4-layer transmission-chain criteria + 1 primary)?

- **发散 Diverge**：先做横纵双轴（纵向追时间：品类/品牌历史、翻车案例；横向切截面：同类活动、真实口碑），再从受众情绪底层用心理机制推理卡选机制（好奇缺口 / 社交货币 / 稀缺 / 损失厌恶 / 身份认同 / 从众 / 情绪峰值），走「动机→情绪→行为」推理链，生成 6-10 个创意方向，并做维度映射自检。

  Analyze on two axes first (diachronic: category/brand history, past failures; synchronic: peer events, real word-of-mouth), then pick psychology levers from reasoning cards (curiosity gap / social currency / scarcity / loss aversion / identity / conformity / peak emotion) via a motive→emotion→behavior chain, generate 6-10 creative directions, and run a dimension-coverage self-check.

- **对抗 Adversarial**：Steelman 先行（把创意说到最强版再攻击），15 个攻击角度逐条过，收敛出「一戳就塌」的根本缺陷，每条高严重度缺陷给可执行修法。

  Steelman first (strengthen the idea before attacking it), run through 13 attack angles, converge on the one fatal flaw, and give an actionable fix for every high-severity defect.

- **成型 Finalize**：按七节骨架输出完整方案（一句话 Big Idea → 目标与传导链判据 → 体验设计 → 传播设计 → 执行设计 → 风险预案 → 效果评估），产出一张四层闭环图，过 QA / 合规 / 算术三重自检，写回案例库形成长闭环，最后导出 docx 交付。

  Output the full plan across 7 sections (Big Idea → goals & transmission-chain criteria → experience → communication → execution → risk → evaluation), produce a 4-layer closed-loop diagram, pass QA / compliance / arithmetic checks, feed results back into the case library, and export a docx deliverable.

---

## Five iron rules

**五条铁律** — 不可违反的底线：

The five iron rules — non-negotiable:

1. **拆到底**：只信不可再拆的事实，行业惯例/预算/形式默认可挑战；拆到底 = 拆动机 + 拆维度。
   **Deconstruct to the bottom** — trust only irreducible facts; convention, budget, format are challengeable by default. Deconstruct = motive + dimensions.
2. **先立后破**：审查前先 steelman 成最强版，禁止打稻草人。
   **Steelman before you strike** — never attack a strawman.
3. **你不点头，不往下走**：每步产出后强制暂停，等确认。
   **No confirmation, no next step** — force-stop after every step.
4. **信息横纵双轴地拿**：纵向追时间，横向切截面，一手来源优先，信息不足就补搜，绝不编造。
   **Gather on two axes** — diachronic (time) + synchronic (cross-section), primary sources first, search more when short, never fabricate.
5. **能力优先**：按能力检索本地 Skill 增强，检索不到就内置兜底，绝不断链。
   **Capability first** — scan local skills to enhance, fall back to built-in methods when none, never break.

---

## File structure

**文件结构** — 一个主文件 + 10 个引用文件，按需加载，读到哪段停哪段：

One main file + 10 reference files, loaded on demand:

```
SKILL.md                     # 主流程：五步 + 五条铁律 + 复杂度分级 + 数据流图
references/
├── axes.md                  # 四维推导轴（七状态×两层对象×五形态×时空，完备覆盖）
├── creative-inputs.md       # 5 Whys 动机拆解 + 横纵双轴 + 心理机制推理卡 + 推理链
├── dimensions.md            # 需求维度完整性清单（七状态 + 利益相关方 + 功能）
├── metrics-flow.md          # 指标传导模型 + 四层×四维 + 闭环图 + 回填规则
├── event-types.md           # 活动类型清单 + 案例锚点（10 大类，快速通道）
├── industries.md            # 14 行业要点（调性/雷区/预算结构/合规红线）
├── adversarial.md           # 对抗审查规则 + 15 攻击角度
├── proposal-schema.md       # 方案最终七节结构模板 + 闭环图 + 推导路径 + docx
├── search-paths.md          # 检索路径库（去哪搜、怎么验证，含非消费端垂直源）
└── skill-routing.md         # 能力检索增强表
```

---

## How to use

**怎么用** — 两步装好，两种方式启动。

Two steps to install, two ways to launch.

### 安装 · Install

**方式一 · git clone**：

```bash
git clone https://github.com/DONGaOtang/ceyuan-skill.git
```

**方式二 · 下载 ZIP**：仓库主页 → Code → Download ZIP，解压即可。

然后把整个文件夹放进你 Agent 的 skills 目录，**文件夹名可保留 `ceyuan-skill`**：

| Agent | 安装路径 |
|---|---|
| WorkBuddy | `~/.workbuddy/skills/ceyuan-skill/` |
| Claude Code | `~/.claude/skills/ceyuan-skill/` |
| Codex | `~/.codex/skills/ceyuan-skill/` |
| 通用 Agents | `~/.agents/skills/ceyuan-skill/` |

> **注意**：`SKILL.md` 必须留在根目录，`references/` 子目录和里面 10 个文件原样保留，别改文件名、别改目录结构。
> **Note**: keep `SKILL.md` at the root and the 10 files under `references/` untouched.

### 启动 · Launch

装好后，两种方式启动：

- **显式命令**：输入 `/ceyuan` 或 `/策划`，或直接说「用策元」。
- **自然语言**：直接说活动需求，自动命中——「帮我策划一场新品发布会」「我们公司年会想做得不一样」「下个月有个招商会」。

Launch it either way:

- **Explicit command**: type `/ceyuan` or just say "use Ceyuan".
- **Natural language**: just describe your need — "Help me plan a product launch", "Make our annual gala different", "Plan a dealer conference next month".

> **验证装好了**：说一句「用策元帮我策划个 XX」，如果它开始反问你「真实动机是什么」「哪些约束能改」，而不是直接丢模板，就说明装好了。
> **Verify it works**: say "use Ceyuan to plan an XX" — if it starts asking about your real motive and challengeable constraints instead of dumping a template, it's installed correctly.

策元会先追问你的**真实动机**和**可挑战的约束**，而不是直接丢一份模板给你。

Ceyuan will first ask about your **real motive** and **challengeable constraints** — not just dump a template on you.

---

## Search keywords

**关键词** — 方便检索（GitHub 搜索 / 搜索引擎 / Skill 市场）：

For discoverability (GitHub search / search engines / skill marketplaces):

- 中文：活动策划、活动方案、发布会、年会、路演、招商会、营销活动、线下活动、AI Agent、Skill、提示词工程、第一性原理、对抗式审查、红队、营销策划
- English: event planning, event marketing, marketing campaign, event management, AI agent skill, AI skill, prompt engineering, first-principles, red team, steelman, brainstorming, Claude skill, WorkBuddy

**推荐 GitHub Topics**（仓库主页 → 齿轮 → Topics 添加）：

Recommended GitHub topics (Repo → gear → Topics):

`event-planning` `event-marketing` `marketing` `ai-agent` `ai-skill` `prompt-engineering` `claude-skill` `workbuddy` `red-team` `first-principles` `chinese` `marketing-campaign`

---

## License

**许可** — MIT License

本项目采用 MIT 许可，可自由使用、修改、分发，用于商业或非商业用途。详见 `LICENSE` 文件。

This project is MIT licensed — free to use, modify, and distribute for commercial or non-commercial purposes. See the `LICENSE` file.
