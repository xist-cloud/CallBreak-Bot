# This contains the basic code that you will need to view the game on the snadbox.
# You will provide all the moves of all the bots in the sandbox.
# The sandbox is for testing purposes only so, the API data format can change
# when quelifiers begin.
# The sandbox is provided so that you can get familiar with buliding bots before
#  the event actually begings.

# To seutp: `pip install flask, flask_cors`
# To run: python app.py

import json


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/hi", methods = ["GET"])
def hi():
    return jsonify({"value": "hello"})

@app.route("/bid", methods=["POST"])
def bid():
    """
    Bid is called at the starting phase of the game in callbreak.
    You will be provided with the following data:
    {
        "matchId": "M1",
        "playerId": "P3",
        "cards": ["1S", "TS", "8S", "7S", "6S", "4S", "3S", "9H", "6H", "5H", "1C", "1D", "JD"],
        "context": {
            "round": 1,
            "players": {
            "P3": {
                "totalPoints": 0,
                "bid": 0
            },
            "P0": {
                "totalPoints": 0,
                "bid": 3
            },
            "P2": {
                "totalPoints": 0,
                "bid": 3
            },
            "P1": {
                "totalPoints": 0,
                "bid": 3
            }
            }
        }
    }

    This is all the data that you will require for the bidding phase.
    """

    body = request.get_json()
    j = json.dumps(body, indent=2)
    # print(j)
    ####################################
    #     Input your code here.        #
    ####################################
    # with open("json/bid_log.json", "w") as handle:
    #     handle.write(j)

    # return should have a single field value which should be an int reprsenting the bid value
    return jsonify({"value": 3})


@app.route("/play", methods=["POST"])
def play():
    """
    Play is called at every hand of the game where the user should throw a card.
    Request data format:
    {
        "matchId": "M1",
        "playerId": "P1",
        "cards": [ "QS", "9S", "2S", "KH", "JH", "4H", "JC", "9C", "7C", "6C", "8D", "6D", "3D"],
        "played": [
            "2H/0",
            "8H/0"
        ],
        "history": [
            [1, ["TS/0", "KS/0", "1S/0", "5S/0"], 3],
            [3, ["QS/0", "6S/0", "TH/0", "2S/0"], 3],
        ],
        "players": ["P0", "P1", "P2", "P3"]
    }
    The `played` field contins all the cards played this turn in order.
    'history` field contains an ordered list of cards played from first hand.
    Format: `start idx, [cards in clockwise order of player ids], winner idx`
        `start idx` is index of player that threw card first
        `winner idx` is index of player who won this hand
    `players`: list of ids in clockwise order (always same for a game)
    """
    body = request.get_json()
    # j = json.dumps(body, indent=2)
    # print(j)
    
    
    # with open("json/play_log.json", "a") as handle:
    #     handle.write(j)
    
    # print(body["cards"].index("KS"))

    # return should have a single field value
    # which should be an string reprsenting the card to play
    # e.g> {"value": "QS"}
    # to play the card "QS"
    trump_cards_list = [card for card in body['cards'] if card[1] == 'S']
    trump_cards_list = sorted(trump_cards_list, key = lambda x: cards_dict[x[0]])
    if body['played']:
        lead_suit = body['played'][0][1]
        lead_suit_cards = [card for card in body['cards'] if card[1] == lead_suit]
        if lead_suit_cards:
            print(lead_suit_cards)
            lead_suit_cards = sorted(lead_suit_cards, key = lambda x: cards_dict[x[0]])
            print(lead_suit_cards)
            played_cards = [card for card in body['played'] if card[1] == lead_suit]
            print(played_cards)
            played_cards = sorted(played_cards, key = lambda x: cards_dict[x[0]])
            print(played_cards)
            if cards_dict[played_cards[-1][0]] > cards_dict[lead_suit_cards[-1][0]]:
                best = lead_suit_cards[0]
            else:
                best = lead_suit_cards[-1]
        elif trump_cards_list:
            best = trump_cards_list[0]
        else:
            best = body['cards'][0]
    else:
        sorted(body['cards'], key = lambda x: cards_dict[x[0]])
        best = body['cards'][0]

    #print(lead_value, lead_suit)
    print(best)

    # value = input(">>>")
    return jsonify({"value": best})


# do not change this port; the sandbox server hits this port on localhost
if __name__ == "__main__":
    cards_dict = {'2': 0, 
                '3': 1,
                '4': 2, 
                '5': 3, 
                '6': 4, 
                '7': 5, 
                '8': 6, 
                '9': 7, 
                'T': 8, 
                'J': 9, 
                'Q': 10, 
                'K': 11, 
                '1': 12
                }
    # number_of_played_cards = {"S": 0,
    #                           "C": 0,
    #                           "H": 0,
    #                           "D": 0
    #                           }
    app.run(port=7000)


