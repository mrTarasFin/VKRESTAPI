from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Настройки соединения с базой данных MySQL
# На своем ноуте не смог настроить соединение с Postgres, проблема с драйвером была
# Решение этой проблемы оставлю для самостоятельного изучения
Base = declarative_base()
engine = create_engine("mysql+pymysql://root:admin@localhost:3306/mydb",
                        echo=True,
                        pool_pre_ping=True,
                        )

Session = sessionmaker(bind=engine)
session_db = Session()
