from PIL import Image
import json

def GetNearestDice(p):
    int1 = 240
    int2 = 231
    int3 = 223
    int4 = 215
    int5 = 206
    int6 = 198

    #Correction
    p = p + 120

    if(p<=int6):
        return '6'
    if(p>int6 and p<int5):
        if(abs(p-int6) < abs(p-int5)):
            return '6'
        else:
            return '5'
    if(p==int5):
        return '5'
    if (p > int5 and p < int4):
        if (abs(p - int5) < abs(p - int4)):
            return '5'
        else:
            return '4'
    if(p==int4):
        return '4'
    if (p > int4 and p < int3):
        if (abs(p - int4) < abs(p - int3)):
            return '4'
        else:
            return '3'
    if(p==int3):
        return '3'
    if (p > int3 and p < int2):
        if (abs(p - int3) < abs(p - int2)):
            return '3'
        else:
            return '2'
    if(p==int2):
        return '2'
    if (p > int2 and p < int1):
        if (abs(p - int2) < abs(p - int1)):
            return '2'
        else:
            return '1'
    if(p>=int1):
        return '1'

def MakeThePicture(dict, DicePicture):
    #The dice width and height in pixels
    WidthDice , HeightDice = Image.open('Dices/1.png').size

    if(WidthDice == HeightDice):
        WidthAndHeightOfDiceImages = WidthDice
    
    #Get the width and height
    width = 0
    height = 0
    for key in dict:
        key1 = key.split(',')[0]
        key1 = int(key1)
        if (width < key1):
            width = key1
        key2 = key.split(',')[1]
        key2 = int(key2)
        if (height < key2):
            height = key2

    #"Stretch" the image to have enough space for each dice image
    StretchedWidth = width * WidthAndHeightOfDiceImages
    StretchedHeight = height * WidthAndHeightOfDiceImages


    Picture = Image.new('L', (StretchedWidth, StretchedHeight))
    img1 = Image.open("Dices/1.png")
    img2 = Image.open("Dices/2.png")
    img3 = Image.open("Dices/3.png")
    img4 = Image.open("Dices/4.png")
    img5 = Image.open("Dices/5.png")
    img6 = Image.open("Dices/6.png")

    data_list = []
    for x in range(width):
        for y in range(height):
            key = str(x+1) + ',' + str(y+1)
            p = int(dict[key])
            xCoord=x * WidthAndHeightOfDiceImages
            yCoord=y * WidthAndHeightOfDiceImages
            numberOnTopOfDice = GetNearestDice(p)
            
            data = {"xCoord": x, "yCoord": y, "numberOnTopOfDice": numberOnTopOfDice}
            # Append the data to the list
            data_list.append(data)
            
            if(numberOnTopOfDice == '1'):
                Picture.paste(img1, (xCoord, yCoord))
            if(numberOnTopOfDice == '2'):
                Picture.paste(img2, (xCoord, yCoord))
            if(numberOnTopOfDice == '3'):
                Picture.paste(img3, (xCoord, yCoord))
            if(numberOnTopOfDice == '4'):
                Picture.paste(img4, (xCoord, yCoord))
            if(numberOnTopOfDice == '5'):
                Picture.paste(img5, (xCoord, yCoord))
            if(numberOnTopOfDice == '6'):
                Picture.paste(img6, (xCoord, yCoord))
    json_data = json.dumps(data_list, indent=2)
    with open("output.json", "w") as json_file:
        json_file.write(json_data)
    Picture.save(DicePicture)
