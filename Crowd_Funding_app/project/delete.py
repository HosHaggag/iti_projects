import json
from modify import check_project_owner
from show import show_all_projects




def delete_project():
    project_id = input('please enter project id (press L/l to list all projects , q to quit): ')
    if project_id.lower() == 'q':
        return None
    if project_id.lower() == 'l':
        show_all_projects()
        return delete_project()
    if check_project_owner(project_id):
        raise Exception(check_project_owner(project_id))

    try:
        with open('projects.json') as file:
            projects = json.load(file)
    except FileNotFoundError:
        projects = []
    for project in projects:
        if project['id'] == project_id:
            projects.remove(project)
            with open('projects.json', 'w') as file:
                json.dump(projects, file, indent=4)
            return project
    else:
        print('project not found.')
        return None