
import keyboard
import time
import random

# Map configuration (15x15 matrix)
WIDTH = 15
HEIGHT = 15

# Player position
position_x = 0  
position_y = 0  

# Beeper position
beeper_position_x = random.randint(0, 14)
beeper_position_y = random.randint(0, 14)

# Score
points = 0

# Time configuration
TIME_LIMIT = 30  # Total game time in seconds

def draw_scene(time_remaining):
    """Draws the map, score, and remaining time"""
    scene = ""
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == position_x and y == position_y:
                scene += "🧍"  
            elif x == beeper_position_x and y == beeper_position_y:
                scene += "💎"  
            else:
                scene += " . "  
        scene += "\n"

    print("\n" * 15)

    # Display remaining time formatted with one decimal place
    print(f"⏱️ TIME: {time_remaining:.1f}s | 🏆 POINTS: {points}")
    print(scene)
    print("Controls: W/A/S/D SPACE to catch the beeper, Q to quit the game | Catch all beepers before time runs out!")

def check_beeper_collision():
    global points, beeper_position_x, beeper_position_y
    if position_x == beeper_position_x and position_y == beeper_position_y:
        points += 1
        beeper_position_x = random.randint(0, 14)
        beeper_position_y = random.randint(0, 14)

def main():
    global position_x, position_y
    print("")
    print("CATCH THE BEEPERS 💎\n")
    print("Welcome to the game! Your goal is to catch all beepers before time runs out.\n")
    print("Controls: W/A/S/D to move, SPACE to catch the beeper, Q to quit the game.\n")
    print("Get ready! The game will start shortly...\n")
    input("Press Enter to start...")
    time.sleep(1)
    
    # Reset the timer just before entering the main loop
    start_time = time.time()
    
    while True:
        # Calculate elapsed and remaining time
        elapsed_time = time.time() - start_time
        time_remaining = TIME_LIMIT - elapsed_time
        
        # IF TIME RUNS OUT, GAME ENDS
        if time_remaining <= 0:
            print("\n" * 15)
            print("TIME'S UP!! ⏱️❌\n")
            print(f"Congratulations, you scored a total of: {points} points. 🏆\n")
            print("Thanks for playing. See you next time! 👋\n")
            break
            
        # Draw the scene with remaining time
        draw_scene(time_remaining)
 
        # Player movement
        if keyboard.is_pressed('a') and position_x > 0:
            position_x -= 1
        elif keyboard.is_pressed('d') and position_x < 14:
            position_x += 1
        elif keyboard.is_pressed('w') and position_y > 0:
            position_y -= 1
        elif keyboard.is_pressed('s') and position_y < 14:
            position_y += 1
        elif keyboard.is_pressed('space'):
            check_beeper_collision()
        elif keyboard.is_pressed('q'):
            print(f"Game canceled. Final score: {points}")
            break
        
        time.sleep(0.1)

# Run the game with timer
main()