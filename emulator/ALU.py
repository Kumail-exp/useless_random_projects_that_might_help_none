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

class Flags:
    def __init__(self):
        self.zero = False
        self.negative = False
        self.carry = False
        self.overflow = False
    def get(self,adress:int):
        match(adress):
            case 0:
                return self.zero
            case 1:
                return self.negative
            case 2:
                return self.carry
            case 3:
                return self.overflow
            case _:
                raise ValueError("Invalid address for flags")

class ALU:
    def __init__(self):
        self.flags = Flags()

    def add_8bit(self, A, B, sub=False):
        output = [False] * 8
        carry = sub

        carry_into_msb = False

        for i in range(7, -1, -1):
            if i == 0:
                carry_into_msb = carry
            output[i], carry = Full_Adder(A[i], XOR(B[i], sub), carry)

        carry_out = carry
        overflow = XOR(carry_into_msb, carry_out)

        return output, carry_out, overflow

    def nand_8bit(self, A, B):
        return [NAND(a, b) for a, b in zip(A, B)]

    def nor_8bit(self, A, B):
        return [NOR(a, b) for a, b in zip(A, B)]

    def xor_8bit(self, A, B):
        return [XOR(a, b) for a, b in zip(A, B)]

    def shr(self, A):
        out = [False] * 8
        for i in range(7):
            out[i + 1] = A[i]
        return out

    def shl(self, A):
        out = [False] * 8
        for i in range(7):
            out[i] = A[i + 1]
        return out

    def no_op(self, A):
        # sry for names but no op is basically pass
        return A.copy()

    def update_flags(self, result, carry=False, overflow=False):
        self.flags.zero = not any(result)
        self.flags.negative = result[0]
        self.flags.carry = carry
        self.flags.overflow = overflow

    def     execute(self, A, B, opcode):
        op = to_num(opcode, 3)

        carry = False
        overflow = False

        match op:
            case 0:
                result = self.no_op(A)

            case 1:
                result, carry, overflow = self.add_8bit(A, B)

            case 2:
                result, carry, overflow = self.add_8bit(A, B, sub=True)

            case 3:
                result = self.nand_8bit(A, B)

            case 4:
                result = self.nor_8bit(A, B)

            case 5:
                result = self.xor_8bit(A, B)

            case 6:
                result = self.shr(A)

            case 7:
                result = self.shl(A)

            case _:
                raise ValueError("Invalid opcode")

        self.update_flags(result, carry, overflow)
        return result
    def get_flags(self,adress:int):
        return [self.flags.zero, self.flags.negative, self.flags.carry, self.flags.overflow][adress]
if __name__=="__main__":
    alu=ALU()
    A=to_stream(int(input("Enter first number: ")))
    B=to_stream(int(input("Enter second number: ")))
    opcode=to_stream(int(input("Enter opcode: ")),3)
    print("Output: ", to_num(alu.execute(A,B,opcode),8,True))