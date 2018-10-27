COMP3317 Assignment 2
Vishnu Chopra

Running the program:
	- The program must be run on Python 3.x
	- Run the following command to run the program with default parameters
	
		python assign2.py

	- This will run the program with threshold = 1.00e+6 and sigma = 1.00
	- The result of this run will be 239 corners detected and plotted

Functions implemented:

1. rgb2gray :
	This function converts the input rgb image (h x w x 3) to a grayscale image of dimensions (h x w). It simply returns a new matrix of shape (hxw) with each cell (i,j) set to the intensity equal to the weighted sum of the R,G,B intensities at (i,j) within the original image. The weights corresponding to R,G,B are [0.299,0.587,0.114] respectively.

2. smooth1D:
	This function performs a 1 dimensional convolution of the gaussian filter on the grayscale image. 
	It first calls get_filter() which returns an appropriate filter according to sigma by generating an array of values produced by the gaussian curve, and then trimming off all the values which fall below 1/1000th of the peak value. It returns this trimmed kernel to the smooth1D function.

	Using the kernel from get_filter(), 1D convolution is performed on the image.

3. smooth2D:
	This function carries out 2D smoothing by making use of smooth1D first along the x axis, and then along the y axis by sending a transpose of the 1D smoothed image and then transposing it again.

4. derivative:
	This function simulates the convolution of the image with a derivative filter [-1,0,1]*(1/2) by making use of numpy slicing and arithmetic. It then returns the new image I' from original image I. For the edges, it simulates the [-1,1] filter.

5. cornerness:
	This function generates a new image R from a given image I's derived images of Ix2, Iy2, and Ixy by setting each pixel R(i,j) equal to the cornerness function using the values of (i,j) in Ix2, Iy2 and Ixy. The formula used is 
	R[i][j]=((Ix2[i][j]*Iy2[i][j]) - (IxIy[i][j]**2)) - (0.04*((Ix2[i][j]+Iy2[i][j])**2))

6. mark_maxima:
	This function traverses the entire image and marks every pixel which is a local maxima in its 8-pixel neighbourhood. It returns an array of all maxima points.

7. mark_corners:
	This functiona makes use of the list of maxima points, the cornerness image R and the threshold parameter to perform corner detection to subpixel accuracy. It makes use of the quadratic formula to identify the points which satisfy the threshold to a sub-pixel level. It returns an array of triples of (x,y,cornerness) with x and y being the sub-pixel accurate x and y coordinates of the corner pixels and the corneness being the R value of the pixel.

8. harris:
	This is the main function which drives the corner detection. It first computes Ix and Iy using the derivative() function on the original image and the transpose of the original function.
	It then computes Ix2, Iy2 and Ixy and then uses smooth2D() to perform smoothing.

	After the smoothed images have been obtained, the R image is generated using the corneness() function.

	Using the mark_maxima() function with the R image as an argument, all local maxima pixels are identified and returned to harris().

	Using the array of local maxima pixels, the R image and the threshold value as arguments, the mark_corners() function is called by harris() to identify to sub-pixel accuracy all corner pixels. This list of triples is returned to harris() which returns it to the driver function in decreasing order of cornerness.




