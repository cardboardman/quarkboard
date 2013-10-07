import web, os
import settings as s
    
urls = (
    '/', 'Index',
    '/sam', 'Sam',
    '/joe', 'Joe',
)

class Index:
    def GET(self):
        return s.render.index()

class Joe:
    def GET(self):
        return s.render.joe()

class Sam:
    def GET(self):
        return s.render.sam()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
