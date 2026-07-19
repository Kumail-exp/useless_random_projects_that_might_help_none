ldi r1 243     # color port
ldi r2 244     # x port
ldi r3 245     # y port

ldi r4 254     # mouse x
ldi r5 255     # mouse y

loop:

    load r6 r4     # mouse x
    load r7 r5     # mouse y

    store r2 r6
    store r3 r7
    store r1 r0

    jump loop