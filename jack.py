import random
from art import*
from cards import*
from replit import clear

def score(hand):
  bust = False
  score = [0]
  for n in range(0,hand["number_of_cards"]):
    card = str("card_"+str(n+1))
    card_current = hand[card]["card_name"]
    if card_current == "Ace":
      #score1 = score[:]
      score1 = [x+1 for x in score]
      #score11 = score[:]
      score11 = [x+11 for x in score]
      score = score1 + score11
    else:
      val = int(hand[card]["card_value"])
      score = [x+val for x in score]
  score = [x for x in score if x<= 21]
  if score == []:
    score = 0
    print(f"Bust! ")
    bust = True
    #return score
    #return bust
  else:
    score = max(score)
    bust = "no"
    print(f"Score is {score}")
  #print(score) 
  #print(bust)
  return bust, score


def openingSequence(p_hand, c_hand):
  p_hand = AddtoHand(p_hand)
  p_hand = AddtoHand(p_hand)
  c_hand = AddtoHand(c_hand)
  printCards(p_hand)
  score(p_hand)
  return p_hand, c_hand

def compScore(c_hand):
  print(f"\n  The computer is showing")
  printCards(c_hand)
  print(f"===========================")


def randCard():
  card = random.choice(list(card_values.keys()))
  #card = "Ace"
  card_sym = random.choice(list(card_symbols.values()))
  card_value = card_values[card]
  return card, card_sym, card_value

def printCards(hand):
  list = []
  for n in range(0,hand["number_of_cards"]):
    card = str("card_"+str(n+1))
    card_current = hand[card]["card_name"] +" "+ hand[card]["card_symbol"]
    list.append(card_current)
  string = "   ".join(list)
  print(string)

def AddtoHand(hand):
  #how have function as an imput
  card, card_symbol, card_value =randCard()
  hand["number_of_cards"] += 1
  card_index = str("card_"+str(hand["number_of_cards"]))
  hand[card_index] = {
    "card_name" : card,
    "card_symbol" : card_symbol,
    "card_value" : card_value,
  }
  return hand