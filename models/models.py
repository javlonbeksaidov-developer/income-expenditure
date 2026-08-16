from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    Time,
)
from sqlalchemy.orm import relationship

from database.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=30))
    surname = Column(String(length=30))
    phone_number = Column(String(length=20))
    email = Column(String, unique=True)
    position = Column(String)
    salary = Column(Float)
    is_active = Column(Boolean, default=True)
    hire_date = Column(DateTime)
    created_at = Column(TIMESTAMP)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department_table = relationship("Departments", back_populates="user")
    work_schedules_table = relationship("Work_Schedules", back_populates="user")
    attendances_table = relationship("Attendances", back_populates="user")
    salaries_table = relationship("Salaries", back_populates="user")


class Departments(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50))
    description = Column(Text)
    created_at = Column(TIMESTAMP)

    user = relationship("Users", back_populates="department_table")


class Work_Schedules(Base):
    __tablename__ = "work_schedules"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(Time)
    end_time = Column(Time)
    work_hours = Column(Float)
    work_days = Column(String)

    user = relationship("Users", back_populates="work_schedules_table")


class Attendances(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Enum)
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    worked_hours = Column(Float)
    status = Column(Enum)
    last_minutes = Column(Integer)
    note = Column(Text)

    user = relationship("Users", back_populates="attendances_table")


class Salaries(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    month = Column(Integer)
    year = Column(Integer)
    base_salary = Column(Float)
    worked_days = Column(Integer)
    worked_hours = Column(Float)
    late_minutes = Column(Float)
    bonus = Column(Float)
    deduction = Column(Float)
    final_salary = Column(Float)
    paid_at = Column(DateTime)

    user = relationship("Users", back_populates="salaries_table")
