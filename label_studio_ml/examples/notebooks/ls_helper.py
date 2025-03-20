from json import JSONDecodeError
from label_studio_sdk.core.api_error import ApiError

def get_project_by_title(ls, project_title):
    projects = ls.projects.list()
    for p in projects:
        if p.title == project_title:
            return p
    return None

def get_project_by_id(ls, project_id):
    projects = ls.projects.list()
    for p in projects:
        if p.id == project_id:
            return p
    return None

def project_exists(ls, project_title):
    for p in ls.projects.list():
        if p.title == project_title:
            return True
    return False

def create_project(ls, project_title, label_config):
    # Create a project with the specified title and labeling configuration
    project = ls.projects.create(
        title=project_title,
        label_config=label_config
    )
    return project

def get_or_create_project(ls, project_title, label_config=None, recreate_project=False):
    p = get_project_by_title(ls, project_title)
    if recreate_project:
        if p != None:
            ls.projects.delete(p.id)
        created_project = create_project(ls, project_title, label_config)
        return created_project
    else:
        return p

def get_or_create_model(ls, 
                        title='MODEL',
                        description='A model backend',
                        url="http://localhost:9090",
                        project_id=39,
                        is_interactive=True):
    # p = get_project_by_id(ls, project_id)
    try:
        l = ls.ml.list()
        for ml in l:
            if ml.title == title:
                return ml
    except (ApiError, JSONDecodeError): 
        # The ML Backend does not exist, so create it
        return ls.ml.create(
                title=title,
                description=description,
                url=url,
                project=project_id,
                is_interactive=is_interactive)