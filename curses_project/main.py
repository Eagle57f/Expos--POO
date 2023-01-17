import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time
import lutin


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    BLUE_AND_GREEN = curses.color_pair(1)
    BLUE_AND_BLACK = curses.color_pair(2)
    
    stdscr.attron(BLUE_AND_BLACK)
    stdscr.border()
    stdscr.attroff(BLUE_AND_BLACK)
    
    # Ajoute le rectangle intérieur droit
    stdscr.attron(BLUE_AND_BLACK)
    rectangle(stdscr, 1, curses.COLS//2, curses.LINES - 2, curses.COLS - 3)
    stdscr.attroff(BLUE_AND_BLACK)
    

    # Ajoute la zone intérieure droite
    win = curses.newwin(curses.LINES - 4, curses.COLS//2-3, 2, curses.COLS//2+1)
    stdscr.refresh()
    
    win.clear()
    win.addstr(0,0,"Quelle action veut tu executer?")
    win.addstr(2,0,"Attaquer", curses.A_REVERSE)
    win.addstr(4,0, "Plus")
    win.addstr(6,0, "jsj")
    win.addstr(8,0, "feffe")
    
    def attack():
        stdscr.addstr(2, 1, "Vous avez attaqué!")
    
    
    options = [
        ((2,0,"Attaquer"), attack),
        ((4,0, "Plus"),),
        ((6,0, "jsj"),),
        ((8,0, "grehgeheh"),),
    ]
    option_target = 0
    
    def options_display(option_target):
        for option_index in range(len(options)):
            win.addstr(10,0, str(option_index))
            win.addstr(11,0, str(option_target))
            if option_target == option_index:
                
                win.addstr(options[option_index][0][0], options[option_index][0][1], options[option_index][0][2], curses.A_REVERSE)
            else:
                win.addstr(options[option_index][0][0], options[option_index][0][1], options[option_index][0][2])
        win.refresh()
    
    win.refresh()
    
    while True:
        key = stdscr.getch()
        
        if key == 450:
            if option_target > 0:
                option_target -= 1
            options_display(option_target)
            
        elif key == 456:
            if option_target < len(options)-1:
                option_target += 1
            options_display(option_target)
            
        elif key == 27:
            stdscr.addstr(1, 1, "Arret du programme en cours")
            stdscr.refresh()
            time.sleep(2)
            break
        
        elif key == 10:
            stdscr.addstr(1, 1, f"Vous avez selectionné l'action {option_target}")
            options[option_target][1]()
            stdscr.refresh()
            
        else:
            stdscr.addstr(1, 1, str(key))

        win.refresh()
    
    
    


    # box = Textbox(win)
    # box.edit()
    # text = box.gather().strip().replace("\n", "")
    # stdscr.addstr(10, 40, text)



wrapper(main)