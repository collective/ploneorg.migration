import json
import transaction


def export_userdb(site):
    """ Exports all the users and passwords to a file """
    pas = site.acl_users
    users = pas.source_users
    thefile = open('userdb.txt', 'w')
    passwords = users._user_passwords
    result = dict(passwords)
    thefile.write(result)
    thefile.close()


def import_userdb(site):
    pas = site.acl_users
    users = pas.source_users
    thefile = open('userdb.txt', 'r')
    passwords = json.loads(thefile.read())
    thefile.close()

    for user in passwords:
        users.addUser(user, user, passwords[user])

    transaction.commit()
