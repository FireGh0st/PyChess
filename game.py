import chess
import logging

class ChessGame:
    def __init__(self, player_white, player_black):
        self.board = chess.Board()
        self.captured_pieces = {"w": [], "b": []}
        self.player_white = player_white
        self.player_black = player_black

    def get_current_player(self):
        if self.board.turn == chess.WHITE:
            return self.player_white
        else:
            return self.player_black

    def handle_click(self, selected_square, mouse_pos):
        player = self.get_current_player()
        if isinstance(player, Player):
            return player.handle_click(self, selected_square, mouse_pos)
        return selected_square

    def make_move(self, move):
        if move in self.board.legal_moves:
            logging.debug(f"Move is legal: {move}")
            captured_piece = self.board.piece_at(move.to_square)
            if captured_piece:
                logging.debug(f"Piece captured: {captured_piece.symbol()} at square: {move.to_square}")
                color = "w" if captured_piece.color else "b"
                self.captured_pieces[color].append(captured_piece.symbol().upper())
            self.board.push(move)
            return True
        logging.debug(f"Move is illegal: {move}")
        return False

class Player:
    def handle_click(self, game, selected_square, mouse_pos):
        logging.debug(f"Handling click at position: {mouse_pos}")
        square_size = 128
        col = (mouse_pos[0] - 256) // square_size
        row = 7 - (mouse_pos[1] // square_size)
        if col < 0 or col > 7 or row < 0 or row > 7:
            logging.debug("Click outside the board detected.")
            return selected_square

        clicked_square = chess.square(col, row)
        logging.debug(f"Translated to board square: {clicked_square}")

        if selected_square is None:
            piece = game.board.piece_at(clicked_square)
            if piece and piece.color == game.board.turn:
                logging.debug(f"Piece selected at square: {clicked_square}")
                return clicked_square
            else:
                logging.debug("No piece at the clicked square or not current player's piece.")
        else:
            move = chess.Move(selected_square, clicked_square)
            if game.make_move(move):
                return None
            else:
                # If the move was not legal, maybe the user wants to select another piece.
                piece = game.board.piece_at(clicked_square)
                if piece and piece.color == game.board.turn:
                    return clicked_square
                else:
                    return None
        return selected_square