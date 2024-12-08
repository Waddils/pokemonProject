I ran this code using...
 - Python 3.11.0
 - Visual Studio Code [downloaded the Python Extension Pack and Python Debugger]

        Name: Python Extension Pack
    Id: donjayamanne.python-extension-pack
    Description: Popular Visual Studio Code extensions for Python
    Version: 1.7.0
    Publisher: Don Jayamanne
    VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack

        Name: Python Debugger
    Id: ms-python.debugpy
    Description: Python Debugger extension using `debugpy`.
    Version: 2024.0.0
    Publisher: Microsoft
    VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy

Now you have 5 files:
 - PokemonColosseum.py
 - Pokemon.py
 - Moves.py
 - pokemon-data.csv
 - moves-data.csv

The 3 .py files are used to run the main game, while the .csv files are utilized by extracting the necessary data from them.
In order to run the main game, all you do is run the "PokemonColosseum.py" and the game proceeds. The user types in their name, gets assigned 3 random pokemon,
chooses moves based on the visual provided, and the battle continues until all of the pokemon on a team are defeated. 

Running the program on VSCode...
1. Download the ZIP folder and drag to desktop or some place
2. Create a folder called "pokemon" or named something else on your desktop
3. Drag the PokemonProject.zip file into the folder
4. Right click on the zip and choose "Extract Here"
    a. All of the files from the zip should go into that folder
4.1. Open Visual Studio Code and click "File" --> "Open Folder" and select the folder you dragged the zip file in
5. Once you have all of the files listed above, click on PokemonColosseum.py
6. Press F5 (Run and Debug hotkey) and something should pop up on the top of the screen called "Select Debugger"
7. Select "Python Debugger", then click "Python File"
8. The program should run successfully