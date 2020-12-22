with open('input.txt') as f:
    lines = f.read().splitlines()

player_1, player_2 = [], []
p1, p2 = False, False

for line in lines:
    if line == '':
        continue
    elif line == 'Player 1:':
        p1, p2 = True, False
        continue
    elif line == 'Player 2:':
        p1, p2 = False, True
        continue
    if p1:
        player_1.append(int(line))
    if p2:
        player_2.append(int(line))

player_1_part2, player_2_part2 = player_1.copy(), player_2.copy()

while True:
    if player_1[0] > player_2[0]:
        player_1.append(player_1.pop(0))
        player_1.append(player_2.pop(0))
    else:
        player_2.append(player_2.pop(0))
        player_2.append(player_1.pop(0))
    if len(player_1) == 0 or len(player_2) == 0:
        break

answer = 0
i = 0
if len(player_1) > 0:
    for card in player_1:
        answer += card * (len(player_1) - i)
        i += 1
else:
    for card in player_2:
        answer += card * (len(player_2) - i)
        i += 1

print(f'The answer to part 1 = {answer}')

class Play(object):
    def __init__(self, hand, game):
        self.game = game
        self.player_1 = list(hand[0])
        self.player_2 = list(hand[1])
        self.hands = set()
        self.hands.add((tuple(self.player_1), tuple(self.player_2)))
        self.card_1, self.card_2 = None, None

    def draw_card(self):
        self.card_1 = self.player_1.pop(0)
        self.card_2 = self.player_2.pop(0)
        if self.card_1 <= len(self.player_1) and self.card_2 <= len(self.player_2):
            new_p1 = tuple(self.player_1[0:self.card_1])
            new_p2 = tuple(self.player_2[0:self.card_2])
            return True, tuple((new_p1, new_p2))
        else:
            if self.card_1 > self.card_2:
                winner = 'p1'
            else:
                winner = 'p2'
            return False, winner

    def set_winner(self, winner):
        if winner == 'p1':
            self.player_1.append(self.card_1)
            self.player_1.append(self.card_2)
        else:
            self.player_2.append(self.card_2)
            self.player_2.append(self.card_1)
        # print(f'--- Game {self.game} ---')
        # print(f'Cards player 1 --> {self.player_1}')
        # print(f'Cards player 2 --> {self.player_2}')
        if len(self.player_1) == 0:
            return True, 'p2'
        elif len(self.player_2) == 0:
            return True, 'p1'
        elif (tuple(self.player_1), tuple(self.player_2)) in self.hands:
            return True, 'p1'
        else:
            self.hands.add((tuple(self.player_1), tuple(self.player_2)))
            return False, None


hand = (tuple(player_1_part2), tuple(player_2_part2))
# print(f'--- Starting hands ---')
# print(f'Cards player 1 --> {player_1_part2}')
# print(f'Cards player 2 --> {player_2_part2}')
cur_game = 0
games = {0: Play(hand, cur_game)}
skip_draw = False
winner = None

while True:
    if not skip_draw:
        val_1 = games[cur_game].draw_card()
        if val_1[0]:
            cur_game += 1
            games[cur_game] = Play(val_1[1], cur_game)
            continue
        winner = val_1[1]
    skip_draw = False
    val_2 = games[cur_game].set_winner(winner)
    if val_2[0] and cur_game == 0:
        if val_2[1] == 'p1':
            winning_hand = games[0].player_1
        else:
            winning_hand = games[0].player_2
        break
    elif val_2[0]:
        winner = val_2[1]
        del games[cur_game]
        cur_game -= 1
        skip_draw = True

answer = 0
i = 0

for card in winning_hand:
    answer += card * (len(winning_hand) - i)
    i += 1

print(f'The answer to part 2 = {answer}')