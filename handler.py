from users import user_data

class UserHandler:
    def __init__(self, name):
        self.name = name

    def get_user_data(self):
        for item in user_data:
            for key, val in item.items():
                if key=='name':
                    if val==self.name:
                        return item

    def parse(self, user):
        return user.get('additional_info')
    
    def main(self):
        if self.name:
            if isinstance(self.name, str):
                resp = self.get_user_data()
                return resp


