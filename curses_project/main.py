# https://docs.python.org/3/library/curses.html


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



    def setup_input(x = 3, y = 3, cols = 20, lines = 1, text = "Please enter your username:"):
        '''
        x (int): x position of top left corner of text_input box. Minimum value: 3
        y (int): y position of top left corner of text_input box. Minimum value: 3
        cols (int): length of text_input box
        lines (int): height of text_input box
        text (str): text to be displayed over the text_input box
        '''
        longest_line_length = 0
        for line in text.split('\n'):
            if len(line) > longest_line_length:
                longest_line_length = len(line)
        
        if cols + 3 >= longest_line_length:
            input_window_cols = cols + 3
        else:
            input_window_cols = len(longest_line_length)
        
        text_lines = len(text.split('\n')) - 1
        
        input_window = curses.newwin(lines + 4 + text_lines, input_window_cols, y - 2, x - 1) # Fenetre text_input
        input_window.addstr(0, 0, text)
        input = curses.newwin(lines, cols, y + text_lines, x)
        tb = Textbox(input)
        rectangle(input_window, 1 + text_lines, 0, lines + 2 + text_lines, cols + 1)
        input_window.refresh()
        input.refresh()
        tb.edit()
        output = tb.gather().strip().replace("\n", "")[:-1]
        stdscr.addstr(2, 1, f"{output}")
        input_window.clear()
        input_window.refresh()
        stdscr.refresh()

    options = [
        ((2,0,"Ajouter un soldat"), lambda: setup_input(curses.COLS - 36, 4, 20, 1, "Nom du soldat:\n\n(exit pour annuler)\nuuuuuuuuuuuu\nttttt")),
        ((4,0, "Plus"),),
        ((6,0, "jsj"),),
        ((8,0, "grehgeheh"),),
    ]
    option_target = 0
    
    def options_display(option_target = 0):
        for option_index in range(len(options)):
            win.addstr(10,0, str(option_index))
            win.addstr(11,0, str(option_target))
            if option_target == option_index:
                
                win.addstr(options[option_index][0][0], options[option_index][0][1], options[option_index][0][2], curses.A_REVERSE)
            else:
                win.addstr(options[option_index][0][0], options[option_index][0][1], options[option_index][0][2])
        win.refresh()



    # Ajoute le rectangle intérieur droit
    stdscr.attron(BLUE_AND_BLACK)
    rectangle(stdscr, 1, curses.COLS//2, curses.LINES - 2, curses.COLS - 3)
    stdscr.attroff(BLUE_AND_BLACK)
    



    # Ajoute la zone intérieure droite
    win = curses.newwin(curses.LINES - 4, curses.COLS//2-3, 2, curses.COLS//2+1)
    stdscr.refresh()
    win.clear()
    win.addstr(0,0,"Quelle action veut tu executer?")
    options_display()
    win.refresh()

    # Ajoute la fenetre d affiche d entrée
    key_input_window = curses.newwin(3, 6, curses.LINES-4, 2)
    key_input_window.attron(BLUE_AND_BLACK)
    key_input_window.border()
    key_input_window.attroff(BLUE_AND_BLACK)
    key_input_window.refresh()





    while True:
        key = stdscr.getch()
        
        if key in (450, 259) :
            if option_target > 0:
                option_target -= 1
            options_display(option_target)
            
        elif key in (456, 258):
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
        print(curses.LINES)
        

        key_input_window.addstr(1, 1, str(key))
        key_input_window.refresh()

    




wrapper(main)
