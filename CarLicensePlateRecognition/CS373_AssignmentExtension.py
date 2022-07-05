import math
import sys
from pathlib import Path

from matplotlib import pyplot
from matplotlib.patches import Rectangle

from PIL import Image
from pytesseract import Output
import pytesseract
import cv2
import numpy as np

# import our basic, light-weight png reader library
import imageIO.png

# this function reads an RGB color png file and returns width, height, as well as pixel arrays for r,g,b
def readRGBImageToSeparatePixelArrays(input_filename):
    image_reader = imageIO.png.Reader(filename=input_filename)
    # png reader gives us width and height, as well as RGB data in image_rows (a list of rows of RGB triplets)
    (image_width, image_height, rgb_image_rows, rgb_image_info) = image_reader.read()

    print("read image width={}, height={}".format(image_width, image_height))

    # our pixel arrays are lists of lists, where each inner list stores one row of greyscale pixels
    pixel_array_r = []
    pixel_array_g = []
    pixel_array_b = []

    for row in rgb_image_rows:
        pixel_row_r = []
        pixel_row_g = []
        pixel_row_b = []
        r = 0
        g = 0
        b = 0
        for elem in range(len(row)):
            # RGB triplets are stored consecutively in image_rows
            if elem % 3 == 0:
                r = row[elem]
            elif elem % 3 == 1:
                g = row[elem]
            else:
                b = row[elem]
                pixel_row_r.append(r)
                pixel_row_g.append(g)
                pixel_row_b.append(b)

        pixel_array_r.append(pixel_row_r)
        pixel_array_g.append(pixel_row_g)
        pixel_array_b.append(pixel_row_b)

    return (image_width, image_height, pixel_array_r, pixel_array_g, pixel_array_b)


# a useful shortcut method to create a list of lists based array representation for an image, initialized with a value
def createInitializedGreyscalePixelArray(image_width, image_height, initValue = 0):
    new_array = [[initValue for x in range(image_width)] for y in range(image_height)]
    return new_array

def frequency_counter(pixel_array, image_width, image_height):
    counter_dict = dict()
    for row in range(image_height):
        for col in range(image_width):
            if pixel_array[row][col] not in counter_dict:
                counter_dict[pixel_array[row][col]] = 1
            else:
                counter_dict[pixel_array[row][col]] += 1
    return counter_dict

def RGBtoGreyScale(image_width, image_height, pixel_array_r, pixel_array_g, pixel_array_b):
    greyscale_pixel_array = createInitializedGreyscalePixelArray(image_width, image_height)

    for i in range(image_height):
        for j in range(image_width):
            greyscale_pixel_array[i][j] = round(
                0.299 * pixel_array_r[i][j] + 0.587 * pixel_array_g[i][j] + 0.114 * pixel_array_b[i][j])

    return greyscale_pixel_array

def StretchValues(pixel_array, image_width, image_height):
    greyPixelArray = createInitializedGreyscalePixelArray(image_width, image_height)
    min_max = computeMinAndMaxValues(pixel_array, image_width, image_height)

    num = 0
    for i in range(image_height):
        for j in range(image_width):
            if (min_max[1] - min_max[0]) != 0:  # zero division check
                num = (pixel_array[i][j] - min_max[0]) * (255 / (min_max[1] - min_max[0]))  # pg33 formula
                if num < 0:
                    greyPixelArray[i][j] = 0
                elif num > 255:
                    greyPixelArray[i][j] = 255
                else:
                    greyPixelArray[i][j] = round(num)

    return greyPixelArray

# calculate the Fmin and Fhigh, Gmin=0 and Ghigh=255
def computeMinAndMaxValues(pixel_array, image_width, image_height):
    minVal = 255
    maxVal = 0
    for i in range(image_height):
        for j in range(image_width):
            if pixel_array[i][j] < minVal:
                minVal = pixel_array[i][j]
            if pixel_array[i][j] > maxVal:
                maxVal = pixel_array[i][j]
    return (minVal, maxVal,)


def computeStandardDeviationImage5x5(pixel_array, image_width, image_height):
    initArray = createInitializedGreyscalePixelArray(image_width, image_height, initValue=0)
    avg = 0
    sd2 = 0

    for row in range(2, image_height - 2):
        for col in range(2, image_width - 2):
            row0 = [pixel_array[row - 2][col - 2], pixel_array[row - 2][col - 1], pixel_array[row - 2][col],
                    pixel_array[row - 2][col + 1], pixel_array[row - 2][col + 2]]
            row1 = [pixel_array[row - 1][col - 2], pixel_array[row - 1][col - 1], pixel_array[row - 1][col],
                    pixel_array[row - 1][col + 1], pixel_array[row - 1][col + 2]]
            row2 = [pixel_array[row][col - 2], pixel_array[row][col - 1], pixel_array[row][col],
                    pixel_array[row][col + 1], pixel_array[row][col + 2]]
            row3 = [pixel_array[row + 1][col - 2], pixel_array[row + 1][col - 1], pixel_array[row + 1][col],
                    pixel_array[row + 1][col + 1], pixel_array[row + 2][col + 2]]
            row4 = [pixel_array[row + 2][col - 2], pixel_array[row + 2][col - 1], pixel_array[row + 2][col],
                    pixel_array[row + 2][col + 1], pixel_array[row + 2][col + 2]]

            tempLst = row0 + row1 + row2 + row3 + row4
            for num in tempLst:
                avg += num
            avg /= 25

            for num in tempLst:
                sd2 += pow(num - avg, 2)

            initArray[row][col] = math.sqrt(sd2 / 25)
            avg = 0
            sd2 = 0
    return initArray

def thresholdingContrast(pixel_array, image_width, image_height, threshold):
    initArray = createInitializedGreyscalePixelArray(image_width, image_height, initValue=0)

    for i in range(image_height):
        for j in range(image_width):
            if pixel_array[i][j] < threshold:
                initArray[i][j] = 0
            else:
                initArray[i][j] = 255
    return initArray

def computeErosion(pixel_array, image_width, image_height):
    initArray = createInitializedGreyscalePixelArray(image_width, image_height)
    s255 = [255, 255, 255, 255, 255, 255, 255, 255, 255]

    for row in range(image_height):
        for col in range(image_width):
            if (row == 0):
                row0 = [0, 0, 0, 0, 0]
                if col == 0:
                    row1 = [0, pixel_array[row][col], pixel_array[row][col + 1]]
                    row2 = [0, pixel_array[row + 1][col], pixel_array[row + 1][col + 1]]
                elif (col == image_width - 1):  # last col index
                    row1 = [pixel_array[row][col - 1], pixel_array[row][col], 0]
                    row2 = [pixel_array[row + 1][col - 1], pixel_array[row + 1][col], 0]
                else:  # col 2 until width-3
                    row1 = [pixel_array[row][col - 1], pixel_array[row][col], pixel_array[row][col + 1]]
                    row2 = [pixel_array[row + 1][col - 1], pixel_array[row + 1][col], pixel_array[row + 1][col + 1]]

            elif (row == image_height - 1):
                row2 = [0, 0, 0, 0, 0]
                if col == 0:
                    row0 = [0, pixel_array[row - 1][col], pixel_array[row - 1][col + 1]]
                    row1 = [0, pixel_array[row][col], pixel_array[row][col + 1]]
                elif (col == image_width - 1):  # last col index
                    row0 = [pixel_array[row - 1][col - 1], pixel_array[row - 1][col], 0]
                    row1 = [pixel_array[row][col - 1], pixel_array[row][col], 0]
                else:  # col 2 until width-3
                    row0 = [pixel_array[row - 1][col - 1], pixel_array[row - 1][col], pixel_array[row - 1][col + 1]]
                    row1 = [pixel_array[row][col - 1], pixel_array[row][col], pixel_array[row][col + 1]]

            elif (col == 0):
                row0 = [0, pixel_array[row - 1][col], pixel_array[row - 1][col + 1]]
                row1 = [0, pixel_array[row][col], pixel_array[row][col + 1]]
                row2 = [0, pixel_array[row + 1][col], pixel_array[row + 1][col + 1]]

            elif (col == image_width - 1):
                row0 = [pixel_array[row - 1][col - 1], pixel_array[row - 1][col], 0]
                row1 = [pixel_array[row][col - 1], pixel_array[row][col], 0]
                row2 = [pixel_array[row + 1][col - 1], pixel_array[row + 1][col], 0]

            else:
                row0 = [pixel_array[row - 1][col - 1], pixel_array[row - 1][col], pixel_array[row - 1][col + 1]]
                row1 = [pixel_array[row][col - 1], pixel_array[row][col], pixel_array[row][col + 1]]
                row2 = [pixel_array[row + 1][col - 1], pixel_array[row + 1][col], pixel_array[row + 1][col + 1]]

            temp = row0 + row1 + row2
            if temp == s255:
                initArray[row][col] = 255

    return initArray

def computeDilation(pixel_array, image_width, image_height):
    initArray = createInitializedGreyscalePixelArray(image_width, image_height)

    for row in range(image_height):
        for col in range(image_width):
            if (row == 0):
                row0 = [0, 0, 0, 0, 0]
                if col == 0:
                    row1 = [0, pixel_array[row][col], pixel_array[row][col + 1]]
                    row2 = [0, pixel_array[row + 1][col], pixel_array[row + 1][col + 1]]
                elif (col == image_width - 1):  # last col index
                    row1 = [pixel_array[row][col - 1], pixel_array[row][col], 0]
                    row2 = [pixel_array[row + 1][col - 1], pixel_array[row + 1][col], 0]
                else:  # col 2 until width-3
                    row1 = [pixel_array[row][col - 1], pixel_array[row][col], pixel_array[row][col + 1]]
                    row2 = [pixel_array[row + 1][col - 1], pixel_array[row + 1][col], pixel_array[row + 1][col + 1]]

            elif (row == image_height - 1):
                row2 = [0, 0, 0, 0, 0]
                if col == 0:
                    row0 = [0, pixel_array[row - 1][col], pixel_array[row - 1][col + 1]]
                    row1 = [0, pixel_array[row][col], pixel_array[row][col + 1]]
                elif (col == image_width - 1):  # last col index
                    row0 = [pixel_array[row - 1][col - 1], pixel_array[row - 1][col], 0]
                    row1 = [pixel_array[row][col - 1], pixel_array[row][col], 0]
                else:  # col 2 until width-3
                    row0 = [pixel_array[row - 1][col - 1], pixel_array[row - 1][col], pixel_array[row - 1][col + 1]]
                    row1 = [pixel_array[row][col - 1], pixel_array[row][col], pixel_array[row][col + 1]]

            elif (col == 0):
                row0 = [0, pixel_array[row - 1][col], pixel_array[row - 1][col + 1]]
                row1 = [0, pixel_array[row][col], pixel_array[row][col + 1]]
                row2 = [0, pixel_array[row + 1][col], pixel_array[row + 1][col + 1]]

            elif (col == image_width - 1):
                row0 = [pixel_array[row - 1][col - 1], pixel_array[row - 1][col], 0]
                row1 = [pixel_array[row][col - 1], pixel_array[row][col], 0]
                row2 = [pixel_array[row + 1][col - 1], pixel_array[row + 1][col], 0]

            else:
                row0 = [pixel_array[row - 1][col - 1], pixel_array[row - 1][col], pixel_array[row - 1][col + 1]]
                row1 = [pixel_array[row][col - 1], pixel_array[row][col], pixel_array[row][col + 1]]
                row2 = [pixel_array[row + 1][col - 1], pixel_array[row + 1][col], pixel_array[row + 1][col + 1]]

            temp = row0 + row1 + row2
            if 255 in temp:
                initArray[row][col] = 255

    return initArray

def connectedComponent(pixel_array, image_width, image_height):
    initArray = createInitializedGreyscalePixelArray(image_width, image_height)
    countDict = dict()
    tupleResult = (initArray, countDict)
    regionLabel = 1
    seenCheck = dict()

    for row in range(image_height):
        for col in range(image_width):
            q = Queue()
            if (row, col) not in seenCheck:
                if pixel_array[row][col] == 1 or pixel_array[row][col] == 255:
                    countDict[regionLabel] = 0
                    seenCheck[row, col] = 1
                    q.enqueue([row, col])
                    initArray[row][col] = regionLabel
                    while not q.isEmpty():
                        current = q.dequeue()
                        temprow = current[0]
                        tempcol = current[1]
                        if temprow == 0:
                            if tempcol == 0:
                                if (temprow, tempcol + 1) not in seenCheck:
                                    if pixel_array[temprow][tempcol + 1] == 1 or pixel_array[temprow][tempcol + 1] == 255:  # right
                                        q.enqueue([temprow, tempcol + 1])
                                        seenCheck[temprow, tempcol + 1] = 1
                                        initArray[temprow][tempcol + 1] = regionLabel
                            elif tempcol == image_width - 1:
                                if (temprow, tempcol - 1) not in seenCheck:
                                    if pixel_array[temprow][tempcol - 1] == 1 or pixel_array[temprow][tempcol - 1] == 255:  # left
                                        q.enqueue([temprow, tempcol - 1])
                                        seenCheck[temprow, tempcol - 1] = 1
                                        initArray[temprow][tempcol - 1] = regionLabel
                            else:
                                if (temprow, tempcol - 1) not in seenCheck:
                                    if pixel_array[temprow][tempcol - 1] == 1 or pixel_array[temprow][tempcol - 1] == 255:  # left
                                        q.enqueue([temprow, tempcol - 1])
                                        seenCheck[temprow, tempcol - 1] = 1
                                        initArray[temprow][tempcol] = regionLabel
                                if (temprow, tempcol + 1) not in seenCheck:
                                    if pixel_array[temprow][tempcol + 1] == 1 or pixel_array[temprow][tempcol + 1] == 255:  # right
                                        q.enqueue([temprow, tempcol + 1])
                                        seenCheck[temprow, tempcol + 1] = 1
                                        initArray[temprow][tempcol + 1] = regionLabel
                            if (temprow + 1, tempcol) not in seenCheck:
                                if pixel_array[temprow + 1][tempcol] == 1 or pixel_array[temprow + 1][tempcol] == 255:  # down
                                    q.enqueue([temprow + 1, tempcol])
                                    seenCheck[temprow + 1, tempcol] = 1
                                    initArray[temprow + 1][tempcol] = regionLabel

                        elif temprow == image_height - 1:
                            if tempcol == 0:
                                if (temprow, tempcol + 1) not in seenCheck:
                                    if pixel_array[temprow][tempcol + 1] == 1 or pixel_array[temprow][tempcol + 1] == 255:  # right
                                        q.enqueue([temprow, tempcol + 1])
                                        seenCheck[temprow, tempcol + 1] = 1
                                        initArray[temprow][tempcol + 1] = regionLabel
                            elif tempcol == image_width - 1:
                                if (temprow, tempcol - 1) not in seenCheck:
                                    if pixel_array[temprow][tempcol - 1] == 1 or pixel_array[temprow][tempcol - 1] == 255:  # left
                                        q.enqueue([temprow, tempcol - 1])
                                        seenCheck[temprow, tempcol - 1] = 1
                                        initArray[temprow][tempcol - 1] = regionLabel
                            else:
                                if (temprow, tempcol - 1) not in seenCheck:
                                    if pixel_array[temprow][tempcol - 1] == 1 or pixel_array[temprow][tempcol - 1] == 255:  # left
                                        q.enqueue([temprow, tempcol - 1])
                                        seenCheck[temprow, tempcol - 1] = 1
                                        initArray[temprow][tempcol - 1] = regionLabel
                                if (temprow, tempcol + 1) not in seenCheck:
                                    if pixel_array[temprow][tempcol + 1] == 1 or pixel_array[temprow][tempcol + 1] == 255:  # right
                                        q.enqueue([temprow, tempcol + 1])
                                        seenCheck[temprow, tempcol + 1] = 1
                                        initArray[temprow][tempcol + 1] = regionLabel
                            if (temprow - 1, tempcol) not in seenCheck:
                                if pixel_array[temprow - 1][tempcol] == 1 or pixel_array[temprow - 1][tempcol] == 255:  # up
                                    q.enqueue([temprow - 1, tempcol])
                                    seenCheck[temprow - 1, tempcol] = 1
                                    initArray[temprow - 1][tempcol] = regionLabel

                        elif tempcol == 0:
                            if (temprow, tempcol + 1) not in seenCheck:
                                if pixel_array[temprow][tempcol + 1] == 1 or pixel_array[temprow][tempcol + 1] == 255:  # right
                                    q.enqueue([temprow, tempcol + 1])
                                    seenCheck[temprow, tempcol + 1] = 1
                                    initArray[temprow][tempcol + 1] = regionLabel
                            if (temprow - 1, tempcol) not in seenCheck:
                                if pixel_array[temprow - 1][tempcol] == 1 or pixel_array[temprow - 1][tempcol] == 255:  # up
                                    q.enqueue([temprow - 1, tempcol])
                                    seenCheck[temprow - 1, tempcol] = 1
                                    initArray[temprow - 1][tempcol] = regionLabel
                            if (temprow + 1, tempcol) not in seenCheck:
                                if pixel_array[temprow + 1][tempcol] == 1 or pixel_array[temprow + 1][tempcol] == 255:  # down
                                    q.enqueue([temprow + 1, tempcol])
                                    seenCheck[temprow + 1, tempcol] = 1
                                    initArray[temprow + 1][tempcol] = regionLabel

                        elif tempcol == image_width - 1:
                            if (temprow, tempcol - 1) not in seenCheck:
                                if pixel_array[temprow][tempcol - 1] == 1 or pixel_array[temprow][tempcol - 1] == 255:  # left
                                    q.enqueue([temprow, tempcol - 1])
                                    seenCheck[temprow, tempcol - 1] = 1
                                    initArray[temprow][tempcol - 1] = regionLabel
                            if (temprow - 1, tempcol) not in seenCheck:
                                if pixel_array[temprow - 1][tempcol] == 1 or pixel_array[temprow - 1][tempcol] == 255:  # up
                                    q.enqueue([temprow - 1, tempcol])
                                    seenCheck[temprow - 1, tempcol] = 1
                                    initArray[temprow - 1][tempcol] = regionLabel
                            if (temprow + 1, tempcol) not in seenCheck:
                                if pixel_array[temprow + 1][tempcol] == 1 or pixel_array[temprow + 1][tempcol] == 255:  # down
                                    q.enqueue([temprow + 1, tempcol])
                                    seenCheck[temprow + 1, tempcol] = 1
                                    initArray[temprow + 1][tempcol] = regionLabel

                        else:
                            if (temprow, tempcol - 1) not in seenCheck:
                                if pixel_array[temprow][tempcol - 1] == 1 or pixel_array[temprow][tempcol - 1] == 255:  # left
                                    q.enqueue([temprow, tempcol - 1])
                                    seenCheck[temprow, tempcol - 1] = 1
                                    initArray[temprow][tempcol - 1] = regionLabel
                            if (temprow, tempcol + 1) not in seenCheck:
                                if pixel_array[temprow][tempcol + 1] == 1 or pixel_array[temprow][tempcol + 1] == 255:  # right
                                    q.enqueue([temprow, tempcol + 1])
                                    seenCheck[temprow, tempcol + 1] = 1
                                    initArray[temprow][tempcol + 1] = regionLabel
                            if (temprow - 1, tempcol) not in seenCheck:
                                if pixel_array[temprow - 1][tempcol] == 1 or pixel_array[temprow - 1][tempcol] == 255:  # up
                                    q.enqueue([temprow - 1, tempcol])
                                    seenCheck[temprow - 1, tempcol] = 1
                                    initArray[temprow - 1][tempcol] = regionLabel
                            if (temprow + 1, tempcol) not in seenCheck:
                                if pixel_array[temprow + 1][tempcol] == 1 or pixel_array[temprow + 1][tempcol] == 255:  # down
                                    q.enqueue([temprow + 1, tempcol])
                                    seenCheck[temprow + 1, tempcol] = 1
                                    initArray[temprow + 1][tempcol] = regionLabel
                        countDict[regionLabel] += 1
                    q = Queue()
                    regionLabel += 1

    return tupleResult

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def aspectRatio(region, pixel_array, image_width, image_height):
    minCol=image_width
    maxCol=0
    minRow=image_height
    maxRow=0

    for row in range(image_height):
        for col in range(image_width):
            if pixel_array[row][col] == region:
                if col < minCol:
                    minCol = col
                if row < minRow:
                    minRow = row
                if col > maxCol:
                    maxCol=col
                if row > maxRow:
                    maxRow = row
    regionWidth = maxCol - minCol
    regionHeight = maxRow - minRow

    return (minCol, minRow, maxCol, maxRow, regionWidth, regionHeight)

# This is our code skeleton that performs the license plate detection.
# Feel free to try it on your own images of cars, but keep in mind that with our algorithm developed in this lecture,
# we won't detect arbitrary or difficult to detect license plates!
def main():

    command_line_arguments = sys.argv[1:]

    SHOW_DEBUG_FIGURES = True

    # this is the default input image filename (plate5 in pdf ex)
    input_filename = "numberplate5.png"

    if command_line_arguments != []:
        input_filename = command_line_arguments[0]
        SHOW_DEBUG_FIGURES = False

    output_path = Path("output_images")
    if not output_path.exists():
        # create output directory
        output_path.mkdir(parents=True, exist_ok=True)

    output_filename = output_path / Path(input_filename.replace(".png", "_output.png"))
    if len(command_line_arguments) == 2:
        output_filename = Path(command_line_arguments[1])


    # we read in the png file, and receive three pixel arrays for red, green and blue components, respectively
    # each pixel array contains 8 bit integer values between 0 and 255 encoding the color values
    (image_width, image_height, px_array_r, px_array_g, px_array_b) = readRGBImageToSeparatePixelArrays(input_filename)

    # setup the plots for intermediate results in a figure
    fig1, axs1 = pyplot.subplots(2, 2)
    axs1[0, 0].set_title('Input red channel of image')
    axs1[0, 0].imshow(px_array_r, cmap='gray')
    axs1[0, 1].set_title('Input green channel of image')
    axs1[0, 1].imshow(px_array_g, cmap='gray')
    axs1[1, 0].set_title('Input blue channel of image')
    axs1[1, 0].imshow(px_array_b, cmap='gray')


    # STUDENT IMPLEMENTATION here
    ## Covert RGB to GreyScale
    GreyScalePixelArray = RGBtoGreyScale(image_width, image_height, px_array_r, px_array_g, px_array_b)
    StretchedValues = StretchValues(GreyScalePixelArray, image_width, image_height)
    px_array = StretchedValues

    ## Find structures with high contrast using standard deviation in pixel neighborhood
    SDpixelNeighborhood = computeStandardDeviationImage5x5(px_array, image_width, image_height)
    StretchedValues = StretchValues(SDpixelNeighborhood, image_width, image_height)
    px_array = StretchedValues

    ## Thresholding to get high contrast regions as binary image, good threshold is 150
    px_array = thresholdingContrast(px_array, image_width, image_height, 150)

    ## 3x3 dilation and 3x3 errosion to get "blob" region
    for dilation in range(4):
        px_array = computeDilation(px_array,image_width, image_height)

    for erosion in range(4):
        px_array = computeErosion(px_array, image_width, image_height)

    ## Connected component analysis to find largest connected object
    connComp = connectedComponent(px_array, image_width, image_height)
    px_array = connComp[0]

    ## check aspect ratio width/height range between 1.5 to 5
    descendingDict = sorted(connComp[1].items(), key = lambda x: x[1], reverse = True)
    (minCol, minRow, maxCol, maxRow, w, h) = (0, 0, 0, 0, 0, 0)
    for e in descendingDict:
        (minCol, minRow, maxCol, maxRow, w, h) = aspectRatio(e[0], px_array, image_width, image_height)
        if h != 0: #zero division error check
            ratio = w/h
            if ratio >= 1.5 and ratio <= 5: #if ratio is within the range we have found the number plate
                print("aspect ratio:", ratio)
                break

    # compute a dummy bounding box centered in the middle of the input image, and with as size of half of width and height
    center_x = image_width / 2.0
    center_y = image_height / 2.0
    bbox_min_x = center_x - image_width / 4.0
    bbox_max_x = center_x + image_width / 4.0
    bbox_min_y = center_y - image_height / 4.0
    bbox_max_y = center_y + image_height / 4.0

    # Draw a bounding box as a rectangle into the input image
    axs1[1, 1].set_title('Final image of detection')
    axs1[1, 1].imshow(px_array, cmap='gray')
    # rect = Rectangle((bbox_min_x, bbox_min_y), bbox_max_x - bbox_min_x, bbox_max_y - bbox_min_y, linewidth=1,
    #                  edgecolor='g', facecolor='none')
    rect = Rectangle((minCol, minRow), w, h, linewidth=1, edgecolor='g', facecolor='none')
    axs1[1, 1].add_patch(rect)


    ##Assignment Extension (read number plate)
    imgopen = Image.open(input_filename)
    crop = imgopen.crop((minCol, minRow, maxCol, maxRow))
    # crop.show()
    npArray = np.array(crop)
    text = pytesseract.image_to_string(npArray)

    if len(text) == 0: #attempt to use openCV if not detected in first try
        norm_img = np.zeros((npArray.shape[0], npArray.shape[1]))
        npArray = cv2.normalize(npArray, norm_img, 0, 255, cv2.NORM_MINMAX)
        npArray = cv2.threshold(npArray, 100, 255, cv2.THRESH_BINARY)[1]
        npArray = cv2.GaussianBlur(npArray, (1, 1), 0)
        text = pytesseract.image_to_string(npArray)

    numberPlate = str()
    for l in text:
        if l.islower():
            continue
        if l.isalpha() or l.isdigit():
            numberPlate += l
        else:  # remove characters that aren't suppose to be in number plates
            numberPlate += " "

    if len(text) == 0: #if still not detected
        print("Number plate not detected!")
    else:
        space = 0
        temp = str()
        numberPlate = numberPlate.strip()
        print("Raw Number Plate: ", numberPlate)
        for l in numberPlate: #remove excess characters
            if space > 2:
                temp = str()
                space = 0
            if l == " ":
                temp += l
                space += 1
            else:
                temp += l
        numberPlate = temp
        print("Detected Number Plate: ", numberPlate.strip())

    # write the output image into output_filename, using the matplotlib savefig method
    extent = axs1[1, 1].get_window_extent().transformed(fig1.dpi_scale_trans.inverted())
    pyplot.savefig(output_filename, bbox_inches=extent, dpi=600)

    if SHOW_DEBUG_FIGURES:
        # plot the current figure
        pyplot.show()


if __name__ == "__main__":
    main()