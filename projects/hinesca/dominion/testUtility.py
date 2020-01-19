"""
Created on Sun January 19 2020

@author: cjhines
"""

import Dominion
import random
from collections import defaultdict


def get_player_names():
    return ["Annie",
            "*Ben",
            "*Carla"]


def get_number_of_victory_cards(players):
    if len(players) > 2:
        return 12
    else:
        return 8


def get_number_of_curse_cards(players):
    return -10 + 10 * len(players)


def get_box(number_of_victory_cards):
    return {"Woodcutter": [Dominion.Woodcutter()] * 10,
            "Smithy": [Dominion.Smithy()] * 10,
            "Laboratory": [Dominion.Laboratory()] * 10,
            "Village": [Dominion.Village()] * 10,
            "Festival": [Dominion.Festival()] * 10,
            "Market": [Dominion.Market()] * 10,
            "Chancellor": [Dominion.Chancellor()] * 10,
            "Workshop": [Dominion.Workshop()] * 10,
            "Moneylender": [Dominion.Moneylender()] * 10,
            "Chapel": [Dominion.Chapel()] * 10,
            "Cellar": [Dominion.Cellar()] * 10,
            "Remodel": [Dominion.Remodel()] * 10,
            "Adventurer": [Dominion.Adventurer()] * 10,
            "Feast": [Dominion.Feast()] * 10,
            "Mine": [Dominion.Mine()] * 10,
            "Library": [Dominion.Library()] * 10,
            "Gardens": [Dominion.Gardens()] * number_of_victory_cards,
            "Moat": [Dominion.Moat()] * 10,
            "Council Room": [Dominion.Council_Room()] * 10,
            "Witch": [Dominion.Witch()] * 10,
            "Bureaucrat": [Dominion.Bureaucrat()] * 10,
            "Militia": [Dominion.Militia()] * 10,
            "Spy": [Dominion.Spy()] * 10,
            "Thief": [Dominion.Thief()] * 10,
            "Throne Room": [Dominion.Throne_Room()] * 10}


def get_supply_order():
    return {0: ['Curse', 'Copper'],
            2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
            3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
            4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
                'Throne Room'],
            5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
            6: ['Gold', 'Adventurer'],
            8: ['Province']}


def get_supply():
    player_names = get_player_names()
    number_of_victory_cards = get_number_of_victory_cards(player_names)
    number_of_curse_cards = get_number_of_curse_cards(player_names)
    box = get_box(number_of_victory_cards)
    # Pick 10 cards from box to be in the supply.
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list, [(k, box[k]) for k in random10])
    # The supply always has these cards
    supply["Copper"] = [Dominion.Copper()] * (60 - len(player_names) * 7)
    supply["Silver"] = [Dominion.Silver()] * 40
    supply["Gold"] = [Dominion.Gold()] * 30
    supply["Estate"] = [Dominion.Estate()] * number_of_victory_cards
    supply["Duchy"] = [Dominion.Duchy()] * number_of_victory_cards
    supply["Province"] = [Dominion.Province()] * number_of_victory_cards
    supply["Curse"] = [Dominion.Curse()] * number_of_curse_cards
    return supply


def get_players():
    players = []
    for name in get_player_names():
        if name[0] == "*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0] == "^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players
