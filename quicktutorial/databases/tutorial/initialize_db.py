import os
import sys

import transaction
from sqlalchemy import engine_from_config
from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
from sqlalchemy.exc import IntegrityError

from tutorial.models import (

    Base,Session,User,Groups
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    try:
        session = Session()
        user1 = User('as','sasas','564545','deewe','genericuser', 'basic123','sd')
        group1 = Groups('basic')
        group2 = Groups('secured')
        session.add(group1)
        session.add(group2)
        user1.mygroups.append(group1)
        session.add(user1)
        transaction.commit()
    except IntegrityError:
        pass

