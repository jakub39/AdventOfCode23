def evaluate_hand_and_bid(line, face):
    card_mapping = {'T': face[0], 'J': face[1], 'Q': face[2], 'K': face[3], 'A': face[4]}
    hand, bid = line.split()
    mapped_hand = ''.join(card_mapping[card] if card in card_mapping else card for card in hand)
    hand_type = sorted(map(mapped_hand.count, mapped_hand), reverse=True)
    return hand_type, mapped_hand, int(bid)

def calculate_score(line_evaluations):
    total_score = 0
    for rank, evaluation in enumerate(sorted(line_evaluations), start=1):
        _, _, bid = evaluation
        total_score += rank * bid


    return total_score

faces = 'ABCDE', 'A0CDE'

with open('advent23_7.txt', 'r') as file:
    lines = file.readlines()

for face in faces:
    line_evaluations = [evaluate_hand_and_bid(line.strip(), face) for line in lines]
    total_score = calculate_score(line_evaluations)
    print(total_score)
