#Utility to populate common context for routing purposes and decorate views
from django.shortcuts import redirect

def common(request):
    context = dict()
    context['group'] = request.user.groups.all()[0].name
    context['page'] = request.path
    return context

def admin_required(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if request.user.groups.all()[0].name != 'CALadmin':
                return redirect('home:index')
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)

def coach_required(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if request.user.groups.all()[0].name != 'Coach':
                return redirect('home:index')
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)

def user_required(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if request.user.groups.all()[0].name != 'User':
                return redirect('home:index')
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)
