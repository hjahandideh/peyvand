from tutorial.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
some_engine = create_engine('sqlite:///peyvand.sqlite')
Session = sessionmaker(bind=some_engine)
session = Session()


GROUPS = {'editor': ['group:editors'],'admin':['group:admin']}
USERS=dict(session.query(User.username,User.password))
def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid,[])
