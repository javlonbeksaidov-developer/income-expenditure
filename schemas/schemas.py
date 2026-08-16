from datetime import datetime, time

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str
    phone_number: str
    email: str
    position: str
    department_id: int
    salary: float
    is_active: bool
    hire_date: datetime


class DepartmentBase(BaseModel):
    name: str
    description: str


class Work_ScheduleBase(BaseModel):
    user_id: int
    start_time: time
    end_time: time
    work_hours: float
    work_days: str


class AttendanceBase(BaseModel):
    user_id: int
    date: str
    check_in: datetime
    check_out: datetime
    worked_hours: float
    status: str
    last_minutes: int
    note: str


class SalaryBase(BaseModel):
    user_id: int
    month: int
    year: int
    base_salary: float
    worked_days: int
    worked_hours: float
    late_minutes: float
    bonus: float
    deduction: float
    final_salary: float
    paid_at: datetime
