
print("Welcome to the Love Calculator!")
print("Please enter both names")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1n2=name1+name2

t= n1n2.count("t")
r= n1n2.count("r")
u= n1n2.count("u")
e= n1n2.count("e")
true= str(t+r+u+e)

l= n1n2.count("l")
o= n1n2.count("o")
v= n1n2.count("v")
e= n1n2.count("e")
love= str(l+o+v+e)

score= love+true
print(f"score is {score}")
score_int= int(score)

if (score_int >90) or (score_int <10):
  print(f"your score is {score} u gus are in peek")
elif score_int >39 and score_int <51:
  print(f"u guys are good in relation")
else:
  print(f"score is {score_int}")