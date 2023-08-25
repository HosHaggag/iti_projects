import keyboard
import json
from project_model import Project
from show import show_all_projects
import setting





def modify_project():
    project_id = input('please enter project id ( press q to quit , press l to show all projects): ')
    if project_id.lower() == 'q':
        return None
    if project_id.lower() == 'l':
        show_all_projects()
        return modify_project()
    if check_project_owner(project_id):
        raise Exception(check_project_owner(project_id))

    try:
        with open('projects.json') as file:
            projects = json.load(file)
    except FileNotFoundError:
        projects = []
    for project in projects:
        if project['id'] == project_id:
            project = Project(project)
            project.title = input_with_default('please enter new title: ', project.title)
            project.details = input_with_default('please enter new details: ', project.details)
            project.target = input_with_default('please enter new target: ', project.target)
            project.start_at = project.str_to_date(input_with_default('please enter new end date: ' , project.date_to_str(project.start_at)))
            project.end_at = project.str_to_date(input_with_default('please enter new end date: ' , project.date_to_str(project.end_at)))
            project.save()
            return project
    else:
        print('project not found.')
        return None
    




def check_project_owner(project_id):
    try:
        with open('projects.json') as file:
            projects = json.load(file)
    except FileNotFoundError:
        projects = []
    for project in projects:
        if project['id'] == project_id:
            if project['owner_id'] == setting.user_data.mobile_number:
                return None
            else:
                return 'you are not the owner of this project.'
    else:
        return 'project not found.'   






def input_with_default(prompt_, default_):
    keyboard.write(default_)
    return input(prompt_)    