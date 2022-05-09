from tiles import TileManager


def run_game():

    tile_manager = TileManager()

    tile_manager.set_start_tile()

    while True:
        tile_manager.move_tile()

        score = tile_manager.score()
        if score != '':
            print(f'{score} won!')
            break

    prompt = input('\nPlay Again? (y/n): ')
    if prompt == 'y':
        run_game()


run_game()
