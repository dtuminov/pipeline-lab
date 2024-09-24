from airflow.decorators import task
@task
def search_embedder()->None:
    print('hello')
