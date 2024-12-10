import pygame
import os


# Constants
pygame.init()
FPS = 60
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 850
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
STARTING_POSTIONS = [ "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"]
MID_OF_SQUARES = [(37.5, 37.5),(112.5, 37.5),(187.5, 37.5),(262.5, 37.5),(337.5, 37.5),(412.5, 37.5),(487.5, 37.5),(562.5, 37.5),(37.5, 112.5),(112.5, 112.5),(187.5, 112.5),(262.5, 112.5),(337.5, 112.5),(412.5, 112.5),(487.5, 112.5),(562.5, 112.5),(37.5, 187.5),(112.5, 187.5),(187.5, 187.5),(262.5, 187.5),(337.5, 187.5),(412.5, 187.5),(487.5, 187.5),(562.5, 187.5),(37.5, 262.5),(112.5, 262.5),(187.5, 262.5),(262.5, 262.5),(337.5, 262.5),(412.5, 262.5),(487.5, 262.5),(562.5, 262.5),(37.5, 337.5),(112.5, 337.5),(187.5, 337.5),(262.5, 337.5),(337.5, 337.5),(412.5, 337.5),(487.5, 337.5),(562.5, 337.5),(37.5, 412.5),(112.5, 412.5),(187.5, 412.5),(262.5, 412.5),(337.5, 412.5),(412.5, 412.5),(487.5, 412.5),(562.5, 412.5),(37.5, 487.5),(112.5, 487.5),(187.5, 487.5),(262.5, 487.5),(337.5, 487.5),(412.5, 487.5),(487.5, 487.5),(562.5, 487.5),(37.5, 562.5),(112.5, 562.5),(187.5, 562.5),(262.5, 562.5),(337.5, 562.5),(412.5, 562.5),(487.5, 562.5),(562.5, 562.5)] 
SQUARE_SIZE = min(WINDOW_WIDTH // 2, WINDOW_HEIGHT) // 8
running = True

# Constants: Pieces # FOR SIZE CHANGE GO TO https://www.shutterstock.com/image-resizer?c3apidt=&gad_source=1&gclid=CjwKCAjwt-OwBhBnEiwAgwzrUgwi70N7tIRmT0xeUDt_DHljvXD5qifqYuvsM2rliDfAjuR8b78PWRoCKygQAvD_BwE&gclsrc=aw.ds&kw=
p = pygame.image.load("ChessPyGame Assets\\blackPawn.png")
P = pygame.image.load('ChessPyGame Assets\\whitePawn.png')
n = pygame.image.load('ChessPyGame Assets\\blackNight.png')
N = pygame.image.load('ChessPyGame Assets\\whiteNight.png')
b = pygame.image.load('ChessPyGame Assets\\blackBISHOP.png')
B = pygame.image.load('ChessPyGame Assets\\whiteBISHOP.png')
r = pygame.image.load('ChessPyGame Assets\\blackRook.png')
R = pygame.image.load('ChessPyGame Assets\\whiteRook.png')
q = pygame.image.load('ChessPyGame Assets\\blackQueen.png')
Q = pygame.image.load('ChessPyGame Assets\\whiteQueen.png')
k = pygame.image.load('ChessPyGame Assets\\blackKING.png')
K = pygame.image.load('ChessPyGame Assets\\whiteKING.png')

YELLOW_RECT = pygame.Rect(0, 0, 75, 75)
GREEN = (115, 149, 82)
WHITE = (235, 236, 208)

BOARD_WIDTH = 8 * SQUARE_SIZE
BOARD_HEIGHT = 8 * SQUARE_SIZE
BOARD_START_X = (WINDOW_WIDTH - BOARD_WIDTH) // 2
BOARD_START_Y = (WINDOW_HEIGHT - BOARD_HEIGHT) // 2

FONT = pygame.font.Font(None, 36)

def get_piece_from_square(square):
    return reverse_chessboard(current_Board)[square[1] * 8 + square[0]]

def get_square_from_mouse(pos):
    x, y = pos
    if BOARD_START_X <= x <= BOARD_START_X + BOARD_WIDTH and BOARD_START_Y <= y <= BOARD_START_Y + BOARD_HEIGHT:
        col = (x - BOARD_START_X) // SQUARE_SIZE
        row = (y - BOARD_START_Y) // SQUARE_SIZE
        row = 7 - (y - BOARD_START_Y) // SQUARE_SIZE  # Flip the row index

        return int(col), int(row)
    return None, None


def reverse_chessboard(chessboard):
    # Validate that the input is 64 elements long
    if len(chessboard) != 64:
        raise ValueError("The chessboard must have exactly 64 elements.")

    # Split the flat list into 8 rows
    rows = [chessboard[i:i+8] for i in range(0, len(chessboard), 8)]

    # Reverse the order of the rows
    revised_board = rows[::-1]

    # Flatten the revised board back into a 1D list
    flattened_board = [piece for row in revised_board for piece in row]

    return flattened_board


def fen_to_Chess_board(board):
    parts = board.split(' ')
    ChessBoard = []
    copy_board = parts[0]
    copy_board = [i for i in copy_board if i != '/']
    turn = parts[1]
    castles = parts[2]
    en_passant = parts[3]
    half_moves = parts[4]
    full_moves = parts[5]
    
    for notion in copy_board:
        if notion.isnumeric():
            for i in range(int(notion)):
                ChessBoard.append('0')
        else:
            ChessBoard.append(notion)
    return ChessBoard

def chess_board_pos_to_fen_pos(chess_board):
    fen, empty_count = '', 0
    for i in range(0, 64, 8):
        row = chess_board[i:i + 8]
        for piece in row:
            if piece == '0':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
                fen += piece
        if empty_count > 0:
            fen += str(empty_count)
            empty_count = 0
        fen += '/'
    return fen[:-1]


def DrawBoard(real_board):
    game_board = real_board.copy()
    WINDOW.fill("aqua")
    mouse_pos = pygame.mouse.get_pos()
    col, row = get_square_from_mouse(mouse_pos)
    # Update label with the current column and row
    col_row_text = f'cols and rows: {col+1}, {row+1}' if col is not None and row is not None else 'N/A'
    WINDOW.blit(FONT.render(f'Mouse pos: {mouse_pos}', True, "darkgray"), (WINDOW_WIDTH - 500, 0))
    WINDOW.blit(FONT.render(col_row_text, True, "darkgray"), (WINDOW_WIDTH - 300, 200))
    if type(selected_square) == tuple:
        WINDOW.blit(FONT.render(f'{get_piece_from_square(selected_square)}', True, "darkgray"), (WINDOW_WIDTH - 300, 300))


    for row in range(8):
        for col in range(8):
            square_number = row * 8 + col
            currentRect = BOARD_START_X + col * SQUARE_SIZE, BOARD_START_Y + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
            # Draw Squares
            
            if (row + col) % 2 == 0:  # Check if the square is even
                pygame.draw.rect(WINDOW, GREEN, currentRect)  # Draw a green square
            else:
                pygame.draw.rect(WINDOW, WHITE, currentRect)  # Draw a white square
            if selected_square != (None, None) and selected_square != None:
                if  selected_square[1] * 8 + selected_square[0] == (7 - row) * 8 + col:
                    pygame.draw.rect(WINDOW, "red", currentRect)    
            # Handle Pieces
            if game_board[square_number] != "0":
                piece_dict = {'K': K, 'k': k, 'P': P, "p": p, 'R': R, 'r': r, 'N': N, 'n': n, 'B': B, 'b': b, 'Q': Q, 'q': q}
                WINDOW.blit(piece_dict[game_board[square_number]], currentRect)

                
def MainGameLoop():
    global selected_square
    global current_Board
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    selected_square = (get_square_from_mouse(pygame.mouse.get_pos()))
                    
                


        DrawBoard(current_Board)  # Call the DrawBoard function to draw the chessboard
        pygame.display.flip()  # Update the display


# RUN THE GAME
current_Board = fen_to_Chess_board(STARTING_POSTIONS[0])
turn = 'w'
castles = "KQkq"
en_passant = "-"
half_moves = 0
full_moves = 1
selected_square = None 
MainGameLoop()


