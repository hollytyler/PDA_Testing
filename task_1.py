
class CardGame:

# In the first function the first mistake would be the =' is meant to be '=='
# The second mistake is the syntax mistake of a missing ':' on the 'else'
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False


# In the second function the first mistake is the spelling mistake 'dif' should be 'def'
# - without 'def' the function is not defined
# The second mistake is in the first return its asking to return 'card' but card doesnt exist in this function
# - the return should be asking for 'card1' otherwise it will not know what to return
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# In the third function, the first mistake is an indentation error. 
# - def should be indented by one otherwise the function will not be properly defined
# The next mistake is that total has no given value
# - it needs to have an '=' with the given value
# The next mistake is that the return needs to be a formatted string. 
# - return a Str + and Int unless its returned like 'f("You have a total of + {total}")
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  