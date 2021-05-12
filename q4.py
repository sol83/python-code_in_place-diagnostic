from karel.stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper()
        move()
        put_beeper()
        turn_left()
        move()
        put_beeper()
        turn_around()
        move()
        turn_left()
        if front_is_clear():
            for i in range(2):
                move()    

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
