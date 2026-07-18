#loading vaues
ldi r1 1
ldi r2 0
ldi r5 100

#mainloop
loop:
add r3 r1 r2
pass r1 r2
pass r2 r3
display r3
sub r4 r5 r3
jc Z end
#if already reached negative then we are above hundres so end it all
jump loop
end:
halt