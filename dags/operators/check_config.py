from airflow.decorators import task


@task
def check_config() -> None:
    print('hello')
