from PIL import Image, ImageDraw, ImageFont

IMG_DIR = r"E:\我的AI项目聚集地\策划skill\小红书配图"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
TARGET = (1242, 1656)


def load_font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def crop_resize(path):
    img = Image.open(path)
    w, h = img.size
    target_h = int(w / 0.75)
    img = img.crop((0, 0, w, min(target_h, h)))
    return img.resize(TARGET, Image.LANCZOS)


def ts(d, text, font):
    b = d.textbbox((0, 0), text, font=font)
    return b[2] - b[0], b[3] - b[1]


def center(d, y, text, size, color, bold=True):
    font = load_font(size, bold)
    for line in text.split("\n"):
        w, h = ts(d, line, font)
        x = (TARGET[0] - w) // 2
        for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
            d.text((x + dx, y + dy), line, font=font, fill=(30, 30, 30, 180))
        d.text((x, y), line, font=font, fill=color)
        y += h + int(size * 0.15)
    return y


def tag(d, t):
    font = load_font(36, False)
    w, h = ts(d, t, font)
    x = (TARGET[0] - w) // 2
    d.rounded_rectangle([x - 24, 48, x + w + 24, 48 + h + 20], radius=30, fill=(255, 255, 255, 200))
    d.text((x, 58), t, font=font, fill=(80, 80, 80))


R = "The_same_Chinese_woman_in_her__2026-08-13T"


def cover(src, dst, title, tagtext, size, color):
    img = crop_resize(f"{IMG_DIR}\\{src}")
    d = ImageDraw.Draw(img)
    tag(d, tagtext)
    center(d, 260, title, size, color)
    img.save(f"{IMG_DIR}\\{dst}")
    print("saved", dst)


def inner(src, dst):
    crop_resize(f"{IMG_DIR}\\{src}").save(f"{IMG_DIR}\\{dst}")
    print("saved", dst)


if __name__ == "__main__":
    cover(f"{R}04-50-04.png", "p1_1_封面.png", "越要创意\n越别让AI写", "怎么用AI", 136, (255, 255, 255))
    cover(f"{R}04-53-51.png", "p2_1_封面.png", "AI 5步出\n活动方案", "活动策划", 142, (255, 255, 255))
    cover(f"{R}04-56-43.png", "p3_1_封面.png", "我不写稿\n让AI陪我一起想", "AI协作", 124, (255, 255, 255))

    inner(f"{R}04-52-01.png", "p1_2_平庸之墙.png")
    inner(f"{R}04-53-09.png", "p1_3_对比.png")
    inner(f"{R}04-54-34.png", "p2_2_五步路径.png")
    inner(f"{R}04-55-17.png", "p2_3_十字路口.png")
    inner(f"{R}04-56-00.png", "p2_4_报告封面.png")
    inner(f"{R}04-57-28.png", "p3_2_双轨协作.png")
    inner(f"{R}04-58-12.png", "p3_3_镜像对抗.png")
    print("done")
