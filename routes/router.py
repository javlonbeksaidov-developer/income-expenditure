from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from models.models import Attendances, Departments, Salaries, Users, Work_Schedules
from schemas.schemas import (
    AttendanceBase,
    DepartmentBase,
    SalaryBase,
    UserBase,
    Work_ScheduleBase,
)

router = APIRouter()

"""User"""


@router.post("/users/user-create/")
def create_user(user: UserBase, db: Session = Depends(get_db)):  # noqa: B008
    new_user = Users(
        name=user.name,
        surname=user.surname,
        phone_number=user.phone_number,
        email=user.email,
        position=user.position,
        department_id=user.department_id,
        salary=user.salary,
        is_active=user.is_active,
        hire_date=user.hire_date,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/")
def get_users(db: Session = Depends(get_db)):  # noqa: B008
    users = db.query(Users).all()
    return users


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):  # noqa: B008
    user = db.query(Users).filter(Users.id == user_id).first()
    return user


@router.put("/users/user-update/{user_id}")
def update_user(user_id: int, user: UserBase, db: Session = Depends(get_db)):  # noqa: B008
    db_user = db.query(Users).filter(Users.id == user_id).first()

    if not db_user:
        return {"message": "User not found"}

    db_user.name = user.name
    db_user.surname = user.surname
    db_user.phone_number = user.phone_number
    db_user.email = user.email
    db_user.position = user.position
    db_user.department_id = user.department_id
    db_user.salary = user.salary
    db_user.is_active = user.is_active
    db_user.hire_date = user.hire_date

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/users/user-delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):  # noqa: B008
    user = db.query(Users).filter(Users.id == user_id).first()

    if not user:
        return {"message": "User not found"}

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}


"""Departments"""


@router.post("/departments/department-create/")
def create_department(department: DepartmentBase, db: Session = Depends(get_db)):  # noqa: B008
    new_department = Departments(
        name=department.name,
        description=department.description,
    )
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department


@router.get("/departments/")
def get_departments(db: Session = Depends(get_db)):  # noqa: B008
    departments = db.query(Departments).all()
    return departments


@router.get("/departments/{department_id}")
def get_department_by_id(department_id: int, db: Session = Depends(get_db)):  # noqa: B008
    department = db.query(Departments).filter(Departments.id == department_id).first()
    return department


@router.put("/departments/department-update/{department_id}")
def update_department(
    department_id: int, department: DepartmentBase, db: Session = Depends(get_db)):  # noqa: B008
    db_department = (
        db.query(Departments).filter(Departments.id == department_id).first()
    )

    if not db_department:
        return {"message": "Department not found"}

    db_department.name = department.name
    db_department.description = department.description

    db.commit()
    db.refresh(db_department)
    return db_department


@router.delete("/departments/department-delete/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_department = (
        db.query(Departments).filter(Departments.id == department_id).first()
    )

    if not db_department:
        return {"message": "Department not found"}

    db.delete(db_department)
    db.commit()
    return {"message": "Department deleted"}


"""Work_Schedules"""


@router.post("/work-schudeles/create/")
def create_work_schudeles(
    work_schudeles: Work_ScheduleBase, db: Session = Depends(get_db)):  # noqa: B008
    new_work_schudeles = Work_Schedules(
        user_id=work_schudeles.user_id,
        start_time=work_schudeles.start_time,
        end_time=work_schudeles.end_time,
        work_hours=work_schudeles.work_hours,
        work_days=work_schudeles.work_days,
    )
    db.add(new_work_schudeles)
    db.commit()
    db.refresh(new_work_schudeles)
    return new_work_schudeles


@router.get("/work-schudeles/")
def get_work_schudeles(db: Session = Depends(get_db)):  # noqa: B008
    work_schudeles = db.query(Work_Schedules).all()
    return work_schudeles


@router.get("/work-schudeles/{work_schudele_id}")
def get_work_schudele_by_id(work_schudele_id: int, db: Session = Depends(get_db)):  # noqa: B008
    work_schudeles = (
        db.query(Work_Schedules).filter(Work_Schedules.id == work_schudele_id).first()
    )
    return work_schudeles


@router.put("/work-schudeles/update/{work_schudele_id}")
def update_work_schudele(
    work_schudele_id: int,
    work_schudele: Work_ScheduleBase,
    db: Session = Depends(get_db),):  # noqa: B008
    db_work_schudele = (
        db.query(Work_Schedules).filter(Work_Schedules.id == work_schudele_id).first()
    )

    if not db_work_schudele:
        return {"message": "Work schudele not found"}

    db_work_schudele.user_id = (work_schudele.user_id)
    db_work_schudele.start_time = (work_schudele.start_time)
    db_work_schudele.end_time = (work_schudele.end_time)
    db_work_schudele.work_hours = (work_schudele.work_hours)
    db_work_schudele.work_days = (work_schudele.work_days)

    db.commit()
    db.refresh(db_work_schudele)
    return db_work_schudele


@router.delete("/work-schudeles/delete/{work_schudele_id}")
def delete_work_schudele(work_schudele_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_work_schudele = (
        db.query(Work_Schedules).filter(Work_Schedules.id == work_schudele_id).first()
    )

    if not db_work_schudele:
        return {"message": "Work schudeles not found"}

    db.delete(db_work_schudele)
    db.commit()
    return {"message": "Work schudeles deleted"}


"""Attendance"""


@router.post("/attendance/create/")
def create_attendance(attendance: AttendanceBase, db: Session = Depends(get_db)):  # noqa: B008
    new_attendance = Attendances(
        user_id=attendance.user_id,
        date=attendance.date,
        check_in=attendance.check_in,
        check_out=attendance.check_out,
        worked_hours=attendance.worked_hours,
        status=attendance.status,
        last_minutes=attendance.last_minutes,
        note=attendance.note,
    )
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance


@router.get("/attendance/")
def get_attendances(db: Session = Depends(get_db)):  # noqa: B008
    attendance = db.query(Attendances).all()
    return attendance


@router.get("/attendance/{attendance_id}")
def get_attendance_by_id(attendance_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_attendance = (
        db.query(Attendances).filter(Attendances.id == attendance_id).first()
    )
    return db_attendance


@router.put("/attendance/update/{attendance_id}")
def update_attendance(
    attendance_id: int, attendance: AttendanceBase, db: Session = Depends(get_db)):  # noqa: B008
    db_attendance = (
        db.query(Attendances).filter(Attendances.id == attendance_id).first()
    )

    if not db_attendance:
        return {"message": "Attendance not found"}

    db_attendance.user_id = attendance.user_id
    db_attendance.date = attendance.date
    db_attendance.check_in = attendance.check_in
    db_attendance.check_out = attendance.check_out
    db_attendance.worked_hours = attendance.worked_hours
    db_attendance.status = attendance.status
    db_attendance.last_minutes = attendance.last_minutes
    db_attendance.note = attendance.note

    db.commit()
    db.refresh(db_attendance)
    return db_attendance


@router.delete("/attendance/delete/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_attendance = (
        db.query(Attendances).filter(Attendances.id == attendance_id).first()
    )

    if not db_attendance:
        return {"message": "Attendance not found."}

    db.delete(db_attendance)
    db.commit()
    return {"message": "Attendance deleted."}


"""Salaries"""


@router.post("/salary/create/")
def create_salary(salary: SalaryBase, db: Session = Depends(get_db)):  # noqa: B008
    new_salary = Salaries(
        user_id=salary.user_id,
        month=salary.month,
        year=salary.year,
        base_salary=salary.base_salary,
        worked_days=salary.worked_days,
        worked_hours=salary.worked_hours,
        late_minutes=salary.late_minutes,
        bonus=salary.bonus,
        deduction=salary.deduction,
        final_salary=salary.final_salary,
        paid_at=salary.paid_at,
    )
    db.add(new_salary)
    db.commit()
    db.refresh(new_salary)
    return new_salary


@router.get("/salary/")
def get_salary(db: Session = Depends(get_db)):  # noqa: B008
    salary = db.query(Salaries).all()
    return salary


@router.get("/salary/{salary_id}/")
def get_salary_by_id(salary_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_salary = db.query(Salaries).filter(Salaries.id == salary_id).first()
    return db_salary


@router.put("/salary/update/{salary_id}")
def update_salary(salary_id: int, salary: SalaryBase, db: Session = Depends(get_db)):  # noqa: B008
    db_salary = db.query(Salaries).filter(Salaries.id == salary_id).first()

    if not db_salary:
        return {"message": "salary not found"}

    db_salary.user_id = salary.user_id
    db_salary.month = salary.month
    db_salary.year = salary.year
    db_salary.base_salary = salary.base_salary
    db_salary.worked_days = salary.worked_days
    db_salary.worked_hours = salary.worked_hours
    db_salary.late_minutes = salary.late_minutes
    db_salary.bonus = salary.bonus
    db_salary.deduction = salary.deduction
    db_salary.final_salary = salary.final_salary
    db_salary.paid_at = salary.paid_at

    db.commit()
    db.refresh(db_salary)
    return db_salary


@router.delete("/salary/delete/{salary_id}")
def delete_salary(salary_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_salary = db.query(Salaries).filter(Salaries.id == salary_id).first()

    if not db_salary:
        return {"message": "salary not found"}

    db.delete(db_salary)
    db.commit()
    return {"message": "Deleted"}
