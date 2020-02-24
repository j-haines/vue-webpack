#! /usr/bin/env python3

from typing import Sequence, Set
import json
import pathlib


class ResourcesConfig:
    def __init__(
        self, static_dir: str, static_url: str, template_dirs: Sequence[str],
    ) -> None:
        # The directory containing static asset files, e.g. img, js, etc
        self.static_dir: str = static_dir

        # The url path to prepend to static asset urls, e.g. example.com/static/index.js
        self.static_url: str = static_url

        # The list of directories to search for html template files.
        self.template_dirs: Set[str] = {
            str(pathlib.Path(template_dir).resolve()) for template_dir in template_dirs
        }


class ServerConfig:
    def __init__(self, debug: bool, host: str, port: int) -> None:
        # Should debug mode be enabled.
        self.debug = debug

        # The host address to bind the server socket to.
        self.host = host

        # The host port to bind the server socket to.
        self.port = port


class ApplicationConfig:
    def __init__(self, resources: ResourcesConfig, server: ServerConfig) -> None:
        self.resources = resources
        self.server = server


def load_config(fp: str) -> ApplicationConfig:
    with open(fp) as config_file:
        config_data = json.load(config_file)

        resources_data = config_data["resources"]
        resources_config = ResourcesConfig(
            static_dir=resources_data["static_dir"],
            static_url=resources_data["static_url"],
            template_dirs=resources_data["template_dirs"],
        )

        server_data = config_data["server"]
        server_config = ServerConfig(
            debug=server_data["debug"],
            host=server_data["host"],
            port=server_data["port"],
        )

    return ApplicationConfig(resources=resources_config, server=server_config)
