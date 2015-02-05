import requests
import sys
from accounts.models import ListUser

class PersonAuthenticationBackend(object):

    def authenticate(self, assertion):
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('sending to mozilla', data, file=sys.stderr)
        resp = request.post('https://verifier.login.persona.org/verify', data=data)
        print('got', resp.content, file=sys.stderr)

        if resp.ok:
            verification_data = resp.json()

            if verification_data['status'] == 'okay':
                email = verification_data['email']
                try:
                    retrun self.get_user(email)
                except:
                    return ListUser.objects.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)

