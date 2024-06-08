############
# HW2 Q1
#Copy WORD array into BYTE array. if number is too big write 0xFF in byte array
############
.data
Warray: .WORD 2,234,345,8,77,134,78
Barray: .SPACE 8
.text
.globl main
main: # main program entry
#$t0=loop counter; $t1=number from array; $a0=address of Warray; $a1=address of Barray;
#use other $t.. registers if needed
#your code'
loop:
	beq $t0,8,end
	lw $t1,Warray($a0)
	slti $t2,$t1,255
	beq $t2,1,less_then_byte
	li $t1,0xFF
	less_then_byte:
	sw $t1, Barray($a0)
	addi $t0,$t0,1
	addi $a0,$a0,4
	j loop
	
end: 



