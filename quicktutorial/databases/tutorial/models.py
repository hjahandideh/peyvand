from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    Text, ForeignKey)
from pyramid.security import (
    Allow,
    Everyone,
    )
from sqlalchemy.orm import (
    scoped_session,
    relationship)
from zope.sqlalchemy import ZopeTransactionExtension
DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()



class User(Base):
    __tablename__='user'
    name=Column(Text)
    lname=Column(Text)
    tel=Column(Integer)
    email=Column(Text)
    username=Column(Text,primary_key=True)
    password=Column(Text)
    semat=Column(Text)
    def __init__(self,name,lname,tel,email,username,password,semat):
        self.name=name
        self.lname=lname
        self.tel=tel
        self.username=username
        self.password=password
        self.semat=semat
class Nameh(Base):
    __tablename__='nameh'
    id=Column(Integer,primary_key=True,autoincrement=True)
    nnameh=Column(Text)
    mnameh=Column(Text)
    chnameh=Column(Text)
    manameh=Column(Text)
    recive=Column(Text, ForeignKey('user.username'))
    ersal=Column(Text, ForeignKey('user.username'))
    tarikher=Column(Text)
    mohlat=Column(Text)
    jahat=Column(Text)
    peyvast=Column(Text)
    usernam = relationship("User",foreign_keys="[Nameh.recive]")
    er=relationship("User",foreign_keys="[Nameh.ersal]")
    def __init__(self,nnameh,mnameh,chnameh,manameh,recive,ersal,tarikher,mohlat,jahat,peyvast):
        self.nnameh=nnameh
        self.mnameh=mnameh
        self.chnameh=chnameh
        self.manameh=manameh
        self.recive=recive
        self.ersal=ersal
        self.tarikher=tarikher
        self.mohlat=mohlat
        self.jahat=jahat
        self.peyvast=peyvast

class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit'),(Allow,'group:admin','admin')]

    def __init__(self, request):
        pass







