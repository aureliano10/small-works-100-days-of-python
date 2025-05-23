import art
import random



def deal_cards():
    '''carta al azar'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(lista):
    '''calcula una lista y devuelve el valor de la suma de una lista'''
    if sum(lista) == 21 and len(lista) == 2:
        return 0

    if 11 in lista and lista > 21:
        lista.remove(11)
        lista.append(1)

    return sum(lista)

def compare(u_score, c_score):
    if u_score == c_score:
        return  "It's a Draw"
    elif c_score == 0:
        return "computer Blackjack"
    elif u_score == 0:
        return "User Blackjack"
    elif u_score > 21:
        return "Lose, you waent over"
    elif c_score > 21:
        return "Win, computer's went over"
    elif u_score > c_score:
        return "You win"
    else:
        return "computer's win"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False


    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}, current score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)


    print(f"You final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack?, type 'y' or 'n'\n") == "y":
    print("\n" * 20)
    play_game()