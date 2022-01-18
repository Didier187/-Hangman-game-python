#the hangman game

#generate the random word
# genrate blanks for as many letters in the word
#get user choice 
#if user choice is in word continue game
#replace the blank with a user choise at the  right Index if no blanks we are winning
# else loose a life, if there are still blanks Continue game
# if no blanks our man is dead
# end game

# garding teh outcome of the game
def grade_game(life, word):
  if(life == len(word)):
    print("your grade is A: You are a master at this")
  else:
    if life == len(word)-1:
      print("your grade is B+")
    elif life == len(word)-2:
      print("your grade is B")
    elif life == len(word)-3:
      print("your grade is c+")
    elif life == len(word)-4:
      print("your grade is c")
    else:
      print("not so bad")
#example word (mouse)
random_word = list("mouse")
#word equivalant _
blanks =[]
#game status
game_on =True
#life
life = len(random_word)
# generate blanks
for i in range(0, len(random_word)):
  blanks.append("_")


while game_on:
  user_choice = input("enter a letter\n")
  if(user_choice in random_word):
    blanks[random_word.index(user_choice)] = user_choice
    print(blanks)
    if(game_on):
      if("_" not in blanks):
        game_on = False
        grade_game(life,random_word)
        print(f"you won with {life} attempts remaining")
  else:
    print('lost a life')
    if(life > 0):
      game_on = True
      life-=1
      print(f"{life} lives remaining")
    else:
      game_on = False
      print("game: ",game_on)


  