import random

def minimax(depth, parent_index, maximizingPlayer, alpha, beta):

    if depth == 0:
        return values[parent_index]
 
    if maximizingPlayer:
      
        max_val = -int(1e9)
 
        for i in range(0, 2):
             
            backup_val = minimax(depth - 1, parent_index * 2 + i, False, alpha, beta)
            max_val = max(max_val, backup_val)
            alpha = max(alpha, max_val)

            if alpha >= beta:
                break
          
        return max_val
      
    else:
        min_val = int(1e9)
 
        for i in range(0, 2):
          
            backup_val = minimax(depth - 1, parent_index * 2 + i, True, alpha, beta)
            min_val = min(min_val, backup_val)
            beta = min(beta, min_val)
 
   
            if alpha >= beta:
                break
          
        return min_val

values = []
value = input("Enter your id: ")

min_point = int(value[4])
win_point = int(value[-1] + value[-2])
max_point = int(win_point * 1.5)

for i in range(8):
  values.append(int(random.randint(min_point, max_point)))

alpha = -int(1e9)
beta = int(1e9)
gained_point = minimax(3, 0, True, alpha, beta)

print(f"Generated 8 random points between the minimum and maximum point limits: {values}")
print(f"Total points to win: {win_point}")
print(f"Achieved point by applying alpha-beta pruning = {gained_point}")

if gained_point >= win_point:
  print("The winner is Optimus Prime")
else:
  print("The winner is Megatron")

#Task - 02
shuffle_quantity = int(value[3])
achieved_points = []

win_count = 0
for i in range(shuffle_quantity):
  random.shuffle(values)
  gained_point = minimax(3, 0, True, alpha, beta)
  achieved_points.append(gained_point)
  if gained_point >= win_point:
    win_count += 1
    
print()
print(f"After the shuffle:\nList of all points values from each shuffles: {achieved_points}")
print(f"The maximum value of all shuffles: {max(achieved_points)}")
print(f"Won {win_count} times out of {shuffle_quantity} number of shuffles")