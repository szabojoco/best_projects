import colorgram

rbg_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rbg_colors.append(new_color)

print(rbg_colors)
