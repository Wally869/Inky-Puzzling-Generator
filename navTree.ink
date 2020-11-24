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
     ++ [Corridor 2]
        -> corridor2


=== classroom0 ===
Your location is: ClassRoom 0.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> classroom0
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 1]
        -> corridor1


=== classroom1 ===
Your location is: ClassRoom 1.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> classroom1
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 1]
        -> corridor1


=== classroom2 ===
Your location is: ClassRoom 2.
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
-> classroom2
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 1]
        -> corridor1


=== corridor0 ===
Your location is: Corridor 0.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> corridor0
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 2]
        -> corridor2
     ++ [Corridor 1]
        -> corridor1


=== corridor1 ===
Your location is: Corridor 1.
What would you like to do here?
  + [Look Around]
    { not hasKey:
        You found a key on the floor!
        ~hasKey= true
    - else: 
        There is nothing here...
    }
-> corridor1
  + [Go Elsewhere]
    Where would you like to go?
     ++ [Corridor 0]
        -> corridor0
     ++ [Corridor 2]
        -> corridor2
     ++ [ClassRoom 0]
        -> classroom0
     ++ [ClassRoom 1]
        -> classroom1
     ++ [ClassRoom 2]
        -> classroom2
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
     ++ [Entrance]
        -> entrance


=== exit ===
Your location is: Exit.
What would you like to do here?
  + [Look Around]
    There is nothing around here...
-> exit
  + [Exit]
    You have reached the exit.
    -> END


