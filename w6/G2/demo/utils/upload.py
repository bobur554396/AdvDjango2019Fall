def task_document_path(instance, filename):
    project_id = instance.project.id
    return f'projects/{project_id}/{filename}'
