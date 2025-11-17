# Found out how to xor two images using link below

#CopyPasteIt, 2019. XOR-ing and Summing Two Black and White Images. 
# Stack Overflow. [online] Available at: https://stackoverflow.com/questions/54398627/xor-ing-and-summing-two-black-and-white-images
#[Accessed 31 October 2025].

#import pillow library , downloaded. using pip install pillow on powershell
#PIL allows image manipulation
from PIL import Image, ImageChops

#cd "C:\Users\35389\Documents\Year 3\Y3_Secure communications\Assesment1\Beginner 10 - 50 pts\Lemur_XOR"
#open the two images - navigate to directory if necessary
image1 = Image.open("flag.png")
image2 = Image.open("lemur.png")

#find the pixel wise difference between the two images
#cannot use imagechops.logalxor in this instance because it only does black and white

# so i used the following 
#Pillow (PIL Fork). (2025). ImageChops (‘channel operations’) module. [online]
#Available at: https://pillow.readthedocs.io/en/stable/reference/ImageChops.html 
#[Accessed 31 Oct. 2025].
result = ImageChops.difference(image1,image2)

result.save("reult.png")




