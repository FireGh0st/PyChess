import chess
import logging

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.captured_pieces = {"w": [], "b": []}

    def handle_click(self, selected_square, mouse_pos):
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
            if self.board.piece_at(clicked_square):
                logging.debug(f"Piece selected at square: {clicked_square}")
                return clicked_square
            else:
                logging.debug("No piece at the clicked square.")
        else:
            move = chess.Move(selected_square, clicked_square)
            if move in self.board.legal_moves:
                logging.debug(f"Move is legal: {move}")
                captured_piece = self.board.piece_at(clicked_square)
                if captured_piece:
                    logging.debug(f"Piece captured: {captured_piece.symbol()} at square: {clicked_square}")
                    color = "w" if captured_piece.color else "b"
                    self.captured_pieces[color].append(captured_piece.symbol().upper())
                self.board.push(move)
            else:
                logging.debug(f"Move is illegal: {move}")
            return None

        return selected_square