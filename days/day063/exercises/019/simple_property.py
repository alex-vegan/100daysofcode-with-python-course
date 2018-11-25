from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name:str, expires:datetime=NOW):
        self.name = name
        self.expires = expires
    
    @property
    def expired(self):
        return self.expires <= datetime.now()


if __name__ == "__main__":
    expired_obj = Promo('expired_object', datetime.now() - timedelta(seconds=5))
    print(f'{expired_obj.name} has been expired? {expired_obj.expired}')
    normal_obj = Promo('normal_object', datetime.now() + timedelta(days=1))
    print(f'{normal_obj.name} has been expired? {normal_obj.expired}')
    
