import os
import sys
import transaction

from sqlalchemy import engine_from_config
from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from tutorial.models import (

    Base,DBSession,Paygham,payam,groups,moerjah,Image,Nameh,User,etela
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
        user=User(name='mohsen',lname='jahndideho',tel='0937239304',email='jahadideh72@yahoo.com',username='jahandideho',password='10772',semat='test')
        nameh=Nameh(nnameh='اداری',mnameh='مرخصی',chnameh='درخواست مرخصی از ریاست',manameh='اابباتاا',recive='jahandideh',ersal="jahandide",tarikher="jun",mohlat="feb",jahat="eghdam",peyvast="no",vaseiyat="0")
        p=Paygham(mpayam="hello",ersal="jahandide")
        pa=payam(mapyam="hello",mopyam="jkjkjk",ersal='jahandide',recive='jahandideh')
        g=groups(usr="jahandideh")
        e=etela(minfo="hihjkdskfspfsdfjlkl")
        erj=moerjah(mer="edsaafuyf'isdf")
        DBSession.add(pa)
        DBSession.add(g)
        DBSession.add(e)
        DBSession.add(erj)
        DBSession.add(p)
        DBSession.add(user)
        DBSession.add(nameh)
