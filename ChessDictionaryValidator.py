print("name:aditya.M,USN:1AY24AI004,sec:'M")
def is_valid_chess_board(board):
    valid_pieces={'pawn','knight','bishop','rook','queen','king'}
    valid_positions={f"{row}{col}"for row in range(1,9) for col in "abcdefgh"}
    piece_count={'w':{'pawn':0,'knoight':0,'bishop':0,'rock':0,'queen':0,'king':0},
             'b':{'pawn':0,'knight':0,'bishop':0,'rock':0,'queen':0,'king':0}
             }
    for position,piece in board.items():
         if position not in valid_positions:
              print(f"invalid positon:{position}")
              return False
         if len(piece)<2 or piece[0] not in ('w','b') or piece[1:] not in valid_pieces:
              print(f"invalid piece:{piece}")
              return False
         color=piece[0]
         name=piece[1:]
         piece_count[color][name] += 1

    if piece_count['w']['king'] !=1 or piece_count['b']['king'] != 1:
        print("each side must have exactly one king.")
        return False
    if sum(piece_count['w'].values())>16 or sum(piece_count['b'].values())>16:
        print("each side can have at most 16 pieces.")
        return False
    if piece_count['w']['pawn']>8 or piece_count['b']['pawn']>8:
        print("each side must have at most 8 pawns.")
        return False
    return True

chess_board={
    '1h':'bking',
    '6c':'wqueen',
    '2g':'bbishop',
    '5h':'bqueen',
    '3e':'wking'
}
if __name__=="__main__":
    if is_valid_chess_board(chess_board):
        print("the chess board is valid.")
    else:
        print("the chess board is invalid.")