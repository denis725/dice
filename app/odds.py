import argparse

from utils import make_check
from utils import roll


parser = argparse.ArgumentParser()
parser.add_argument("check", type=int, 
                    help='Int, the check that you want to reach')
parser.add_argument("dice", type=int, nargs='+',
                    help='List of ints, the dice you throw (e.g. 6 12 20)')
parser.add_argument("--bonus", type=int, nargs='+', default=0,
                    help='List of ints, bonus or malus for your check')
parser.add_argument('-g', '--strictly_greater', action='store_true',
                    help='Flag, if set, you need to 1 more to pass the check')
parser.add_argument('-r', '--roll', action='store_true',
                    help='Flag, if set, simulate a dice roll')
args = parser.parse_args()

if args.bonus: args.bonus = sum(args.bonus)


def odds(args):
    # The input
    welcome = '- You attempt to make a check of {}'.format(args.check)
    welcome += ' by rolling a d{}'.format(', d'.join([str(die) for
                                                       die in args.dice[:-1]]))
    if len(args.dice) > 1: welcome += ' and a d'
    welcome += '{}.'.format(args.dice[-1])
    if args.bonus:
        welcome += '\n- Your bonus on the check is {}.'.format(args.bonus)
    print(welcome)
    hits, total, percent = make_check(args.check, args.dice,
                                      args.bonus, args.strictly_greater)

    # The odds
    if not args.roll:
        if percent % 1 == 0:
            print("- The odds of winning are {} in {}, i.e. {} %.".
                  format(*map(int, (hits, total, percent))))
        else:
            print("- The odds of winning are {} in {}, i.e. roughly {:.0f} %.".
                  format(*map(int, (hits, total, percent))))
    else: # Roll the dice
        result = roll(args.dice) + args.bonus
        if result >= args.check + args.strictly_greater:
            print("- Rolling dice ... the result is {} ({} was required), "
                  "you win!" .format(result,
                                     args.check + args.strictly_greater))
        else:
            print("- Rolling dice ... the result is {} ({} was required), "
                  "you lose!" .format(result,
                                      args.check + args.strictly_greater))


if __name__ == "__main__":
#    if np.cumprod(args.dice)[-1] > 1e7:
    if reduce(lambda x, y: x * y, args.dice) > 1e7:
        print('Too many dice, my head explodes!')
    else:
        odds(args)
