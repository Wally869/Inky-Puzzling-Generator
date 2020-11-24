# Inky-Puzzling-Generator
Experimenting with generating short puzzles to be run with the [Ink Scripting Language](https://www.inklestudios.com/ink/)


## Overview  
The intent is to automate the generation of explorable "mazes" to create procedurally generated text adventures.

It creates a certain number of Locations (instance of the Location class) among a certain number of types (Entrance, Exit, Corridor, Classroom).
Reaching the exit successfully is dependent on finding certains items, placed at random. 

In latest version, a key is located in one of the corridors, and that key is used to open a safe in one of the classrooms. That safe in turn contains a pass to exit the game successfuly.


## How it works
For now, the nav_tree.py is the generator used.
It generates the locations, sets the items and creates the connections at random.
All locations generated are referenced in an array and are an Instance of the Location class.

This Location class has a Stringify method, which generates valid Inky code and takes into account data associated with the Instance (which items are in that location, and what locations are linked to this one)

Then we just iterate on the locations array, and append an output string value by the content of each Stringify method call.
The output is then written to an ink file, to be run in the Inky editor



## To Improve  
This is a quick and dirty first versions, with a few things. Improvements coming (crossed items have been implemented):  
- ~~Replace currently used string concatenation by an array of string. Perform the concatenation at the end only.~~
- ~~Create a function to set an appropriate amount of whitespacing when generating content to be indented (take into account the indentation level, whether it's a choice or not, and if it's sticky). This is obviously much cleaner than appending stuff like "  * " by hand.~~
- Adding random text selection from an initial knowledge base? 
- Cleaner Map generator
- Implement check to ensure map is fully connected and all nodes are accessible



## Things to Know  
I have met a few problems, which are good to know in advance if you want to do something similar:  
- Newlines are significant when writing a conditional segment, write them like this
```
{ condition1: 
    logicRelated to condition1.
    ~variable1 = new value
}
```
The parser has been having trouble when dealing with value setting when not in a new line while in a conditional block. 
Might have been a mistake on my part, will investigate more.

