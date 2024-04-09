test_grade = int(input("enter your test grade: "))
homework_avg = int(input("enter your homework average: "))
homework_count = int(input("how many assignments did you submit? "))
final_grade = test_grade  # sets the final grade as the test grade, a lot of the times the homework average won't count

if homework_count <= 4:
    final_grade = 0
elif homework_count <= 6:
    if test_grade >= 55:
        final_grade = test_grade * 0.8 + homework_avg * 0.2
elif homework_avg > test_grade:
    if test_grade <= 54:
        if homework_avg >= 80:
            final_grade = test_grade * 0.75 + homework_avg * 0.25
        else:
            final_grade = test_grade * 0.8 + homework_avg * 0.2
    else:
        final_grade = test_grade * 0.7 + homework_avg * 0.3

print(f"your final grade is {final_grade}")
