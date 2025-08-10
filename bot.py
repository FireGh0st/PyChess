import chess
import random

class Bot:
    def __init__(self, board):
        self.board = board

    def get_move(self):
        raise NotImplementedError

    def evaluate_board(self):
        if self.board.is_checkmate():
            if self.board.turn:
                return -float('inf')
            else:
                return float('inf')
        if self.board.is_stalemate() or self.board.is_insufficient_material():
            return 0

        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0
        }

        eval = 0
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                if piece.color == chess.WHITE:
                    eval += piece_values[piece.piece_type]
                else:
                    eval -= piece_values[piece.piece_type]
        return eval

class RandomBot(Bot):
    def get_move(self):
        legal_moves = list(self.board.legal_moves)
        return random.choice(legal_moves)

class MinimaxBot(Bot):
    def __init__(self, board, depth=3):
        super().__init__(board)
        self.depth = depth

    def get_move(self):
        if self.board.turn == chess.WHITE:
            return self.get_max_move()
        else:
            return self.get_min_move()

    def get_max_move(self):
        best_move = None
        best_value = -float('inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            board_value = self.minimax(self.depth - 1, False)
            self.board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
        return best_move

    def get_min_move(self):
        best_move = None
        best_value = float('inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            board_value = self.minimax(self.depth - 1, True)
            self.board.pop()
            if board_value < best_value:
                best_value = board_value
                best_move = move
        return best_move

    def minimax(self, depth, is_maximizing):
        if depth == 0 or self.board.is_game_over():
            return self.evaluate_board()

        if is_maximizing:
            best_value = -float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                best_value = max(best_value, self.minimax(depth - 1, not is_maximizing))
                self.board.pop()
            return best_value
        else:
            best_value = float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                best_value = min(best_value, self.minimax(depth - 1, not is_maximizing))
                self.board.pop()
            return best_value

class AlphaBetaBot(Bot):
    def __init__(self, board, depth=3):
        super().__init__(board)
        self.depth = depth

    def get_move(self):
        if self.board.turn == chess.WHITE:
            return self.get_max_move()
        else:
            return self.get_min_move()

    def get_max_move(self):
        best_move = None
        best_value = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            board_value = self.alphabeta(self.depth - 1, alpha, beta, False)
            self.board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
            alpha = max(alpha, best_value)
        return best_move

    def get_min_move(self):
        best_move = None
        best_value = float('inf')
        alpha = -float('inf')
        beta = float('inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            board_value = self.alphabeta(self.depth - 1, alpha, beta, True)
            self.board.pop()
            if board_value < best_value:
                best_value = board_value
                best_move = move
            beta = min(beta, best_value)
        return best_move

    def alphabeta(self, depth, alpha, beta, is_maximizing):
        if depth == 0 or self.board.is_game_over():
            return self.evaluate_board()

        if is_maximizing:
            best_value = -float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                best_value = max(best_value, self.alphabeta(depth - 1, alpha, beta, not is_maximizing))
                self.board.pop()
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_value
        else:
            best_value = float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                best_value = min(best_value, self.alphabeta(depth - 1, alpha, beta, not is_maximizing))
                self.board.pop()
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value
