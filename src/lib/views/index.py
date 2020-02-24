#! /usr/bin/env python3

from aiohttp.web import Response, View
import aiohttp_jinja2


class IndexView(View):
    async def get(self) -> Response:
        return aiohttp_jinja2.render_template("index.html", self.request, {})
