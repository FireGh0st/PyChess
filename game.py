import chess

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.captured_pieces = {"w": [], "b": []}

    def handle_click(self, selected_square, mouse_pos):
        square_size = 128
        col = (mouse_pos[0] - 256) // square_size
        row = 7 - (mouse_pos[1] // square_size)
        if col < 0 or col > 7 or row < 0 or row > 7:
            return selected_square

        clicked_square = chess.square(col, row)

        if selected_square is None:
            if self.board.piece_at(clicked_square):
                return clicked_square
        else:
            move = chess.Move(selected_square, clicked_square)
            if move in self.board.legal_moves:
                captured_piece = self.board.piece_at(clicked_square)
                if captured_piece:
                    color = "w" if captured_piece.color else "b"
                    self.captured_pieces[color].append(captured_piece.symbol().upper())
                self.board.push(move)
            return None

        return selected_square