

ori $s2,5
li $s1,5
li $t1,6
li $t3,2


slt $s3,$s2,$s1
beq $s3,$zero,else
add $t3,$t3,$t3
else:
addi $t1,$t1,1