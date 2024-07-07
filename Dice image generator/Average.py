from PIL import Image
import math
from functools import reduce

def MakeDictOfDices(CroppedImage, Resolution):
    Image = CroppedImage[0]
    width = CroppedImage[1]
    height = CroppedImage[2]
    im_grey = Image.convert('LA')  # convert to grayscale
    total = dict()
    elem = ''

    for i in range(0, width):
        for j in range(0, height):
            if ((i+1)%Resolution==0):
                ii=int((i+1)/Resolution)
            else:
                ii= int(math.floor((i+1)/Resolution) + 1)
            if ((j+1)%Resolution==0):
                jj=int((j+1)/Resolution)
            else:
                jj= int(math.floor((j+1)/Resolution) + 1)

            elem=str(ii) + ',' + str(jj)
            total[elem] = ''

    for i in range(0, width):
        for j in range(0, height):
            if ((i+1)%Resolution==0):
                ii=int((i+1)/Resolution)
            else:
                ii= int(math.floor((i+1)/Resolution) + 1)
            if ((j+1)%Resolution==0):
                jj=int((j+1)/Resolution)
            else:
                jj= int(math.floor((j+1)/Resolution) + 1)

            elem=str(ii) + ',' + str(jj)
            if(total[elem] ==''):

                total[elem] = str(im_grey.getpixel((i,j))[0])
            else:

                total[elem] = total[elem] + ',' + str(im_grey.getpixel((i,j))[0])

    return total


def ListAverage(lst):
    #Calculates the average of the list
    new_list = []
    for item in lst:
        new_list.append(float(item))
    return reduce(lambda a, b: a + b, new_list) / len(new_list)

def Average(dict):
    #Calculating the average of each values of the dict
    #dict = {'1,1': '1,3,5', '1,2': '6,7,8', '1,3': '0,1,2'}
    #returns:
    #dict = {'1,1': 3, '1,2': 7, '1,3': 1}
    for key in dict:
        list=[]
        list = dict[key].split(',')
        dict[key]=ListAverage(list)
    return dict
