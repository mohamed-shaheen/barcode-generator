from django.db import models
import os
from twilio.rest import Client
# Create your models here.


class Score(models.Model):
    result = models.PositiveIntegerField()


    def __str__(self):
        return str(self.result)


    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'the current result is bad - {self.result}',
                                        from_='+15017122661',
                                        to='+15558675310'
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)