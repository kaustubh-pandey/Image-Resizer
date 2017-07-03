import PIL
from PIL import Image
print("Enter file name with extension(.png,.jpeg)")
file=input()
print("Enter the size (width x length pixels)format without any spaces")
a=input().split("x")
basewidth=int(a[0])
hsize=int(a[1])
img=Image.open(file)
img=img.resize((basewidth,hsize),(PIL.Image.ANTIALIAS))
img.save("resized_"+file)
