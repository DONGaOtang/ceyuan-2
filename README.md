# 策元 · Ceyuan

**活动策划方案生成器 · Event Planning Skill**

> 把一句模糊的需求，经过「拆解 → 重建 → 发散 → 对抗 → 成型」五步，产出可落地的活动方案。
> A vague request in, a deliverable event plan out — through a 5-step pipeline: Deconstruct → Rebuild → Diverge → Adversarial → Finalize.

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

策元是一个把「模糊需求」加工成「可落地活动方案」的 AI Skill。它覆盖的不只是发布会、年会、快闪、招商会这些消费端活动，还包括开工仪式、校招宣讲、危机公关、政企招商这些容易被忽略的非消费端活动。

它回答的不是「这个活动怎么做得热闹」，而是「这个活动**本质上要达成什么商业目的、覆盖几个维度、踩中什么心理、怎么衡量才算成功**」。

<a id="zh-why"></a>
## 为什么不一样

市面上的策划工具大多是两种：**模板填空**（给你一堆方案模板自己填）和**一问一答**（丢一个需求吐一份方案）。策元是第三种——一条**会思考的策划流水线**：

1. **活动是手段，不是目的（第一性原理）** — 同是「发布会」，动机是「募资给投资人看」还是「卖货给渠道」，方案是两种物种。策元先用 5 Whys 挖出真实动机，再决定形式。动机错了，后面全错。
2. **清单会漏，推导轴不会** — 用「七状态目的 × 两层对象 × 五形态 × 时空」四维轴，现场推导任意活动类型。冷门、新兴的活动，清单里没有，推导轴也能定位。
3. **动机不够，维度才完整** — 除了「为什么办」，还拆「办成什么、为谁办、承担几个功能」。奥莱只做促销、丢了整体演绎，就是这个坑。
4. **判据是传导链，不是并列 KPI** — 四层传导链（投入 → 中间指标 → 结果指标 → 长线资产）× 四维测量（数量/质量/效率/成本），外加一张闭环图。只列「到场率、GMV」是拍脑袋。
5. **心理机制是推理卡，不是名词表** — 每个机制带「理论出处 + 触发条件 + 失效边界」，选它不是挑顺眼的，是挑「触发条件成立」的。
6. **自己攻击自己（Red Team + Steelman）** — 每个创意先被「钢化」成最强版本，再用 15 个攻击角度打它（含「推导路径定位错了没」），逼出「一戳破整个结构就塌」的根本缺陷。

<a id="zh-pipeline"></a>
## 五步流程

每一步产出都必须过一轮对抗式审查，且必须等你确认才进入下一步。入口先按预算、受众、合规三个信号做**复杂度分级**——团建（L1）走精简流程，发布会（L2）走完整五步，峰会（L3）再加完整检索，不会给 30 分钟的团建套 300 万发布会的流程。

```
Step 1 · 拆解 ── 5 Whys 挖动机 + 七状态拆维度 + 问信息矿 + 字段表
Step 2 · 重建 ── 第一性原理定目标 + 四层传导链判据（含主判据）
Step 3 · 发散 ── 横纵双轴 + 心理推理卡 → 6-10 个创意（带推导路径）
Step 4 · 对抗 ── Steelman + 15 攻击角度 → 找根本缺陷
Step 5 · 成型 ── 七节方案 + 闭环图 + 推导路径验证 + docx
```

- **拆解**：用 5 Whys 把「表面需求」和「真实动机」分开（钱 / 权 / 关系 / 怕）；按七状态拆「办成什么」；主动问用户手上的独家资源（私域流量、会员数、上次复盘数据）；再把需求拆成字段表，标出哪些是「假硬约束」可挑战。
- **重建**：抛开「同类活动怎么做」，回到第一性原理定目标；判据按「四层传导链 × 四维测量」定，标出主判据落在哪层。
- **发散**：先做横纵双轴（纵向追时间、横向切截面）拿信息；用心理机制推理卡选支点，走「动机 → 情绪 → 行为」推理链；生成 6-10 个创意，每个标注推导路径 `[七状态] → [对象] → [形态] → [时空]`。
- **对抗**：Steelman 先行，15 个攻击角度逐条过（含「推导路径定位错了没」），收敛出「一戳就塌」的根本缺陷，每条高严重度缺陷给可执行修法。
- **成型**：按七节骨架输出完整方案（Big Idea → 传导链判据 → 体验 → 传播 → 执行 → 风险 → 评估）+ 四层闭环图 + 推导路径验证，过 QA / 合规 / 算术三重自检，导出 docx。

<a id="zh-mechanisms"></a>
## 三大核心机制

策元的内核，是三样别人没有的东西：

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
├── creative-inputs.md        # 5 Whys + 横纵双轴 + 心理机制推理卡 + 推理链
├── event-types.md            # 活动类型清单（10 大类 + 案例锚点）
├── industries.md             # 14 行业要点（调性/雷区/预算结构/合规红线）
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

> **验证装好了**：说一句「用策元帮我策划个 XX」，如果它开始反问你「真实动机是什么」「要覆盖哪几个维度」，而不是直接丢模板，就说明装好了。

策元会先追问你的**真实动机**、**要覆盖的维度**和**可挑战的约束**，而不是直接丢一份模板给你。

<a id="zh-keywords"></a>
## 关键词

方便检索（GitHub 搜索 / 搜索引擎 / Skill 市场）：

- 中文：活动策划、活动方案、发布会、年会、路演、招商会、营销活动、线下活动、AI Agent、Skill、提示词工程、第一性原理、对抗式审查、红队、营销策划、横纵分析、指标模型、活动类型、开工仪式、危机公关

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

Ceyuan is an AI Skill that turns a vague request into a **deliverable event plan**. It covers not only consumer-facing events — product launches, annual galas, pop-ups, dealer conferences — but also easily-overlooked non-consumer ones: groundbreaking ceremonies, campus recruiting talks, crisis PR, and government-business investment roadshows.

It answers not "how to make the event fun", but "**what business goal this event is really for, how many dimensions it covers, what psychology it triggers, and how success is measured**".

<a id="en-why"></a>
## Why it's different

Most planning tools are either **template-fillers** or **one-shot Q&A generators**. Ceyuan is the third kind — a **thinking pipeline**:

1. **An event is a means, not an end (first-principles)** — a "product launch" driven by fundraising vs. sales-channel stocking are two different species. Ceyuan digs out the real motive with 5 Whys before choosing a format. Wrong motive → wrong everything.
2. **A list misses things; a derivation axis doesn't** — a four-dimensional axis (seven-state purpose × two-level object × five forms × space-time) derives *any* event type on the spot. Cold or emerging event types absent from any list are still locatable.
3. **Motive isn't enough; dimensions complete it** — beyond "why hold it", it also unpacks "achieve what, for whom, and how many functions". An outlet mall doing only promotions and dropping overall storytelling is exactly this trap.
4. **Criteria are a conduction chain, not parallel KPIs** — a four-layer chain (input → intermediate → outcome → long-term asset) × four-dimensional measurement (quantity/quality/efficiency/cost), plus a closed-loop diagram. Listing only "attendance, GMV" is guessing.
5. **Psychology levers are reasoning cards, not a noun list** — each lever carries "theoretical origin + trigger condition + failure boundary"; you pick the one whose *trigger condition holds*, not the one that looks nice.
6. **It attacks its own ideas (Red Team + Steelman)** — every idea is steelmanned to its strongest form, then hit from 15 angles (including "is the derivation path mis-positioned?") to expose the one fatal flaw.

<a id="en-pipeline"></a>
## The 5-step pipeline

Every step's output is adversarially reviewed and must be confirmed before moving on. At the entry, three signals (budget / audience / compliance) drive **complexity routing** — team-building (L1) uses a lean path, product launch (L2) the full pipeline, summit (L3) adds full research. A 30-minute team-building won't get a 3-million-yuan launch process.

```
Step 1 · Deconstruct ── 5 Whys for motive + seven-state dimensions + info mine + field table
Step 2 · Rebuild     ── first-principles goal + four-layer conduction criteria (1 primary)
Step 3 · Diverge     ── diachronic/synchronic analysis + reasoning cards → 6-10 ideas (with derivation path)
Step 4 · Adversarial ── Steelman + 15 attack angles → find the fatal flaw
Step 5 · Finalize    ── 7-section plan + closed-loop diagram + derivation-path check + docx
```

- **Deconstruct**: use 5 Whys to separate "surface request" from "real motive" (money / power / relationship / fear); unpack "achieve what" via the seven states; proactively ask for the user's exclusive resources (private traffic, membership count, last-event review data); break the request into a field table and mark which "hard constraints" are actually soft.
- **Rebuild**: put aside "what peers do" and set the goal from first principles; define criteria on the "four-layer conduction chain × four-dimensional measurement", marking which layer the primary criterion sits on.
- **Diverge**: gather info on two axes (diachronic: time; synchronic: cross-section); pick psychology levers via reasoning cards, walk the "motive → emotion → behavior" chain; generate 6-10 ideas, each tagged with a derivation path `[seven-state] → [object] → [form] → [space-time]`.
- **Adversarial**: Steelman first, run 15 attack angles (including "is the derivation path wrong?"), converge on the one fatal flaw, and give an actionable fix for each high-severity defect.
- **Finalize**: output the full plan across 7 sections (Big Idea → conduction criteria → experience → communication → execution → risk → evaluation) + a four-layer closed-loop diagram + a derivation-path check, pass QA / compliance / arithmetic checks, and export to docx.

<a id="en-mechanisms"></a>
## Three core mechanisms

Ceyuan's core is three things others don't have:

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
├── creative-inputs.md        # 5 Whys + diachronic/synchronic analysis + psychology reasoning cards
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

> **Verify it works**: say "use Ceyuan to plan an XX" — if it starts asking about your real motive and which dimensions to cover instead of dumping a template, it's installed correctly.

Ceyuan will first ask about your **real motive**, **the dimensions to cover**, and **challengeable constraints** — not just dump a template on you.

<a id="en-keywords"></a>
## Search keywords

For discoverability (GitHub search / search engines / skill marketplaces):

- English: event planning, event marketing, marketing campaign, event management, AI agent skill, AI skill, prompt engineering, first-principles, red team, steelman, brainstorming, Claude skill, WorkBuddy, metrics model, KPI, event type

**Recommended GitHub topics** (Repo → gear → Topics):

`event-planning` `event-marketing` `marketing` `ai-agent` `ai-skill` `prompt-engineering` `claude-skill` `workbuddy` `red-team` `first-principles` `chinese` `marketing-campaign`

<a id="en-license"></a>
## License

This project is MIT licensed — free to use, modify, and distribute for commercial or non-commercial purposes. See the `LICENSE` file.

</details>
