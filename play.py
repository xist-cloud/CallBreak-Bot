def play_card(body, cards_dict):

    # body
    """
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
    """
    
    cards_in_hand = {
                    'S': sorted([card for card in body['cards'] if card[1] == 'S'], key = lambda x: cards_dict[x[0]]),
                    'C': sorted([card for card in body['cards'] if card[1] == 'C'], key = lambda x: cards_dict[x[0]]),
                    'H': sorted([card for card in body['cards'] if card[1] == 'H'], key = lambda x: cards_dict[x[0]]),
                    'D': sorted([card for card in body['cards'] if card[1] == 'D'], key = lambda x: cards_dict[x[0]]),
                    }
    cards_not_in_hand = {
                        'S': sorted([key+'S' for key in cards_dict.keys() if key+'S' not in cards_in_hand['S']], key = lambda x: cards_dict[x[0]]),
                        'C': sorted([key+'C' for key in cards_dict.keys() if key+'C' not in cards_in_hand['C']], key = lambda x: cards_dict[x[0]]),
                        'H': sorted([key+'H' for key in cards_dict.keys() if key+'H' not in cards_in_hand['H']], key = lambda x: cards_dict[x[0]]),
                        'D': sorted([key+'D' for key in cards_dict.keys() if key+'D' not in cards_in_hand['D']], key = lambda x: cards_dict[x[0]]),
                        }
    lead_card = body['played'][0]