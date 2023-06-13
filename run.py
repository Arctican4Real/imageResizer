from PIL import Image
import glob

i = 1
total = len(glob.glob("./source/*.*"))
for file in glob.glob("./source/*.*"):
    try:
        img = Image.open(file)
    except :
        print("Unable to access")

    jpgV = img.convert("RGB")
    res = jpgV.resize((128,128))
    res.save(f"./output/emoji{i}.jpg")
    print(f"{i} / {total} converted")
    i += 1
