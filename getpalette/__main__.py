#  MIT License
#
#  Copyright (c) 2019 Sabu Siyad
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import colorsys
import math
import os

import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from scipy import cluster

from getpalette import SHOW, IMAGE, COUNT


def get_color_palette(input_file, output_file, num_colors, display_color):
    img = plt.imread(input_file)
    red, green, blue = [], [], []
    for line in img:
        for pixel in line:
            r, g, b = pixel
            red.append(r)
            green.append(g)
            blue.append(b)

    df = pd.DataFrame({
        'red': red,
        'green': green,
        'blue': blue
    })

    df['standardized_red'] = cluster.vq.whiten(df['red'])
    df['standardized_green'] = cluster.vq.whiten(df['green'])
    df['standardized_blue'] = cluster.vq.whiten(df['blue'])

    color_palette, distortion = cluster.vq.kmeans(df[['standardized_red', 'standardized_green', 'standardized_blue']], num_colors)
    colors = []
    red_std, green_std, blue_std = df[['red', 'green', 'blue']].std()
    for color in color_palette:
        scaled_red, scaled_green, scaled_blue = color
        colors.append((
            math.ceil(scaled_red * red_std),
            math.ceil(scaled_green * green_std),
            math.ceil(scaled_blue * blue_std)
        ))

    colors.sort(key=lambda x: step(x[0], x[1], x[2], 8))

    img_org = Image.open(input_file)
    img_org_width, img_org_height = img_org.size

    palette_height = math.floor(img_org_height / 4)
    if img_org_height > img_org_width:
        palette_height = math.floor(img_org_height / 6)

    palette = Image.new('RGB', (img_org_width, palette_height), (255, 255, 255))
    block_width = math.floor(img_org_width / num_colors)

    # FIXME: need a smart way to resize fonts based on picture size
    font_size = 10
    proper_font_size = False
    sample_text = "#F8F8F7"
    font = ImageFont.truetype("Roboto-Medium.ttf", font_size)

    while not proper_font_size:
        if get_text_width(font, sample_text) > block_width and font_size > 1:
            font_size -= 1
            font = ImageFont.truetype("Roboto-Medium.ttf", font_size)
        elif get_text_width(font, sample_text) < block_width - 20:
            font_size += 1
            font = ImageFont.truetype("Roboto-Medium.ttf", font_size)
        else:
            proper_font_size = True

    for i in range(len(colors)):
        new_img = Image.new('RGB', (block_width, palette_height), colors[i])
        palette.paste(new_img, (block_width * i, 0))
        if display_color:
            draw = ImageDraw.Draw(palette)
            draw.text((block_width * i, palette_height - 20 - get_text_height(font, sample_text)), get_hex_color(colors[i]), (255, 255, 255), font=font)

    palette.save(output_file)
    return colors


def append_color_palette(original_image, color_palette, output_file, grid):
    img_org = Image.open(original_image)
    img_org_width, img_org_height = img_org.size
    palette_img = Image.open(color_palette)
    palette_width, palette_height = palette_img.size

    height_offset = math.ceil(img_org_height / 40)
    if img_org_height > img_org_width:
        height_offset = math.ceil(img_org_height / 60)

    width_offset = math.ceil(img_org_width / 60)
    # if img_org_height > img_org_width:
    #     width_offset = math.ceil(img_org_height / 30)

    total_width = img_org_width + (width_offset * 2)
    total_height = img_org_height + palette_height + height_offset

    combined_img = Image.new('RGB', (total_width, total_height), (255, 255, 255))

    for i in range(len(grid)):
        bg_block = Image.new('RGB', (math.ceil(total_width/len(grid)), total_height), grid[i])
        combined_img.paste(bg_block, ((math.ceil(total_width/len(grid))) * i, 0))

    combined_img.paste(img_org, (width_offset, height_offset))
    combined_img.paste(palette_img, (width_offset * 2, img_org_height + height_offset))

    combined_img.save(output_file)


def create_palette(filename, num_colors, display_color):
    file_extn = filename.split(".")[-1]
    if file_extn in ("png", "jpg", "jpeg"):
        output_palette = os.path.join(os.getcwd(), (filename.replace(f".{file_extn}", "") + "_palette." + file_extn))
        output_combined = os.path.join(os.getcwd(), (filename.replace(f".{file_extn}", "") + "_with_palette." + file_extn))
        grid = get_color_palette(filename, output_palette, num_colors, display_color)
        append_color_palette(filename, output_palette, output_combined, grid)
    else:
        print("Only JPG and PNG supported currently")
        exit()


def step(r, g, b, repetitions=1):
    lum = math.sqrt(0.241 * r + 0.691 * g + 0.068 * b)

    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h2 = int(h * repetitions)
    v2 = int(v * repetitions)

    if h2 % 2 == 1:
        v2 = repetitions - v2
        lum = repetitions - lum

    return (h2, lum, v2)


def get_hex_color(color):
    return '#%02x%02x%02x' % color


def get_text_width(font, text):
    width = 0
    for ch in text:
        width += font.getsize(ch)[0]
    return width


def get_text_height(font, text):
    height = []
    for ch in text:
        height.append(font.getsize(ch)[1])
    return max(height)


def main():
    try:
        create_palette(IMAGE, COUNT, SHOW)
        # test this
    except Exception as e:
        raise Exception


if __name__ == '__main__':
    main()
