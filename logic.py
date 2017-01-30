from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import db_access
from models import Establishment, Country

some_engine = create_engine(db_access)
Session = sessionmaker(bind=some_engine)

session = Session()


# Так, конечно не работает
# print(session.query(Establishment).order_by(Country.name.asc()).all())
"""sqlalchemy.exc.ProgrammingError: (psycopg2.ProgrammingError) missing FROM-clause entry for table "Country_test"
LINE 2: FROM "Establishment_test" ORDER BY "Country_test".name ASC
                                           ^
 [SQL: 'SELECT "Establishment_test".id AS "Establishment_test_id", "Establishment_test".name AS "Establishment_test_name" \nFROM "Establishment_test" ORDER BY "Country_test".name ASC']"""

# Пробую приджоинить Country
print(session.query(Establishment).join(Country).order_by(Country.name.asc()).all())
"""sqlalchemy.exc.InvalidRequestError: Could not find a FROM clause to join from.  Tried joining to <class 'models.Country'>, but got: Can't find any foreign key relationships between 'Establishment_test' and 'Country_test'."""

# Цель - сортировать (равно как и фильтровать) Establishment по business адресу, но куда засунуть условие по типу адреса не понимаю
