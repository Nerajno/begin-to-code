class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

barkley  = Record(name="Charles Barkley",    num=14, pos="PF", gp=6, pts=98)
bird     = Record(name="Larry Bird",         num=7,  pos="SF", gp=2, pts=19)
clyde    = Record(name="Clyde Drexler",      num=10, pos="SG", gp=5, pts=69)
ewing    = Record(name="Patrick Ewing",      num=6,  pos="C",  gp=5, pts=59)
magic    = Record(name="Magic Johnson",      num=15, pos="PG", gp=6, pts=58)
jordan   = Record(name="Michael Jordan",     num=9,  pos="SG", gp=6, pts=76)
laettner = Record(name="Christian Laettner", num=4,  pos="PF", gp=6, pts=44)
malone   = Record(name="Carl Malone",        num=11, pos="PF", gp=6, pts=89)
mullin   = Record(name="Chris Mullin",       num=13, pos="SF", gp=6, pts=86)
pippen   = Record(name="Scottie Pippen",     num=8,  pos="SF", gp=6, pts=48)
robinson = Record(name="David Robinson",     num=5,  pos="C",  gp=6, pts=71)
stockton = Record(name="John Stockton",      num=12, pos="PG", gp=2, pts=10)

dream_team = [
    barkley, bird, clyde, ewing, magic, jordan, laettner,
    malone, mullin, pippen, robinson, stockton
]

def highest_scorer_by_position(players):
    highest_scorers = {}
    for player in players:
        if player.pos in highest_scorers:
            high = highest_scorers[player.pos]
            if high.pts < player.pts:
                highest_scorers[player.pos] = player
        else:
            highest_scorers[player.pos] = player
    return highest_scorers

def create_jersey_number_map(players):
    jersey_map = {}
    for player in players:
        jersey_map[player.num] = player
    return jersey_map

scorers = highest_scorer_by_position(dream_team)
jersey_map = create_jersey_number_map(dream_team)
print(jersey_map)
