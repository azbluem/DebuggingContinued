from gameoflife import width, height, stage, print_stage, count_neighbors

def init_stage(stage):
    for v_pos in range(0, height):
      for h_pos in range(0, width):
        if h_pos == 1:
          stage[v_pos][h_pos] = True
        else:
          stage[v_pos][h_pos] = False

# Generation Rules:
# 1. Any live cell with < 2 neighbors dies
# 2. Any live cell with 2-3 neighbors lives
# 3. Any live cell with > 3 neighbors dies
# 4. Any dead cell with 3 neighbors comes alive

def one_generation(stage):
    new_board=[]
    for i in range(height):
        new_board.append([False]*width)
    for v_pos in range(len(stage)):
        for h_pos in range(len(stage[v_pos])):
            neighbors = count_neighbors(stage, v_pos, h_pos)
            if not stage[v_pos][h_pos] and neighbors == 3:
                new_board[v_pos][h_pos] = True
            #elif stage[v_pos][h_pos] and neighbors < 2:
                #new_board[v_pos][h_pos] = False
            elif stage[v_pos][h_pos] and (neighbors == 2 or neighbors == 3):
                new_board[v_pos][h_pos] = True
            else: #stage[v_pos][h_pos] and neighbors > 3:
                new_board[v_pos][h_pos] = False
    stage=new_board
    return new_board
                

init_stage(stage)
game_range=["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"]
for gen in range (len(game_range)):
    print(f"{game_range[gen]} Generation:")
    print_stage(stage)
    stage = one_generation(stage)