bagrut_avg = int(input("enter your bagrut average: "))
psycho = int(input("enter your psychometric grade: "))
psycho_quant = int(input("enter your psychometric quantitative grade: "))
psycho_eng = int(input("enter your psychometric english grade: "))
calculated = psycho * 0.8 + bagrut_avg / 1.2

if bagrut_avg >= 102:
    message = "you are accepted!"
elif psycho >= 700 and psycho_quant >= 145 and psycho_eng >= 120:
    message = "you are accepted!"
elif calculated >= 600:
    message = "you are accepted!"
else:
    message = "you are not accepted"
print(message)
