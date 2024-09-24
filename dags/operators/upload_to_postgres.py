from airflow.decorators import task
@task
def upload_to_postgres()->None:
    print('hello')
