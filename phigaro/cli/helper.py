import argparse
import os
import yaml

from phigaro.helper import setup


def main():
    home = os.getenv('HOME')
    parser = argparse.ArgumentParser(description="Phigaro setup helper")
    parser.add_argument('-c', '--config', default=os.path.join(home, '.phigaro.yml'))

    args = parser.parse_args()
    config = setup()

    with open(args.config, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)


if __name__ == '__main__':
    main()
