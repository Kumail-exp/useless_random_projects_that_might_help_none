from itertools import product
import inspect
from gates import *

def Full_Adder(A,B,C):
    # sum,carry
    return XOR(XOR(A,B),C),OR(OR(AND(A,B),AND(B,C)),AND(A,C))

def truth_table(f):
    # stole this online this is so optimised and short
    n = len(inspect.signature(f).parameters)
    return [(*inputs, f(*inputs)) for inputs in product((False, True), repeat=n)]

def to_stream(num:int,size=8):
    b=bin(num)[2:]
    binary=[False]*size
    for i in range(len(b)):
        binary[size-len(b)+i]=bool(int(b[i]))
    return binary
def to_num(stream: list[bool], size=None, two_complement=False):
    if size is None:
        size = len(stream)  
    value = 0
    if two_complement:
        value -= int(stream[0]) * (1 << (size - 1))
        start = 1
    else:
        start = 0

    for i in range(start, size):
        value += int(stream[i]) * (1 << (size - 1 - i))

    return value

class Register:
    def __init__(self, size=8):
        self.size = size
        self.value = [False] * size

    def load(self, new_value: list[bool]):
        self.value = new_value.copy()

    def read(self) -> list[bool]:
        return self.value.copy()

# for i in truth_table(Full_Adder):
#     print(i)