from models import Drivers, db_session



def insert_driver(driver):
    driver.save


def search_driver(who):
    driver = Drivers.query.filter_by(who).first()


def all_drivers(): 
    drivers = Drivers.query.all

