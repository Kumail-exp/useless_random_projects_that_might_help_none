ldi r1 252      # Keyboard register
ldi r2 246      # RNG register
ldi r3 1

loop:
    load r4 r1

    shr r4 r4
    shr r4 r4
    shr r4 r4
    shr r4 r4

    cmp r4 r3
    jc z pressed
    jump loop

pressed:
    load r5 r2
    display r5

release:
    load r4 r1

    shr r4 r4
    shr r4 r4
    shr r4 r4
    shr r4 r4

    cmp r4 r3
    jc z release      # Stay here while Space is still held

    jump loop