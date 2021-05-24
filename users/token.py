  
from itsdangerous import TimedJSONWebSignatureSerializer

RAMDOM_STRING = 'uzia1&t+l6@_=rh$91n4nrlqmb3x7fq1fajw+9b!6u+2=c^4yh'

class Token():
    def check_token(self, user, token,**kwargs):
        s = TimedJSONWebSignatureSerializer(RAMDOM_STRING)
        try:
            data = s.loads(token)
            if data['email'] == user.email:
                return True
            else:
                False
        except:
            return False

    def give_token(self, **kwargs):
        s = TimedJSONWebSignatureSerializer(RAMDOM_STRING, expires_in=3600)
        token = s.dumps(kwargs).decode('utf-8')
        return token


token = Token()