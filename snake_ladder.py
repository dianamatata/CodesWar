# https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python
import sys
sys.path.append('/Users/dianaavalos/Programming/python-test-framework')
import codewars_test as test



class SnakesLadders():

    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.current_player = 0  # 1 for player 0, 0 for player 1
        self.square = 0
        self.finished = False
        self.position_switch = {2: 38, 16: 6, 7: 14, 8: 31, 49: 11, 15: 26, 62: 19, 28:84, 46: 25, 21: 42, 36:44,
                   51:67, 74:53, 64:60, 71: 91, 95:75, 78:98, 99:80, 92:88, 87:94}


    def play(self, die1, die2):
        print("dies", die1, " ", die2)

        if self.finished == True:
            return "Game over!"
        if self.current_player == 0:
            self.square = self.player1 + die1 + die2
        else:
            self.square = self.player2 + die1 + die2

        print(" player ", self.current_player + 1, "square", self.square)
        if self.square == 100:
            self.finished = True
            return "Player %d Wins!" % (self.current_player + 1)
        if self.square > 100: self.square = 100 - (self.square - 100)
        if self.square in self.position_switch.keys(): self.square = self.position_switch[self.square]

        if self.current_player == 0:
            self.player1 = self.square
        else:
            self.player2 = self.square

        self.actual_player = self.current_player
        if die1 != die2: self.current_player = abs(1 - self.current_player); self.current_player = self.current_player
        return "Player %s is on square %d" % ((self.actual_player + 1), self.square)



# https://www.codewars.com/kata/587136ba2eefcb92a9000027/solutions/python



# better version

board = {2: 38, 7: 14, 8: 31, 15: 26, 16: 6, 21: 42, 28: 84, 36: 44, 46: 25, 49: 11, 51: 67, 62: 19, 64: 60,
         71: 91, 74: 53, 78: 98, 87: 94, 89: 68, 92: 88, 95: 75, 99: 80}

class SnakesLadders():
    def __init__(self):
        self.pos = [0, 0]
        self.who = 0

    def play(self, a, b):
        if 100 in self.pos: return "Game over!"

        w, p = self.who, 200 - (self.pos[self.who] + a + b) if self.pos[self.who] + a + b > 100 else self.pos[
                                                                                                         self.who] + a + b

        self.pos[self.who], self.who = board.get(p, p), (self.who if a == b else (self.who + 1) % 2)
        return 'Player {} Wins!'.format(w + 1) if 100 in self.pos else 'Player {} is on square {}'.format(w + 1,
                                                                                                          self.pos[
                                                                                                              w])
### other ideas
def _get_new_position(self, current_position, num_turns):
    new_position = current_position + num_turns

    if new_position > 100:
        new_position = 100 - (new_position - 100)

    pos_key = str(new_position)
    if pos_key in self._ladders_snakes:
        new_position = self._ladders_snakes[pos_key]

    return new_position

def _game_message(self, position):
    if self._game_over:
        return "Game over!"
    elif position == 100:
        self._game_over = True
        return f"Player {self._active_player} Wins!"
    else:
        return f"Player {self._active_player} is on square {position}"


@test.describe('Example Tests')
def example_tests():
    game = SnakesLadders()

    @test.it("Should return: 'Player 1 is on square 38'")
    def example_test_case():
        test.assert_equals(game.play(1, 1), "Player 1 is on square 38")

    @test.it("Should return: 'Player 1 is on square 44'")
    def example_test_case():
        test.assert_equals(game.play(1, 5), "Player 1 is on square 44")

    @test.it("Should return: 'Player 2 is on square 31'")
    def example_test_case():
        test.assert_equals(game.play(6, 2), "Player 2 is on square 31")

    @test.it("Should return: 'Player 1 is on square 25'")
    def example_test_case():
        test.assert_equals(game.play(1, 1), "Player 1 is on square 25")

