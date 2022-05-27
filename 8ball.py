import random
from tracemalloc import stop

list_of_answers = [
    "It is certain", "Reply hazy, try again",	"Don’t count on it",
    "It is decidedly so", "Ask again later",	"My reply is no",
    "Without a doubt",	"Better not tell you now", "My sources say no",
    "Yes definitely",	"Cannot predict now",	"Outlook not so good",
    "You may rely on it",	"Concentrate and ask again",	"Very doubtful",
    "As I see it, yes",	   "Most likely",		"Outlook good",	 "Yes",		
    "Signs point to yes" ]


def game():
  random_answer = random.choice(list_of_answers)
  question = input ("Enter your question: ")
  print(random_answer)
  replay()


def replay():
  next_question = input ('Do you want to ask another question? [Y/N] ')
  if next_question == 'Y':
    game()
  elif next_question == 'N':
    print("Thank you for playing!")
    quit

game()