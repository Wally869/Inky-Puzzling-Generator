from dataclasses import dataclass, field

from typing import List
from enum import Enum

from random import randint, choice

# article: runtime creation of a navigable location


class LocationTypes(Enum):
    Entrance = 0,
    Corridor = 1,
    Classroom = 2,
    Exit = 3


class Items(Enum):
    Key = 0,
    Pass = 1,
    Safe = 2


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
    def GetActionsText(self):
        text = "  + [Look Around]\n    You decide to take a look around\n"
        if len(self.Items) == 0:
            text += "    There was nothing.\n"
        else:
            for item in self.Items:
                if item == Items.Key:
                    text += "    {hasKey == false:\n        You Found a key!\n        ~hasKey = true\n    }\n" # else: This is where you found that key.\n}"
                if item == Items.Safe:
                    # safe contains the pass
                    text += "    You found a safe!\n"
                    text += "    {hasPass: But it's empty...}\n" 
                    text += "    {not hasPass: \n        {hasKey:\n            You open it with your key. There was a pass inside! You pick it up.\n            ~hasPass = true\n        }\n        {not hasKey:\n            But you have no way to open it\n        }\n        }\n"
        text += "    -> {}\n".format(self.Identifier)
        text += "  + [Go somewhere else]\n"
        for conn in self.ConnectedLocations:
            text += "     ++ [{}].\n-> {}\n".format(conn.Name, conn.Identifier)
        return text
    def Stringify(self):
        stringified = self.LocationMarker
        stringified += self.GetArrivalText()
        if self.LocationType != LocationTypes.Exit:
            stringified += "What would you like to do?\n"
            stringified += self.GetActionsText()
        else:
            stringified += "{ hasPass: "
            stringified += "You have reached the exit! Congrats! "
            stringified += "-> END}\n "
            stringified += "{not hasPass: "
            stringified += "No pass, no exit."
            stringified += "YOU STAY HERE FOREVER! -> END}\n"
        return stringified


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
    choice(rooms).Items.append(Items.Safe)

    # generate corridors
    corridors = []
    for i in range(nbCorridors):
        corridors.append(
            Location("Corridor {}".format(i), "corridor{}".format(i), LocationTypes.Corridor)
        )
    
    # put the key in one of the corridors
    choice(corridors).Items.append(Items.Key)

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

for room in mapRooms:
    output += room.Stringify()




with open("navTree.ink", "w+") as f:
    f.write(output)
