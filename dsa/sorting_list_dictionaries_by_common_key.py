from operator import itemgetter, attrgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# rows_by_name = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# print(rows_by_name)
# print(rows_by_uid)

# rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
# print(rows_by_lfname)

# Alternative of itemgetter, using lamada
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))


# Sorting objects without native comparison

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)

print(sorted(users, key=lambda u: u.user_id))

print(sorted(users, key=attrgetter('user_id')))
