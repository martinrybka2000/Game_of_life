# Game_of_life

## Table of contents  
  - [Description](#description)
  - [Controls](#controls)
    * [Moving](#moving)
    * [Next generation](#next-generation)
    * [Zooming](#zooming)
    * [Creating cells](#creating-cells)
    * [Exiting](#exiting)
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

### Exiting
You can use Esc or the 'x' button

## Next generation algorithm description
For generating the next generation of cells the algorytm stores the alive cells in a hashmap.  
Iterating thru the alive cells the algorithm is adding every connected cell to the hashmap and itereting the neighbour counter.  

```
    def Step_up(self, num_of_steps):

        new_cells = {}

        for coord in self.__alive_cells:
            new_cells[coord] = Cell(0, True)

        for coord in self.__alive_cells:

            for x_dif, y_dif in ([-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]):
                if((coord[0] + x_dif, coord[1] + y_dif) in new_cells):
                    new_cells[(coord[0] + x_dif, coord[1] + y_dif)].n += 1
                else:
                    new_cells[(coord[0] + x_dif, coord[1] + y_dif)] = Cell(1, False)

        self.__alive_cells = new_cells

        self.__Judge_cells()
```
The algorithm that judges the state of the cell on the neighbour count  

```
    def __Judge_cells(self):
            # rules of the game of life
            for coord, cell in list(self.__alive_cells.items()):
                if (cell.alive == True):
                    if (cell.n < 2 or cell.n > 3):
                        del self.__alive_cells[coord]
                elif (cell.n != 3):
                    del self.__alive_cells[coord]
```

## Instalation
For installation it is recommended to create a virtual environment using [venv](https://docs.python.org/3/tutorial/venv.html) or any other  
  
1. Creating a destination directory  
```
mkdir [name]  
cd [name]
```

2. Creating and activating virtual environment: 
```
python3 -m venv venv  
source venv/bin/activate  
git clone https://github.com/martinrybka2000/Game_of_life.git 
cd Game_of_life  
pip install -r requirements.txt
```  

3. Run:  
```
python3 main.py
```

## ToDo
- Add a list of most popular game of life structures

Work in progress..
