import falcon.asgi

# app = falcon.asgi.App()

import falcon.asgi

from .config import Config
from .images import Images, Thumbnails
from .store import Store
from .home import Home


def create_app(config=None):
    config = config or Config()
    store = Store(config)
    images = Images(config, store)
    home = Home()
    thumbnails = Thumbnails(store)

    app = falcon.asgi.App()
    app.add_route('/images', images)
    app.add_route('/images/{image_id:uuid}.jpeg', images, suffix='image')
    app.add_route(
        '/thumbnails/{image_id:uuid}/{width:int}x{height:int}.jpeg',
        thumbnails
    )
    app.add_route('/', home)

    return app
    