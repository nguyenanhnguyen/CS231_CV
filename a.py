from PIL import Image
from pathlib import Path

# Khai báo thư mục bằng raw string r"..."
img_dir = Path(r"D:\z_DaiHoc\HK-V\CS231-CV\code\img")

# Toán tử / tự động ghép đúng chuẩn đường dẫn
img_path = img_dir / "1.jpg"

print(img_path)

img01 = Image.open(img_path)
img01.show()