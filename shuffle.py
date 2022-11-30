#!/usr/bin/env python3.11
import random

# Here is an example of an orderd playlist with the artists of the songs.
# Some artists have more songs in the playlist than others, and currently
# they're all grouped together
examplePlaylist: list[str] = [
  "Artist A", "Artist B", "Artist B", "Artist C", "Artist D", "Artist E", "Artist E", "Artist E", "Artist E",
  "Artist F", "Artist F", "Artist F", "Artist G", "Artist H", "Artist H", "Artist I", "Artist J", "Artist J", 
]

# This method to shuffle selects one item randomly and then appends it to a new list
# This method is not effective, when one item in an array appears more frequently, it
# is more likely to be picked in a row and will appear in a sequence with itself in the
# 'shuffled' list.
def shuffle_one(pl: list[str]) -> list[str]:
  s: list = []
  for _ in range(len(pl)):
    i = pl[random.randint(0, len(pl)) - 1]
    pl.remove(i)
    s.append(i)
  return s

# This algorithm is much better, it applies randomness to every element, selecting a random
# spot to shuffle with every time, this enables items previously shuffled to once again be
# shuffles to make a seemingly more 'random' shuffle.
def shuffle_two(pl: list[str]) -> list[str]:
  for i in range(len(pl)):
    swap_idx = random.randrange(i, len(pl))
    pl[i], pl[swap_idx] = pl[swap_idx], pl[i]
  return pl

def main() -> None:
  print(shuffle_one(list(examplePlaylist)))
  print(shuffle_two(list(examplePlaylist)))

if __name__ == '__main__':
  main()