import json
from project_model import Project




class User:
    def __init__(self, json_data):
        self.first_name = json_data['first_name']
        self.last_name = json_data['last_name']
        self.email = json_data['email']
        self.password = json_data['password']
        self.mobile_number = json_data['mobile_number']
        self.is_active = json_data['is_active']
        self.projects = self.get_user_projects(json_data['projects'])  
        

    def to_json(self):
         return {
             'first_name': self.first_name,
             'last_name': self.last_name,
             'email': self.email,
             'password': self.password,
             'mobile_number': self.mobile_number,
             'is_active': self.is_active,
             'projects': self.projects,
         }  
    

    def get_user_projects(self,projects_data):
        projects = []
        for project in projects_data:
            project = Project(project)
            projects.append(project)
        return projects
    


    def save(self):
        try:
            with open('users.json') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []
        for user in users:
            if user['email'] == self.email:
                users.remove(user)
                users.append(self.to_json())
                with open('users.json' , 'w') as file:
                    json.dump(users, file, indent=4)
                return user
        else :
            users.append(self.to_json())
            with open('users.json' , 'w') as file:
                json.dump(users, file, indent=4)
            return self.to_json()
    