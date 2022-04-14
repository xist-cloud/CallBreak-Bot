import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import bid as bd
import play as pl

app = Flask(__name__)
CORS(app)

@app.route("/hi", methods = ["GET"])
def hi():
    return jsonify({"value": "hello"})

@app.route("/bid", methods=["POST"])
def bid():
    body = request.get_json()

    # j = json.dumps(body, indent=2)
    # print(j)
    ####################################
    #     Input your code here.        #
    ####################################
    # with open("json/bid_log.json", "w") as handle:
    #     handle.write(j)

    value = bd.bid_value(body)

    # return should have a single field value which should be an int reprsenting the bid value
    return jsonify({"value": value})


@app.route("/play", methods=["POST"])
def play():
    body = request.get_json()
    # j = json.dumps(body, indent=2)
    # print(j)
    
    
    # with open("json/play_log.json", "a") as handle:
    #     handle.write(j)
    value = pl.play_card(body, cards_dict)
    
    return jsonify({"value": value})


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


