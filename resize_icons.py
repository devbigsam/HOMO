from PIL import Image
import os

img_dir = 'HOMO/html/assets/img/'

for i in range(1,5):
    img_path = os.path.join(img_dir, f'icon-coin-{i}.png')
    img = Image.open(img_path)
    img_resized = img.resize((26,26))
    img_resized.save(img_path)
