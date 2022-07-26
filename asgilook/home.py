import falcon

file = open('./page/index.html')
file = file.read()

class Home:
    async def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_HTML
        # resp.status = falcon.HTTP_200
        # ya falcon pone por defecto el status 200
        resp.text = (file)
        


