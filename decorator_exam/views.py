# Create your tests here.
from decorators import login_required
from base import WSGIRequest

#--- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        print('LoginRequiredMixin as_view')
        view = super(LoginRequiredMixin, cls).as_view()
        return login_required()

class View:
    def __init__(self):
        self.request = WSGIRequest()

    @classmethod
    def as_view(cls):
        print('View as_view')
        def view(request,*args, **kwargs):
            self = cls()
            print('View -> view fuc')
            return None
        return view

class CreateView(View):
    pass

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    pass;


if __name__ == "__main__":
    view_callbac = BookmarkCreateView.as_view()
    request = WSGIRequest()
    request.setUser(name='wntjq01')
    request.Login()
    view_callbac(request)


