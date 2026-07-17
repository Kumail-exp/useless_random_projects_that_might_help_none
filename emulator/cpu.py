from gates import *
from IC import *
from regfile import *
from ALU import *

instructions = []



class CPU:
    def __init__(self):
        self.reg = REG()
    def execute(self,instruction:list[bool]):
        # first 4 bit opcode(last one bit is reserve for future), then 4 bit write1, then 4 bit read1 then 4 bit read2
        opcode = instruction[:3]
        immediate = instruction[3]
        dest = instruction[4:8]

        if immediate:
            self.reg.write(dest, instruction[8:16], enable=True)
        else:
            a = self.reg.read(instruction[8:12])
            b = self.reg.read(instruction[12:16])
            self.reg.write(dest, alu(a, b, opcode), enable=True)
    def display(self,adress:list[bool]):
        print(to_num(self.reg.read(adress)))

if __name__=="__main__":
    cpu = CPU()

    # sample program to test the Cpu
    program = [
    [0,0,0,1, 0,0,0,1, 0,0,0,0,0,0,0,0],
    [0,0,0,1, 0,0,1,0, 0,0,0,0,0,0,0,1],
    [0,0,1,0, 0,0,1,1, 0,0,0,1,0,0,1,0],
    [0,0,1,0, 0,0,0,1, 0,0,1,0,0,0,1,1],
    [0,0,1,0, 0,0,1,0, 0,0,1,1,0,0,0,1],
    ]
    cpu.execute(program[0])
    cpu.execute(program[1])
    cpu.display(to_stream(1))
    cpu.display(to_stream(2))
    cpu.execute(program[2])
    cpu.display(to_stream(3))
    cpu.execute(program[3])
    cpu.display(to_stream(1))
    cpu.execute(program[4])
    cpu.display(to_stream(2)) 