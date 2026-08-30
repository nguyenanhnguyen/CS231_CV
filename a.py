#import lớp image
from PIL import Image

dir = "D:\z_DaiHoc\HK-V\CS231-CV\code\img"

img_path = dir + "\1.jpg"

print(img_path)

img01 = Image.open(img_path)