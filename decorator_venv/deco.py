from functools import wraps

def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("아 진짜 안된다니까 그러네..")
        return func(*args, **kwargs)
    return wrapper

class Greet(object):
    current_user = None

    @is_admin
    def set_name(self, username):
        self.current_user = username

    @is_admin
    def get_greeting(self, username):
        """
        greeting

        :param username: 이름
        :type username: string
        """
        return "Hello {}".format(self.current_user)


greet = Greet()

print (greet.get_greeting.__name__)
# 'get_greeting'

print (greet.get_greeting.__doc__)