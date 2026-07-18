ldi r1 6
ldi r2 7
ldi r3 0
ldi r4 1
ldi r5 0

loop:
add r3 r3 r1
add r5 r5 r4

sub r6 r5 r2
jc Z end

jump loop

end:
display r3
halt