from airflow.decorators import task
@task
def clean_JSONL() -> None:
    print('hello')
