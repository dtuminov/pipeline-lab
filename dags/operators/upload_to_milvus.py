from airflow.decorators import task
@task
def upload_to_milvus()->None:
    print('hello')
