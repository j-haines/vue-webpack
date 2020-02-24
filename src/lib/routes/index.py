#! /usr/bin/env python3

from aiohttp.web import Application

from lib.views.index import IndexView


def add_routes(app: Application) -> None:
    app.router.add_view("/", IndexView)
