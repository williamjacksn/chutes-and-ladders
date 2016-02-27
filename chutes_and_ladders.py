import random


def log(message):
    print(message)


def get_next_space(start, roll):
    special = {1: 38, 4: 14, 9: 31, 16: 6, 21: 42, 28: 84, 36: 44, 48: 26,
               49: 11, 51: 67, 56: 53, 62: 19, 64: 60, 71: 91, 80: 100, 87: 24,
               93: 73, 95: 75, 98: 78}
    next_space = start + roll
    if next_space > 100:
        return start
    return special.get(next_space, next_space)


class Player(object):
    def __init__(self, name):
        self.name = name
        self.space = 0

    def __repr__(self):
        return 'Player({})'.format(repr(self.name))

    def __str__(self):
        return self.name


def main():
    game_on = True
    round_num = 0
    players = []
    for name in ['Player 1', 'Player 2', 'Player 3', 'Player 4']:
        players.append(Player(name))
    log('** Let\'s play Chutes and Ladders!')
    while game_on:
        round_num += 1
        log('** Begin round {}'.format(round_num))
        for player in players:
            roll = random.randint(1, 6)
            old_space = player.space
            player.space = get_next_space(player.space, roll)
            m = '{} rolled {}, moved from {} to {}'
            log(m.format(player, roll, old_space, player.space))
            if player.space == 100:
                game_on = False
                log('{} wins!'.format(player))
                break
        log('** End of round {}'.format(round_num))

if __name__ == '__main__':
    main()
