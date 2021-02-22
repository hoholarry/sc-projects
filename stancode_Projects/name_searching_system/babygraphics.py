"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    years = 0
    for i in YEARS:
        years += 1
    line_width = (width-GRAPH_MARGIN_SIZE*2)/years
    line_x_coordinate = GRAPH_MARGIN_SIZE + line_width*year_index
    return line_x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    for i in YEARS:
        index = YEARS.index(i)
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, index)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text = str(i), anchor = tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    for name in lookup_names:
        for year in YEARS:
            color_number = lookup_names.index(name)
            color = COLORS[color_number%4]
            print(name_data[name])
            if str(year) in name_data[name]:
                ranking = name_data[name][str(year)]

                x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)) + TEXT_DX
                y_coordinate = ((int(ranking) - 1) / 999) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) + GRAPH_MARGIN_SIZE

                canvas.create_text(x_coordinate, y_coordinate, text=name + ' ' + ranking, anchor=tkinter.SW, fill=color)

                if year == 2010:
                    pass

                elif str(year+10) not in name_data[name]:
                    next_x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)+1) + TEXT_DX
                    next_y_coordinate = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) + GRAPH_MARGIN_SIZE

                    canvas.create_line(x_coordinate - TEXT_DX, y_coordinate, next_x_coordinate, next_y_coordinate,
                                       fill=color)

                else:
                    next_ranking = name_data[name][str(year + 10)]

                    next_x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year) + 1) + TEXT_DX
                    next_y_coordinate = ((int(next_ranking) - 1) / 999) * (
                                CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) + GRAPH_MARGIN_SIZE

                    canvas.create_line(x_coordinate-TEXT_DX, y_coordinate, next_x_coordinate, next_y_coordinate, fill=color)

            else:
                x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)) + TEXT_DX
                y_coordinate = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) + GRAPH_MARGIN_SIZE
                canvas.create_text(x_coordinate, y_coordinate, text=name+' *', anchor=tkinter.SW, fill=color)

                if str(year+10) in name_data[name]:
                    next_ranking = name_data[name][str(year + 10)]

                    next_x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year) + 1) + TEXT_DX
                    next_y_coordinate = ((int(next_ranking) - 1) / 999) * (
                            CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) + GRAPH_MARGIN_SIZE

                    canvas.create_line(x_coordinate-TEXT_DX, y_coordinate, next_x_coordinate, next_y_coordinate, fill=color)
                else:
                    next_x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year) + 1) + TEXT_DX
                    canvas.create_line(x_coordinate-TEXT_DX, y_coordinate, next_x_coordinate, y_coordinate, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()

if __name__ == '__main__':
    main()
