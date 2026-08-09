import curses
import numpy as np
def innit():
    wg = np.zeros([9,9])
    wg[0] = [0,0,4, 0,9,3, 0,0,0]
    wg[1] = [3,0,0, 0,6,0, 0,9,5]
    wg[2] = [6,0,2, 0,7,0, 0,0,0]
    wg[3] = [0,0,0, 4,8,0, 1,5,6]
    wg[4] = [8,0,0, 6,5,2, 0,7,0]
    wg[5] = [5,0,0, 0,0,1, 4,0,0]
    wg[6] = [0,3,0, 0,0,0, 9,0,4]
    wg[7] = [1,8,0, 7,0,0, 0,0,2]
    wg[8] = [0,0,9, 0,0,0, 5,0,0]
    wg = wg.astype(int)
    return wg

def main(stdscr):
    # Initialize curses settings
    curses.curs_set(1)  # Make cursor visible
    stdscr.keypad(True)  # Enable arrow keys and special keys
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)  # Highlight style

    # Grid configuration (e.g., 5 rows by 5 columns)
    rows, cols = 9, 9
    grid = innit()

    # Current cursor coordinates within our grid
    curr_r, curr_c = 0, 0

    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        # Render instructions and helper UI
        instructions = "Use Arrow Keys / WASD to move. Type to input text. Press 'q' to quit."
        if max_y > rows + 4 and max_x > len(instructions):
            stdscr.addstr(0, 0, instructions)
            stdscr.addstr(
                1, 0, f"Current Grid Position -> Row: {curr_r + 1}, Col: {curr_c + 1}"
            )

        # Draw the grid cells
        # Let's offset the grid drawing down by 3 lines and left by 2 columns
        start_y, start_x = 3, 2

        for r in range(rows):
            for c in range(cols):
                # Calculate screen coordinates for each cell (giving each cell width of 5 chars)
                cell_y = start_y + (r * 2)
                cell_x = start_x + (c * 6)

                # Draw cell borders and content box
                if grid[r][c] == 0:
                    cell_str = f"[ ]"
                else:
                    cell_str = f"[{grid[r][c]}]"


                # Highlight the cell if the cursor is currently on it
                if r == curr_r and c == curr_c:
                    stdscr.addstr(cell_y, cell_x, cell_str, curses.color_pair(1))
                else:
                    stdscr.addstr(cell_y, cell_x, cell_str)

        # Explicitly place the physical terminal cursor onto the active cell
        active_y = start_y + (curr_r * 2)
        active_x = start_y + (curr_c * 6) + 1  # Point inside the brackets [ ]
        stdscr.move(active_y, active_x)

        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()

        if key == ord("q") or key == ord("Q"):
            break

        # Navigation handling
        elif key in (curses.KEY_UP, ord("w"), ord("W")):
            curr_r = max(0, curr_r - 1)
        elif key in (curses.KEY_DOWN, ord("s"), ord("S")):
            curr_r = min(rows - 1, curr_r + 1)
        elif key in (curses.KEY_LEFT, ord("a"), ord("A")):
            curr_c = max(0, curr_c - 1)
        elif key in (curses.KEY_RIGHT, ord("d"), ord("D")):
            curr_c = min(cols - 1, curr_c + 1)

        # Backspace / Deletion handling
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            grid[curr_r][curr_c] = 0

        # Standard Character Input handling
        elif 32 <= key <= 126:  
            # Printable ASCII characters
            grid[curr_r][curr_c] = chr(key)


if __name__ == "__main__":
    curses.wrapper(main)