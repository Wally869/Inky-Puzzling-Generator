from dataclasses import dataclass, field

from typing import List
from enum import Enum

from random import randint, choice

from InkyUtils import *

# article: runtime creation of a navigable location


class LocationTypes(Enum):
    Entrance = 0,
    Corridor = 1,
    Classroom = 2,
    Exit = 3


class ItemsType(Enum):
    Key = 0,
    Pass = 1,
    Safe = 2


@dataclass
class Item:
    pass



@dataclass
class Location:
    Name: str
    Identifier: str
    LocationType: LocationTypes
    ConnectedLocations: List = field(default_factory=list) # Location
    Items: List = field(default_factory=list)
    def __eq__(self, other):
        if type(self) == type(other):
            return self.Identifier == other.Identifier
        else:
            return TypeError("Invalid type for eq operation.")
    def AddConnection(self, location):
        self.ConnectedLocations.append(location)
    @property
    def NbConnections(self):
        return len(self.ConnectedLocations)
    @property
    def LocationMarker(self):
        return "=== {} ===\n".format(self.Identifier)
    def GetArrivalText(self):
        return "Your location is: {}.\n".format(self.Name)


def GenerateText_LocationConnections(location: Location, depth: int = 0):
    generated = [GetLineHeaderText(depth), "Where would you like to go?\n"]
    for c in location.ConnectedLocations:
        generated += [GetLineHeaderChoice(depth, True), "[", c.Name, "]", "\n"]
        generated += [GetLineHeaderText(depth + 1), "-> ", c.Identifier, "\n"]
    return generated


def GenerateText_LookAround(location: Location, depth: int = 0):
    generated = []
    if len(location.Items) == 0:
        generated += [GetLineHeaderText(depth), "There is nothing around here...", "\n"]
    else:
        for item in location.Items:
            if item == ItemsType.Key:
                generated += GenerateConditionalAndToggle("hasKey", "You found a key on the floor!", "There is nothing here...", depth)
            elif item == ItemsType.Safe:
                conditionalPassText = GenerateConditionalAndToggle("hasPass", "You find a safe, with a keyhole. You open the safe using the key, and find a pass inside!", "There is an open safe, but there's nothing in it...", depth+1)
                generated += GenerateConditional("hasKey", "There is a safe, I wonder how I can open it?", conditionalPassText, depth)
            else:
                pass
    generated += ["-> ", location.Identifier, "\n"]
    return generated


def GenerateText_LocationChoices(location: Location, depth: int = 0):
    generated = ["What would you like to do here?\n"]
    generated += [GetLineHeaderChoice(depth, True), "[", "Look Around", "]", "\n"]
    generated += GenerateText_LookAround(location, depth + 1)
    if location.LocationType == LocationTypes.Exit:
        generated += [GetLineHeaderChoice(depth, True), "[", "Exit", "]", "\n"]
        generated += [GetLineHeaderText(depth + 1), "You have reached the exit.", "\n"]
        generated += [GetLineHeaderText(depth + 1), "-> END", "\n"]
    else:
        generated += [GetLineHeaderChoice(depth, True), "[", "Go Elsewhere", "]", "\n"]
        generated += GenerateText_LocationConnections(location, depth + 1)
    return generated


def GenerateLocationText(location: Location):
    # Get Initial texts
    elements = [location.LocationMarker, location.GetArrivalText()]
    elements += GenerateText_LocationChoices(location, 0)
    elements += "\n\n"
    return elements







def GenerateMap(nbRooms: int = 3, nbCorridors: int = 3):
    locations = []
    locations.append(
        Location("Entrance", "entrance", LocationTypes.Entrance)
    )
    rooms = []
    for i in range(nbRooms):
        rooms.append(
            Location("ClassRoom {}".format(i), "classroom{}".format(i), LocationTypes.Classroom)
        )
    # put the safe in one of the rooms
    choice(rooms).Items.append(ItemsType.Safe)

    # generate corridors
    corridors = []
    for i in range(nbCorridors):
        corridors.append(
            Location("Corridor {}".format(i), "corridor{}".format(i), LocationTypes.Corridor)
        )
    
    # put the key in one of the corridors
    choice(corridors).Items.append(ItemsType.Key)

    # generate links between corridors. Need to check if fully connected btw.
    for _, corr in enumerate(corridors):
        while len(corr.ConnectedLocations) < 2:
            chosenCorridor = choice(corridors)
            if chosenCorridor != corr and chosenCorridor not in corr.ConnectedLocations:
                corr.ConnectedLocations.append(chosenCorridor)
                chosenCorridor.ConnectedLocations.append(corr)

    # generate links between rooms and corridors
    for room in rooms:
        chosenCorridor = choice(corridors)
        room.ConnectedLocations.append(chosenCorridor)
        chosenCorridor.AddConnection(room)
    
    # generate links between entrance and corridor
    chosenCorridor = choice(corridors)
    locations[0].ConnectedLocations.append(chosenCorridor)
    chosenCorridor.ConnectedLocations.append(locations[0])
    locations += rooms
    locations += corridors
    locations.append(
        Location(
        "Exit", "exit", LocationTypes.Exit, [choice(corridors)]
    )
    )
    choice(corridors).AddConnection(locations[-1])
    return locations


    



# scene is composed of sub elements with sticky choices 
# follows a simple pattern: when reaching the thing, we say "ok you have reached here"
# then they can choose to do thing here (for now only wait) or navigate
# if navigate, can choose to go to connected locations

mapRooms = GenerateMap()

output = "VAR hasKey = false\nVAR hasPass = false\n"

output += "-> entrance\n\n"

elems = []
print(len(mapRooms))
for room in mapRooms:
    #output += room.Stringify()
    elems += GenerateLocationText(room)

#print(elems)
#roomsText = "".join(elems)
roomsText = ""
for idElem, elem in enumerate(elems):
    if type(elem) == list:
        elems[idElem] = "".join(elem)

roomsText = "".join(elems)
output = output + roomsText


with open("navTree.ink", "w+") as f:
    f.write(output)
