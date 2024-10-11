from PIL import Image as image

abc = "abcdefghijklmnopqrstuvwxyz"

def getRGBValue(char: str):
    return abc.find(char)

def write(path: str, text: str, start=0):
    img = image.open(path)
    img.convert("RGB")
    pixArray = img.load()
    for i in range(len(text)-1):
        px = pixArray[i, 0]
        px[0] = getRGBValue(text[i])
        print(pixArray[i, 0][0])
    img.save("output.jpg")

write("image.jpg", "hallo", 0)


