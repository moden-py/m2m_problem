from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class Country(Base):
    __tablename__ = 'Country_test'
    id = Column('id', Integer, primary_key=True)
    geoid = Column('geoid', Integer, nullable=False, unique=True)
    name = Column('name', String(64), nullable=False)


establishment_address = Table(
     'EstablishmentAddress_test',
     Base.metadata,
     Column('establishment_id', Integer, ForeignKey("Establishment_test.id")),
     Column('address_id', Integer, ForeignKey("Address_test.id"))
 )


class Address(Base):
    __tablename__ = 'Address_test'
    id = Column(Integer, primary_key=True)
    country_id = Column('Country_id', Integer, ForeignKey("Country_test.id"),
                        nullable=False)
    country = relationship("Country", foreign_keys=[country_id])
    type = Column(Enum('business',
                       'mail',
                       'billing',
                       name='address_type_test'), nullable=False)


class Establishment(Base):
    __tablename__ = 'Establishment_test'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(64), nullable=False)
    addresses = relationship('Address',
                             secondary=establishment_address,
                             lazy="dynamic",
                             backref=backref(
                                 'establishments',
                                 lazy='dynamic')
                             )
