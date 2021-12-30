import time
from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserProfile(BaseModel):
    nickname: str
    location: Optional[str] = None
    subscribed_newsletter: bool = True


class Model(BaseModel):
    # Don't do this
    d: datetime = datetime.now()


user = UserProfile(nickname="jdoe")
print(user)


o1 = Model()
print(o1.d)
time.sleep(1)
o2 = Model()
print(o2.d)
print(o1.d < o2.d)