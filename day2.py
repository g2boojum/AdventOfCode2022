# day2.py

testdata = """A Y
B X
C Z""".splitlines()

with open('day2.txt') as fp:
    data = fp.read().splitlines()

outcomes = {'AX': 1+3,# rock, rock (draw)
            'AY': 2+6,# rock, paper (win)
            'AZ': 3+0,# rock, scissors (lose)
            'BX': 1+0,# paper, rock (lose)
            'BY': 2+3,# paper, paper (draw)
            'BZ': 3+6,# paper, scissors (win)
            'CX': 1+6,# scissors, rock (win)
            'CY': 2+0,# scissors, paper (lose)
            'CZ': 3+3,# scissors, scissors (draw)
            }


def score(line):
    you_me = ''.join([line[0],line[2]])
    return outcomes[you_me]


if __name__ == '__main__':
    testsum = sum(score(line) for line in testdata)
    print('Part 1')
    print('test result: ', testsum)
    datasum = sum(score(line) for line in data)
    print('data result: ', datasum)


outcomes2 = {'AX': 3+0,# rock, lose (scissors)
             'AY': 1+3,# rock, draw (rock)
             'AZ': 2+6,# rock, win (paper)
             'BX': 1+0,# paper, lose (rock)
             'BY': 2+3,# paper, draw (paper)
             'BZ': 3+6,# paper, win (scissors)
             'CX': 2+0,# scissors, lose (paper)
             'CY': 3+3,# scissors, draw (scissors)
             'CZ': 1+6,# scissors, win (rock)
            }

def score2(line):
    you_res = ''.join([line[0],line[2]])
    return outcomes2[you_res]

if __name__ == '__main__':
    testsum = sum(score2(line) for line in testdata)
    print()
    print('Part 2')
    print('test result: ', testsum)
    datasum = sum(score2(line) for line in data)
    print('data result: ', datasum)




