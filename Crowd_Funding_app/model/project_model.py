

import datetime
import json
import re



class Project:

    def __init__(self, json_data):
        self.id = json_data['id']
        self.ownerId = json_data['owner_id']
        self.title = json_data['title']
        self.details = json_data['details']
        self.target = json_data['target']
        self.start_at = self.str_to_date(json_data['start_at'], '%Y-%m-%d')
        self.end_at = self.str_to_date(json_data['end_at'], '%Y-%m-%d')
        return self

    def to_json(self):
        return {
            'id': self.id,
            'owner_id': self.ownerId,
            'title': self.title,
            'details': self.details,
            'target': self.target,
            'start_at': self.date_to_str(self.start_at),
            'end_at':self.date_to_str(self.end_at),
        }
    


    def save(self):
        try:
            with open('projects.json') as file:
                projects = json.load(file)
        except FileNotFoundError:
            projects = []
        for project in projects:
            if project['id'] == self.id:
                projects.remove(project)
                projects.append(self.to_json())
                with open('projects.json' , 'w') as file:
                    json.dump(projects, file, indent=4)
                return project
        else :
            projects.append(self.to_json())
            with open('projects.json' , 'w') as file:
                json.dump(projects, file, indent=4)
            return self.to_json()    
        

    
    def str_to_date(self,date_str):
        if not re.match(r'^\d{4}-\d{2}-\d{2}', date_str):
            raise Exception('date format is invalid.')
        return datetime.strptime(date_str, '%Y-%m-%d')
    


    def date_to_str(self,date):
        if not isinstance(date, datetime):
            raise Exception('date format is invalid.')
        return date.strftime('%Y-%m-%d')
    




