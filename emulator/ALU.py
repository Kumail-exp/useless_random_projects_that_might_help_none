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


if __name__=="__main__":
    A=to_stream(int(input("Enter first number: ")))
    B=to_stream(int(input("Enter second number: ")))
    sub=bool(int(input("Enter 1 for subtraction, 0 for addition: ")))
    out=add_8bit(A,B,sub)
    print("Output: ",to_num(out,two_complement=True))
