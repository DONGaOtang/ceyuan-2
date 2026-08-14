# 策元 · Ceyuan

**活动策划方案生成器 · Event Planning Skill**

> **灵感是你的，策元负责把它逼出来、打磨到扛得住攻击。** 不替你想创意，陪你过招。
> **Your inspiration, Ceyuan's job is to force it out and sharpen it until it survives attack.** It doesn't brainstorm for you — it spars with you.

<details open>
<summary><strong>🇨🇳 中文文档</strong></summary>

## 目录

- [策元是什么](#zh-what)
- [为什么不一样](#zh-why)
- [五步流程](#zh-pipeline)
- [三大核心机制](#zh-mechanisms)
- [五条铁律](#zh-rules)
- [文件结构](#zh-structure)
- [怎么用](#zh-usage)
- [关键词](#zh-keywords)
- [许可](#zh-license)

<a id="zh-what"></a>
## 策元是什么

策元是一个**「创意陪练」型 AI Skill**——不替你想创意，陪你过招，把一句模糊需求逼成可落地的活动方案。它覆盖的不只是发布会、年会、快闪、招商会这些消费端活动，还包括开工仪式、校招宣讲、危机公关、政企招商这些容易被忽略的非消费端活动。

它回答的不是「这个活动怎么做得热闹」，而是「这个活动**本质上要达成什么商业目的、覆盖几个维度、踩中什么心理、怎么衡量才算成功**」——然后用对抗式审查把你的创意打磨到扛得住攻击。

<a id="zh-why"></a>
## 为什么不一样

市面上的策划工具大多是两种：**模板填空**（给你一堆方案模板自己填）和**一问一答**（丢一个需求吐一份方案）。策元是第三种——一个**懂创意的陪练**：

1. **灵感是你的，策元负责逼出来（陪练，不是生成器）** — 不替你脑暴，陪你过招。每个想法都过一轮测试再出手，而不是丢给你一份「AI 觉得不错」的方案。
2. **发散和收敛彻底分开（过早贴标签会压死创意）** — 发散时创意自由飞（只给「核心概念 + 为什么有意思」），维度、推导路径这些标签全部后置到收敛阶段。过早贴标签 = 给创意套枷锁，创意点会死。
3. **先出 3 个锐利的，不设数量死限（质量优先）** — 3 个扎得深的，胜过 10 个平庸的。不满意再按量扩。
4. **强制跨界移植（用不相干的行业逼灵感）** — 殡仪业怎么做仪式感、游戏业怎么做留存、宗教怎么做峰终时刻。一个完全不相干的行业怎么解你的动机，往往就是破局的点。
5. **活动是手段，不是目的（第一性原理）** — 同是「发布会」，动机是「募资」还是「卖货」，方案是两种物种。先用 5 Whys 挖出真实动机，再决定形式。动机错了，后面全错。
6. **心理机制是推理卡，不是名词表** — 每个机制带「理论出处 + 触发条件 + 失效边界」，当发散燃料用，选的是「触发条件成立」的那个，不是顺眼的那个。
7. **攻击是修，不是杀（Red Team + Steelman）** — 15 个攻击角度逐条过，但每条攻击的默认落点是「怎么让它可行」（给修法、给预案、给降级版），不是判它死。最有创意的想法第一眼永远最不可落地，对抗是把它修成能落地，不是把它杀了。

<a id="zh-pipeline"></a>
## 五步流程

每一步产出都必须过一轮对抗式审查，且必须等你确认才进入下一步。入口先按预算、受众、合规三个信号做**复杂度分级**——团建（L1）走精简流程，发布会（L2）走完整五步，峰会（L3）再加完整检索，不会给 30 分钟的团建套 300 万发布会的流程。

```
Step 1 · 拆解 ── 5 Whys 挖动机 + 七状态拆维度 + 问信息矿 + 钱流/合规 + 字段表
Step 2 · 重建 ── 第一性原理定目标 + 四层传导链判据（含主判据）
Step 3 · 发散 ── 先自由发散（3 个锐利 + 跨界移植）→ 后收敛标注（维度/推导路径）
Step 4 · 对抗 ── Steelman + 15 攻击角度 + 判词规则 → 找根本缺陷
Step 5 · 成型 ── 七节方案 + 闭环图 + 推导路径验证 + docx
```

- **拆解**：用 5 Whys 把「表面需求」和「真实动机」分开（钱 / 权 / 关系 / 怕）；按七状态拆「办成什么」；主动问用户手上的独家资源（私域流量、会员数、上次复盘数据）；**必问钱流**（谁付钱、收入怎么构成、盈亏粗算）和**合规边界**（报批/消防/许可，一阶约束提前问，别拖到终审才发现报批不过）；再把需求拆成字段表，标出哪些是「假硬约束」可挑战。
- **重建**：抛开「同类活动怎么做」，回到第一性原理定目标；判据按「四层传导链 × 四维测量」定，标出主判据落在哪层。
- **发散（先自由发散，后收敛标注）**：横纵分析（纵向追时间、横向切截面，可挂载到任意拆解节点）拿信息；心理机制推理卡当发散燃料；**先出 3 个锐利的创意（质量优先、数量不设死）+ 强制跨界移植**；每个创意只给「一句核心概念 + 一句为什么有意思」；发散完再贴维度、推导路径标签，标签后置、不污染发散。
- **对抗**：Steelman 先行，15 个攻击角度逐条过（含「推导路径定位错了没」），**判词规则——攻击是修不是杀**（默认落点「怎么让它可行」，只有攻击 13 才能判「别办了」），收敛出「一戳就塌」的根本缺陷。
- **成型**：按七节骨架输出完整方案（Big Idea → 传导链判据 → 体验 → 传播 → 执行 → 风险 → 评估）+ 四层闭环图 + 推导路径验证，过 QA / 合规 / 算术三重自检，导出 docx。

<a id="zh-mechanisms"></a>
## 三大核心机制

创意是策元的**天花板**，下面是**地板**——三样别人没有的完备性机制，保证创意落地时扛得住追问：

### 1. 四维推导轴（清单会漏，推导轴不会）

```
活动类型 = 七状态目的 × 两层对象 × 五形态 × 时空
```

- **七状态目的**：认知 / 情感 / 行为 / 关系 / 资源 / **身份** / **生理能力**——后两个是常见清单漏掉的：剪彩揭牌是「确认身份资格」，体检培训是「改变身体能力」，都不属于前五类。
- **两层对象**：参与者（谁来现场）/ 受益者（谁最终获益）——公益/环保活动两者分离，必须分开写清。
- **五形态**：接受 / 参与 / 仪式 / 连接 / 共创。
- **时空**：线下 / 线上 / 混合 × 单次 / 周期。

任何活动都能落进这四维的某个组合；推导不出来，说明它不是「活动」，或者轴又漏了（漏了就在对应维度加一个枚举值）。**清单是快速通道，推导轴保证完备。**

### 2. 需求维度完整性（动机不够，维度才完整）

动机只回答了「为什么办」，还没拆「办成什么、为谁办、承担几个功能」：

- **目的维度**：这场活动要改变受众的哪个状态？
- **对象维度**：参与者是谁、受益者是谁，各方诉求有没有互相打架？
- **功能维度**：同时承担几个功能（商业转化 / 品牌演绎 / 内容传播 / 关系经营 / 体验创新 / 数据资产）。

奥莱的病：只盯「促销」一个最显眼、最好量化的维度，把「整体演绎」挤掉了。**显眼维度 ≠ 唯一维度。**

### 3. 指标传导模型（判据是链，不是并列 KPI）

```
投入层 → 中间指标层 → 结果指标层 → 长线资产层
```

每层按「数量 / 质量 / 效率 / 成本」四维枚举；主判据落在**结果指标层**，向上归因（由哪几个中间指标驱动）、向下归因（由哪项投入驱动）。每份方案产出一张**闭环图**，活动后逐层回填「目标 vs 实际」，**断在哪层，下次就补哪层**——这张断点就是喂回案例库的关键字段。

<a id="zh-rules"></a>
## 五条铁律

不可违反的底线：

1. **拆到底**：只信不可再拆的事实，行业惯例/预算/形式默认可挑战。
2. **先立后破**：审查前先 steelman 成最强版，禁止打稻草人。
3. **你不点头，不往下走**：每步产出后强制暂停，等确认。
4. **信息横纵双轴地拿**：纵向追时间，横向切截面，一手来源优先，信息不足就补搜，绝不编造。
5. **能力优先**：按能力检索本地 Skill 增强，检索不到就内置兜底，绝不断链。

<a id="zh-structure"></a>
## 文件结构

一个主文件 + 10 个引用文件，按需加载，读到哪段停哪段：

```
SKILL.md                     # 主流程：五步 + 五条铁律 + 复杂度分级 + 数据流图
references/
├── axes.md                   # 四维推导轴（七状态 × 两层对象 × 五形态 × 时空）
├── dimensions.md             # 需求维度完整性清单（三轴防角度缺失）
├── metrics-flow.md           # 指标传导模型 + 闭环图 + 回填规则
├── creative-inputs.md        # 5 Whys + 横纵分析（元方法）+ 心理机制推理卡 + 推理链 + 跨界移植
├── event-types.md            # 活动类型清单（10 大类 + 案例锚点）
├── industries.md             # 16 行业要点（调性/雷区/预算结构/合规红线/标准模块）
├── adversarial.md            # 对抗审查规则 + 15 攻击角度
├── proposal-schema.md        # 方案七节结构模板 + 闭环图 + 推导路径验证
├── search-paths.md           # 检索路径库（含非消费端垂直源）
└── skill-routing.md          # 能力检索增强表
```

<a id="zh-usage"></a>
## 怎么用

### 安装

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

### 启动

装好后，两种方式启动：

- **显式命令**：输入 `/ceyuan` 或 `/策划`，或直接说「用策元」。
- **自然语言**：直接说活动需求，自动命中——「帮我策划一场新品发布会」「我们公司年会想做得不一样」「下个月有个招商会」。

> **验证装好了**：说一句「用策元帮我策划个 XX」，如果它开始反问你「真实动机是什么」「钱从哪来、谁付钱」，而不是直接丢模板，就说明装好了。

策元会先追问你的**真实动机**、**钱流**和**可挑战的约束**，然后陪你过招，而不是直接丢一份模板给你。

<a id="zh-keywords"></a>
## 关键词

方便检索（GitHub 搜索 / 搜索引擎 / Skill 市场）：

- 中文：活动策划、活动方案、发布会、年会、路演、招商会、营销活动、线下活动、AI Agent、Skill、提示词工程、第一性原理、对抗式审查、红队、营销策划、创意陪练、横纵分析、指标模型、跨界移植、开工仪式、危机公关

**推荐 GitHub Topics**（仓库主页 → 齿轮 → Topics 添加）：

`event-planning` `event-marketing` `marketing` `ai-agent` `ai-skill` `prompt-engineering` `claude-skill` `workbuddy` `red-team` `first-principles` `chinese` `marketing-campaign`

<a id="zh-license"></a>
## 许可

本项目采用 MIT 许可，可自由使用、修改、分发，用于商业或非商业用途。详见 `LICENSE` 文件。

</details>

<details>
<summary><strong>🇬🇧 English</strong></summary>

## Table of Contents

- [What is Ceyuan](#en-what)
- [Why it's different](#en-why)
- [The 5-step pipeline](#en-pipeline)
- [Three core mechanisms](#en-mechanisms)
- [Five iron rules](#en-rules)
- [File structure](#en-structure)
- [How to use](#en-usage)
- [Search keywords](#en-keywords)
- [License](#en-license)

<a id="en-what"></a>
## What is Ceyuan

Ceyuan is a **creative-sparring AI Skill** — it doesn't brainstorm for you, it spars with you, forcing a vague request into a deliverable event plan. It covers not only consumer-facing events (product launches, annual galas, pop-ups, dealer conferences) but also easily-overlooked non-consumer ones: groundbreaking ceremonies, campus recruiting talks, crisis PR, and government-business investment roadshows.

It answers not "how to make the event fun", but "**what business goal this event is really for, how many dimensions it covers, what psychology it triggers, and how success is measured**" — then adversarially sharpens your idea until it survives attack.

<a id="en-why"></a>
## Why it's different

Most planning tools are either **template-fillers** or **one-shot Q&A generators**. Ceyuan is the third kind — a **sparring partner that gets creativity**:

1. **Your inspiration, Ceyuan's job to force it out (a sparring partner, not a generator)** — it doesn't brainstorm for you, it spars with you. Every idea gets tested before it ships, instead of dumping a "this AI thought it was cool" plan on you.
2. **Divergence and convergence are strictly separated (labeling too early kills ideas)** — during divergence, ideas fly free (only "core concept + why it's interesting"); dimension and derivation-path labels are all postponed to the convergence stage. Labeling too early = handcuffs on the idea.
3. **Start with 3 sharp ideas, no hard quota (quality first)** — 3 deep ones beat 10 mediocre ones. Expand only if unsatisfied.
4. **Forced cross-industry transplant (borrow inspiration from unrelated industries)** — how funeral homes do ritual, how games do retention, how religions do peak-end moments. How a totally unrelated industry solves your motive is often the breakthrough.
5. **An event is a means, not an end (first-principles)** — a "product launch" driven by fundraising vs. sales-channel stocking are two different species. Dig out the real motive with 5 Whys before choosing a format. Wrong motive → wrong everything.
6. **Psychology levers are reasoning cards, not a noun list** — each carries "theoretical origin + trigger condition + failure boundary", used as divergence fuel; you pick the one whose *trigger condition holds*, not the one that looks nice.
7. **Attack to fix, not to kill (Red Team + Steelman)** — 15 attack angles run through, but each attack's default landing is "how to make it feasible" (a fix, a plan B, a downgrade), not a death sentence. The most creative idea is always the least landable at first glance — the review is there to *repair* it into something landable, not to kill it.

<a id="en-pipeline"></a>
## The 5-step pipeline

Every step's output is adversarially reviewed and must be confirmed before moving on. At the entry, three signals (budget / audience / compliance) drive **complexity routing** — team-building (L1) uses a lean path, product launch (L2) the full pipeline, summit (L3) adds full research. A 30-minute team-building won't get a 3-million-yuan launch process.

```
Step 1 · Deconstruct ── 5 Whys + seven-state dimensions + info mine + money-flow/compliance + field table
Step 2 · Rebuild     ── first-principles goal + four-layer conduction criteria (1 primary)
Step 3 · Diverge     ── free divergence first (3 sharp ideas + cross-industry transplant) → convergence labeling after
Step 4 · Adversarial ── Steelman + 15 attack angles + fix-not-kill rule → find the fatal flaw
Step 5 · Finalize    ── 7-section plan + closed-loop diagram + derivation-path check + docx
```

- **Deconstruct**: use 5 Whys to separate "surface request" from "real motive" (money / power / relationship / fear); unpack "achieve what" via the seven states; proactively ask for the user's exclusive resources (private traffic, membership count, last-event review data); **must-ask money-flow** (who pays, how revenue is composed, rough P&L) and **compliance boundary** (permits / fire capacity / licenses — a first-order constraint, ask early, don't discover at final review that the permit won't pass); then break the request into a field table and mark which "hard constraints" are actually soft.
- **Rebuild**: put aside "what peers do" and set the goal from first principles; define criteria on the "four-layer conduction chain × four-dimensional measurement", marking which layer the primary criterion sits on.
- **Diverge (free divergence first, then convergence labeling)**: gather info on two axes (diachronic: time; synchronic: cross-section); use reasoning cards as divergence fuel; **start with 3 sharp ideas (quality first, no hard quota) + a forced cross-industry transplant**; each idea gets only "one core concept + why it's interesting"; only after diverging do you attach dimension and derivation-path labels — labeling comes later, never pollutes divergence.
- **Adversarial**: Steelman first, run 15 attack angles (including "is the derivation path wrong?"), apply the **fix-not-kill rule** (default landing is "how to make it feasible"; only attack #13 may judge "don't hold it"), and converge on the one fatal flaw.
- **Finalize**: output the full plan across 7 sections (Big Idea → conduction criteria → experience → communication → execution → risk → evaluation) + a four-layer closed-loop diagram + a derivation-path check, pass QA / compliance / arithmetic checks, and export to docx.

<a id="en-mechanisms"></a>
## Three core mechanisms

Creativity is Ceyuan's **ceiling**; below it is the **floor** — three completeness mechanisms no one else has, so your creative idea survives scrutiny when it lands:

### 1. Four-dimensional derivation axis (a list misses; an axis doesn't)

```
event type = seven-state purpose × two-level object × five forms × space-time
```

- **Seven-state purpose**: cognition / emotion / behavior / relationship / resource / **identity** / **physical capability** — the last two are what common lists miss: groundbreaking and plaque-unveiling are "confirming identity", health check-ups and training are "changing physical capability", neither fits the first five.
- **Two-level object**: participant (who shows up) / beneficiary (who ultimately benefits) — for charity/CSR events the two separate, and must be written out separately.
- **Five forms**: accept / participate / ritual / connect / co-create.
- **Space-time**: offline / online / hybrid × one-off / periodic.

Any event lands in some combination of these four dimensions; if it doesn't derive, either it isn't an "event", or the axis missed a value (add one — don't rebuild). **The list is a fast lane; the axis guarantees completeness.**

### 2. Demand-dimension completeness (motive isn't enough)

Motive only answers "why hold it" — it doesn't yet unpack "achieve what, for whom, how many functions":

- **Purpose dimension**: which state of the audience does this event change?
- **Object dimension**: who participates, who benefits, and do their demands conflict?
- **Function dimension**: how many functions it carries at once (commercial conversion / brand storytelling / content spread / relationship management / experience innovation / data asset).

The outlet-mall disease: fixating on "promotion" — the most visible, most measurable dimension — and squeezing out "overall storytelling". **The visible dimension ≠ the only dimension.**

### 3. Metric conduction model (criteria are a chain, not parallel KPIs)

```
input layer → intermediate layer → outcome layer → long-term asset layer
```

Each layer enumerates by "quantity / quality / efficiency / cost"; the primary criterion sits on the **outcome layer**, attributed upward (which intermediate metrics drive it) and downward (which input drives those). Every plan produces a **closed-loop diagram**; after the event, each layer is back-filled with "target vs actual" — **whichever layer broke, that's what you fix next time**. That break-point is the key field fed back into the case library.

<a id="en-rules"></a>
## Five iron rules

Non-negotiable:

1. **Deconstruct to the bottom** — trust only irreducible facts; convention, budget, format are challengeable by default.
2. **Steelman before you strike** — never attack a strawman.
3. **No confirmation, no next step** — force-stop after every step.
4. **Gather on two axes** — diachronic (time) + synchronic (cross-section), primary sources first, search more when short, never fabricate.
5. **Capability first** — scan local skills to enhance, fall back to built-in methods when none, never break.

<a id="en-structure"></a>
## File structure

One main file + 10 reference files, loaded on demand:

```
SKILL.md                     # main flow: 5 steps + 5 rules + complexity routing + data flow
references/
├── axes.md                   # four-dimensional derivation axis (7 states × 2 objects × 5 forms × space-time)
├── dimensions.md             # demand-dimension completeness checklist
├── metrics-flow.md           # metric conduction model + closed-loop diagram + back-fill rules
├── creative-inputs.md        # 5 Whys + diachronic/synchronic + psychology reasoning cards + reasoning chain + cross-industry transplant
├── event-types.md            # event-type playbook (10 categories + case anchors)
├── industries.md             # 14 industry notes (tone/red flags/budget/compliance)
├── adversarial.md            # adversarial review rules + 15 attack angles
├── proposal-schema.md        # 7-section proposal template + closed-loop diagram + derivation-path check
├── search-paths.md           # search-path library (incl. non-consumer vertical sources)
└── skill-routing.md          # capability enhancement table
```

<a id="en-usage"></a>
## How to use

### Install

**Option 1 · git clone**:

```bash
git clone https://github.com/DONGaOtang/ceyuan-skill.git
```

**Option 2 · Download ZIP**: repo page → Code → Download ZIP, then extract.

Then drop the whole folder into your agent's skills directory (you may keep the folder name `ceyuan-skill`):

| Agent | Install path |
|---|---|
| WorkBuddy | `~/.workbuddy/skills/ceyuan-skill/` |
| Claude Code | `~/.claude/skills/ceyuan-skill/` |
| Codex | `~/.codex/skills/ceyuan-skill/` |
| Generic Agents | `~/.agents/skills/ceyuan-skill/` |

> **Note**: keep `SKILL.md` at the root and the 10 files under `references/` untouched — don't rename or restructure them.

### Launch

Launch it either way:

- **Explicit command**: type `/ceyuan` or just say "use Ceyuan".
- **Natural language**: just describe your need — "Help me plan a product launch", "Make our annual gala different", "Plan a dealer conference next month".

> **Verify it works**: say "use Ceyuan to plan an XX" — if it starts asking about your real motive and "who pays, where the money comes from" instead of dumping a template, it's installed correctly.

Ceyuan will first ask about your **real motive**, **money-flow**, and **challengeable constraints** — then spar with you, not just dump a template on you.

<a id="en-keywords"></a>
## Search keywords

For discoverability (GitHub search / search engines / skill marketplaces):

- English: event planning, event marketing, marketing campaign, event management, AI agent skill, AI skill, prompt engineering, first-principles, red team, steelman, brainstorming, Claude skill, WorkBuddy, creative sparring, cross-industry, metrics model, KPI, event type

**Recommended GitHub topics** (Repo → gear → Topics):

`event-planning` `event-marketing` `marketing` `ai-agent` `ai-skill` `prompt-engineering` `claude-skill` `workbuddy` `red-team` `first-principles` `chinese` `marketing-campaign`

<a id="en-license"></a>
## License

This project is MIT licensed — free to use, modify, and distribute for commercial or non-commercial purposes. See the `LICENSE` file.

</details>
