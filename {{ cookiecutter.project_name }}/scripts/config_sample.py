import argparse
import logging.config
import os
import sys

from dotenv import load_dotenv
from envyaml import EnvYAML

from {{cookiecutter.project_slug}}.example import hello, show_message

# Load root .env file
load_dotenv()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="path to configuration file", type=str)
    args = parser.parse_args()

    return args


def main():
    args = get_args()
    config = EnvYAML(args.config)

    env_var_value = os.getenv("ENV_VARIABLE")

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

    print(f"ENV_VARIABLE = {env_var_value}")


if __name__ == "__main__":
    sys.exit(main())
