from sys import stdin
from collections import defaultdict

deck_cards = defaultdict(set)
player_decks = defaultdict(set)

for line in stdin:
    if line == "" or line == "\n":
        break

    a, b = line.strip().split('/')
    a = a.strip()
    b = b.strip()

    if a.isnumeric():
        deck_cards[int(a)].add(b)
    elif b.isnumeric():
        player_decks[a].add(int(b))

player_card_counts = dict()

for player, player_decks in player_decks.items():
    card_count = len(set(x for deck in player_decks for x in deck_cards[deck]))
    player_card_counts[player] = card_count

max_card_count = max(player_card_counts.values())
max_card_count_players = []

for player, card_count in player_card_counts.items():
    if card_count == max_card_count:
        max_card_count_players.append(player)

for player in sorted(max_card_count_players):
    print(player)
