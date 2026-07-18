ldi r1 1        ; constant 1
ldi r2 0        ; address
ldi r3 100      ; limit

fill:
store r2 r2     ; MEM[r2] = r2
display r2
add r2 r2 r1    ; address++
sub r0 r3 r2
jc Z read
jump fill

read:
sub r2 r2 r1    ; r2 = 99

disp:
load r4 r2      ; r4 = MEM[r2]
display r4

sub r2 r2 r1    ; r2--
jc N end
jump disp

end:
halt