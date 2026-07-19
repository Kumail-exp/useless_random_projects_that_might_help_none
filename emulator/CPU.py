from assembler import read
from gates import *
from IC import *
from regfile import *
from ALU import *

instructions = []



class CPU:
    def __init__(self,program:list[list[bool]]):
        self.reg = REG()
        self.pc:int=0
        self.programm=program
        self.running=True
        self.alu=ALU()
        self.memory = [[False] * 8 for _ in range(256)]


    def execute(self,instruction:list[bool]):
        # print(instruction)
        opcode = instruction[:4]
        r1 = instruction[4:8]
        r2 = instruction[8:12]
        r3 = instruction[12:16]
        extra=instruction[8:16]
        ocn=to_num(opcode)
        # print(
        #     f"PC={self.pc:02}",
        #     f"OP={to_num(opcode)}",
        #     f"R1={to_num(r1)}",
        #     f"R2={to_num(r2)}",
        #     f"R3={to_num(r3)}"
        #         ) for debugging reasons
        match(ocn):

            case 8:#ldi
                self.reg.write(r1, instruction[8:16], enable=True)
            case 9:#display
                self.display(r1)
            case 10:#jump
                return to_num(extra)
            case 11:#jc 
                if(self.alu.get_flags(to_num(r1))):
                    return to_num(extra)
            case 12:#store
                self.memory[to_num(self.reg.read(r1))]=self.reg.read(r2)
            case 13:#load
                self.reg.write(r1,self.memory[to_num(self.reg.read(r2))],enable=True)
            case 14:#cmp
                a = self.reg.read(r1)
                b = self.reg.read(r2)
                self.alu.execute(a, b, [False,True,False])  #using sub for comparison without storing the result
            case 15:#halt
                self.running=False

            case _:
                a = self.reg.read(r2)
                b = self.reg.read(r3)
                self.reg.write(r1, self.alu.execute(a, b, opcode[1:]), enable=True)
        return self.pc+1
    def start(self):
        while self.running:
            self.pc=self.execute(self.programm[self.pc])
            if(self.pc>=len(self.programm)):
                self.running=False
            
    def reset(self):
        self.pc=0
        self.running=True
    def display(self,adress:list[bool]):
        print(to_num(self.reg.read(adress)))

if __name__=="__main__":
    cpu = CPU(read())

    cpu.start()