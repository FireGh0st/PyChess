import pygame
import logging
from game import ChessGame
from gui import ChessGUI

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.debug("Starting the main game loop.")
    game = ChessGame()
    gui = ChessGUI()

    selected_square = None
    running = True
    while running:
        for event in pygame.event.get():
            logging.debug(f"Event detected: {event}")
            if event.type == pygame.QUIT:
                logging.debug("Quit event detected.")
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                logging.debug(f"Mouse click at position: {event.pos}")
                selected_square = game.handle_click(selected_square, event.pos)

        logging.debug("Redrawing the board and updating the display.")
        gui.draw_board()
        gui.display_turn(game.board.turn)
        # gui.display_captured_pieces(game.captured_pieces)
        if selected_square is not None:
            logging.debug(f"Highlighting moves for square: {selected_square}")
            gui.highlight_moves(game.board.legal_moves, selected_square)
        gui.draw_pieces(game.board)
        pygame.display.flip()
        pygame.time.delay(100)
    logging.debug("Exiting the main game loop.")

    pygame.quit()

if __name__ == "__main__":
    main()