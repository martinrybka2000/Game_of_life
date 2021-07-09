# Game_of_life

## Table of contents  
  - [Description](#description)
  - [Controls](#controls)
    * [Moving](#moving)
    * [Next generation](#next-generation)
    * [Zooming](#zooming)
    * [Creating cells](#creating-cells)
  - [Next generation algorithm description](#next-generation-algorithm-description)
  - [Instalation](#instalation)
  - [ToDo](#todo)

## Description

This is an implementation on **game of life** based on the original [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

Made in [pygame](https://www.pygame.org/news)

## Controls

### Moving
For moving the grid you can use: wasd, arrows, mouse  
  
<img src="https://user-images.githubusercontent.com/39592198/124986292-c2279b80-e03b-11eb-9624-a09ca65af097.gif" width="450" height="300"/>

### Next generation
For skipping to the next generation you can hold space or click 'N'
  
<img src="https://user-images.githubusercontent.com/39592198/125062648-ebcdda80-e0ae-11eb-9f91-8e3adda1dbe6.gif" width="450" height="300"/>

### Zooming
For zooming in and out you can use 'q' and 'e' or mouse wheel
  
<img src="https://user-images.githubusercontent.com/39592198/125063783-33a13180-e0b0-11eb-8194-4b4f5f32c54e.gif" width="450" height="300"/>

### Creating cells
For creating or destroying cells you can use mouse + CTRL
  
<img src="https://user-images.githubusercontent.com/39592198/125063119-63036e80-e0af-11eb-8e0d-b17103dcee2e.gif" width="450" height="300"/>

## Next generation algorithm description

## Instalation
For installation it is recommended to create a virtual environment using [venv](https://docs.python.org/3/tutorial/venv.html) or any other  
  
Creating and activating virtual environment: 
```
python3 -m venv venv  
source venv/bin/activate  
git clone https://github.com/martinrybka2000/Game_of_life.git  
pip install -r requirements.txt
```  

Run:  
```
python3 main.py
```

## ToDo
- Add a list of most popular game of life structures

Work in progress..
