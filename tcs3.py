age=[]

for i in range(0,5):
    n=int(input())
    if n=="":
        break
    elif n in range(0,120):
      age.append(n)
    else:
        print("invalid input")

total_income=0
for j in age:
   if j<17:
    total_income+=200
   elif j<40:
    total_income+=400
   else:
    total_income+=300
print(total_income)

