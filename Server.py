import web, os
import settings as s
import joeFunctions as jF
    
urls = (
    '/', 'Index',
    '/sam', 'Sam',
    '/joe', 'Joe',
)

class Index:
    def GET(self):
        return s.render.index("Quarkboard")

class Joe:
    def GET(self):
        return jF.GetWebpage(web, s.render.Joe)

class Sam:
    def GET(self):
        return Make(s.render.sam, "Mr. Cardboardman")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
