# Dice image generator and website made with Python, Three.js

## Features of the generator and the website

- Generates an image, which is made of dices
- You can specify the "resolution" of the generated image
- Generates a json file which contains the coordinates and the number
- 3D view of the generated picture made of dices

### Original image :

![](https://github.com/ricsi94/Dice-image/blob/main/Dice%20image%20generator/image.png)

### Generated image in small :

![](https://github.com/ricsi94/Dice-image/blob/main/Dice%20image%20generator/small-dicepicture.png)

### Generated image full size : full-size-dicepicture.png

### How to use it
##### Generate the 2D image:
Run ```main.py``` . This will make the 2D image and also the json file which you can use with Three.js
##### Use it with Three.js:
1. Copy the generated json file into ```src``` folder ( src\output.json )
2. Run ```npm install``` and ```npm run build```
3. Open ```dist\index.html``` with live server.

##### My portfolio : https://ricsi94.github.io/portfolio