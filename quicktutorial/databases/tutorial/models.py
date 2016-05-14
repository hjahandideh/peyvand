from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    Text, ForeignKey, BLOB)
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
class payam(Base):
    __tablename__='payamha'
    id=Column(Integer,primary_key=True,autoincrement=True)
    mapyam=Column(Text)
    mopyam=Column(Text)
    ersal=Column(Text,ForeignKey('user.username'))
    recive=Column(Text,ForeignKey('user.username'))
    usernam = relationship("User",foreign_keys="[payam.recive]")
    er=relationship("User",foreign_keys="[payam.ersal]")

class groups(Base):
    __tablename__='grooh'
    id=Column(Integer,primary_key=True,autoincrement=True)
    usr=Column(Text,ForeignKey('user.username'))
    er=relationship("User",foreign_keys="[groups.usr]")
class moerjah(Base):
    __tablename__='erjah'
    mer=Column(Text,primary_key=True)
class etela(Base):
    __tablename__='info'
    id=Column(Integer,primary_key=True,autoincrement=True)
    minfo=Column(Text)
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
        self.email=email
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
    jahat=Column(Text,ForeignKey('erjah.mer'))
    peyvast=Column(Text)
    vaseiyat=Column(Text)
    usernam = relationship("User",foreign_keys="[Nameh.recive]")
    er=relationship("User",foreign_keys="[Nameh.ersal]")
    erja=relationship("moerjah",foreign_keys="[Nameh.jahat]")
    def __init__(self,nnameh,mnameh,chnameh,manameh,recive,ersal,tarikher,mohlat,jahat,peyvast,vaseiyat):
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
        self.vaseiyat=vaseiyat
class Image(Base):
    __tablename__='img'
    name=Column(Text,ForeignKey('user.username'))
    img=Column(Text,primary_key=True)
    er=relationship("User",foreign_keys="[Image.name]")


class Paygham(Base):
    __tablename__='payam'
    id=Column(Integer,primary_key=True,autoincrement=True)
    mpayam=Column(Text)
    ersal=Column(Text,ForeignKey('user.username'))
    img=Column(Text)
    usernam = relationship("User",foreign_keys="[Paygham.ersal]")
    def __init__(self,mpayam,ersal,img):
        self.mpayam=mpayam
        self.ersal=ersal
        self.img=img
class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit'),(Allow,'group:admin','admin')]

    def __init__(self, request):
        pass







