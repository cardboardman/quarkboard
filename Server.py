import web, os
import settings as s
    
urls = (
    '/', 'Index',
    '/about', 'About',
    '/blog', 'Blog',
    '/projects', 'Projects',
    '/python', 'Python'
)

def Make(func, name, funcParse = [""]):
    if len(funcParse) and funcParse != [""]:
        return str(s.render.header(name))+str(func(funcParse))+str(s.render.footer())
    return str(s.render.header(name))+str(func())+str(s.render.footer())

class Index:
    def GET(self):
        return Make(s.render.index, "Peilonrayz")

class About:
    def GET(self):
        return Make(s.render.about, "About")

class Blog:
    def GET(self):
        i = web.input(b="")
        if i['b'] != "":
            b = s.Blogs._lookup(i['b'])[1]
            if b != None:
                return s.Format([Make(s.Blogs._template(i['b']), s.BlogsList[int(i['b'])])])
        return Make(s.render.blog, "Blog", s.BlogsList)

class Projects:
    def GET(self):
        i = web.input(p="")
        if i['p'] != "":
            p = s.Projects._lookup(i['p'])[1]
            if p != None:
                return s.Format([Make(s.Projects._template(i['p']), s.ProjectsList[int(i['p'])])])
        return Make(s.render.projects, "Projects", s.ProjectsList)

class Python:
    def GET(self):
        i = web.input(p="")
        if i['p'] != "":
            p = s.Python._lookup(i['p'])[1]
            if p != None:
                return s.Format([Make(s.Python._template(i['p']), s.PythonList[int(i['p'])])])
        return Make(s.render.python, "Python", s.PythonList)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
