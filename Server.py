import web, os
import settings as s
    
urls = (
    '/', 'Index',
    '/sam', 'Sam',
    '/joe', 'Joe',
)

def Make(func, name, funcParse = [""]):
    if len(funcParse) and funcParse != [""]:
        return str(s.render.header(name))+str(func(funcParse))+str(s.render.footer())
    return str(s.render.header(name))+str(func())+str(s.render.footer())

class Index:
    def GET(self):
        return Make(s.render.index, "Quarkboard")

class Joe:
    def GET(self):
        return Make(s.render.joe, "Peilonrayz")

class Sam:
    def GET(self):
        return Make(s.render.sam, "Mr. Cardboardman")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
