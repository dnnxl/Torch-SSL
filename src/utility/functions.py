from imagecorruptions import corrupt

from imagecorruptions import get_corruption_names

for corruption in get_corruption_names():
    for severity in range(5):
        corrupted = corrupt(image, corruption_name=corruption, severity=severity+1)

