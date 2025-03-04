import random
import time

operators = ["+","-","*"]
min_operand = int(input("İstediğiniz aralıkta ki en düşük sayıyı giriniz ="))
max_operand = int(input("İstediğiniz aralıkta ki en yüksek sayıyı giriniz ="))
total_problems = 3

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)
    ques = str(left) + " " + operator + " " + str(right)
    answer = eval(ques)
    return ques, answer

start_time = time.time()

wrong = 0
input("Hazırsanız başlamak için enter'a basın.")
print("...................................")

for i in range(total_problems):
    ques, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i+1) + ":   " + ques + " =")
        if guess == str(answer):
            break
        
        wrong +=1
        
end_time = time.time()
total_time = round(end_time - start_time,2)

print("................................")
print("Yarışma bitti,", total_time, "saniye")