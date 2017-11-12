import web
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin',
    '/post-activity', "PostActivity",
    '/profile/(.*)', "Profile",
    '/settings', "Settings",
    '/update-settings', 'UpdateSettings',
    '/submit-comment', 'SubmitComment'
)

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})

# Classes/Routes
class Home:
    def GET(self):
        data = type('obj', (object,), {"username": "Adro", "password": "avocado1"})

        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data['user'] = isCorrect

        post_model = Posts.Posts();
        posts = post_model.get_all_posts()

        return render.Home(posts)


class Register:
    def GET(self):
        return render.Register()


class Login():
    def GET(self):
        return render.Login()
        

class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"


class Logout:
    def GET(self):
        session["user"] = None
        session_data['user'] = None

        session.kill()
        return "success"


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"


class Profile:
    def GET(self, username):
        # data = type('obj', (object,), {"username": "Adro", "password": "avocado1"})

        login = LoginModel.LoginModel()
        # isCorrect = login.check_user(data)

        # if isCorrect:
        #     session_data['user'] = isCorrect
        
        user_info = login.get_profile(username)
        
        post_model = Posts.Posts()
        posts = post_model.get_user_posts(username)
        return render.Profile(posts, user_info)


class Settings:
    def GET(self):
        return render.Settings()


class UpdateSettings:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        settings_model = LoginModel.LoginModel()
        if settings_model.update_info(data):
            return "success"
        else:
            return "Could not update :("


class SubmitComment:
    def POST(self):
        data = web.input()
        data.username = session_data["user"]["username"]

        post_model = Posts.Posts()
        added_comment = post_model.add_comment(data)

        if added_comment:
            return added_comment
        else:
            return "error"

if __name__ == "__main__":
    app.run()
