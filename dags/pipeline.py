from airflow import DAG
import datetime as dt


from operators import check_config
from operators import clean_JSONL
from operators import upload_to_postgres
from operators import get_rec_embeddings
from operators import search_embedder
from operators import upload_to_Milvus
from operators import make_backup

with DAG(
    dag_id='name_of_pipeline',
    start_date=dt.datetime(2021, 3, 1),
    schedule='@once'
) as dag:

    task1 = check_config.check_config()
    task2 = clean_JSONL.clean_JSONL()
    task3 = upload_to_postgres.upload_to_postgres()
    task4 = get_rec_embeddings.get_rec_embeddings()
    task5 = search_embedder.search_embedder()
    task6_1 = upload_to_Milvus.upload_to_Milvus()
    task6_2 = upload_to_Milvus.upload_to_Milvus()
    task7 = make_backup.make_backup()

    task1 >> task2 >> [task3, task4, task5]
    task3 >> task7
    [task4 >> task6_1, task5 >> task6_2] >> task7




    #check_config.check_config() >> clean_JSONL.clean_JSONL() >> [upload_to_postgres.upload_to_postgres(),
     #   get_rec_embeddings.get_rec_embeddings(),
      #  search_embedder.search_embedder() >> upload_to_Milvus.upload_to_Milvus()] >> make_backup.make_backup()

