from typing import List


SPACE_PER_INDENT = 4

# Choice is considered as belonging to level of text introducing the choice (e.g. where do you want to go? + left  + right are all on same depth)
def GetLineHeaderChoice(depth: int, isSticky: bool = False):
    currDepth = depth + 1
    header = [" "  for _ in range(currDepth * SPACE_PER_INDENT)]
    temp = header[(-1-currDepth):-1]
    for i in range(len(temp)):
        if (isSticky):
            temp[i] = "+"
        else:
            temp[i] = "*"
    header[(-1-currDepth):-1] = temp
    return "".join(header)
    

def GetLineHeaderText(depth: int):
    return "".join([" " * SPACE_PER_INDENT for _ in range(depth)])


# CAREFUL: checking for NOT first
def GenerateConditional(conditional: str, alternative1: str, alternative2: str, depth: int):
    generated = [GetLineHeaderText(depth),"{ not ", conditional, ":\n"]
    generated += [GetLineHeaderText(depth + 1), alternative1, "\n"]
    generated += [GetLineHeaderText(depth), "- else: ", "\n"]
    generated += [GetLineHeaderText(depth + 1), alternative2, "\n"]
    generated += [GetLineHeaderText(depth), "}", "\n"]
    return generated

def GenerateConditionalAndToggle(conditional: str, alternative1: str, alternative2: str, depth: int):
    generated = [GetLineHeaderText(depth),"{ not ", conditional, ":\n"]
    generated += [GetLineHeaderText(depth + 1), alternative1, "\n"]
    generated += [GetLineHeaderText(depth + 1), "~", conditional, "= true" "\n"]
    generated += [GetLineHeaderText(depth), "- else: ", "\n"]
    generated += [GetLineHeaderText(depth + 1), alternative2, "\n"]
    generated += [GetLineHeaderText(depth), "}", "\n"]
    return generated