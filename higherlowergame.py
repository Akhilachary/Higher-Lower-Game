# print("hare krishna Radhe Radhe")
# print("jai jaganath")
# print("Sai ram")


import random
import logoss
import database

def game(val,val2,score):
    chce = int(input("Who has more followers type '1' or '2': "))
    if chce == 1:
        if val['followers'] > val2['followers']:
            score += 1
            print(f"You are right. Your score is {score}")
            return True,score

        else:
            print(f'You are wrong.. Your final score is {score}')
            return False,score
    elif chce == 2:
        if val['followers'] < val2['followers']:
            score += 1
            print(f"You are right. Your score is {score}")
            return True,score

        else:
            print(f'You are wrong.. Your final score is {score}')
            return False,score


winner=True
score=0
while (winner):
    print(logoss.logo)
    val = random.choice(database.data)
    # fomat=random.choice(f"{}")
    val2 = random.choice(database.data)
    while val==val2:
        val2=random.choice(database.data)
    print(f"Compare 1: {val['name']}, a {val['description']}, from {val['country']}")
    print(logoss.vs)
    print(f"Compare 2: {val2['name']}, a {val2['description']}, from {val2['country']}")
    winner,score=game(val,val2,score)


