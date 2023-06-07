import argparse
import Game


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--players-count', type=int, default=2, choices=[*range(2, 11)])
    args = parser.parse_args()
    main_player_name = input("Введите ваше имя:")
    game = Game.MTSGame(main_player_name=main_player_name, players_count=args.players_count)
    game.start()
    game.finish()


if __name__ == '__main__':
    main()
