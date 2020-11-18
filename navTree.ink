VAR hasKey = false
VAR hasPass = false
-> entrance

=== entrance ===
Your location is: Entrance.
What would you like to do?
  + [Look Around]
    You decide to take a look around
    There was nothing.
    -> entrance
  + [Go somewhere else]
     ++ [Corridor 0].
-> corridor0
=== classroom0 ===
Your location is: ClassRoom 0.
What would you like to do?
  + [Look Around]
    You decide to take a look around
    There was nothing.
    -> classroom0
  + [Go somewhere else]
     ++ [Corridor 2].
-> corridor2
=== classroom1 ===
Your location is: ClassRoom 1.
What would you like to do?
  + [Look Around]
    You decide to take a look around
    There was nothing.
    -> classroom1
  + [Go somewhere else]
     ++ [Corridor 0].
-> corridor0
=== classroom2 ===
Your location is: ClassRoom 2.
What would you like to do?
  + [Look Around]
    You decide to take a look around
    You found a safe!
    {hasPass: But it's empty...}
    {not hasPass: 
        {hasKey:
            You open it with your key. There was a pass inside! You pick it up.
            ~hasPass = true
        }
        {not hasKey:
            But you have no way to open it
        }
        }
    -> classroom2
  + [Go somewhere else]
     ++ [Corridor 0].
-> corridor0
=== corridor0 ===
Your location is: Corridor 0.
What would you like to do?
  + [Look Around]
    You decide to take a look around
    There was nothing.
    -> corridor0
  + [Go somewhere else]
     ++ [Corridor 1].
-> corridor1
     ++ [Corridor 2].
-> corridor2
     ++ [ClassRoom 1].
-> classroom1
     ++ [ClassRoom 2].
-> classroom2
     ++ [Entrance].
-> entrance
=== corridor1 ===
Your location is: Corridor 1.
What would you like to do?
  + [Look Around]
    You decide to take a look around
    {hasKey == false:
        You Found a key!
        ~hasKey = true
    }
    -> corridor1
  + [Go somewhere else]
     ++ [Corridor 0].
-> corridor0
     ++ [Corridor 2].
-> corridor2
=== corridor2 ===
Your location is: Corridor 2.
What would you like to do?
  + [Look Around]
    You decide to take a look around
    There was nothing.
    -> corridor2
  + [Go somewhere else]
     ++ [Corridor 0].
-> corridor0
     ++ [Corridor 1].
-> corridor1
     ++ [ClassRoom 0].
-> classroom0
     ++ [Exit].
-> exit
=== exit ===
Your location is: Exit.
{ hasPass: You have reached the exit! Congrats! -> END}
 {not hasPass: No pass, no exit.YOU STAY HERE FOREVER! -> END}
