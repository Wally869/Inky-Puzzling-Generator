VAR hasKey = false
VAR hasPass = false
-> entrance

=== entrance ===
Your location is: Entrance.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> entrance
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 1]
        -> corridor1


=== classroom0 ===
Your location is: ClassRoom 0.
What would you like to do here?
  + [Look Around]
    { not hasKey:
        There is a safe, I wonder how I can open it?
    - else: 
                { not hasPass:
            You find a safe, with a keyhole. You open the safe using the key, and find a pass inside!
            ~hasPass= true
        - else: 
            There is an open safe, but there's nothing in it...
        }

    }
-> classroom0
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 0]
        -> corridor0


=== classroom1 ===
Your location is: ClassRoom 1.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> classroom1
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 0]
        -> corridor0


=== classroom2 ===
Your location is: ClassRoom 2.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> classroom2
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 1]
        -> corridor1


=== corridor0 ===
Your location is: Corridor 0.
What would you like to do here?
  + [Look Around]
    { not hasKey:
        You found a key on the floor!
        ~hasKey= true
    - else: 
        There is nothing here...
    }
-> corridor0
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 1]
        -> corridor1
     ++ [Corridor 2]
        -> corridor2
     ++ [ClassRoom 0]
        -> classroom0
     ++ [ClassRoom 1]
        -> classroom1


=== corridor1 ===
Your location is: Corridor 1.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> corridor1
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 0]
        -> corridor0
     ++ [Corridor 2]
        -> corridor2
     ++ [ClassRoom 2]
        -> classroom2
     ++ [Entrance]
        -> entrance
     ++ [Exit]
        -> exit


=== corridor2 ===
Your location is: Corridor 2.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> corridor2
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 0]
        -> corridor0
     ++ [Corridor 1]
        -> corridor1


=== exit ===
Your location is: Exit.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> exit
  + [Exit]
    { not hasPass:
        There is an exit door. You decide to use your pass on it. The door slowly opens... You are free!
    - else: 
        No key, no exit
    }
    { not hasPass:
        -> END
    - else: 
        -> exit
    }


