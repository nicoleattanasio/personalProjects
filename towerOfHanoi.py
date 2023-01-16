#created by Nicole Attanasio
#Tower of Hanoi command line game

#building elements
elements = ["|", "_", "___", "_____", "_______"]

#constructor
def newGame():
   global tower
   global totalMoves
   totalMoves = -1
   tower = [[4,3,2,1], [], []]
   printTowers()

#prints instructions and game template
def printTowers():
   global totalMoves
   totalMoves += 1
   line = ""
   print("\u0332".join("Game Instructions "))
   print("The objective of this game is to move all of the disks\n"
         "from the first tower to the third tower in as few moves as possible\n")
   print("\u0332".join("Rules "))
   print("You can only move one disk at a time and can never place a\n"
         "disk on top of a disk smallar than itself")

   print("~"*7*3)
   for row in range(3, -1, -1):
      for col in range(3): #number of towers
         try:
            line += elements[tower[col][row]].center(7)
         except IndexError:
            line += elements[0].center(7)
      print(line)
      line = ""
   print("~"*7*3)

#moves disks
def gameEngine():
   while True:
      m = input("Enter inital tower number(1-3) followed by destination tower number(1-3): ")
      move = [int(i)-1 for i in m.split()]

      if len(tower[move[0]]):
         if len(tower[move[1]]):
            if tower[move[0]][-1] < tower[move[1]][-1]:
               tower[move[1]].append(tower[move[0]][-1])
               tower[move[0]].pop()
               printTowers()
            else:
               print("Invalid move.")
         else:
            tower[move[1]].append(tower[move[0]][-1])
            tower[move[0]].pop()
            printTowers()
      else:
         print("Invalid move.")

      #detect when game is complete
      if len(tower[2]) == 4:
         print("CONGRATULATIONS YOU WON!!!\nYou finished it in", totalMoves, "moves!")
         if totalMoves == 15:
            print("This was the optimal number of moves.")
         else:
            print("This was not the optimal number of moves.")
         break


playAgain = "y"
while playAgain == "y":
   newGame()
   gameEngine()
   playAgain = input("Play again? (y/n) ")