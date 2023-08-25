


import json

def show_all_projects():
    try :
        with open('projects.json') as file:
            projects = json.load(file)
    except FileNotFoundError:
        projects = []
    for project in projects:
        print(f"project id: {project['id']}")
        print(f"project title: {project['title']}")
        print(f"project details: {project['details']}")
        print(f"project target: {project['target']}")
        print(f"project start date: {project['start_at']}")
        print(f"project end date: {project['end_at']}")
        print('-----------------------------')