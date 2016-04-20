import os
import sys
import transaction

from sqlalchemy import engine_from_config
from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from .models import (
    Nameh,User,
    Base,DBSession,Paygham,payam,groups,moerjah,etela,Image
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
        user=User(name='mohsen',lname='jahndideh',tel='0937239304',email='jahadideh72@yahoo.com',username='jahandideh626',password='10772',semat='test')
        nameh=Nameh(nnameh='اداری',mnameh='مرخصی',chnameh='درخواست مرخصی از ریاست',manameh='اابباتاا',recive='jahandide79',ersal="jahandide65",tarikher="jun",mohlat="feb",jahat="eghdam",peyvast="no",st=0)
        p=Paygham(mpayam="hello",ersal="jahandide")
        pa=payam(mapyam="hello",mopyam="jkjkjk",ersal='jahandide',recive='jahandideh72')
        g=groups(usr="jahandideh79")
        e=etela(minfo="hihjkdsksfsdfjlkl")
        erj=moerjah(mer="edsaauyfsdf")
        im=Image(name='jahandide',img=config_uri('tutorial/images/peyvand.png'))
        DBSession.add(im)
        DBSession.add(pa)
        DBSession.add(g)
        DBSession.add(e)
        DBSession.add(erj)
        DBSession.add(p)
        DBSession.add(user)
        DBSession.add(nameh)
