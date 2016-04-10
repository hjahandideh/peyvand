from tutorial.models import DBSession,User

GROUPS = {'editor': ['group:editors']}


USERS=dict(DBSession.query(User.username,User.password).all())


def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid,[])
