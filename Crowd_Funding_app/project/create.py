import datetime
import json
from project_model import Project
import setting
from modify import check_project_owner
from show import show_all_projects




def create_project():
    project_title = input('enter project title: ')
    project_details = input('enter project details: ')
    project_target = input('enter project target: ')
    project_start_at = input('enter project start date (i.e YYYY-MM-DD ) : ')
    project_end_at = input('enter project end date (i.e YYYY-MM-DD ) : ')
    project = Project({
        'id': generate_project_id(),
        'owner_id': setting.user_data.mobile_number,
        'title': project_title,
        'details': project_details,
        'target': project_target,
        'start_at': project_start_at,
        'end_at': project_end_at,
    })
    error = validate_project_data(project)
    if error:
        raise Exception(error)
    
    project.save()
    setting.project_data = project
    print('project created successfully')
    return project





def validate_project_data(project: Project):
    if project.title == '' or len(project.title) < 3:
        return 'project title is required and must be at least 3 characters.'
    if project.details == '' or len(project.details) < 10:
        return 'project details is required and must be at least 10 characters.'
    if project.target == '' or project.target < 100:
        return 'project target is required and must be at least 100 EGP.'
    if project.start_at == '' or project.start_at < datetime.now() :
        return 'project start date is required.'
    if project.end_at == '' or project.end_at < project.start_at  :
        return 'project end date is required.'
    
    return None




def generate_project_id():
    try:
        with open('projects.json') as file:
            projects = json.load(file)
    except FileNotFoundError:
        projects = []
    if len(projects) == 0:
        return 1
    return projects[-1]['id'] + 1