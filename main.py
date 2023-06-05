import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--players-count', type=int, default=2)
    args = parser.parse_args()


if __name__ == '__main__':
    main()
