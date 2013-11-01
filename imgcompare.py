import Image
import math
import sys
import ImageChops
import operator

def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))

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

def mydiff2(im1, im2):
	h = ImageChops.difference(im1, im2).histogram()
	rms=0
	for i in range(len(h)):
		rms=rms+h[i]**2
	rms=math.sqrt(rms/len(h))
	return rms

def mydiff3(im1, im2):
	h = ImageChops.difference(im1, im2).histogram()
	rms=0
	for i in range(len(h)):
		rms=rms+h[i]**2
	rms=math.sqrt(rms)/len(h)
	return rms

def splitdiff(im1, im2):
	nbox=20
	w1=im1.size[0]/nbox
	h1=im1.size[1]/nbox
	w2=im2.size[0]/nbox
	h2=im2.size[1]/nbox
	#for i in range():
	return nbox

if __name__=="__main__":
	img1=Image.open(sys.argv[1])
	img2=Image.open(sys.argv[2])
	if equal(img1, img2):
		print "Duplicate detected"
	else:
		print mydiff(img1, img2)
		print mydiff2(img1, img2)
		print mydiff3(img1, img2)
		print mydiff(img1, img2)+mydiff2(img1, img2)+mydiff3(img1, img2)
		print splitdiff(img1, img2);