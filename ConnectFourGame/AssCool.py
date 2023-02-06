"""
NAME : THERESA NATHANIA LAN
UPI : tlan121
ID : 569504563
DESCRIPTION : CS130 ASSIGNMENT 1 - FOUR IN A ROW WITH AI
"""
import sys
import time
shell = sys.stdout.shell

class GameBoard:
    def __init__(self, size):
        self.size = size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)] 
        self.points = [0] * 2
		
    def num_free_positions_in_column(self, column): #section 1
        col_size = self.size
        for e in self.items:
            if e[column] != 0:
                col_size -= 1 #reduce the size if a disk is inserted
        return col_size
    
    def game_over(self):
        row_col_total = self.size ** 2 #caculate the total slots
        sum_entries = 0
        for e in self.num_entries: #calculate the sum of entries 
            sum_entries += e
        return sum_entries == row_col_total #if the entries is equal to board size, it means there's no available slots and the game is finished
    
    def display(self, col):
        chosen_col = col
        comp_col = ""
        if col.lower() == "red":
            chosen_col = "COMMENT"
            comp_col = "STRING"
        elif col.lower() == "orange":
            chosen_col = "KEYWORD"
            comp_col = "DEFINITION"
        elif col.lower() == "green":
            chosen_col = "STRING"
            comp_col = "COMMENT"
        else:
            chosen_col = "DEFINITION"
            comp_col = "KEYWORD"

        for e in range(len(self.items) - 1, -1, -1): #board is flipped -> self.items[0] is at the very bottom, not at the top
            for i in self.items[e]: #iterate into each elements in self.items, if 0 = empty, 1 = player 1 (o) and 2 = player 2 (x)
                if i == 0:
                    print(" ", end = " ")
                elif i == 1:
                    shell.write("o ", chosen_col)
                    #print("o", end = " ")
                else:
                    shell.write("x ",comp_col)
                    #print("x", end = " ")
            print()
                     
        horizontal_line = (self.size * 2) - 1
        print(horizontal_line * "-") 
        for n in range (self.size):
            print(n, end=" ")
            
        print()
        
        points_p1 = self.points[0]
        points_p2 = self.points[1]
        print("Points player 1:", points_p1)
        print("Points player 2:", points_p2)
    
    def add(self, column, player): #section 2
        if self.num_entries[column] < 0 or self.num_entries[column] >= self.size: #column can't be <0 or >board size, so there are no entries for the column
            return False
        else:
            self.num_entries[column] += 1 #if available, a disk is inserted into the column
            if self.num_entries[column] <= self.size: #if the column still has an empty slot
                self.items[self.num_entries[column] - 1][column] = player
                new_pts = self.num_new_points(self.num_entries[column] - 1, column, player)
                self.points[player - 1] += new_pts
            return True

    def num_new_points(self, row, column, player): #section 3
        new_pts = 0

        new_pts += self.horizontal_check(row, column, player) #check for horizontal
        new_pts += self.vertical_check(row, column, player) #check for vertical
        new_pts += self.diagonal_check_left(row, column, player) #check for diagonal negative slope
        new_pts += self.diagonal_check_right(row, column, player) #check for diagonal positive slope

        return new_pts
    
    def total_count(self, count):
        #counts the total points from 2 directions of each horizontal, vertical and diagonals from the coordinate
        pts = ((count - 1) % 4) + 1 
        return pts
    
    def horizontal_check(self, r, c, player):
        pts = 0
        count1 = 1
        count2 = 1
        temp_c = c

        if c > 0:
            while self.items[r][temp_c - 1] == self.items[r][temp_c] and temp_c - 1>= 0 and temp_c >= c - 3: #left
                count1 += 1
                if count1 == 4:
                    break 
                temp_c -= 1
                
        temp_c = c
        if temp_c + 1 < self.size and self.items[r][temp_c + 1] != 0:
            while temp_c + 1 < self.size and self.items[r][temp_c + 1] == self.items[r][temp_c] and temp_c <= c + 3: #right
                count2 += 1
                if count2 == 4:
                    break 
                temp_c += 1

        #count the total points from both directions        
        if count1 + count2 > 4: 
            pts = self.total_count(count1 + count2)
            return pts
        return 0
                
    def vertical_check(self, r, c, player) :
        pts = 0
        count1 = 1
        count2 = 1
        temp_r = r
        if r > 0:
            while self.items[temp_r - 1][c] == self.items[temp_r][c] and temp_r - 1>= 0 and temp_r >= r - 3: #down
                count1 += 1
                if count1 == 4:
                    break
                temp_r -= 1
                
        temp_r = r
        if temp_r + 1 < self.size and self.items[temp_r + 1][c] != 0:
            while temp_r + 1 < self.size and self.items[temp_r + 1][c] == self.items[temp_r][c] and temp_r <= r + 3: #up
                count2 += 1
                if count2 == 4:
                    break
                temp_r += 1

        #count the total points from both directions       
        if count1 + count2 > 4: 
            pts = self.total_count(count1 + count2)
            return pts
        return 0 

    def diagonal_check_left(self, r, c, player):
        pts = 0
        count1 = 1
        count2 = 1
        temp_r = r
        temp_c = c
        if c > 0:
            while temp_c - 1 >= 0 and temp_r + 1 < self.size and self.items[temp_r + 1][temp_c - 1] == self.items[temp_r][temp_c] and temp_c >= c - 3 and temp_r <= r + 3: #up
                count1 += 1
                if count1 == 4:
                    break
                temp_c -= 1
                temp_r += 1

        temp_r = r
        temp_c = c
        if temp_r - 1 >= 0 and temp_c + 1 < self.size and self.items[temp_r - 1][temp_c + 1] != 0: #down
            while temp_r - 1 >= 0 and temp_c + 1 < self.size and self.items[temp_r - 1][temp_c + 1] == self.items[temp_r][temp_c] and temp_r >= r - 3 and temp_c <= c + 3: #down
                count2 += 1
                if count2 == 4:
                    break
                temp_c += 1
                temp_r -= 1

        #count the total points from both directions       
        if count1 + count2 > 4: 
            pts = self.total_count(count1 + count2)
            return pts
        return 0 
                
    def diagonal_check_right(self, r, c, player):
        pts = 0
        count1 = 1
        count2 = 1
        temp_r = r
        temp_c = c
        if c > 0:
            while temp_c - 1 >= 0 and temp_r - 1 >= 0:
                if self.items[temp_r - 1][temp_c - 1] == self.items[temp_r][temp_c]: #down
                    count1 += 1
                    if count1 == 4:
                        break
                temp_c -= 1
                temp_r -= 1
                
        temp_r = r
        temp_c = c
        if temp_r + 1 < self.size and temp_c + 1 < self.size and self.items[temp_r + 1][temp_c + 1] != 0: #up
            while temp_r + 1 < self.size and temp_c + 1 < self.size and self.items[temp_r + 1][temp_c + 1] == self.items[temp_r][temp_c] and temp_r <= r + 3 and temp_c <= c + 3: #up
                count2 += 1
                if count2 == 4:
                    break
                temp_r += 1
                temp_c += 1

        #count the total points from both directions        
        if count1 + count2 > 4: 
            pts = self.total_count(count1 + count2)
            return pts
        return 0  
        
    def free_slots_as_close_to_middle_as_possible(self): #section 4
        temp_lst = []
        for c in range (self.size): #append the numbers 0 up to size
            temp_lst.append(c)
        
        ordered_lst = []
        
        #the order always goes from left -> right -> left -> right -> ... starting from the mid value
        if len(temp_lst) % 2 == 0: #has 2 mid values
            r = len(temp_lst) // 2
            l = r - 1
            ordered_lst.append(temp_lst[l])
            ordered_lst.append(temp_lst[r])
            left = True #starts from left
            if len(temp_lst) > 1:
                while len(ordered_lst) <= len(temp_lst) and l >= 0 and r + 1 < len(temp_lst):
                    if left == True:
                        l -= 1
                        ordered_lst.append(temp_lst[l])
                        left = False #then takes the values from the right hand side
                    else:
                        r += 1
                        ordered_lst.append(temp_lst[r])
                        left = True 
            
        else: #has only 1 mid value
            mid = len(temp_lst) // 2
            ordered_lst.append(temp_lst[mid])
            if len(temp_lst) > 1:
                r = mid + 1
                l = mid - 1
                ordered_lst.append(temp_lst[l])
                ordered_lst.append(temp_lst[r])
                left = True
                while len(ordered_lst) <= len(temp_lst) and l >= 0 and r + 1 < len(temp_lst):
                    if left == True:
                        l -= 1
                        ordered_lst.append(temp_lst[l])
                        left = False
                    else:
                        r += 1
                        ordered_lst.append(temp_lst[r])
                        left = True

        #after arranging the values from middle to end points, filter out the ones which are still available to insert
        excluded_list = [] 
        for e in (ordered_lst):
            if self.num_entries[e] < self.size:
                excluded_list.append(e)
        return excluded_list
    
    def column_resulting_in_max_points(self, player): #section 5
        mid_val = {}
        lst = []
        close_to_mid = self.free_slots_as_close_to_middle_as_possible()
        for e in close_to_mid: 
            mid_val[e] = []

        #insert the coordinates [row, column] to the dictionary where the keys are the 'still available columns closest to the centre'    
        for row in range (self.size): 
            for col in range (self.size):
                if self.items[row][col] == 0:
                    mid_val[col].append([row,col])

        #extract the arranged coordinates back into a list for better iteration to each coordinates
        for e in mid_val.values(): 
            for i in e:
                lst.append(i)
  
        if player == 1:
            to_insert = self.player_1_move(lst) #returns [row, column, points]
            #check if below the coordinate for disk to be inserted is empty, if it is coordinate is invalid since connect 4 is a stack
            if to_insert[0] - 1 >= 0 and self.items[to_insert[0] - 1][to_insert[1]] == 0: 
                return (lst[0][1], 0) #if coordinate is invalid, returns the column closest to the middle with point = 0
            else:
                to_insert = (to_insert[1], to_insert[2]) #if valid, then returns a tuple of (column, points)

        else:
            to_insert = self.player_2_move(lst) #returns [row, column, points]
            #check if below the coordinate for disk to be inserted is empty, if it is coordinate is invalid since connect 4 is a stack
            if to_insert[0] - 1 >= 0 and self.items[to_insert[0] - 1][to_insert[1]] == 0: 
                return (lst[0][1], 0) #if coordinate is invalid, returns the column closest to the middle with point = 0
            else:
                to_insert = (to_insert[1], to_insert[2]) #if valid, then returns a tuple of (column, points)
        
        return to_insert
    
    def player_1_move(self, lst):
        for i in range(len(lst)):
            self.items[lst[i][0]][lst[i][1]] = 1 #assume that the disk is player 1
            pts = self.num_new_points(lst[i][0],lst[i][1],1) #check if there will be 4 points or more if the disk is put in that coordinate
            self.items[lst[i][0]][lst[i][1]] = 0 #initialise the disk back to 0
            if pts >= 1:
                self.items[lst[i][0]][lst[i][1]] = 0 #initialise the disk back to 0
                return [lst[i][0],lst[i][1], pts]
        if pts == 0:
            return [lst[0][0],lst[0][1], pts]

    def player_2_move(self, lst):
        for i in range(len(lst)):
            self.items[lst[i][0]][lst[i][1]] = 2 #assume that the disk is player 2
            pts = self.num_new_points(lst[i][0],lst[i][1],2) #check if there will be 4 points or more if the disk is put in that coordinate
            self.items[lst[i][0]][lst[i][1]] = 0 #initialise the disk back to 0
            if pts >= 1:
                self.items[lst[i][0]][lst[i][1]] = 0 #initialise the disk back to 0
                return [lst[i][0],lst[i][1], pts]
        if pts == 0:
            return [lst[0][0],lst[0][1], pts]

class FourInARow:
    def __init__(self, size):
        self.board=GameBoard(size)
        self.size = size
    def play(self):
        print("*****************NEW GAME*****************")
        choose_user_color = input("User choose your color(RED, ORANGE, GREEN, BLUE): ")
        while choose_user_color.lower() != "red" and choose_user_color.lower() != "orange" and choose_user_color.lower() != "green" and choose_user_color.lower() != "blue":
            choose_user_color = input("Please choose either RED, ORANGE, GREEN or BLUE: ")
        self.board.display(choose_user_color)
        player_number=0
        print()
        while not self.board.game_over():
            print("Player ",player_number+1,": ")
            if player_number==0:
                while True:
                    try:
                        column = int(input("Please input slot: "))
                    except ValueError:
                        print("Input must be an integer in the range 0 to", self.board.size)
                        if player_number + 1 == 1:
                            self.countdown(self.size)
                        continue
                    else:
                        if column<0 or column>=self.board.size:
                            print("Input must be an integer in the range 0 to", self.board.size)
                            if player_number + 1 == 1:
                                self.countdown(self.size)
                            continue
                        else:
                            if self.board.add(column, player_number+1):
                                break
                            else:
                                print("Column ", column, "is already full. Please choose another one.")
                                if player_number + 1 == 1:
                                    self.countdown(self.size)
                                continue
                
            else:
                # Choose move which maximises new points for computer player
                (c,maxPoints)=self.board.column_resulting_in_max_points(1)
                if maxPoints>0:
                    column=c
                else:
                    # if no move adds new points choose move which minimises points opponent player gets
                    (c,maxPoints)=self.board.column_resulting_in_max_points(2)
                    if maxPoints>0:
                        column=c
                    else:
                        # if no opponent move creates new points then choose column as close to middle as possible
                        column = self.board.free_slots_as_close_to_middle_as_possible()[0]
                self.board.add(column, player_number+1)
                print("The AI chooses column ", column)
            self.board.display(choose_user_color)   
            player_number=(player_number+1)%2

        chosen_col = ""
        comp_col = ""
        if choose_user_color.lower() == "red":
            chosen_col = "COMMENT"
            comp_col = "STRING"
        elif choose_user_color.lower() == "orange":
            chosen_col = "KEYWORD"
            comp_col = "DEFINITION"
        elif choose_user_color.lower() == "green":
            chosen_col = "STRING"
            comp_col = "COMMENT"
        else:
            chosen_col = "DEFINITION"
            comp_col = "KEYWORD"
            
        if (self.board.points[0]>self.board.points[1]):
            shell.write("Player 1 (circles) wins!", chosen_col)
            print()
            self.play_again()
        elif (self.board.points[0]<self.board.points[1]):    
            shell.write("Player 2 (crosses) wins!", comp_col)
            print()
            self.play_again()
        else:  
            shell.write("It's a draw!", "")
            print()
            self.play_again()
                          
    def countdown(self, size):
        game = GameBoard(size)
        time.sleep(1)
        print()
        need_help = input('Need help? (answer Y or N) ')
        print()
        need_help = need_help.upper()
        if need_help == "Y" :
            t = 5
            while t > 0:
                time.sleep(2)
                print(".", end='')
                t -= 1
            time.sleep(3)
            print()
            print()
            print("BEST MOVE: COLUMN", list(game.column_resulting_in_max_points(1))[0])
            print()
            time.sleep(1)
        else:
            time.sleep(2)
            print("GOOD LUCK!")
            print()
            time.sleep(1)

    def play_again(self):
        time.sleep(3)
        play_again = input("HAVING FUN? PLAY AGAIN? (Y or N)")
        play_again = play_again.upper()
        if play_again == "Y":
            board_size = 0
            while not 4 <= board_size <= 99:
                try:
                    board_size = int(input("Enter board size (4 to 99): "))
                       
                except ValueError:
                    print("Please enter a number!")
                    board_size = 0
                else:
                    if not 4 <= board_size <= 99: 
                        print("Invalid board size!")
                    
            game = FourInARow(board_size)
            game.play()
        else:
            time.sleep(2)
            print("THANK YOU FOR PLAYING!")        
            
board_size = 0
while not 4 <= board_size <= 99:
    try:
        board_size = int(input("Enter board size (4 to 99): "))
           
    except ValueError:
        print("Please enter a number!")
        board_size = 0
    else:
        if not 4 <= board_size <= 99: 
            print("Invalid board size!")
        
game = FourInARow(board_size)
game.play()
