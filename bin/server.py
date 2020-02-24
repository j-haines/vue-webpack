#! /usr/bin/env python3

from argparse import ArgumentParser, Namespace
import pathlib
import sys

from lib.app import App
from lib.config import ApplicationConfig, load_config


def main(opts: Namespace) -> int:
    config: ApplicationConfig = load_config(opts.config)

    app = App(config)
    app.setup_routes()

    try:
        app.run_app()

        return 0
    except Exception:
        return 1


def parse_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument(
        "-c",
        "--config",
        help="path to the server application config file",
        default=pathlib.Path("config/config.json").resolve(),
    )

    return parser.parse_args()


if __name__ == "__main__":
    opts = parse_args()

    sys.exit(main(opts))
