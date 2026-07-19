ldi r1 253
ldi r2 0
load r5 r1 #starting time
loop:
pass r3 r2
load r2 r1
cmp r3 r2
jc z loop
sub r6 r2 r5
display r6
jump loop