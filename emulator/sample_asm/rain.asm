ldi r1 243     # color port
ldi r2 244     # x port
ldi r3 245     # y port
ldi r4 246     # RNG

loop:
    load r5 r4     # color
    load r6 r4     # x
    load r7 r4     # y

    store r2 r6
    store r3 r7
    store r1 r5

    jump loop