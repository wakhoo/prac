#pseudo code
#load a list of first names
#load a list of surnames
#choose a first name at random
#assign the name to a variable
#choose a surname at random
#assign the name to a variable
#print the names to the screen in order and in red font
#ask the user quit or play again
#if user plays again:
#   repeat
#if user quits:
#   end and exit


#책에 나온 코드는 재밌는 이름 만들어 보기 이지만 내 목표느 우선 랜덤으로 이름 만들기를 만들어본 이후에 수정을 해서 소설 속 주인공 이름 짓기와 같은 코드로 탈바꿈해 볼 예정

import sys, random

print("welcome to the random name picker!\n")

first = ('김','권','강','곽','나','노','이','우','유','연','라','박','임','오','고','신','공','양','차','전')

midle = ('은','원','채','정','지','기','소','서','연','미','온','제','영','용','강','윤','세','종','진','준')

last=('정','범','양','호','이','규','균','성','홍','윤','식','원','휘','현','란','영')

while True:
  firstName = random.choice(first)
  midleName = random.choice(midle)
  lastName = random.choice(last)
  
  
  print("\n\n")
  print("{}{}{}".format(fisrtName,midleName,lastName),file=sys.stderr)
  print("\n\n")
  
  try_again = input("\n\n Try again? (press enter n to quit)\n")
  if try_again.lower()=="n":
    break
    
  input("\n Press enter to exit.")
  
  
