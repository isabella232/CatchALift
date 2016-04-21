groups = {
    0:'CALadmin',
    1:'Coaches',
    2:'Users',
}

def get_group(user, group):
    return len(user.groups.filter(group))
