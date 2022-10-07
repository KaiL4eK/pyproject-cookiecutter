import argparse
import logging.config
import sys

from envyaml import EnvYAML

from {{cookiecutter.project_slug}}.example import hello, show_message


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="path to configuration file", type=str)
    args = parser.parse_args()

    return args


def main():
    args = get_args()
    config = EnvYAML(args.config)

    try:
        logging.config.dictConfig(config["logger"])
    except Exception as e:
        print(e)
        print("Error in Logging Configuration. Using default configs")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

    greeting: str = hello(config["username"])
    show_message(greeting)


if __name__ == "__main__":
    sys.exit(main())
