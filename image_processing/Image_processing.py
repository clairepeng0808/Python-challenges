from PIL import Image, ImageFilter, ImageEnhance


img = Image.open('./bagel/maltese_trio.jpg')
print(img.format, img.size, img.mode)
# print(dir(img))

filtered = img.filter(ImageFilter.BLUR)
filtered.save("./processed/blurred_maltese_trio.png", 'png')

bagel_grass = Image.open('./bagel/bagel_grass.jpg')
sharpened = bagel_grass.filter(ImageFilter.SHARPEN)
sharpened.save("./processed/sharpened_bagel_grass.png")

bagel_grass.thumbnail((300, 300))  # return NoneType
bagel_grass.save("./processed/thumbnail_bagel_grass_300x300.png")

bagel_taitung = Image.open('./bagel/bagel_taitung.jpg')
greyscaled = bagel_taitung.convert('L')
portrait_greyscaled = greyscaled.transpose(Image.ROTATE_270)
portrait_greyscaled.save("./processed/greyscaled_bagel_taitung.png")

bagel_home = Image.open('./bagel/bagel_home.jpg')
resized = bagel_home.resize((500, 500))
resized.save("./processed/resized_bagel_home_500x500.png")

bagel_parade = Image.open('./bagel/bagel_parade.jpg')
enh = ImageEnhance.Contrast(bagel_parade)
enh.enhance(1.3).save("./processed/enhanced_bagel_parade_30.png")
