from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import os
from dotenv import load_dotenv
SQLALCHAMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(
    SQLALCHAMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=10,
    max_overflow=20
)
SessinLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    phone = Column(String,unique=True,index=True)
    otp_code = Column(String,nullable=True)
    set_role = Column(String,nullable=True)
    Job = relationship("User",back_populates="owner")
    worker_vacansy = relationship("WorkerVacansy",back_populates="owner")

class WorkerVacansy(Base):
    __tablename__ = "worker_vacansy"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    experience = Column(String)
    salary = Column(String,nullable=True)
    location = Column(String)
    owner_id = Column(Integer,ForeignKey("users.id"))
    owner = relationship("Job",back_populates="worker_vacansy")
Base.metadata.create_all(bind=engine)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    experience = Column(String)
    salary = Column(String,nullable=True)
    location = Column(String)
    owner_id = Column(Integer,ForeignKey("users.id"))
    owner = relationship("Job",back_populates="jobs")
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessinLocal()
    try:
        yield db
    finally:
        db.close()
