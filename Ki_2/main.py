import math
import random
import time


class Player(object):
    def __init__(self, symbol, tic, player):
        self.tic: TicTacToe = tic
        self.symbol = symbol
        self.player = player

    def get_move(self, move):
        pass

    def set_move(self, eingabe):
        self.tic.board[eingabe] = self.symbol

    def routine(self):
        pass


class MinMaxPlayer(Player):
    def __init__(self, symbol, tic, player):
        super().__init__(symbol, tic, player)
        self.playermove = ""
        if self.symbol == "X":
            self.gegner = "O"
        else:
            self.gegner = "X"

        self.utility_value = {
            " ": -1,
            self.gegner: 0,
            "-": 1,
            self.symbol: 2
        }

    def get_move(self, move):
        computertime = 0
        start = time.time()
        # self.min_value()
        self.set_move(self.MINIMAX_DECISION())
        end = time.time()
        computertime += end - start
        print("Calculation Time: " + str(computertime) + "s")

    def routine(self):
        print()
        self.tic.move += 1
        self.get_move(self.tic.move)
        if self.tic.is_winner(self.symbol):
            self.tic.show_board()
            print("The winner is " + self.symbol + "_MinMax")
            self.tic.schliessen()
        elif self.tic.is_board_full():
            self.tic.schliessen()
        self.tic.show_board()

    def getTerminaton(self):
        if self.tic.is_winner(self.symbol):
            return self.symbol
        if self.tic.is_winner(self.gegner):
            return self.gegner
        for i in range(0, 9):
            if self.tic.board[str(i)] == " ":
                return " "
        return "-"

    def max_value(self):
        if self.getTerminaton() != " ":  # if TERMINAL-TEST ( _state ) then
            return self.utility_value[self.getTerminaton()]  # return UTILITY ( _state )
        max_outcome = -math.inf  # _v ← −∞
        for i in range(0, 9):  # for each _a in ACTIONS ( _state ) do
            if self.tic.is_field_free(str(i)):  # is action possible
                self.tic.board[str(i)] = self.symbol  # action
                value = self.min_value()  # min_value
                if value > max_outcome:  # biggest min
                    max_outcome = value  # ""_v ← max ( _v, MIN-VALUE ( RESULT ( _state, _a ) ) )
                self.tic.board[str(i)] = " "  # reverse action
        return max_outcome  # return _v

    def min_value(self):
        if self.getTerminaton() != " ":  # if TERMINAL-TEST ( _state ) then
            return self.utility_value[self.getTerminaton()]  # return UTILITY ( _state )
        min_outcome = math.inf  # _v ← ∞
        for i in range(0, 9):  # for each _a in ACTIONS ( _state ) do
            if self.tic.is_field_free(str(i)):  # is action possible
                self.tic.board[str(i)] = self.gegner  # do action
                value = self.max_value()  # max_value
                if value < min_outcome:  # value smaller than old ones
                    min_outcome = value  # save value
                self.tic.board[str(i)] = " "  # reverse action
        return min_outcome  # retun _v

    def MINIMAX_DECISION(self):
        next_move = ""
        valueret = -math.inf
        for i in range(0, 9):  # for each _a in ACTIONS ( _state ) do
            if self.tic.is_field_free(str(i)):  # is action possible
                self.set_move(str(i))  # do action
                value = self.min_value()
                if valueret < value:  # Größer Als aktueller wert
                    next_move = str(i)  # neue action merken
                    valueret = value    # neuen util value merken
                self.tic.board[str(i)] = " " # undo action
        return next_move


class PlayerHuman(Player):
    def __init__(self, symbol, tic, player):
        super().__init__(symbol, tic, player)

    def get_move(self, move):
        eingabe = input("Move #" + self.tic.move.__str__() + ">")
        if eingabe != "" and int(eingabe) < 9 and self.tic.is_field_free(eingabe):
            self.set_move(eingabe)
        else:
            print("Falsche Eingabe")
            self.get_move(move)

    def routine(self):
        print("Choose a field for payler " + self.player + " (symbol '" + self.symbol + "'):")
        self.tic.move += 1
        self.get_move(self.tic.move)
        if self.tic.is_winner(self.symbol):
            self.tic.show_board()
            print("The winner is " + self.symbol)
            self.tic.schliessen()
        if self.tic.is_board_full():
            self.tic.schliessen()
        self.tic.show_board()


class RandomNPC(Player):
    def __init__(self, symbol, tic, player):
        super().__init__(symbol, tic, player)

    def get_move(self, move):
        ran = random
        zahl = ran.randint(0, 8)
        while not self.tic.is_field_free(zahl.__str__()):
            zahl = ran.randint(0, 8)
        eingabe = zahl.__str__()
        self.set_move(eingabe)

    def routine(self):
        print()
        self.tic.move += 1
        self.get_move(self.tic.move)
        if self.tic.is_winner(self.symbol):
            self.tic.show_board()
            print("The winner is " + self.symbol + "_NPC")
            self.tic.schliessen()
        elif self.tic.is_board_full():
            self.tic.schliessen()
        self.tic.show_board()


class TicTacToe(object):
    def __init__(self, npc_a, npc_b):
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
        self.move = 0
        self.player_A_Mode = npc_a
        self.player_B_Mode = npc_b
        self.win_A = 0
        self.win_B = 0
        self.draw = 0
        self.aio = False

    def show_board(self):
        s = self.board
        print(s.get("6") + "|" + s.get("7") + "|" + s.get("8"))
        print("-+-+-")
        print(s.get("3") + "|" + s.get("4") + "|" + s.get("5"))
        print("-+-+-")
        print(s.get("0") + "|" + s.get("1") + "|" + s.get("2"))

    def is_field_free(self, move):
        return self.board[move] == ' '

    def is_board_full(self):
        for i in range(0, 9):
            if self.is_field_free(str(i)):
                return False
        self.show_board()
        print("Draw")
        return True

    def is_ai_only(self):
        return self.player_A_Mode == "Y" and self.player_B_Mode == "Y" and self.aio

    def is_winner(self, player_symbol):
        liste = [["0", "1", "2"],
                 ["3", "4", "5"],
                 ["6", "7", "8"],
                 ["0", "3", "6"],
                 ["1", "4", "7"],
                 ["2", "5", "8"],
                 ["0", "4", "8"],
                 ["2", "4", "6"]]
        for i in range(0, 8):
            count = 0
            for j in range(0, 3):
                if self.board[liste[i][j]] == player_symbol:
                    count += 1
                    if count == 3:
                        return True
        return False

    def schliessen(self):
        z = input("Play again with the same settings? Y/N ")
        if z == "n":
            z = input("Play again? Y/N ").lower()
            if z == "n":
                exit()
            elif z == "y":
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
                self.move = 0
                self.player_A_Mode = ""
                self.player_B_Mode = ""
                self.win_A = 0
                self.win_B = 0
                self.draw = 0
                self.aio = False
                self.start()
        elif z == "y":
            self.__init__(self.player_A_Mode, self.player_B_Mode)
            self.start()
        else:
            self.schliessen()

    def start(self):
        print(self.player_A_Mode and self.player_B_Mode)
        while self.player_A_Mode != "1" and self.player_A_Mode != "2" and self.player_A_Mode != "3":
            self.player_A_Mode = input("Player A mode: Human = 1,Random = 2, MinMax = 3: ").lower()
        while self.player_B_Mode != "1" and self.player_B_Mode != "2" and self.player_B_Mode != "3":
            self.player_B_Mode = input("Player B mode: Human = 1,Random = 2, MinMax = 3: ").lower()

        print("Possible input: digit 0, 1, 2, ...,8")
        print()
        print("6|7|8")
        print("-+-+-")
        print("3|4|5")
        print("-+-+-")
        print("0|1|2")
        print()

        if self.player_A_Mode == "1":
            erster = PlayerHuman("X", self, "A")
        elif self.player_A_Mode == "2":
            erster = RandomNPC("X", self, "A")
        else:
            erster = MinMaxPlayer("X", self, "A")
        if self.player_B_Mode == "1":
            zweiter = PlayerHuman("O", self, "B")
        elif self.player_B_Mode == "2":
            zweiter = RandomNPC("O", self, "B")
        else:
            zweiter = MinMaxPlayer("O", self, "B")
        while not self.is_board_full():
            erster.routine()
            zweiter.routine()
        self.schliessen()


if __name__ == '__main__':
    tick = TicTacToe("", "")
    tick.start()
