from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import datetime
import sqlalchemy as sa
import os
from hashlib import sha1
from sqlalchemy import (
    Column,DateTime,
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
Session = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
class Groups(Base):
    __tablename__ = 'groups'
    id = sa.Column(sa.Integer,
                   sa.Sequence('groups_seq_id', optional=True),
                   primary_key=True)
    groupname = sa.Column(sa.Unicode(255), unique=True)

    def __init__(self, groupname):
        self.groupname = groupname
class payam(Base):
    __tablename__='payamha'
    id=Column(Integer,primary_key=True,autoincrement=True)
    state=Column(Integer)
    mapyam=Column(Text)
    mopyam=Column(Text)
    ersal=Column(Text,ForeignKey('users.username'))
    recive=Column(Text,ForeignKey('users.username'))
    usernam = relationship("User",foreign_keys="[payam.recive]")
    er=relationship("User",foreign_keys="[payam.ersal]")

class groups(Base):
    __tablename__='grooh'
    id=Column(Integer,primary_key=True,autoincrement=True)
    usr=Column(Text,ForeignKey('users.username'))
    er=relationship("User",foreign_keys="[groups.usr]")
class moerjah(Base):
    __tablename__='erjah'
    mer=Column(Text,primary_key=True)
class etela(Base):
    __tablename__='info'
    id=Column(Integer,primary_key=True,autoincrement=True)
    minfo=Column(Text)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
class Nameh(Base):
    __tablename__='nameh'
    id=Column(Integer,primary_key=True,autoincrement=True)
    nnameh=Column(Text)
    mnameh=Column(Text)
    chnameh=Column(Text)
    manameh=Column(Text)
    recive=Column(Text, ForeignKey('users.username'))
    ersal=Column(Text, ForeignKey('users.username'))
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
    name=Column(Text,ForeignKey('users.username'))
    img=Column(Text,primary_key=True)
    er=relationship("User",foreign_keys="[Image.name]")


class Paygham(Base):
    __tablename__='payam'
    id=Column(Integer,primary_key=True,autoincrement=True)
    mpayam=Column(Text)
    ersal=Column(Text,ForeignKey('users.username'))
    img=Column(Text)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    usernam = relationship("User",foreign_keys="[Paygham.ersal]")
    def __init__(self,mpayam,ersal,img,created_date):
        self.mpayam=mpayam
        self.ersal=ersal
        self.img=img
        self.created_date=created_date
class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer,
                   sa.Sequence('users_seq_id', optional=True),
                   primary_key=True)
    name = sa.Column(sa.Unicode(80), nullable=False)
    lname = sa.Column(sa.Unicode(80), nullable=False)
    tel = sa.Column(sa.Unicode(80), nullable=False)
    email = sa.Column(sa.Unicode(80), nullable=False)
    username = sa.Column(sa.Unicode(80), nullable=False, unique=True)
    password = sa.Column(sa.Unicode(80), nullable=False)
    semat = sa.Column(sa.Unicode(80), nullable=False)
    mygroups = relationship(Groups, secondary='user_group')

    def __init__(self,name,lname,tel,email, username, password,semat):
        self.name = name
        self.lname=lname
        self.tel = tel
        self.email = email
        self.username = username
        self._set_password(password)
        self.semat=semat

    @classmethod
    def by_id(cls, userid):
        return Session.query(User).filter(User.id == userid).first()

    @classmethod
    def by_username(cls, username):
        return Session.query(User).filter(User.username == username).first()

    def _set_password(self, password):
        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update((password + salt.hexdigest()).encode('UTF-8'))
        hashed_password = salt.hexdigest() + hash.hexdigest()

        self.password =hashed_password

    def validate_password(self, password):
        hashed_pass = sha1()
        hashed_pass.update((password + self.password[:40]).encode('UTF-8'))
        return self.password[40:] == hashed_pass.hexdigest()


user_group_table = sa.Table('user_group', Base.metadata,
                            sa.Column('user_id', sa.Integer, sa.ForeignKey(User.id)),
                            sa.Column('group_id', sa.Integer, sa.ForeignKey(Groups.id)),
                            )
class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'everybody'),
               (Allow, 'basic', 'entry'),
               (Allow, 'secured', ('entry', 'topsecret'))
               ]

    def __init__(self, request):
        pass



def groupfinder(userid, request):
    user = User.by_id(userid)
    return [g.groupname for g in user.mygroups]







