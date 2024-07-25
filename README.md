# Python Tetris

It's just Tetris coded in python.  
This was made only for Windows and may not work on other operating systems.  

---

## Extra pieces

Upon starting the game you will notice a popup asking you, if you'd like to play with extra pieces.  
This popup exists, because [SmilerV](https://github.com/SmilerV) got a little carried away when making the pieces for the game, resulting in ridiculous difficulty.  
I wanted the game to still be playable by normal people, not just tetris addicts, hence the popup.  

## Controls

The blocks can be moved with the arrow keys.  
The up key will turn the block clockwise.

## Config file

The config file is automatically generated in `%appdata%\python-tetris\config.json`  
If you installed python via the Microsoft Store the location will instead be something like:  
`%localappdata%\packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\Roaming\python-tetris\config.json`  
It is a (as the file-ending suggests) json file that as of release 1.1 includes the following settings:  

| Setting        | Description                                                                                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| speed_modifier | A float. This is divided by 100 and then multiplied by the total amount of<br/>points to calculate the falling speed of the blocks in grid spaces per second.<br/>The result of this operation will have base_speed added on top to account for the base speed.<br/>You may set this setting to 0 to avoid this game mechanic. |
| base_speed     | A float that should be larger than 0.<br/>It is used to calculate the falling speed of the blocks, as described in the description of speed_modifier.                                                                                                                                                                          |


## Todo
- [x] Release new Version including the change