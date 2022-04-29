from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text, DateTime

from app.configs import db


@dataclass
class CommentUserGroupModel(db.Model):
    id: int
    comments: str
    timestamp: str

    __tablename__ = "comments_users_groups"

    id = Column(Integer, primary_key=True)
    comments = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
