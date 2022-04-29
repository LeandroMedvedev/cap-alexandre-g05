from dataclasses import dataclass

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates

from ..exceptions import LevelInvalidError
from app.configs import db


@dataclass
class SkillModel(db.Model):
    skill = str
    level = str

    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    skill = Column(String(100), nullable=False, unique=True)
    level = Column(String(50), nullable=False)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)

    @validates('level')
    def validade_importance(self, key, level):
        if (
            level != 'Iniciante'
            and level != 'Intermediario'
            and level != 'Avançado'
        ):
            raise LevelInvalidError
