# Python Tetris

It's just Tetris coded in python.  

---

## Extra pieces

Upon starting the game you will notice a popup asking you, if you'd like to play with extra pieces.  
This popup exists, because [SmilerV](https://github.com/SmilerV) got a little carried away when making the pieces for the game, resulting in ridiculous difficulty.  
I wanted the game to still be playable by normal people, not just tetris addicts, hence the popup.  

## Controls

The blocks can be moved with the arrow keys.  
The up key will turn the block clockwise.  

[config]: #config-file
## Config file

The config file is automatically generated in `%appdata%\python-tetris\config.json`  
It is a (as the file-ending suggests) json file that as of release 1.0 includes the following settings:  

| Setting        | Description                                                                                                                                                                                                                                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| speed_modifier | This is divided by 100 and then multiplied by the total amount of points<br/>to calculate the falling speed of the blocks in grid spaces per second.<br/>The result of this operation will have 2 added on top to account for the<br/>base speed. You may set this setting to 0 to avoid this game mechanic. |