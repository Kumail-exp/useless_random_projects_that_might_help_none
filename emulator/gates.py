    
def NAND(a: bool, b: bool) -> bool:
    return not (a and b)
def NOT(a: bool) -> bool:
    return NAND(a, a)
def AND(a: bool, b: bool) -> bool:
    return NOT(NAND(a, b))
def OR(a: bool, b: bool) -> bool:
    return NAND(NOT(a), NOT(b))
def NOR(a: bool, b: bool) -> bool:
    return NOT(OR(a, b))
def XOR(a: bool, b: bool) -> bool:
    return AND(OR(a, b), NAND(a, b))
def XNOR(a: bool, b: bool) -> bool:
    return NOT(XOR(a, b))
def BUFFER(a: bool) -> bool:
    return a
def IMPLIES(a: bool, b: bool) -> bool:
    return OR(NOT(a), b)
def EQUIVALENT(a: bool, b: bool) -> bool:
    return XNOR(a, b)
