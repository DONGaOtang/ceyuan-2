# -*- coding: utf-8 -*-
"""小红书三篇文案配套图：排版大字报 + 信息图 + 截图卡片，代码精确生成（中文清晰，去AI味）"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = r"E:\我的AI项目聚集地\策划skill\小红书配图"
os.makedirs(OUT, exist_ok=True)

W, H = 1242, 1656  # 3:4 竖版
FB = r"C:\Windows\Fonts\msyhbd.ttc"   # 微软雅黑 Bold
FR = r"C:\Windows\Fonts\msyh.ttc"    # 微软雅黑 Regular

BLACK = (17, 17, 17)
DARK = (44, 54, 66)
GRAY = (120, 130, 140)
LGRAY = (242, 243, 245)
CARD = (237, 239, 242)
RED = (255, 36, 66)
REDBG = (253, 236, 239)
BLUE = (26, 82, 118)
BLUECARD = (235, 242, 248)
WHITE = (255, 255, 255)
BORDER = (222, 226, 231)

_F = {}
def ft(size, bold=True):
    k = (size, bold)
    if k not in _F:
        _F[k] = ImageFont.truetype(FB if bold else FR, size)
    return _F[k]

def cv(bg=WHITE):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)

def txt(d, cx, y, s, size, color, bold=True, anchor="ma"):
    d.text((cx, y), s, font=ft(size, bold), fill=color, anchor=anchor)

def segs(d, y, size, segments):
    f = ft(size, True)
    widths = [d.textlength(t, font=f) for t, _ in segments]
    x = (W - sum(widths)) / 2
    for (t, c), w in zip(segments, widths):
        d.text((x, y), t, font=f, fill=c, anchor="la")
        x += w

def rrect(d, box, r, fill=None, outline=None, w=2):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=w)

def wrap(d, s, size, maxw, bold=False):
    f = ft(size, bold)
    lines, cur = [], ""
    for ch in s:
        t = cur + ch
        if d.textlength(t, font=f) > maxw and cur:
            lines.append(cur); cur = ch
        else:
            cur = t
    if cur: lines.append(cur)
    return lines

def bar(d, y):
    d.rectangle((W/2 - 90, y, W/2 + 90, y + 10), fill=RED)

# ============ 篇1 ============
def p1_cover():
    img, d = cv()
    txt(d, W/2, 470, "怎么用AI", 54, GRAY)
    txt(d, W/2, 610, "越要创意，", 120, BLACK)
    segs(d, 780, 120, [("越", BLACK), ("别", RED), ("让AI写", BLACK)])
    bar(d, 1030)
    txt(d, W/2, 1090, "创意行业用 AI 的正确姿势", 42, GRAY, bold=False)
    img.save(f"{OUT}\\p1_1_封面.png")

def p1_slogan():
    img, d = cv(LGRAY)
    txt(d, W/2, 110, "AI 给的创意，十条全一个味", 54, BLACK)
    rrect(d, (70, 210, W-70, 1380), 30, fill=WHITE, outline=BORDER, w=2)
    # 提问行
    d.text((120, 260), "我：帮我写 10 条护肤品 slogan", font=ft(38, False), fill=GRAY, anchor="la")
    d.line((120, 340, W-120, 340), fill=BORDER, width=2)
    d.text((120, 375), "AI：", font=ft(40, True), fill=BLACK, anchor="la")
    slogans = ["焕活肌肤新生力", "给肌肤喝饱水", "莹润透亮一整天", "唤醒年轻光采",
               "深层滋养，由内而外", "一触即化，喝饱营养", "绽放光采，魅力如初",
               "锁住水润一整天", "唤醒肌肤，重获新生", "由内而外的水润呵护"]
    y = 470
    for i, s in enumerate(slogans, 1):
        d.ellipse((120, y, 168, y+48), fill=CARD)
        txt(d, 144, y, str(i), 34, GRAY, anchor="mm")
        d.text((190, y+2), s, font=ft(38, False), fill=DARK, anchor="lm")
        y += 88
    txt(d, W/2, 1465, "十条全一个味 —— 这就是 AI 的「平均」", 44, RED)
    img.save(f"{OUT}\\p1_2_对话slogan.png")

def p1_compare():
    img, d = cv()
    txt(d, W/2, 120, "被逼着想过之后，才有一条能用的", 50, BLACK)
    # 左卡（灰，平庸）
    rrect(d, (70, 280, 600, 1150), 28, fill=CARD, outline=BORDER, w=2)
    txt(d, 335, 330, "AI 给的", 48, GRAY)
    for i, ln in enumerate(wrap(d, "焕活肌肤新生力，由内而外绽放光采", 44, 420, bold=False)):
        txt(d, 335, 560 + i*70, ln, 44, GRAY, bold=False)
    txt(d, 335, 940, "似曾相识", 36, GRAY, bold=False)
    # 右卡（红，有力）
    rrect(d, (642, 280, W-70, 1150), 28, fill=REDBG, outline=(240, 180, 190), w=2)
    txt(d, 907, 330, "你想的", 48, RED)
    for i, ln in enumerate(wrap(d, "我把千元面霜停了，皮肤反而更好了", 46, 420, bold=True)):
        txt(d, 907, 560 + i*74, ln, 46, BLACK)
    txt(d, 907, 940, "反平均，能用", 36, RED, bold=False)
    txt(d, W/2, 1260, "同一个需求，两条命的创意", 42, DARK, bold=False)
    img.save(f"{OUT}\\p1_3_对比.png")

# ============ 篇2 ============
def p2_cover():
    img, d = cv()
    txt(d, W/2, 500, "活动策划", 54, GRAY)
    f1, f2 = ft(118, True), ft(210, True)
    s1, s2, s3 = "AI ", "5", " 步出活动方案"
    w1, w2, w3 = (d.textlength(s, font=f) for s, f in [(s1, f1), (s2, f2), (s3, f1)])
    x = (W - w1 - w2 - w3) / 2
    base = 860
    d.text((x, base), s1, font=f1, fill=BLACK, anchor="ls")
    d.text((x + w1, base), s2, font=f2, fill=RED, anchor="ls")
    d.text((x + w1 + w2, base), s3, font=f1, fill=BLACK, anchor="ls")
    bar(d, 1010)
    txt(d, W/2, 1065, "拆解 · 重建 · 发散 · 对抗 · 成型", 40, GRAY, bold=False)
    img.save(f"{OUT}\\p2_1_封面.png")

def p2_flow():
    img, d = cv()
    txt(d, W/2, 100, "策元五步，逼出能落地的方案", 52, BLACK)
    steps = [("1", "拆解", "先挖你到底图什么，再拆成一张表"),
             ("2", "重建", "要达成什么、谁来为什么来、成功怎么判"),
             ("3", "发散", "纵看品类历史，横看竞品口碑，生出 6-10 个方向"),
             ("4", "对抗", "先说到最强版，再攻击最强版，找致命漏洞"),
             ("5", "成型", "输出方案，过目标、合规、算术三重自检")]
    y, x0, x1 = 220, 110, W - 110
    for num, title, desc in steps:
        rrect(d, (x0, y, x1, y + 178), 24, fill=BLUECARD, outline=(200, 214, 224), w=2)
        d.ellipse((x0 + 36, y + 44, x0 + 136, y + 144), fill=BLUE)
        txt(d, x0 + 86, y + 94, num, 62, WHITE, anchor="mm")
        d.text((x0 + 170, y + 36), title, font=ft(58, True), fill=BLACK, anchor="la")
        for i, ln in enumerate(wrap(d, desc, 34, x1 - x0 - 210, bold=False)):
            d.text((x0 + 170, y + 112 + i * 42), ln, font=ft(34, False), fill=DARK, anchor="la")
        if num != "5":
            d.line((W/2, y + 178, W/2, y + 214), fill=RED, width=8)
            d.polygon([(W/2 - 16, y + 196), (W/2 + 16, y + 196), (W/2, y + 214)], fill=RED)
        y += 214
    img.save(f"{OUT}\\p2_2_五步流程.png")

def p2_cross():
    img, d = cv()
    txt(d, W/2, 120, "横纵分析：两条轴，交叉出判断", 52, BLACK)
    cx, cy = W/2, 880
    d.line((cx, 1320, cx, 470), fill=BLUE, width=10)  # 纵轴
    d.polygon([(cx - 18, 490), (cx + 18, 490), (cx, 458)], fill=BLUE)
    txt(d, cx, 350, "纵轴 · 时间", 48, BLUE)
    txt(d, cx, 410, "诞生 → 现在", 36, GRAY, bold=False)
    d.line((210, cy, 1080, cy), fill=RED, width=10)  # 横轴
    d.polygon([(1060, cy - 18), (1060, cy + 18), (1088, cy)], fill=RED)
    txt(d, 1000, cy - 90, "横轴 · 竞品", 48, RED, anchor="ra")
    d.ellipse((cx - 32, cy - 32, cx + 32, cy + 32), fill=RED)
    txt(d, cx, cy + 56, "洞察", 46, BLACK)
    for i, ln in enumerate(wrap(d, "纵向追时间，横向切竞品。两条轴一交叉，出别人说不出的判断。", 38, W - 220, bold=False)):
        txt(d, W/2, 1430 + i * 52, ln, 38, GRAY, bold=False)
    img.save(f"{OUT}\\p2_3_十字坐标.png")

def p2_pdf():
    img, d = cv()
    rrect(d, (180, 200, W-180, 1500), 12, fill=WHITE, outline=BORDER, w=3)
    txt(d, W/2, 470, "某新消费品牌", 92, BLUE)
    txt(d, W/2, 620, "横纵分析报告", 60, BLACK)
    txt(d, W/2, 740, "横纵分析法深度研究报告", 42, GRAY, bold=False)
    txt(d, W/2, 810, "研究时间：2026-08 ｜ 类型：品牌", 34, GRAY, bold=False)
    d.rectangle((W/2 - 200, 900, W/2 + 200, 908), fill=BLUE)
    txt(d, W/2, 1320, "—— 报告封面（示意）——", 36, GRAY, bold=False)
    img.save(f"{OUT}\\p2_4_PDF封面.png")

# ============ 篇3 ============
def p3_cover():
    img, d = cv()
    txt(d, W/2, 520, "AI协作", 54, GRAY)
    segs(d, 660, 116, [("我", BLACK), ("不写稿", RED), ("，", BLACK)])
    txt(d, W/2, 810, "我让AI陪我一起想", 98, BLACK)
    bar(d, 1010)
    txt(d, W/2, 1065, "人和 AI 的正确分工", 40, GRAY, bold=False)
    img.save(f"{OUT}\\p3_1_封面.png")

def pill(d, cx, cy, w, h, text, size, tc, fill):
    rrect(d, (cx - w/2, cy - h/2, cx + w/2, cy + h/2), h // 2, fill=fill)
    txt(d, cx, cy, text, size, tc, anchor="mm")

def p3_lane():
    img, d = cv()
    txt(d, W/2, 120, "人和 AI 的正确分工", 52, BLACK)
    # 上泳道：我
    rrect(d, (70, 250, W-70, 660), 28, fill=REDBG, outline=(240, 180, 190), w=2)
    pill(d, 175, 370, 130, 130, "我", 56, WHITE, RED)
    my = ["定方向", "拍板", "看它攻击对不对"]
    xs = [420, 630, 915]
    ws = [210, 180, 330]
    for s, x, w in zip(my, xs, ws):
        pill(d, x, 370, w, 110, s, 38, DARK, WHITE)
    txt(d, W/2, 530, "想清楚、做决策、把好关", 40, GRAY, bold=False)
    # 中间双向箭头
    d.line((W/2, 660, W/2, 740), fill=GRAY, width=8)
    d.polygon([(W/2-16, 740-18), (W/2+16, 740-18), (W/2, 740)], fill=GRAY)
    d.polygon([(W/2-16, 660+18), (W/2+16, 660+18), (W/2, 660)], fill=GRAY)
    # 下泳道：AI
    rrect(d, (70, 740, W-70, 1180), 28, fill=BLUECARD, outline=(200, 214, 224), w=2)
    pill(d, 175, 870, 150, 130, "AI", 56, WHITE, BLUE)
    ai = ["拆需求", "联网核实", "推导", "红队自己"]
    xs = [420, 625, 810, 1020]
    ws = [180, 200, 160, 200]
    for s, x, w in zip(ai, xs, ws):
        pill(d, x, 870, w, 110, s, 38, DARK, WHITE)
    txt(d, W/2, 1060, "干脏活累活：追问、搜集、挑刺", 40, GRAY, bold=False)
    txt(d, W/2, 1330, "AI 负责想，我负责拍板", 44, BLACK)
    img.save(f"{OUT}\\p3_2_泳道.png")

def p3_fight():
    img, d = cv(LGRAY)
    txt(d, W/2, 110, "它先给方案，再自己攻击自己", 52, BLACK)
    rrect(d, (70, 210, W-70, 1450), 30, fill=WHITE, outline=BORDER, w=2)
    # 方案卡（蓝）
    rrect(d, (120, 280, W-120, 620), 24, fill=BLUECARD, outline=(200, 214, 224), w=2)
    d.text((160, 320), "AI 给的方案", font=ft(40, True), fill=BLUE, anchor="la")
    for i, ln in enumerate(wrap(d, "办一场 200 人的线下发布会，预算 15 万，主打沉浸式体验。", 38, W-320, bold=False)):
        d.text((160, 400 + i*54), ln, font=ft(38, False), fill=DARK, anchor="la")
    # 箭头
    d.line((W/2, 620, W/2, 680), fill=RED, width=8)
    d.polygon([(W/2-16, 680-18), (W/2+16, 680-18), (W/2, 680)], fill=RED)
    # 推翻卡（红框圈出「根本缺陷」）
    rrect(d, (120, 680, W-120, 1160), 24, fill=REDBG, outline=RED, w=5)
    d.text((160, 720), "AI 自己推翻", font=ft(40, True), fill=RED, anchor="la")
    body = "但这个方案有个根本缺陷：200 人的场地报批加消防，最少要提前 45 天，你只剩 20 天——落地不了。"
    for i, ln in enumerate(wrap(d, body, 38, W-320, bold=False)):
        d.text((160, 800 + i*54), ln, font=ft(38, False), fill=DARK, anchor="la")
    txt(d, W/2, 1240, "红框里，就是它自己揪出来的「根本缺陷」", 40, RED)
    txt(d, W/2, 1490, "方案不是它给的，是它逼你想出来的", 44, BLACK)
    img.save(f"{OUT}\\p3_3_对话对抗.png")

for fn in [p1_cover, p1_slogan, p1_compare, p2_cover, p2_flow, p2_cross, p2_pdf,
           p3_cover, p3_lane, p3_fight]:
    fn()
    print("[OK]", fn.__name__)
print("ALL DONE ->", OUT)
