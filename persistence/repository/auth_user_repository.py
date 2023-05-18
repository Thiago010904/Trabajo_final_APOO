import sqlalchemy as db
from persistence.model import Auth_user
from sqlalchemy.orm import Session

class AuthUserRepository():
    def __init__(self):
        self.engine = db.create_engine("sqlite:///db/login.sqlite", echo= False, future= True)

    def get_user_by_username(self, usern_name: str):
        user: Auth_user = None
        with Session(self.engine) as session:
            user = session.query(Auth_user).filter_by(username = usern_name).first()
        return user
    
    def insert_user(self, user: Auth_user):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()