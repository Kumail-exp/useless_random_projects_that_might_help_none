from gates import *
from IC import *

class REG:
    def __init__(self):
        self.regs=[Register(8) for i in range(16)]
    def read(self,adress:list[bool]):
        return self.regs[to_num(adress)].read()
    def write(self,adress:list[bool],value:list[bool],enable=True):
        self.regs[to_num(adress)].load(value)