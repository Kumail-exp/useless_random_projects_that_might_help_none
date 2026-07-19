import time
from assembler import read
from gates import *
from IC import *
from regfile import *
from ALU import *
import random
import pyautogui
from pynput.keyboard import Key, KeyCode
from pynput import keyboard
import pygame
width, height = pyautogui.size() #will need this later
x_fact=width//255
y_fact=width//255
pressed = set() 

def on_press(key):
    pressed.add(key)

def on_release(key):
    pressed.discard(key)

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)
listener.start()

instructions = []
class Display:
    def __init__(self, scale=2):
        self.width = 255
        self.height = 255
        self.scale = scale

        pygame.init()

        self.window = pygame.display.set_mode(
            (self.width * scale, self.height * scale)
        )

        pygame.display.set_caption("SHARK-8 Display")

        self.screen = [
            [255 for _ in range(self.width)]
            for _ in range(self.height)
        ]

        self.running = True

    def set_pixel(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.screen[y][x] = max(0, min(255, value))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        for y in range(self.height):
            for x in range(self.width):
                c = self.screen[y][x]

                pygame.draw.rect(
                    self.window,
                    (c, c, c),
                    (
                        x * self.scale,
                        y * self.scale,
                        self.scale,
                        self.scale
                    )
                )

        pygame.display.flip()

    def clear(self, value=255):
        for y in range(self.height):
            for x in range(self.width):
                self.screen[y][x] = value

    def close(self):
        pygame.quit()


class CPU:
    def __init__(self,program:list[list[bool]]):
        self.reg = REG()
        self.pc:int=0
        self.programm=program
        self.running=True
        self.alu=ALU()
        self.memory = [[False] * 8 for _ in range(256)]
        self.disp=Display()

    def map_mem(self):
        def pack(*k):
            return to_stream(
                sum((1 << i) for i, key in enumerate(k) if key in pressed),
                8
            )


        self.memory[246] = to_stream(random.randint(0, 255), 8)

        self.memory[247] = pack(
            KeyCode.from_char('z'),
            KeyCode.from_char('1'),
            KeyCode.from_char('2'),
            KeyCode.from_char('3'),
            KeyCode.from_char('4'),
            KeyCode.from_char('5'),
            KeyCode.from_char('6'),
            KeyCode.from_char('7'),
        )

        self.memory[248] = pack(
            KeyCode.from_char('8'),
            KeyCode.from_char('9'),
            KeyCode.from_char('q'),
            KeyCode.from_char('w'),
            KeyCode.from_char('e'),
            KeyCode.from_char('r'),
            KeyCode.from_char('t'),
            KeyCode.from_char('y'),
        )

        self.memory[249] = pack(
            KeyCode.from_char('u'),
            KeyCode.from_char('i'),
            KeyCode.from_char('o'),
            KeyCode.from_char('p'),
            KeyCode.from_char('a'),
            KeyCode.from_char('s'),
            KeyCode.from_char('d'),
            KeyCode.from_char('f'),
        )

        self.memory[250] = pack(
            KeyCode.from_char('g'),
            KeyCode.from_char('h'),
            KeyCode.from_char('j'),
            KeyCode.from_char('k'),
            KeyCode.from_char('l'),
            KeyCode.from_char('z'),
            KeyCode.from_char('x'),
            KeyCode.from_char('c'),
        )

        self.memory[251] = pack(
            KeyCode.from_char('v'),
            KeyCode.from_char('b'),
            KeyCode.from_char('n'),
            KeyCode.from_char('m'),
            KeyCode.from_char(','),
            KeyCode.from_char('.'),
            KeyCode.from_char('/'),
            KeyCode.from_char(';'),
        )

        self.memory[252] = pack(
            Key.up,
            Key.down,
            Key.left,
            Key.right,
            Key.space,
            Key.ctrl_l if Key.ctrl_l in pressed else Key.ctrl_r,
            Key.shift_l if Key.shift_l in pressed else Key.shift_r,
            Key.alt_l if Key.alt_l in pressed else Key.alt_r,
        )

        self.memory[253] = to_stream(int(time.time()) & 0xFF, 8)

        x, y = pyautogui.position()
        mx = x * 255 // (width - 1)
        my = y * 255 // (height - 1)
        self.memory[254] = to_stream(mx, 8)
        self.memory[255] = to_stream(my, 8)

    def execute(self,instruction:list[bool]):
        self.map_mem()
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
        self.updating_IO()
        return self.pc+1
    def updating_IO(self):
        color = to_num(self.memory[243])
        x = to_num(self.memory[244])
        y = to_num(self.memory[245])

        self.disp.set_pixel(x, y, color)
        self.disp.update()
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