import pygame

class ChessGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 1024))
        pygame.display.set_caption("PyChess")
        self.colors = [pygame.Color("white"), pygame.Color("gray")]
        self.square_size = 128
        self.piece_images = {
            'P': pygame.image.load("assets/w_pawn.png"),
            'R': pygame.image.load("assets/w_rook.png"),
            'N': pygame.image.load("assets/w_knight.png"),
            'B': pygame.image.load("assets/w_bishop.png"),
            'Q': pygame.image.load("assets/w_queen.png"),
            'K': pygame.image.load("assets/w_king.png"),
            'p': pygame.image.load("assets/b_pawn.png"),
            'r': pygame.image.load("assets/b_rook.png"),
            'n': pygame.image.load("assets/b_knight.png"),
            'b': pygame.image.load("assets/b_bishop.png"),
            'q': pygame.image.load("assets/b_queen.png"),
            'k': pygame.image.load("assets/b_king.png"),
        }

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = self.colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(256 + col * self.square_size, row * self.square_size, self.square_size, self.square_size))  # Décalage du plateau à droite

    def draw_pieces(self, board):
        for square, piece in board.piece_map().items():
            row = 7 - (square // 8)
            col = square % 8
            self.screen.blit(self.piece_images[piece.symbol()], (256 + col * self.square_size, row * self.square_size)) 

    def highlight_moves(self, legal_moves, selected_square):
        highlight_color = pygame.Color("blue")
        for move in legal_moves:
            if move.from_square == selected_square:
                to_square = move.to_square
                row = 7 - (to_square // 8)
                col = to_square % 8
                pygame.draw.rect(self.screen, highlight_color, pygame.Rect(256 + col * self.square_size, row * self.square_size, self.square_size, self.square_size), 5)

    def display_turn(self, turn):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Turn: {'White' if turn else 'Black '}", True, pygame.Color("white"), pygame.Color("black"))
        self.screen.blit(text, (10, 10))

    def display_captured_pieces(self, captured_pieces): # not use on purpose
        font = pygame.font.Font(None, 36)
        y_offset = 50
        for color, pieces in captured_pieces.items():
            text_lines = [pieces[:2]] + [pieces[i:i+5] for i in range(2, len(pieces), 5)] # The first group contains 2 elements, the others 5
            for line in text_lines:
                text = font.render(f"{'White' if color == 'w' else 'Black '} captured: {', '.join(line)}", True, pygame.Color("white"), pygame.Color("black"))
                self.screen.blit(text, (10, y_offset))
                y_offset += 30
            y_offset += 10 