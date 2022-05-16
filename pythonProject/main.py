import time


class TicTacToe(object):
    def __init__(self):
        self.player1symbol = "X"
        self.player2symbol = "O"
        self.player1move = ""
        self.player2move = ""
        self.board = {
            "0": " ",
            "1": " ",
            "2": " ",
            "3": " ",
            "4": " ",
            "5": " ",
            "6": " ",
            "7": " ",
            "8": " "
        }
        self.utility_value = {
            " ": -1,
            "O": 0,
            "-": 1,
            "X": 2
        }

    def show_board(self):
        print(self.board["0"] + "|" + self.board["1"] + "|" + self.board["2"])
        print("-+-+-")
        print(self.board["3"] + "|" + self.board["4"] + "|" + self.board["5"])
        print("-+-+-")
        print(self.board["6"] + "|" + self.board["7"] + "|" + self.board["8"])
        print("\n")

    def get_player1_move(self):
        self.player1move = input("Spieler X: ")

    def set_move_player1(self):
        if self.is_spot_free(self.player1move):
            self.board[self.player1move] = self.player1symbol
        else:
            print("Nicht frei, oder falsche Eingabe! Bitte erneut versuchen\n")
            self.get_player1_move()
            self.set_move_player1()

    def is_spot_free(self, move):
        return self.board[move] == " "

    def terminate_test(self):
        for p in ["X", "O"]:
            if self.board["0"] == self.board["1"] == self.board["2"] == p:
                return p
            elif self.board["3"] == self.board["4"] == self.board["5"] == p:
                return p
            elif self.board["6"] == self.board["7"] == self.board["8"] == p:
                return p
            elif self.board["0"] == self.board["3"] == self.board["6"] == p:
                return p
            elif self.board["1"] == self.board["4"] == self.board["7"] == p:
                return p
            elif self.board["2"] == self.board["5"] == self.board["8"] == p:
                return p
            elif self.board["0"] == self.board["4"] == self.board["8"] == p:
                return p
            elif self.board["2"] == self.board["4"] == self.board["6"] == p:
                return p
        for i in range(0, 9):
            if self.board[str(i)] == " ":
                return " "
        return "-"

    def max_value(self):
        # Letzter Zustand
        if self.terminate_test() != " ":
            return self.utility_value[self.terminate_test()]
        max_outcome = -1
        for i in range(0, 9):
            if self.board[str(i)] == " ":
                self.board[str(i)] = self.player1symbol
                value = self.min_value()
                if value > max_outcome:
                    max_outcome = value
                self.board[str(i)] = " "
        return max_outcome

    def min_value(self):
        # Letzter Zustand
        if self.terminate_test() != " ":
            return self.utility_value[self.terminate_test()]
        min_outcome = 3
        next_move = ""
        for i in range(0, 9):
            if self.board[str(i)] == " ":
                self.board[str(i)] = self.player2symbol
                value = self.max_value()
                if value < min_outcome:
                    next_move = str(i)
                    min_outcome = value
                self.board[str(i)] = " "
        self.player2move = next_move
        return min_outcome

    def start(self):
        self.show_board()
        computertime = 0
        while self.terminate_test() == " ":
            self.get_player1_move()
            self.set_move_player1()
            self.show_board()
            if self.terminate_test() != " ":
                break
            start = time.time()
            self.min_value()
            end = time.time()
            computertime += end - start
            print("Computer Zug:")
            self.board[self.player2move] = self.player2symbol
            if self.terminate_test() != " ":
                break
            self.show_board()
        self.show_board()
        result = self.terminate_test()
        if result == "X":
            print("Spieler X hat gewonnen!")
        elif result == "-":
            print("Unentschieden!")
        elif result == "O":
            print("Spieler O hat gewonnen!")
        print("Der Computer benötigte " + str(computertime) + " Sekunden!")


ttt = TicTacToe()
ttt.start()
