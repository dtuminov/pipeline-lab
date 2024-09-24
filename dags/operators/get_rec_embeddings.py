from airflow.decorators import task
@task
def get_rec_embeddings()->None:
    print('hello')
