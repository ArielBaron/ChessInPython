import pygame
import os


def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')


def reverse_board(board):
    reversed_board = "/".join(reversed(board.split("/")))
    return reversed_board


def fen_to_Chess_board(fen_notion):
    ChessBoard = []
    fen_notion = fen_notion.split(' ')[0]
    fen_notion = [i for i in fen_notion if i != '/']
    for notion in fen_notion:
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
    window.fill("white")
    board_width = 8 * square_size
    board_height = 8 * square_size
    board_x = (window_width - board_width) // 2
    board_y = (window_height - board_height) // 2
    
    for row in range(8):
        for col in range(8):
            square_number = row*8+col
            # Draw Squares
            if (row + col) % 2 == 0:  # Check if the square is even
                pygame.draw.rect(window, (115, 149, 82), (board_x + col * square_size, board_y + row * square_size, square_size, square_size))  # Draw a gray square
            else:
                pygame.draw.rect(window, (235, 236, 208), (board_x + col * square_size, board_y + row * square_size, square_size, square_size))  # Draw a white square
            # Handle Pieces
            if game_board[square_number] != "0":
                piece_dict = {'K':K,'k':k,'P':P,"p":p,'R':R,'r':r,'N':N,'n':n,'B':B,'b':b,'Q':Q,'q':q}
                window.blit(piece_dict[game_board[square_number]],(board_x + col * square_size, board_y + row * square_size))
def MainGameLoop():
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        DrawBoard(Current_Board)  # Call the DrawBoard function to draw the chessboard
        pygame.display.flip()  # Update the display

# Constants
pygame.init()
FPS = 60
window_width = 1535
window_height = 863
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True
Starting_postion =[ "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1","r1bqkbnr/pnnppnkp/8/k2nnQ2/3P1P1k/1k5n/PPk1PPPP/RnBQKBNR w KQ - 0 1"]
Current_Board = fen_to_Chess_board(chess_board_pos_to_fen_pos(fen_to_Chess_board(Starting_postion[1])))
The_Middle_of_all_squares = [(37.5, 37.5),(112.5, 37.5),(187.5, 37.5),(262.5, 37.5),(337.5, 37.5),(412.5, 37.5),(487.5, 37.5),(562.5, 37.5),(37.5, 112.5),(112.5, 112.5),(187.5, 112.5),(262.5, 112.5),(337.5, 112.5),(412.5, 112.5),(487.5, 112.5),(562.5, 112.5),(37.5, 187.5),(112.5, 187.5),(187.5, 187.5),(262.5, 187.5),(337.5, 187.5),(412.5, 187.5),(487.5, 187.5),(562.5, 187.5),(37.5, 262.5),(112.5, 262.5),(187.5, 262.5),(262.5, 262.5),(337.5, 262.5),(412.5, 262.5),(487.5, 262.5),(562.5, 262.5),(37.5, 337.5),(112.5, 337.5),(187.5, 337.5),(262.5, 337.5),(337.5, 337.5),(412.5, 337.5),(487.5, 337.5),(562.5, 337.5),(37.5, 412.5),(112.5, 412.5),(187.5, 412.5),(262.5, 412.5),(337.5, 412.5),(412.5, 412.5),(487.5, 412.5),(562.5, 412.5),(37.5, 487.5),(112.5, 487.5),(187.5, 487.5),(262.5, 487.5),(337.5, 487.5),(412.5, 487.5),(487.5, 487.5),(562.5, 487.5),(37.5, 562.5),(112.5, 562.5),(187.5, 562.5),(262.5, 562.5),(337.5, 562.5),(412.5, 562.5),(487.5, 562.5),(562.5, 562.5)] 
#  Constants: Calculate square size
square_size = min(window_width // 2, window_height) // 8

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

#Constants: Selection Rect
yellow_rect = pygame.Rect(0, 0, 75, 75)


# RUN THE GAME
MainGameLoop()
# EXIT
clear_terminal()
pygame.quit()
exit()
