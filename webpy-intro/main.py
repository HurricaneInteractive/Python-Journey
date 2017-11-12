'''
    Project requires webpy  : http://webpy.org/
'''
import web

# defines a url path that can accept two parameters : http://baseurl/param1/param2
# maps this url to the index class
urls = (
    '/(.*)/(.*)', 'index'
)

# defines template location
render = web.template.render("resources/")
# defines app variable and passes in the urls
app = web.application(urls, globals())

# index class
class index:
    # defines a GET method with two arguements
    def GET(self, name, age):
        # returns main.html in the resources folder and passes two variables
        return render.main(name, age)

# Run the application
if __name__ == "__main__":
    app.run()
