# utility functions:
from IC import *


def reg_adress(addr:str):
    return int(addr[1:])%16

OPCODES={
    0:"pass",
    1:"add",
    2:"sub",
    3:"nand",
    4:"nor",
    5:"xor",
    6:"shr",
    7:"shl",
    8:'ldi',
    9:'display',
    10:'jump',
    11:'jc',
    12:'store',
    13:'load',
    14:'cmp',
    15:'halt'

}
opcode_to_bin={v:to_stream(k,4) for k,v in OPCODES.items()}
class ASM:
    def __init__(self,program:str):
        self.program=program.splitlines()
        self.instructions=[]
        self.labels={}
    def labelise(self):
        pc = 0
        for line in self.program:
            line = line.strip().lower()

            if line == "" or line.startswith("#") or line.startswith(";"):
                continue

            if line.endswith(":"):
                self.labels[line[:-1]] = pc
            else:
                pc += 1
    def assemble(self):
        self.labelise()
        for i,line in enumerate(self.program):
            line=line.strip().lower()
            if line=="":
                continue
            if line.endswith(":"):
                continue
            if line.startswith("#") or line.startswith(";"):
                continue
            instruction=[]

            words=line.split()
            match words[0]:
                case "pass":
                    instruction=opcode_to_bin["pass"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+[False]*4
                case "add":
                    instruction=opcode_to_bin["add"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+to_stream(reg_adress(words[3]),4)
                case "sub":
                    instruction=opcode_to_bin["sub"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+to_stream(reg_adress(words[3]),4)
                
                case "nand":
                    instruction=opcode_to_bin["nand"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+to_stream(reg_adress(words[3]),4)
                
                case "nor":
                    instruction=opcode_to_bin["nor"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+to_stream(reg_adress(words[3]),4)
                case "xor":
                    instruction=opcode_to_bin["xor"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+to_stream(reg_adress(words[3]),4)
                case "shr":
                    instruction=opcode_to_bin["shr"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+[False]*4
                case "shl":
                    instruction=opcode_to_bin["shl"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+[False]*4
                case "ldi":
                    instruction=opcode_to_bin["ldi"]+to_stream(reg_adress(words[1]),4)+to_stream(int(words[2]),8)
                case "display":
                    instruction=opcode_to_bin["display"]+to_stream(reg_adress(words[1]),4)+[False]*8
                case "jump":
                    address=(to_stream(self.labels[words[1]],8)) if words[1] in self.labels else to_stream(int(words[1]),8)
                    instruction=opcode_to_bin["jump"]+[False]*4+address
                case "jc":
                    address=(to_stream(self.labels[words[2]],8)) if words[2] in self.labels else to_stream(int(words[2]),8)
                    instruction=opcode_to_bin["jc"]+to_stream({"z":0,"n":1,"c":2,"v":3}[words[1]],4)+address
                case "store":
                    instruction=opcode_to_bin["store"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+[False]*4
                case "load":
                    instruction=opcode_to_bin["load"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+[False]*4
                case "cmp":
                    instruction=opcode_to_bin["cmp"]+to_stream(reg_adress(words[1]),4)+to_stream(reg_adress(words[2]),4)+[False]*4
                case "halt":
                    instruction=opcode_to_bin["halt"]+[False]*12

                case _:
                    raise ValueError(f"Unknown instruction: {words[0]}")
            self.instructions.append(instruction)
            
                
def read():
    import sys
    with open(sys.argv[1]) as f:
        asm = ASM(f.read())
        asm.assemble()
        # for i, ins in enumerate(asm.instructions):
        #     print(i, to_num(ins[:4]))
        return asm.instructions