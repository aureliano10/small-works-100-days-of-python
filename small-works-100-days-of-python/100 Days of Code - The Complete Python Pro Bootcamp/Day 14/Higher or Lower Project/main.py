import random
import art
import game_data

#diccionario de personas hay 50

def random_person():
    random_number = random.randint(0, 49)
    return game_data.data[random_number]


person_1 = random_person()
person_2 = random_person()

while person_1["name"] == person_2["name"]:
    person_2 = random_person()

#hasta aqui elegi dos personas y me aseguro de que no sean las mismas

def compare_followers(followers_1, followers_2):
    if followers_1["follower_count"] > followers_2["follower_count"]:
        return "a"
    else:
        return "b"


score = 0
stop_game = False
while not stop_game:
    print(art.logo)
    if score > 0:
        print(f"You're right, current score: {score}")
    print(f"Compare A: {person_1["name"]}, a {person_1["description"]}, from {person_1["country"]}")
    print(art.vs)
    print(f"Against B: {person_2["name"]}, a {person_2["description"]}, from {person_2["country"]}")

    user_answer = input("Who has more followers?, Type 'A' or 'B': ").lower()
    if user_answer == compare_followers(person_1, person_2):
        score += 1
        person_1 = person_2
        person_2 = random_person()
        print("\n" * 20)
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        stop_game = True

