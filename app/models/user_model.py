from datetime import datetime


class user:
    def __init__(self, id, firstname, lastname, othernames, email, phone_no,
                 username, IsAdmin):
                    self.id = id
                    self.firstname = firstname
                    self.lastname = lastname
                    self.email = email
                    self.phone_no = phone_no
                    self.username = username
                    self.registered_date = datetime.today()
                    self.IsAdmin = IsAdmin

    def create_user(self):
        user_details = {}
        user_details['id'] = self.id
        user_details['firstname'] = self.firstname
        user_details['lastname'] = self.lastname
        user_details['email'] = self.email
        user_details['phone_no'] = self.phone_no
        user_details['username'] = self.username
        user_details['registered_date'] = datetime.today()
        user_details['IsAdmin'] = self.IsAdmin
        return user_details
