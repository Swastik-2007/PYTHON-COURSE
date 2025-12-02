import pickle

def add_game():
    """Add a new game to the binary file."""
    with open("Games.dat", "ab") as file:
        game_id = input("Enter game ID: ")
        name = input("Enter game name: ")
        genre = input("Enter game genre: ")
        price = float(input("Enter game price: "))
        
        record = {
            "GameID": game_id,
            "Name": name,
            "Genre": genre,
            "Price": price
        }
        pickle.dump(record, file)
        print("Game added successfully!\n")

def display_games():
    """Display all games from the binary file."""
    try:
        with open("Games.dat", "rb") as file:
            print("\nList of Games:")
            while True:
                record = pickle.load(file)
                print(record)
    except EOFError:
        pass
    except FileNotFoundError:
        print("\nNo games found. Add some games first.")

def search_game():
    """Search for a specific game by ID."""
    game_id = input("Enter game ID to search: ")
    found = False
    try:
        with open("Games.dat", "rb") as file:
            while True:
                record = pickle.load(file)
                if record["GameID"] == game_id:
                    print("\nGame Found:", record)
                    found = True
                    break
    except EOFError:
        if not found:
            print("\nGame not found.")
    except FileNotFoundError:
        print("\nNo games found. Add some games first.")
def main():
    while True:
        print("\nMenu:")
        print("1. Add Game")
        print("2. Display Games")
        print("3. Search Game")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_game()
        elif choice == '2':
            display_games()
        elif choice == '3':
            search_game()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
