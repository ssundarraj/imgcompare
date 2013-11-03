from PIL import Image, ImageChops, ImageStat
import math
import sys

def equal(im1, im2):
	return ImageChops.difference(im1, im2).getbbox() is None

def mydiff(img1, img2):
	h1=img1.histogram()
	h2=img2.histogram()
	rms=0
	for i in range(len(h1)):
		rms=rms+(h1[i]**2-h2[i]**2)/2
	rms=rms/len(h1)
	rms=math.sqrt(math.fabs(rms))
	return rms

def splitdiff(im1, im2, n):
	nbox=n
	width1=im1.size[0]/nbox
	height1=im1.size[1]/nbox
	width2=im2.size[0]/nbox
	height2=im2.size[1]/nbox
	p1=im1.load()
	p2=im2.load()
	il1=[0]*(nbox**2)#stores the sum of the RGB values for each box
	il2=[0]*(nbox**2)
	rms=0
	for x in range(nbox):
		for y in range(nbox):
			for i in range(width1):
				for j in range(height1):
					il1[nbox*x+y]=il1[nbox*x+y]+(sum(p1[width1*y+i, height1*x+j]))
			il1[nbox*x+y]=il1[nbox*x+y]/(height1*width1)
			for i in range(width2):
				for j in range(height2):
					il2[nbox*x+y]=il2[nbox*x+y]+(sum(p2[width2*y+i, height2*x+j]))
			il2[nbox*x+y]=il2[nbox*x+y]/(height2*width2)
	for i in range(min(len(il1), len(il2))):
		rms+=math.fabs(il1[i]**2-il2[i]**2)
	rms=math.sqrt(rms/min(len(il1), len(il2)))
	return rms

def brightness(im):
	stat=ImageStat.Stat(im)
	r,g,b=stat.mean
	brightness=math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
	return brightness

def brightnessdiff(im1, im2):
	bdiff=math.fabs(brightness(im1)-brightness(im2))
	return bdiff

def edgedetect():
	pass

if __name__=="__main__":
	img1=Image.open(sys.argv[1])
	img2=Image.open(sys.argv[2])
	if equal(img1, img2):
		print("Duplicate detected")
	else:
		print mydiff(img1, img2)
		print splitdiff(img1, img2, 20)
	print brightnessdiff(img1, img2)