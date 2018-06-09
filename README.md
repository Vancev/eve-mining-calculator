# Eve Mining Calculator 

Copyright (c) 2018 VanceV

## What is the mining calculator?
The eve mining calculator is a tool for [EVE Online](https://www.eveonline.com/) that gives you get a better idea on what to mine, and how profitable mining can be. This calculator can calculate the following:
* Mining time to a full hold
* Average price of each ore
* Value of a full hold for each ore
* ISK per hour of mining for each ore
* ISK per hour of mining, given a round trip travel time for each ore
* Mining time to break even for each ore

Additionally, the user can enter the lowest security level they're comfortable mining in and only receive information for ores in the corresponding security levels. 

## Getting Started
1. Open up the command prompt or terminal. 
2. Change to the directory you wish to run the program in.
3. Run ```git clone https://github.com/Vancev/eve-mining-calculator.git```
4. Type in ``` pip install PrettyTable```
5. Now change into the new directory named ```eve-mining-calculator```
6. Run ```python main.py```

## Using the calculator 
You will be promted to enter the following information when running the calculator:

**Lowest security level to mine in:**

	This tells the program to only show ores at the entered security level and above
    
**Your total cargo size:**

	This is the total cargo size used when mining, including any haulers and support ships.
    
**The mining lasers mining amount:**

	This is the mining amount for each laser. If you have multiple lasers with different mining amounts, please enter an average of all lasers. 
    
**The lasers duration in seconds:**

	This is the mining laser duration. If using multiple lasers with different durations, enter an average for all durations.
    
**The number of lasers:**
	
    The total number of lasers used.
    
**Round trip travel time in minutes.**
	
    This is optional. This is the round trip travel time from the mining location to the station that wil hold the mined ores.
    
**Amount of ISK needed to break even.**

	This is how much ISK you you need to break even.
    
## License

This program is licensed under the "MIT License". Please see the file LICENSE in the source distribution of this software for license terms.