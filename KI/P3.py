import random


class TicTacToe(object):
    # symbol player A: X
    # symbol player B: O
    def __init__(self, npc_A, npc_B):
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
        self.input = " "
        self.npc_A = npc_A
        self.npc_B = npc_B
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

        """for key, value in self.board.items():
            if key%3 == 0:
                print("|", end='')
            if key < 3 or key == 0:
                print(value+"|", end='')
            if 2 < key < 5:
                print(value+"|", end='')
            if 4 < key < 9:
                print(value+"|", end='')
                if key == 8:
                    print()
                    print()
            if key == 2 or key == 5:
                print()
                print("+-+-+-+")
            """

    def get_move_playerA(self):
        self.input = input("Move #" + self.move.__str__() + ">")
        if self.input != "" and int(self.input) < 9 and self.is_field_free(self.input):
            self.set_move_playerA()
        else:
            print("Falsche Eingabe")
            self.get_move_playerA()

    def get_move_playerB(self):
        self.input = input("Move #" + self.move.__str__() + ">")
        if self.input != "" and int(self.input) < 9 and self.is_field_free(self.input):
            self.set_move_playerB()
        else:
            print("Falsche Eingabe")
            self.get_move_playerB()

    def set_move_playerA(self):
        self.board[self.input] = "X"
        # self.show_board()

    def set_move_playerB(self):
        self.board[self.input] = "O"
        # self.show_board()

    def is_field_free(self, move):
        return self.board[move] == ' '

    def is_board_full(self):
        for i in range(0, 9):
            if self.is_field_free(str(i)):
                return False
        if not self.is_ai_only():
            print("Board full")
        return True

    def is_ai_only(self):
        return self.npc_A == "Y" and self.npc_B == "Y" and self.aio

    def is_winner(self, player_symbol):
        liste = [["0", "1", "2"],
                 ["3", "4", "5"],
                 ["6", "7", "8"],
                 ["0", "3", "6"],
                 ["1", "4", "7"],
                 ["2", "5", "8"],
                 ["0", "4", "8"],
                 ["2", "4", "6"]]
        for i in range(0, 7):
            count = 0
            for j in range(0, 3):
                if self.board[liste[i][j]] == player_symbol:
                    count += 1
                    if count == 3:
                        return True
        return False

    def schliessen(self):
        if self.is_ai_only():
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
        else:
            z = input("Play again with the same settings? Y/N ")
            if z == "N":
                z = input("Play again? Y/N ")
                if z == "N":
                    exit()
                elif z == "Y":
                    self.__init__("", "")
            elif z == "Y":
                self.__init__(self.npc_A, self.npc_B)
                self.start()
            else:
                self.schliessen()

    def player_A_routine(self):
        print("Choose a field for payler A (symbol 'X'):")
        self.move += 1
        self.get_move_playerA()
        if self.is_winner("X"):
            self.show_board()
            print("The winner is " + "X")
            self.schliessen()
        if self.is_board_full():
            self.schliessen()
        self.show_board()

    def player_B_routine(self):
        print("Choose a field for payler B (symbol 'O'):")
        self.move += 1
        self.get_move_playerB()
        if self.is_winner("O"):
            self.show_board()
            print("The winner is " + "O")
            self.schliessen()
        if self.is_board_full():
            self.schliessen()
        self.show_board()

    def player_A_routine_NPC(self):
        if not self.is_ai_only():
            print()
        ran = random
        zahl = ran.randint(0, 8)
        while not self.is_field_free(zahl.__str__()):
            zahl = ran.randint(0, 8)
        self.input = zahl.__str__()
        self.set_move_playerA()
        self.move += 1
        if not self.is_ai_only():
            if self.is_winner("X"):
                self.show_board()
                print("The winner is " + "X_NPC")
                self.schliessen()
            if self.is_board_full():
                self.schliessen()
            self.show_board()

    def player_B_routine_NPC(self):
        if not self.is_ai_only():
            print()
        ran = random
        zahl = ran.randint(0, 8)
        while not self.is_field_free(zahl.__str__()):
            zahl = ran.randint(0, 8)
        self.input = zahl.__str__()
        self.set_move_playerB()
        self.move += 1
        if not self.is_ai_only():
            if self.is_winner("O"):
                self.show_board()
                print("The winner is " + "O_NPC")
                self.schliessen()
            if self.is_board_full():
                self.schliessen()
            self.show_board()

    def start(self):
        print(self.npc_A and self.npc_B)
        while self.npc_A != "Y" and self.npc_A != "N":
            self.npc_A = input("Player A NPC Y/N")
        while self.npc_B != "Y" and self.npc_B != "N":
            self.npc_B = input("Player B NPC Y/N")
        print("Possible input: digit 0, 1, 2, ...,8")
        print()
        print("6|7|8")
        print("-+-+-")
        print("3|4|5")
        print("-+-+-")
        print("0|1|2")
        print()

        while not self.is_board_full():
            if self.npc_A == "N":
                self.player_A_routine()
            else:
                self.player_A_routine_NPC()
            if self.npc_B == "N":
                self.player_B_routine()
            else:
                self.player_B_routine_NPC()
        self.schliessen()

    def ai_only(self, games):
        self.aio = True
        l = []
        f = True
        for i in range(0, games):
            f = True
            while f:
                self.player_A_routine_NPC()
                if self.is_winner("X"):
                    self.win_A += 1
                    f = False
                    self.schliessen()
                if self.is_board_full():
                    self.draw += 1
                    f = False
                    self.schliessen()
                self.player_B_routine_NPC()
                if self.is_winner("O"):
                    self.win_B += 1
                    f = False
                    self.schliessen()
                if self.is_board_full():
                    self.draw += 1
                    f = False
                    self.schliessen()
        l.append(self.win_A)
        l.append(self.win_B)
        l.append(self.draw)
        return l

if __name__ == '__main__':
    #tick = TicTacToe("Y", "Y")
    tick = TicTacToe("", "")
    tick.start()
    #l = tick.ai_only(100000)
    #print("Win X: "+l[0].__str__() +" Win_O: "+ l[1].__str__() + " Draw: "+l[2].__str__())
    #print("Win X: " + ((l[0]/(l[0]+l[1]+l[2]))*100).__round__(2).__str__() + "% Win_O: " + ((l[1]/(l[0]+l[1]+l[2]))*100).__round__(2).__str__() + "% Draw: " + ((l[2]/(l[0]+l[1]+l[2]))*100).__round__(2).__str__() + "%")
    #print(l[0]+l[1]+l[2])
