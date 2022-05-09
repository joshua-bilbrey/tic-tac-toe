"""Create and control tic tac toe tiles."""


import os
from ascii import *
from key_press import get_key_press


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Tile:
    """Represents each square on the tic tac toe board."""
    def __init__(self, coord):
        # value can be 0 (nothing), 1 (x), or 2 (o)
        self.value = 0
        self.coordinate = coord


class TileManager:
    """Create board with coordinates and update when necessary."""
    def __init__(self):
        self.all_coords = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        self.all_tiles = []
        self.board_elements = []
        self.final_string = ''
        self.current_tile = None
        self.current_team = 1
        self.create_tiles()

    def create_tiles(self):
        for coord in self.all_coords:
            new_tile = Tile(coord)
            self.all_tiles.append(new_tile)

    def calculate_board(self):
        num = 1
        self.board_elements = []
        while num <= 9:
            for tile in self.all_tiles:

                if tile.coordinate == self.all_coords[num - 1]:
                    # create list of all board elements
                    self.board_elements.append(tile_dict[tile.value])
                    if num % 3:
                        self.board_elements.append(board_leg)

                num += 1

        # create full board string
        first_row = self.board_elements[:5]
        middle_row = self.board_elements[5:10]
        last_row = self.board_elements[10:]

        self.final_string = ''

        for row in [first_row, middle_row, last_row]:
            if self.final_string:
                self.final_string = self.final_string + '  ' + board_arm + '\n'
            working_list = []
            for index in range(5):
                split_string = row[index].split('\n')
                working_list.append(split_string)
            for inner_index in range(4):
                temp_string = '    '
                for outer_index in range(5):
                    temp_string += working_list[outer_index][inner_index]
                temp_string += '\n'
                self.final_string += temp_string

        # draw tic tac toe board
        self.draw_board()

    def draw_board(self):
        cls()
        print(logo)
        print(self.final_string)

    def set_start_tile(self):
        if self.all_tiles[4].value == 0:
            self.current_tile = self.all_tiles[4]
            self.all_tiles[4].value = self.current_team + 2
        else:
            for tile in self.all_tiles:
                if tile.value == 0:
                    self.current_tile = tile
                    tile.value = self.current_team + 2
                    break
        self.calculate_board()

    def set_selector(self, tile):
        # change value to empty, change tile, set to selector
        self.current_tile.value = 0
        self.current_tile = tile
        self.current_tile.value = self.current_team + 2

    def move_tile(self):
        def move(key):
            if key == 'Up' and current_coord[0] != 1:
                current_coord[0] -= 1
            elif key == 'Down' and current_coord[0] != 3:
                current_coord[0] += 1
            elif key == 'Left' and current_coord[1] != 1:
                current_coord[1] -= 1
            elif key == 'Right' and current_coord[1] != 3:
                current_coord[1] += 1

        press = get_key_press()

        if press in ['Up', 'Down', 'Left', 'Right']:
            # move selector
            current_coord = list(self.current_tile.coordinate)
            move(press)
            for tile in self.all_tiles:
                if tile.coordinate == tuple(current_coord) and tile.value == 0:
                    self.set_selector(tile)

            # allow skipping over filled tiles
            while current_coord != list(self.current_tile.coordinate):
                press_again = get_key_press()
                move(press_again)
                for next_tile in self.all_tiles:
                    if next_tile.coordinate == tuple(current_coord) and next_tile.value == 0:
                        self.set_selector(next_tile)

            self.calculate_board()

        elif press == 'Return':
            # select tile
            self.select_tile()
        else:
            # print error
            print(f'Press the arrow keys to move, or enter to place your letter. Current letter: '
                  f'\n{tile_dict[self.current_team]}')

    def select_tile(self):
        # set tile with current teams letter
        self.current_tile.value = self.current_team

        # change team from x to o or vice versa
        if self.current_team == 1:
            self.current_team = 2
        elif self.current_team == 2:
            self.current_team = 1
        self.set_start_tile()

    def score(self):
        score_dict = {tile.coordinate: tile.value for tile in self.all_tiles}
        empty_list = [key for key in score_dict if score_dict[key] in [0, 3, 4]]
        x_list = [key for key in score_dict if score_dict[key] == 1]
        o_list = [key for key in score_dict if score_dict[key] == 2]
        for team_list in [x_list, o_list]:
            winner = False
            if (1, 1) in team_list and (2, 2) in team_list and (3, 3) in team_list:
                winner = True
            elif (1, 3) in team_list and (2, 2) in team_list and (3, 1) in team_list:
                winner = True
            else:
                first_coords = [list_item[0] for list_item in team_list]
                second_coords = [list_item[1] for list_item in team_list]
                for num in range(1, 4):
                    if first_coords.count(num) == 3 or second_coords.count(num) == 3:
                        winner = True

            if winner:
                if team_list == x_list:
                    return 'X Team'
                if team_list == o_list:
                    return 'O Team'
        if len(empty_list) == 0:
            return "It's a tie! Nobody"
        else:
            return ''
