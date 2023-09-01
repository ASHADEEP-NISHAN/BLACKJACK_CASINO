logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print("\n")
print("WELLCOME TO ASHADEEP'S CASINO\n\n")
play_again=True
while play_again==True:
    a = input("If You Want To Play BLACKJACK Type 'y' else 'n'\n").lower()
    if a == 'y':
        print(logo)
    else:
        exit()
    money = int(input("HOW MUCH MONEY YOU WANT TO BET:\n"))
    import random as r
    card_dec = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    c1 = r.choice(card_dec)
    c2 = r.choice(card_dec)
    player_cards.append(c1)
    player_cards.append(c2)
    current_score = sum(player_cards)
    comp1 = r.choice(card_dec)
    computer_choice = []
    computer_choice.append(comp1)
    comp_2=r.choice(card_dec)
    computer_choice.append(comp_2)
    if current_score ==21:
        print("YOU WON\nYOU GOT A BLACKJACK")
        print(f"your Final Hand:{player_cards} and Final score: {current_score}")
        print(f"Computer's Final Hand: {computer_choice} And Final Score: {sum(computer_choice)}")
        exit()
    elif sum(computer_choice)==21:
        print("COMPUTER GOT A BLACKJACK\nYOU LOSE")
        print(f"your Final Hand:{player_cards} and Final score: {current_score}")
        print(f"Computer's Final Hand: {computer_choice} And Final Score: {sum(computer_choice)}")
        exit()
    elif current_score ==21 and sum(computer_choice)==21:
        print("USE AND COMPUTER BOTH GET BLACKJACK\nMATCH DRAW")
    print(f"your cards:{player_cards} and current score: {current_score}")
    print(f"Computer's first card:{comp1}")
    check = True
    while check == True:
        next_card = input("Type 'y' to get another card and 'n' to pass\n").lower()
        if next_card == 'y':
            c3 = r.choice(card_dec)
            player_cards.append(c3)
            current_score1 = sum(player_cards)
            if current_score1 > 21 and c3 == 11:
                player_cards.remove(c3)
                player_cards.append(1)
                print(f"your cards:{player_cards} and current score: {current_score1}")
                print(f"Computer's first card:{comp1}")
            elif current_score1 > 21:
                print(f"your Final Hand:{player_cards} and Final score: {current_score1}")
                print(f"Computer's Final Hand: {computer_choice} And Final Score: {sum(computer_choice)}")
                print("YOU WENT OVER.YOU LOSE")
                print("TOTAL MONEY YOU WON",money*0)
                exit()
            else:
                print(f"your cards:{player_cards} and current score: {current_score1}")
                print(f"Computer's first card:{comp1}")
        else:
            check = False
    sum_comp = sum(computer_choice)
    while sum_comp < 17:
        comp3 = r.choice(card_dec)
        computer_choice.append(comp3)
        sum_comp = sum(computer_choice)
    z = sum(player_cards)
    print(f"your Final Hand:{player_cards} and Final score: {z}")
    print(f"Computer's Final Hand: {computer_choice} And Final Scorre: {sum_comp}")
    def check_win():
        if z > 21:
            print("YOU WENT OVER.YOU LOSE 😢")
            print("TOTAL MONEY YOU WON RS:",money*0)
        elif z <= 21 and z > sum_comp:
            print("YOU WON 😁")
            print("TOTAL MONEY YOU WON RS:",money * 2)
        elif z < 21 and sum_comp > 21:
            print("YOU WON.COMPUTER WENT OVER 😁")
            print("TOTAL MONEY YOU WON RS:",money * 2)
        elif z < 21 and z < sum_comp:
            print("YOU LOSE.COMPUTER WON 🤨")
            print("TOTAL MONEY YOU WON RS:",money * 0)
        elif z == sum_comp:
            print("MATCH DRAW 🙃")
            print("TOTAL MONEY YOU WON RS:",money)
    check_win()
    x=input("Do You Want To Play Again; type y / n\n").lower()
    if x != 'y':
        play_again = False