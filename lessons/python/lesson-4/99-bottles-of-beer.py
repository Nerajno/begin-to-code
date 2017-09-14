
number_of_beers = 99
while number_of_beers > 2:
    print("%d bottles of beer on the wall, %d bottles of beer." % (number_of_beers, number_of_beers))
    number_of_beers = number_of_beers - 1
    print("Take one down and pass it around, %d bottles of beer on the wall." % number_of_beers)

print("""2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.""")
