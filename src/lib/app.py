#! /usr/bin/env python3

import asyncio

from aiohttp.web import Application, run_app
from jinja2 import FileSystemLoader
import aiohttp_jinja2

from lib.config import ApplicationConfig
from lib.routes import index


class App:
    def __init__(self, config: ApplicationConfig) -> None:
        self._config = config

        asyncio.get_event_loop().set_debug(self._config.server.debug)

        self._app = Application()
        self._app["config"] = self._config

        self._register_app_hooks()
        self._init_extensions()

    def run_app(self) -> None:
        run_app(self._app, host=self._config.server.host, port=self._config.server.port)

    def setup_routes(self) -> None:
        self._setup_dynamic_routes()
        self._setup_static_routes()

    async def _on_app_cleanup(self, app: Application) -> None:
        pass

    async def _on_app_startup(self, app: Application) -> None:
        pass

    def _init_extensions(self) -> None:
        self._init_jinja2()

    def _init_jinja2(self) -> None:
        self._templates_loader = FileSystemLoader(self._config.resources.template_dirs)
        aiohttp_jinja2.setup(self._app, loader=self._templates_loader)

        self._app["static_root_url"] = self._config.resources.static_dir

    def _register_app_hooks(self) -> None:
        self._app.on_cleanup.append(self._on_app_cleanup)
        self._app.on_startup.append(self._on_app_startup)

    def _setup_dynamic_routes(self) -> None:
        index.add_routes(self._app)

    def _setup_static_routes(self) -> None:
        self._app.router.add_static("/static/dist", "static/dist", name="dist")
        self._app.router.add_static("/static/img", "static/img", name="img")
