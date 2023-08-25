import datetime
import json
import project_model




projects = []

def search_for_project_by_date():
    is_found = False
    global projects
    projects = get_all_projects()
    search_date = datetime.strptime(input('please enter date in project duration (i.e YYYY-MM-DD) : '), '%Y-%m-%d')
    for project in projects:
        if project.start_at <= search_date and project.end_at >= search_date:
            is_found = True
            print(f"project id: {project.id}")
            print(f"project title: {project.title}")
            print(f"project details: {project.details}")
            print(f"project target: {project.target}")
            print(f"project start date: {project.start_at}")
            print(f"project end date: {project.end_at}")
            print('-----------------------------')

    if not is_found:
        print('no projects up found in this date.')        
    return projects



def get_all_projects():
    global projects
    try :
        with open('projects.json') as file:
            projects = json.load(file)

        for project in projects:
            project = project_model.Project(project)    
    except FileNotFoundError:
        projects = []


    return projects

