import falcon.asgi

# app = falcon.asgi.App()

from .config import Config
from .cache import RedisCache
from .images import Images, Thumbnails
from .store import Store
from .home import Home



def create_app(config=None):
    config = config or Config()
    cache = RedisCache(config)
    store = Store(config)
    images = Images(config, store)
    home = Home()
    thumbnails = Thumbnails(store)

    app = falcon.asgi.App(middleware=[cache])
    app.add_route('/', home)
    app.add_route('/images', images)
    app.add_route('/images/{image_id:uuid}.jpeg', images, suffix='image')
    app.add_route(
        '/thumbnails/{image_id:uuid}/{width:int}x{height:int}.jpeg',
        thumbnails
    )


    return app
    