from airflow.decorators import task
@task
def upload_to_Milvus()->None:
    print('hello')
