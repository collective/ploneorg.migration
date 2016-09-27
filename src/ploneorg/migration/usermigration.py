import json
import transaction


def import_userdb(site):
    pas = site.acl_users
    users = pas.source_users
    thefile = open('userdb.txt', 'r')
    passwords = json.loads(thefile.read())
    thefile.close()

    for user in passwords:
        users.addUser(user, user, passwords[user])

    transaction.commit()
