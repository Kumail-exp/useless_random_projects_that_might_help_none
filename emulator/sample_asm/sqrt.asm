#made by my friend Zamanat husain

ldi r1 49
ldi r2 1
ldi r3 0
ldi r4 2
ldi r5 1
while:
sub r1 r1 r2
add r2 r2 r4
add r3 r3 r5
add r1 r1 r0
jc z end
jc n end
jump while

end:
display r3
halt