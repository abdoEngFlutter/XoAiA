from collections import deque
from time import perf_counter

HUMAN = "X"
AI = "O"
EMPTY = " "

WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def print_board(board):
    print("\n" + "=" * 25)
    for row in range(3):
        cells = []
        for col in range(3):
            index = row * 3 + col
            value = board[index]
            cells.append(value if value != EMPTY else str(index + 1))
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")
    print("=" * 25)


def get_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return get_winner(board) is None and EMPTY not in board


def available_moves(board):
    return [i for i, value in enumerate(board) if value == EMPTY]


def make_move(board, index, player):
    new_board = list(board)
    new_board[index] = player
    return tuple(new_board)


def bfs_search(board):
    """Explore game states with BFS and score possible AI moves."""
    legal_moves = available_moves(board)
    if not legal_moves:
        return None, 0, 0.0

    start_time = perf_counter()
    queue = deque()
    results = {
        move: {"wins": 0, "draws": 0, "losses": 0}
        for move in legal_moves
    }

    for move in legal_moves:
        next_board = make_move(board, move, AI)
        queue.append((next_board, HUMAN, move))

    explored = 0
    while queue:
        current_board, turn, first_move = queue.popleft()
        explored += 1
        winner = get_winner(current_board)
        if winner == AI:
            results[first_move]["wins"] += 1
            continue
        if winner == HUMAN:
            results[first_move]["losses"] += 1
            continue
        if is_draw(current_board):
            results[first_move]["draws"] += 1
            continue

        next_player = AI if turn == HUMAN else HUMAN
        for move in available_moves(current_board):
            next_board = make_move(current_board, move, turn)
            queue.append((next_board, next_player, first_move))

    for move in legal_moves:
        test_board = make_move(board, move, AI)
        if get_winner(test_board) == AI:
            elapsed = (perf_counter() - start_time) * 1000
            return move, explored, elapsed

    for move in legal_moves:
        test_board = make_move(board, move, HUMAN)
        if get_winner(test_board) == HUMAN:
            elapsed = (perf_counter() - start_time) * 1000
            return move, explored, elapsed

    def evaluate(move):
        data = results[move]
        wins, draws, losses = data["wins"], data["draws"], data["losses"]
        total = wins + draws + losses
        score = (wins - losses) / total
        draw_rate = draws / total
        center = 1 if move == 4 else 0
        corner = 1 if move in (0, 2, 6, 8) else 0
        return (score, draw_rate, center, corner, -move)

    best_move = max(legal_moves, key=evaluate)
    elapsed = (perf_counter() - start_time) * 1000
    return best_move, explored, elapsed


def human_turn(board):
    while True:
        try:
            move = int(input("\nChoose position (1-9): "))
            if move < 1 or move > 9:
                print("Please choose a number from 1 to 9.")
                continue
            index = move - 1
            if board[index] != EMPTY:
                print("This position is already occupied.")
                continue
            return index
        except ValueError:
            print("Invalid input. Enter a number.")


def play_game():
    board = tuple([EMPTY] * 9)
    print("\n================================")
    print("       XO SEARCH ARENA")
    print("       HUMAN VS BFS AI")
    print("================================")
    print("You are X | Computer is O")
    print("Choose a position from 1 to 9.")

    while True:
        print_board(board)
        move = human_turn(board)
        board = make_move(board, move, HUMAN)
        if get_winner(board) == HUMAN:
            print_board(board)
            print("\nCongratulations! You win!")
            break
        if is_draw(board):
            print_board(board)
            print("\nGame ended in a draw!")
            break

        print("\nAI is searching using BFS...")
        ai_move, explored, elapsed = bfs_search(board)
        board = make_move(board, ai_move, AI)
        print(f"AI selected position: {ai_move + 1}")
        print(f"Explored states: {explored}")
        print(f"Search time: {elapsed:.3f} ms")
        if get_winner(board) == AI:
            print_board(board)
            print("\nAI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("\nGame ended in a draw!")
            break


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing XO Search Arena!")
            break


if __name__ == "__main__":
    main()
