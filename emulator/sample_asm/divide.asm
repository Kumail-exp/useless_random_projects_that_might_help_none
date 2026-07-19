ldi r1 51
ldi r2 17
ldi r3 0
ldi r4 1

loop:
add r3 r4 r3
sub r1 r1 r2
jc z end
jc n end
jump loop
end:
display r3
halt