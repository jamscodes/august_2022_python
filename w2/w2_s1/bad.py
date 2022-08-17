jonathan = {
    'f_name': 'Jonathan',
    'l_name': 'Moore',
    'is_instructor': True,
    'is_cd_staff': True,
    'permissions': {
        'edit_site': True,
        'edit_discord_members': True
    }
}

rene = {
    'f_name': 'Rene',
    'l_name': 'Marino',
    'is_instructor': False,
    'is_cd_staff': True,
    'permissions': {
        'edit_site': True,
        'edit_discord_members': False
    }
}
def intro(name):
    print(name)

kyle = {
    'f_name': 'Kyle',
    'l_name': 'Doe',
    'is_instructor': False,
    'is_cd_staff': True,
    'permissions': {
        'edit_site': True,
        'edit_discord_members': False
    },
    'intro': intro('Kyle')
}
