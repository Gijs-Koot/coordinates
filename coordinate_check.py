from PIL import Image, ImageDraw

img = Image.new(size=(10, 20), mode="RGB", color="blue")

img.save("blue.png")

draw = ImageDraw.Draw(img)

# draw red cross

draw.point((1, 9), fill="purple")

img.save("img.png")
