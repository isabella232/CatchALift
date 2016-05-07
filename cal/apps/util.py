#Utility to populate common context for routing purposes
def common(request):
    context = dict()
    context['group'] = request.user.groups.all()[0].name
    context['page'] = request.path
    return context
