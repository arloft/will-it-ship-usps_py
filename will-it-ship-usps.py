def shippingSize(width, height, length):
	totalSize = ((float(width)+float(height))*2)+float(length)
	# print(type(totalSize))
	if totalSize <= 130:
		print("Length + Girth is " + str(totalSize) + ", it fits!")
	else:
		print("----------\n" "Length + Girth is " + str(totalSize) + " (over 130\"), nope, too big :( \n========")
	return totalSize

L = input("--------\nPackage length (size of longest side)? ")
W = input("Package width (size across)? ")
H = input("Package height (size up or down)? ")

shippingSize(W,H,L)