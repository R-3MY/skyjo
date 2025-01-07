import random

def main():
    # Number of each card in the deck
    cards = {
        -2 : 5,
        -1 : 10,
        0 : 15,
        1 : 10,
        2 : 10,
        3 : 10,
        4 : 10,
        5 : 10,
        6 : 10,
        7 : 10,
        8 : 10,
        9 : 10,
        10 : 10,
        11 : 10,
        12 : 10,
    }
    
    # Number of rows and columns of the game board of each player
    rows = 3
    cols = 4

    # Randomize the deck
    deck = randomize_deck(cards)

    # Deal the cards to the players
    player1, deck = player_board(deck, rows, cols)
    player2, deck = player_board(deck, rows, cols)

    # print("Player 1's hand: ", player1)
    # print("Player 2's hand: ", player2)

    # print("Deck: ", deck)
    print_board(player1)


def player_board(deck, rows, cols):
    # Deal the cards to the player
    board = deck[:rows*cols]
    board = [board[i:i+4] for i in range(0, len(board), 4)]
    deck = deck[rows*cols:]
    return board, deck

def randomize_deck(cards):
    # Randomize the deck
    deck = []
    for card in cards:
        deck += [card] * cards[card]
    random.shuffle(deck)
    return deck

def print_board(board):
    print("x" + "====x" * len(board[0]))
    for row in board:
        for card in row:
            print("|", f"{card:2}", end=" ")
        print("|\r")
    print("x" + "====x" * len(board[0]))

main()