# 策元 · Ceyuan

**活动策划方案生成器 · Event Planning Skill**

> **灵感是你的，策元负责把它逼出来、打磨到扛得住攻击。** 不替你想创意，陪你过招。
> **Your inspiration, Ceyuan's job is to force it out and sharpen it until it survives attack.** It doesn't brainstorm for you — it spars with you.

<details open>
<summary><strong>🇨🇳 中文文档</strong></summary>

## 🚀 小白 30 秒上手

**就三步：装 → 说 → 答。**

**① 装**：把整个文件夹下载下来，放进你 AI 工具的 `skills` 目录（路径见下方「怎么用」）。

**② 说**：直接说人话就行——

- 「帮我策划一场新品发布会」
- 「公司年会想做得不一样」
- 「下个月有个招商会」

**③ 答**：它不会直接甩你一份方案，会反过来问你几个问题，照着答就行。**答不上就说「不知道」，它不会卡住。**

**它会问你什么（就这 3 类，别慌）：**

| 它问 | 为什么问 | 答不上怎么办 |
|---|---|---|
| 为什么要办这个活动？ | 动机决定方案——「募资」和「卖货」是两种完全不同的发布会 | 说「不清楚」，它按最可能的先走 |
| 钱谁出、预算大概多少？ | 决定做多大、做多重 | 说「没定」，它按轻量版先做 |
| 你手上有啥现成的？（私域、会员、上次活动数据） | 这些它搜不到，只有你知道 | 说「没有」，它标出来再想办法 |

**你会得到什么：**

- 一份能落地的方案（含预算表、时间线、物料清单，导出 .docx）
- 先出 3 个创意方向，你选一个，它帮你打磨到扛得住质疑

**你会面临什么（提前打预防针）：**

1. **它会反问你，不是一键出稿** —— 你可能觉得「怎么还问我」。这正是它和模板的区别：问清楚动机和预算，方案才不跑偏。你就当跟一个靠谱的策划在聊天。
2. **每一步会停下来等你点头** —— 它出一步，你看一眼说「行」或「改」，才往下走。所以不会出现「跑偏了才后悔」。
3. **需要你提供点内部信息** —— 谁付钱、上次活动数据这些它搜不到。答不上也没事，说「没有」，它标出来，不会死磕。

**一个真实对话，感受一下：**

```
你：帮我策划个公司年会
策元：先问一句——这次年会主要想达成什么？让员工开心、还是给领导看成果？
你：主要是让大家放松，顺便表彰优秀员工
策元：钱谁出？大概预算多少？
你：行政预算，5 万左右
策元：明白了，这是轻量活动。我先给你 3 个方向，不直接甩 50 页方案……
```

> 核心就一句：**它不是替你写方案，是陪你过招——你越说越清楚，它越做越准。**

---

## 目录

- [策元是什么](#zh-what)
- [为什么不一样](#zh-why)
- [五步流程](#zh-pipeline)
- [核心机制](#zh-mechanisms)
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
2. **发散是乘法，不是加法（交叉网络引擎）** — 创意 = 锚点 × 可变域。锁定活动锚点（发布会=悬念、快闪=稀缺），从热点 / 文化 / 情绪 / 跨界 / 感官 / 冲突六个可变域实时调取要素，用「嫁接 / 双域碰撞 / 三域撞击」撞出 N×M 个反直觉组合——而不是线性列 N 个方向。
3. **发散和收敛彻底分开（过早贴标签会压死创意）** — 发散时创意自由飞（只给「核心概念 + 为什么有意思」），维度、推导路径这些标签全部后置到收敛阶段。过早贴标签 = 给创意套枷锁，创意点会死。
4. **先出 3 个锐利的，不设数量死限（质量优先）** — 交叉出 10–20 个候选，挑最反直觉的 3–5 个。3 个扎得深的，胜过 10 个平庸的。
5. **活动是手段，不是目的（第一性原理）** — 同是「发布会」，动机是「募资」还是「卖货」，方案是两种物种。先用 5 Whys 挖出真实动机，再决定形式。动机错了，后面全错。
6. **攻击是修，不是杀（Red Team + Steelman）** — 15 个攻击角度逐条过，但每条攻击的默认落点是「怎么让它可行」（给修法、给预案、给降级版），不是判它死。最有创意的想法第一眼永远最不可落地，对抗是把它修成能落地，不是把它杀了。
7. **具体内容动态生成，不靠堆清单** — 行业、活动类型、执行环节都是「动态判断 + 搜索」现场生成的，硬编码清单只是快速通道，不是兜底。策元补的是「方法」，不是「知识」。

<a id="zh-pipeline"></a>
## 五步流程

每一步产出都必须过一轮对抗式审查，且必须等你确认才进入下一步。入口先按预算、受众、合规三个信号做**复杂度分级**——团建（L1）走精简流程，发布会（L2）走完整五步，峰会（L3）再加完整检索，不会给 30 分钟的团建套 300 万发布会的流程。

```
Step 1 · 拆解 ── 5 Whys 挖动机 + 七状态拆维度 + 问信息矿 + 钱流/合规 + 字段表
Step 2 · 重建 ── 第一性原理定目标 + 四层传导链判据（含主判据）
Step 3 · 发散 ── 交叉网络乘法引擎（锚点 × 6 可变域）→ 先自由发散 → 后收敛标注
Step 4 · 对抗 ── Steelman + 15 攻击角度 + 判词规则 → 找根本缺陷
Step 5 · 成型 ── 七节方案 + 闭环图 + 推导路径验证 + docx
```

- **拆解**：用 5 Whys 把「表面需求」和「真实动机」分开（钱 / 权 / 关系 / 怕）；按七状态拆「办成什么」；主动问用户手上的独家资源（私域流量、会员数、上次复盘数据）；**必问钱流**（谁付钱、收入怎么构成、盈亏粗算）和**合规边界**（报批/消防/许可，一阶约束提前问）；再把需求拆成字段表，标出哪些是「假硬约束」可挑战。
- **重建**：抛开「同类活动怎么做」，回到第一性原理定目标；判据按「四层传导链 × 四维测量」定，标出主判据落在哪层。
- **发散（先自由发散，后收敛标注）**：先跑**交叉网络**——锁定活动锚点，从热点 / 文化 / 情绪 / 跨界 / 感官 / 冲突六个可变域实时调取要素，用「嫁接 / 双域碰撞 / 三域撞击」撞出反直觉候选，挑最反直觉的 3–5 个；每个创意只给「一句核心概念 + 一句为什么有意思」；发散完再贴维度、推导路径标签，标签后置、不污染发散。
- **对抗**：Steelman 先行，15 个攻击角度逐条过（含「推导路径定位错了没」），**判词规则——攻击是修不是杀**（默认落点「怎么让它可行」，只有攻击 13 才能判「别办了」），收敛出「一戳就塌」的根本缺陷。
- **成型**：按七节骨架输出完整方案（Big Idea → 传导链判据 → 体验 → 传播 → 执行 → 风险 → 评估）+ 四层闭环图 + 推导路径验证，过 QA / 合规 / 算术三重自检，导出 docx。

<a id="zh-mechanisms"></a>
## 核心机制

策元的内核是「**一个乘法引擎 + 四块地基**」——引擎负责逼出创意（天花板），地基负责扛住攻击（地板）。

### 🚀 创意引擎 · 交叉网络（发散总引擎）

```
创意 = 锚点 × 可变域 → 反直觉组合
```

- **锚点域（1 个，不变）**：活动的核心元素——发布会=悬念、快闪=稀缺、答谢会=专属、招商会=信任、年会=归属。
- **可变域（6 个，动态生成，不硬编码）**：H 热点（及时性）/ C 文化（共鸣）/ E 情绪（底层）/ X 跨界（借机制）/ S 感官（五感）/ T 冲突（张力）。
- **交叉算子（3 种）**：① 嫁接（把外部要素焊到锚点上）② 双域碰撞（锚点 × 任一变域）③ 三域撞击（锚点 × 两个变域，撞出「只有这个组合才有」的创意）。
- **产出**：交叉出 10–20 个候选，挑最反直觉的 3–5 个，只给「一句核心概念 + 一句为什么有意思」，不做评判（评判交给 Step 4）。
- **热点借势铁律**：借势，不是蹭——提取热点背后的「情绪」当燃料，不贴热点标签（「塌房」→ 提取「对真诚的渴望」，而不是蹭明星名字）。

> 横纵分析（产素材）、心理机制推理卡（产情绪）、跨界移植（产机制）不是并列动作，而是交叉网络的**输入**——分别喂进 H/C 域、E 域、X 域。发散时先跑交叉网络，缺哪个域再回头调对应方法。

### 🧱 地基 · 四样完备性机制

**1. 横纵分析（贯穿全流程的元拆解方法）** — 纵向追「时间演变」、横向切「同期截面」，Step 1 拆需求、Step 2 拆目标、Step 3 拆创意、Step 5 拆环节都能挂载，按需不强制；拆解对象由活动类型决定，不是通用清单硬套。

**2. 四维推导轴（清单会漏，推导轴不会）** — `七状态目的 × 两层对象 × 五形态 × 时空`。七状态里「身份」（剪彩揭牌）和「生理能力」（体检培训）是常见清单漏掉的；公益/环保的参与者与受益者分离。任何活动都能落进这四维，推导不出来说明它不是「活动」或轴又漏了。

**3. 需求维度完整性（动机不够，维度才完整）** — 动机只答「为什么办」，还要拆「办成什么、为谁办、承担几个功能」。奥莱只盯「促销」一个显眼维度，把「整体演绎」挤掉了。**显眼维度 ≠ 唯一维度。**

**4. 指标传导模型（判据是链，不是并列 KPI）** — `投入层 → 中间指标层 → 结果指标层 → 长线资产层`，每层按「数量/质量/效率/成本」四维枚举。每份方案产出一张闭环图，活动后逐层回填「目标 vs 实际」，**断在哪层，下次就补哪层**。

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
├── creative-inputs.md        # 交叉网络（发散总引擎）+ 5 Whys + 横纵分析 + 心理推理卡 + 跨界移植
├── axes.md                   # 四维推导轴（七状态 × 两层对象 × 五形态 × 时空）
├── dimensions.md             # 需求维度完整性清单（三轴防角度缺失）
├── metrics-flow.md           # 指标传导模型 + 闭环图 + 回填规则
├── event-types.md            # 活动类型清单（10 大类 + 案例锚点）
├── industries.md             # 16 行业要点（调性/雷区/预算/合规/标准模块，示例快速通道 + 动态判断）
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

- **显式命令**：输入 `/ceyuan2` 或 `/策划`，或直接说「用策元」。
- **自然语言**：直接说活动需求，自动命中——「帮我策划一场新品发布会」「我们公司年会想做得不一样」「下个月有个招商会」。

> **验证装好了**：说一句「用策元帮我策划个 XX」，如果它开始反问你「真实动机是什么」「钱从哪来、谁付钱」，而不是直接丢模板，就说明装好了。

<a id="zh-keywords"></a>
## 关键词

方便检索（GitHub 搜索 / 搜索引擎 / Skill 市场）：

- 中文：活动策划、活动方案、发布会、年会、路演、招商会、营销活动、线下活动、AI Agent、Skill、提示词工程、第一性原理、对抗式审查、红队、营销策划、创意陪练、横纵分析、交叉网络、指标模型、跨界移植、开工仪式、危机公关

**推荐 GitHub Topics**（仓库主页 → 齿轮 → Topics 添加）：

`event-planning` `event-marketing` `marketing` `ai-agent` `ai-skill` `prompt-engineering` `claude-skill` `workbuddy` `red-team` `first-principles` `chinese` `marketing-campaign`

<a id="zh-license"></a>
## 许可

本项目采用 MIT 许可，可自由使用、修改、分发，用于商业或非商业用途。详见 `LICENSE` 文件。

</details>

<details>
<summary><strong>🇬🇧 English</strong></summary>

## 🚀 Quick start in 30 seconds

**Three steps: Install → Ask → Answer.**

**① Install**: download the whole folder and drop it into your agent's `skills` directory (paths below).

**② Ask**: just talk normally —

- "Help me plan a product launch"
- "Make our annual gala different"
- "Plan a dealer conference next month"

**③ Answer**: it won't dump a plan on you — it'll ask a few questions back. Just answer as best you can. **Don't know? Say "I don't know" — it won't get stuck.**

**What it'll ask (just these 3, don't panic):**

| It asks | Why | If you don't know |
|---|---|---|
| Why hold this event? | Motive decides the plan — "fundraising" vs. "selling" are two different launches | Say "unclear", it proceeds on the most likely one |
| Who pays? Roughly how much? | Decides scale and depth | Say "undecided", it does a lightweight version first |
| What do you already have? (private traffic, members, last-event data) | Things it can't search, only you know | Say "none", it flags it and works around it |

**What you'll get:**

- A landable plan (budget table, timeline, materials list, exported to .docx)
- 3 creative directions first — you pick one, it sharpens it until it survives scrutiny

**What to expect (heads-up):**

1. **It asks back, it's not one-click** — you might think "why is it asking me". That's the difference from templates: motive and budget clarified, the plan won't drift. Treat it like chatting with a solid planner.
2. **It pauses at each step for your nod** — it outputs a step, you glance and say "ok" or "change", then it moves on. So no "I regret it after it drifted".
3. **It needs a bit of inside info** — who pays, last-event data, things it can't search. Don't have it? Say "none", it flags it, won't nag.

**A real exchange, to feel it:**

```
You: Help me plan our company's annual gala
Ceyuan: First question — what's the main goal? Keep employees happy, or show results to the boss?
You: Mostly to relax everyone, and recognize top performers
Ceyuan: Who pays? Roughly what budget?
You: Admin budget, about 50k RMB
Ceyuan: Got it, that's a lightweight event. I'll start with 3 directions, not a 50-page plan...
```

> The one-liner: **it doesn't write the plan for you — it spars with you. The clearer you get, the sharper it gets.**

---

## Table of Contents

- [What is Ceyuan](#en-what)
- [Why it's different](#en-why)
- [The 5-step pipeline](#en-pipeline)
- [Core mechanisms](#en-mechanisms)
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
2. **Divergence is multiplication, not addition (the cross-network engine)** — idea = anchor × variable domains. Lock the event anchor (launch = suspense, pop-up = scarcity), pull elements in real time from six domains (hot topic / culture / emotion / cross-industry / senses / conflict), and collide them via "graft / dual-domain collision / triple-domain impact" into N×M counter-intuitive combos — not a linear list of N directions.
3. **Divergence and convergence are strictly separated (labeling too early kills ideas)** — during divergence, ideas fly free (only "core concept + why it's interesting"); dimension and derivation-path labels are all postponed to the convergence stage. Labeling too early = handcuffs on the idea.
4. **Start with 3 sharp ideas, no hard quota (quality first)** — cross out 10–20 candidates, keep the 3–5 most counter-intuitive. 3 deep ones beat 10 mediocre ones.
5. **An event is a means, not an end (first-principles)** — a "product launch" driven by fundraising vs. sales-channel stocking are two different species. Dig out the real motive with 5 Whys before choosing a format. Wrong motive → wrong everything.
6. **Attack to fix, not to kill (Red Team + Steelman)** — 15 attack angles run through, but each attack's default landing is "how to make it feasible" (a fix, a plan B, a downgrade), not a death sentence. The most creative idea is always the least landable at first glance — the review is there to *repair* it into something landable, not to kill it.
7. **Concrete content is generated dynamically, not stacked in lists** — industries, event types, and execution modules are generated on the fly by "dynamic judgment + search"; hard-coded lists are just fast lanes, never the fallback. Ceyuan adds *methods*, not *knowledge*.

<a id="en-pipeline"></a>
## The 5-step pipeline

Every step's output is adversarially reviewed and must be confirmed before moving on. At the entry, three signals (budget / audience / compliance) drive **complexity routing** — team-building (L1) uses a lean path, product launch (L2) the full pipeline, summit (L3) adds full research. A 30-minute team-building won't get a 3-million-yuan launch process.

```
Step 1 · Deconstruct ── 5 Whys + seven-state dimensions + info mine + money-flow/compliance + field table
Step 2 · Rebuild     ── first-principles goal + four-layer conduction criteria (1 primary)
Step 3 · Diverge     ── cross-network engine (anchor × 6 domains) → free divergence → convergence labeling
Step 4 · Adversarial ── Steelman + 15 attack angles + fix-not-kill rule → find the fatal flaw
Step 5 · Finalize    ── 7-section plan + closed-loop diagram + derivation-path check + docx
```

- **Deconstruct**: use 5 Whys to separate "surface request" from "real motive" (money / power / relationship / fear); unpack "achieve what" via the seven states; proactively ask for the user's exclusive resources (private traffic, membership count, last-event review data); **must-ask money-flow** (who pays, how revenue is composed, rough P&L) and **compliance boundary** (permits / fire capacity / licenses — a first-order constraint); then break the request into a field table and mark which "hard constraints" are actually soft.
- **Rebuild**: put aside "what peers do" and set the goal from first principles; define criteria on the "four-layer conduction chain × four-dimensional measurement", marking which layer the primary criterion sits on.
- **Diverge (free divergence first, then convergence labeling)**: run the **cross-network** first — lock the anchor, pull elements from six domains (hot topic / culture / emotion / cross-industry / senses / conflict), collide them via "graft / dual-domain collision / triple-domain impact" into counter-intuitive candidates, keep the 3–5 most counter-intuitive; each idea gets only "one core concept + why it's interesting"; only after diverging do you attach dimension and derivation-path labels.
- **Adversarial**: Steelman first, run 15 attack angles (including "is the derivation path wrong?"), apply the **fix-not-kill rule** (default landing is "how to make it feasible"; only attack #13 may judge "don't hold it"), and converge on the one fatal flaw.
- **Finalize**: output the full plan across 7 sections (Big Idea → conduction criteria → experience → communication → execution → risk → evaluation) + a four-layer closed-loop diagram + a derivation-path check, pass QA / compliance / arithmetic checks, and export to docx.

<a id="en-mechanisms"></a>
## Core mechanisms

Ceyuan's core is "**one multiplication engine + four foundations**" — the engine forces out creativity (the ceiling), the foundations survive attack (the floor).

### 🚀 Creative engine · Cross-network (the divergence master engine)

```
idea = anchor × variable domains → counter-intuitive combos
```

- **Anchor domain (1, fixed)**: the event's core element — launch = suspense, pop-up = scarcity, appreciation gala = exclusivity, dealer conference = trust, annual gala = belonging.
- **Variable domains (6, generated dynamically, not hard-coded)**: H hot-topic (timeliness) / C culture (resonance) / E emotion (underlying) / X cross-industry (borrowed mechanism) / S senses (five senses) / T conflict (tension).
- **Collision operators (3)**: ① graft (weld an external element onto the anchor) ② dual-domain collision (anchor × one domain) ③ triple-domain impact (anchor × two domains — a combo only this combination yields).
- **Output**: cross out 10–20 candidates, keep the 3–5 most counter-intuitive, each with only "one core concept + why it's interesting", no judgment (judgment is Step 4's job).
- **Hot-topic iron rule**: ride the trend, don't leech — extract the *emotion* behind a hot topic as fuel, don't stick the hot topic's label on it (a "scandal" → extract "the yearning for sincerity", not the celebrity's name).

> Diachronic/synchronic analysis (feeds material), psychology reasoning cards (feeds emotion), and cross-industry transplant (feeds mechanism) are not parallel actions — they are the cross-network's **inputs**, feeding the H/C, E, and X domains respectively. Run the cross-network first; only pull the corresponding method when a domain is empty.

### 🧱 Foundations · Four completeness mechanisms

**1. Diachronic/synchronic analysis (a meta-decomposition method across the whole flow)** — diachronic tracks time-evolution, synchronic cuts the cross-section; mountable at Step 1 (requirements), Step 2 (goals), Step 3 (ideas), Step 5 (execution), on demand. *What* to decompose is decided by the event type, not a generic checklist.

**2. Four-dimensional derivation axis (a list misses; an axis doesn't)** — `seven-state purpose × two-level object × five forms × space-time`. The seven states include "identity" (groundbreaking) and "physical capability" (health check-up) that common lists miss; charity/CSR separates participant from beneficiary. Any event lands in these four dimensions.

**3. Demand-dimension completeness (motive isn't enough)** — motive only answers "why hold it"; also unpack "achieve what, for whom, how many functions". An outlet mall fixated on "promotion" squeezed out "overall storytelling". **The visible dimension ≠ the only dimension.**

**4. Metric conduction model (criteria are a chain, not parallel KPIs)** — `input → intermediate → outcome → long-term asset`, each layer enumerated by "quantity/quality/efficiency/cost". Every plan produces a closed-loop diagram; back-fill "target vs actual" layer by layer after the event — **whichever layer broke, that's what you fix next time**.

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
├── creative-inputs.md        # cross-network (divergence engine) + 5 Whys + diachronic/synchronic + reasoning cards + cross-industry transplant
├── axes.md                   # four-dimensional derivation axis (7 states × 2 objects × 5 forms × space-time)
├── dimensions.md             # demand-dimension completeness checklist
├── metrics-flow.md           # metric conduction model + closed-loop diagram + back-fill rules
├── event-types.md            # event-type playbook (10 categories + case anchors)
├── industries.md             # 16 industry notes (tone/red flags/budget/compliance/standard modules — fast-lane examples + dynamic judgment)
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

- **Explicit command**: type `/ceyuan2` or just say "use Ceyuan".
- **Natural language**: just describe your need — "Help me plan a product launch", "Make our annual gala different", "Plan a dealer conference next month".

> **Verify it works**: say "use Ceyuan to plan an XX" — if it starts asking about your real motive and "who pays, where the money comes from" instead of dumping a template, it's installed correctly.

<a id="en-keywords"></a>
## Search keywords

For discoverability (GitHub search / search engines / skill marketplaces):

- English: event planning, event marketing, marketing campaign, event management, AI agent skill, AI skill, prompt engineering, first-principles, red team, steelman, brainstorming, Claude skill, WorkBuddy, creative sparring, cross-network, cross-industry, metrics model, KPI, event type

**Recommended GitHub topics** (Repo → gear → Topics):

`event-planning` `event-marketing` `marketing` `ai-agent` `ai-skill` `prompt-engineering` `claude-skill` `workbuddy` `red-team` `first-principles` `chinese` `marketing-campaign`

<a id="en-license"></a>
## License

This project is MIT licensed — free to use, modify, and distribute for commercial or non-commercial purposes. See the `LICENSE` file.

</details>
