# Membuat sample colllection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategi:  Lakukan iterasi pada salinan
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Buat collection baru
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status