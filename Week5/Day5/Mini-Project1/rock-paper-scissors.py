from ast import While
import game as g

results = {'You win!': 0, 'Computer win!': 0, 'Draw':0}

def get_user_menu_choice():
    users_choise = input("""
    Menu:
    (g) Play a new game
    (x) Show scores and exit
    Your choice: """)
    if users_choise == 'g' or users_choise == 'x':
        return users_choise
    else: 
        print('Invalid')
        return get_user_menu_choice()

    


def print_results(results):
    print(f"""
    Game Results:
     You won {results['You win!']} times
     You lose {results['Computer win!']} times
     You drew {results['Draw']} times

    Thank you for playing!
    """)
    

def main(results):
    game = g.Game()
    while True:
        choice = get_user_menu_choice()
        if choice == 'g':
            game.play(results)
        elif choice == 'x':
            print_results(results)
            break


main(results)