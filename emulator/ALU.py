from gates import *
from IC import *


inputs=[False]*8
outputs=[False]*8
opcode=[False]*3

def add_8bit(A,B,sub:bool=False):
    outputs=[False]*8
    carry=sub
    for i in range(7,-1,-1):
        outputs[i],carry=Full_Adder(A[i],XOR(B[i],sub),carry)
    return outputs

def nand_8bit(A,B):
    return [NAND(i,j) for i,j in zip(A,B)] 
def nor_8bit(A,B):
    return [NOR(i,j) for i,j in zip(A,B)] 
def xor_8bit(A,B):
    return [XOR(i,j) for i,j in zip(A,B)] 

def shr(A):
    """Logical right shift of an 8-bit boolean list."""
    out = [False] * 8
    for i in range(7):
        out[i + 1] = A[i]
    return out


def shl(A):
    """Logical left shift of an 8-bit boolean list."""
    out = [False] * 8
    for i in range(7):
        out[i] = A[i + 1]
    return out
def no_op(A):
    return A
def alu(A,B,opcode):
    if opcode==[False,False,False]:
        return no_op(A)
    elif opcode==[False,False,True]:
        return add_8bit(A,B)
    elif opcode==[False,True,False]:
        return add_8bit(A,B,sub=True)
    elif opcode==[False,True,True]:
        return nand_8bit(A,B)
    elif opcode==[True,False,False]:
        return nor_8bit(A,B)
    elif opcode==[True,False,True]:
        return xor_8bit(A,B)
    elif opcode==[True,True,False]:
        return shr(A)
    elif opcode==[True,True,True]:
        return shl(A)
if __name__=="__main__":
    A=to_stream(int(input("Enter first number: ")))
    B=to_stream(int(input("Enter second number: ")))
    opcode=to_stream(int(input("Enter opcode: ")),3)
    print("Output: ", to_num(alu(A,B,opcode),8,True))