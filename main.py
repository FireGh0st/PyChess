import pygame
import logging
from game import ChessGame
from gui import ChessGUI

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    game = ChessGame()
    gui = ChessGUI()

    selected_square = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_square = game.handle_click(selected_square, event.pos)

        gui.draw_board()
        gui.display_turn(game.board.turn)
        # gui.display_captured_pieces(game.captured_pieces)
        if selected_square is not None:
            gui.highlight_moves(game.board.legal_moves, selected_square)
        gui.draw_pieces(game.board)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()