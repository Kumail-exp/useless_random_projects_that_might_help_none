ldi r1 7
ldi r3 1
sub r2 r1 r3
pass r4 r1
loop:
add r1 r1 r4
sub r2 r2 r3
jc z end
jump loop
end:
display r1
halt