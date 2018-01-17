from record import Record

# num - Jersey #
# pos - position:
#    C - Center
#    PF - Power Forward
#    SF - Small Forward
#    SG - Shooting Guard
#    PG - Point Guard
# GP - # of games played
# PTS - total # of points across all games played
# FGM - # of field goals (shots) made
# FGA - # of field goals (shots) attempted
#
# Source: https://en.wikipedia.org/wiki/1992_United_States_men%27s_Olympic_basketball_team

barkley  = Record(name="Charles Barkley",    num=14, pos="PF", gp=6, pts=98, fgm=34, fga=58)
bird     = Record(name="Larry Bird",         num=7,  pos="SF", gp=2, pts=19, fgm=8,  fga=11)
clyde    = Record(name="Clyde Drexler",      num=10, pos="SG", gp=5, pts=69, fgm=27, fga=39)
ewing    = Record(name="Patrick Ewing",      num=6,  pos="C",  gp=5, pts=59, fgm=27, fga=43)
magic    = Record(name="Magic Johnson",      num=15, pos="PG", gp=6, pts=58, fgm=19, fga=34)
jordan   = Record(name="Michael Jordan",     num=9,  pos="SG", gp=6, pts=76, fgm=29, fga=53)
laettner = Record(name="Christian Laettner", num=4,  pos="PF", gp=6, pts=44, fgm=18, fga=31)
malone   = Record(name="Carl Malone",        num=11, pos="PF", gp=6, pts=89, fgm=33, fga=53)
mullin   = Record(name="Chris Mullin",       num=13, pos="SF", gp=6, pts=86, fgm=31, fga=49)
pippen   = Record(name="Scottie Pippen",     num=8,  pos="SF", gp=6, pts=48, fgm=20, fga=30)
robinson = Record(name="David Robinson",     num=5,  pos="C",  gp=6, pts=71, fgm=32, fga=42)
stockton = Record(name="John Stockton",      num=12, pos="PG", gp=2, pts=10, fgm=5,  fga=6 )

dream_team = [
    barkley, bird, clyde, ewing, magic, jordan, laettner,
    malone, mullin, pippen, robinson, stockton
]

def most_points(players):
    highest_pts = 0
    highest_player = None
    for player in players:
        if player.pts > highest_pts:
            highest_pts = player.pts
            highest_player = player
    return highest_player

def highest_fg_avg(players):
    highest_avg = 0
    highest_player = None
    for player in players:
        fg_avg = player.fgm / player.fga
        if fg_avg > highest_pts:
            highest_avg = fg_avg
            highest_player = player
    return highest_player

def higest_point_avg(players):
    highest_point_avg = 0
    highest_player = None
    for player in players:
        avg = player.pts / player.gp
        if avg > highest_point_avg:
            highest_point_avg = avg
            highest_player = player
    return highest_player

p = most_points(dream_team)
print("The player with the most points is %s with %d points." % (p.name, p.pts))
