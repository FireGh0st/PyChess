import pygame
import logging
from game import ChessGame, Player
from gui import ChessGUI
from bot import RandomBot, MinimaxBot, AlphaBetaBot

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.debug("Starting the main game loop.")

    # Game mode selection
    # 1: Player vs. Player
    # 2: Player vs. Bot
    # 3: Bot vs. Bot
    game_mode = 2

    player_white = None
    player_black = None

    if game_mode == 1:
        player_white = Player()
        player_black = Player()
    elif game_mode == 2:
        player_white = Player()
        player_black = AlphaBetaBot(None, depth=3)
    elif game_mode == 3:
        player_white = MinimaxBot(None, depth=3)
        player_black = AlphaBetaBot(None, depth=3)

    game = ChessGame(player_white, player_black)
    if isinstance(player_white, (MinimaxBot, AlphaBetaBot, RandomBot)):
        player_white.board = game.board
    if isinstance(player_black, (MinimaxBot, AlphaBetaBot, RandomBot)):
        player_black.board = game.board

    gui = ChessGUI()

    selected_square = None
    running = True
    while running:
        current_player = game.get_current_player()

        if isinstance(current_player, (MinimaxBot, AlphaBetaBot, RandomBot)):
            move = current_player.get_move()
            if move:
                game.make_move(move)
        else:
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