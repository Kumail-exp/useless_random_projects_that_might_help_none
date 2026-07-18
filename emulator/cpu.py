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


    def execute(self,instruction:list[bool]):
        # print(instruction)
        opcode = instruction[:4]
        r1 = instruction[4:8]
        r2 = instruction[8:12]
        r3 = instruction[12:16]
        extra=instruction[8:16]
        ocn=to_num(opcode)
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
    cpu = CPU([
        [1,0,0,0,  0,0,0,1, 0,0,0,0,0,1,1,1],
        [1,0,0,1,  0,0,0,1, 0,0,0,0,0,0,0,0],
        [1,0,1,0,  0,0,0,0, 0,0,0,0,0,0,0,1],
        
    ])

    cpu.start()