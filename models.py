from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base


engine = create_engine('sqlite:///parkinglot.db')

db_session = scoped_session(sessionmaker(autocommit=False,
                            bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Cars(Base):
    __tablename__ =  'cars'
    id = Column(Integer, primary_key=True)
    model = Column(String(50))
    plate = Column(String(7), index=True)
    driver_id = Column(Integer, ForeignKey('drivers.identity'))
    driver = relationship('Drivers')


    def __repr__(self):
        return '<Model {}, Plate {}>'.format(self.model, self.plate)
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Drivers(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    identity = Column(String(11), index=True)
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()