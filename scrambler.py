import random

def generate_scramble(n, length):
    if n < 2:
        return "No scramble for a 1x1 cube."
    
    faces = ["R", "L", "U", "D", "F", "B"]
    modifiers = ["", "'", "2"]
    
    scramble = []
    last_move_face = None
    
    while len(scramble) < length:
        face = random.choice(faces)
        
        if last_move_face and (face == last_move_face or 
                               ('R' in [face, last_move_face] and 'L' in [face, last_move_face]) or
                               ('U' in [face, last_move_face] and 'D' in [face, last_move_face]) or
                               ('F' in [face, last_move_face] and 'B' in [face, last_move_face])):
            continue

        move = face
        
        if n > 3 and random.random() < 0.5:
            move += "w"
        
        if n > 5 and 'w' in move and random.random() < 0.5:
            deep_layer_moves = [str(i) for i in range(2, n // 2 + 1)]
            move = random.choice(deep_layer_moves) + move

        modifier = random.choice(modifiers)
        
        full_move = move + modifier
        scramble.append(full_move)
        
        last_move_face = face
    
    return " ".join(scramble)

print(f"3x3 scramble (20 moves): {generate_scramble(3, 20)}")
print(f"5x5 scramble (50 moves): {generate_scramble(5, 50)}")
print(f"7x7 scramble (70 moves): {generate_scramble(7, 70)}")
print(f"100x100 scramble (300 moves): {generate_scramble(100, 300)}")
print(f"1000x1000 scramble (800 moves): {generate_scramble(1000, 800)}")
