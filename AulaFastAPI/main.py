from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

app = FastAPI()

engine = create_engine('postgresql://postgres:postgres@localhost:6700/postgres')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(bind=engine)

@app.get("/users")

def read_users():
    users = session.query(User).all()
    
    user_list = []

    for user in users:
        user_list.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })

    return JSONResponse(content=user_list)

@app.post("/users")

def create_user(name: str, email: str):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()

    return JSONResponse(content={
        "id": user.id,
        "name": user.name,
        "email": user.email
    })

@app.get("/users/{user_id}")

def read_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()

    return JSONResponse(content={
        "id": user.id,
        "name": user.name,
        "email": user.email
    })

