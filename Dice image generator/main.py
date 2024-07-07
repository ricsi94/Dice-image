import Average
import Picture
import Crop

input("\n Your original image's name needs to be 'image.png' . Press Enter to start generating the dice image.")

# "Resolution" of the generated image
Resolution = 9

#1. Cropping the image to fit every dice into every pixel.
CroppedImage = Crop.cropimage('image.png', Resolution)

#2. Making a dictionary. 
#The keys of the dictionary will be the dice (not pixels) coordinates of the new image.
#Each dice coordinate contains grayscale values of the original image
DictOfDices = Average.MakeDictOfDices(CroppedImage, Resolution)

#3. Replacing each dictionary values with the average of them
DictAverage = Average.Average(DictOfDices)

#4. Put dice images into dice coordinates.
Picture.MakeThePicture(DictAverage, 'DICEPICTURE.png')

print("\n Done.")