from json import JSONDecodeError
from label_studio_sdk.core.api_error import ApiError
from datetime import datetime
import requests
import uuid
import os

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

def export_annotated_data(project_id, ls_url, api_key):
    # Get the export of the annotations
    url = ls_url + "/api/projects/" + str(project_id) + "/export"
    token = 'Token ' + api_key
    Headers = { 'Authorization' : token }
    response = requests.get(url, headers=Headers )
    return response

def get_timestamp():
    return datetime.timestamp(datetime.now())

def get_random_chars(length=4):
    random_string = str(uuid.uuid4()).replace('-', '')[:length]
    print(random_string)
    return random_string

def create_dir(directory_name):
    # Create the directory
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_file_name(file_name_prefix, file_ext):
    ts = str(get_timestamp())
    random_chars = get_random_chars()
    fn = file_name_prefix + ts + random_chars + file_ext
    return fn

def export_to_file(data, file_name='exported_data', dir_name='exports'):
    create_dir(dir_name)
    fn = get_file_name(file_name, '.json')
    path = os.path.join(dir_name, fn) 
    f = open(path, "w")
    f.write(data)
    f.close()
