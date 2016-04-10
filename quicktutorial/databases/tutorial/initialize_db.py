import os
import sys
import transaction

from sqlalchemy import engine_from_config
from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from .models import (
    Page,Nameh,User,Logi,
    Base,DBSession,
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
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        user=User(name='hasan',lname='jahndideh72',tel='0937239304',email='jahadideh72@yahoo.com',username='jahandideh72',password='10772',semat='test')
        nameh=Nameh(nnameh='اداری',mnameh='مرخصی',chnameh='درخواست مرخصی از ریاست',manameh='اابباتاا',recive='jahandide',ersal="jahandideh72",tarikher="jun",mohlat="feb",jahat="eghdam",peyvast="no")
        model = Page(title='Rootgh1', body='Roomj')
        l=Logi(username='jahandideh72',name='hh')

        DBSession.add(model)
        DBSession.add(l)
        DBSession.add(user)
        DBSession.add(nameh)
