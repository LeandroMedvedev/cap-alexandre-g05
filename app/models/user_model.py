from dataclasses import dataclass

from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.configs import db
from app.exceptions import InvalidEmailError


@dataclass
class UserModel(db.Model):
    id: int
    name: str
    email: str
    skills: list
    works: list

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    is_validate = Column(Boolean, default=False)
    password_hash = Column(String)

    skills = relationship('SkillModel', cascade='all,delete', backref='user')

    works = relationship('WorkModel', cascade='all,delete', backref='user')

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email or not email.endswith('.com'):
            raise InvalidEmailError

        return email.lower()

    @property
    def password(self):
        raise AttributeError('Password cannot be accessed!')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, compare_to_password):
        return check_password_hash(self.password_hash, compare_to_password)
