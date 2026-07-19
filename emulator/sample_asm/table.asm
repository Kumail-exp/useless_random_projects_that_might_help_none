ldi r1 5 #modify this to change the table
ldi r2 0
ldi r3 1
ldi r4 11
ldi r5 1

loop:
add r2 r2 r1
display r2
add r3 r3 r5
cmp r4 r3
jc z end
jump loop
end:
halt
