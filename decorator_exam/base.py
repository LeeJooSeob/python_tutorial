from models import AnonymousUser

class WSGIRequest(object):
    def __init__(self):
        self.user = AnonymousUser()

    def setUser(self, name):
        self.user.username = name

    def Login(self):
        self.user.is_active = True

