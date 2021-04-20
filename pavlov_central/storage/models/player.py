import peewee as pw
from pavlov_central.storage.models.base_model import BaseModel


class Player(BaseModel):
    email = pw.TextField(primary_key=True)
    nickname = pw.TextField()
    power = pw.IntegerField()

    class Meta:
        table_name = 'players'

    @property
    def serialize(self):
        data = {
            'email': self.email,
            'nickname': self.nickname,
            'power': self.power
        }
        return data
