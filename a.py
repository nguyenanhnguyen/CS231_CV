from pathlib import Path
from PIL import Image

img_path = Path(r"D:\z_DaiHoc\HK-V\CS231-CV\code\img\1.jpg")

if not img_path.exists():
    print("Không tìm thấy ảnh:", img_path)
else:
    with Image.open(img_path) as image:
        print("Tên file:", img_path.name)
        print("Đường dẫn:", img_path)
        print("Định dạng:", image.format)
        print("Kích thước:", image.size)
        print("Chiều rộng:", image.width)
        print("Chiều cao:", image.height)
        print("Chế độ màu:", image.mode)
        print("Số kênh màu:", len(image.getbands()))
        print("Tên các kênh:", image.getbands())