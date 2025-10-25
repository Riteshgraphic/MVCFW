from fwfiles.ORM.base import Model
from fwfiles.ORM import feilds


class User(Model):
    __tablename__="users"

    id=feilds.IntegerField(primary_key=True, increment=True)
    name=feilds.CharField(max_length=255)
    password=feilds.CharField(max_length=255)
    status=feilds.CharField(max_length=255)