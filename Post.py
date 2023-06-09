from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200))
    content = Column(Text)
    category = Column(String(100))
    created_date = Column(TIMESTAMP)
    updated_date = Column(TIMESTAMP, default=func.current_timestamp())
    status = Column(Enum('publish', 'draft', 'thrash', name='post_status'))

    def __repr__(self):
        return f'<Post(title=\'{self.title}\', category=\'{self.category}\')>'