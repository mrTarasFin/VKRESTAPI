from sqlalchemy import Column, String, Integer, DateTime, Text
from config_db import Base


# Модель таблицы в базе данных
class DataRequest(Base):
    __tablename__="data_request"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    field_search = Column(String(50), nullable=False)
    id_user = Column(String(25), nullable=False)
    groups = Column(Text)
