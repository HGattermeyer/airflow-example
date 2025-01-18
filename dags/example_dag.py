from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

# Função de exemplo
def hello_world():
    print("Hello, Airflow!")

# Definição do DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='example_dag',
    default_args=default_args,
    description='Uma DAG de exemplo',
    schedule_interval='@daily',  # Executa diariamente
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    start = DummyOperator(task_id='start')

    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=hello_world,
    )

    end = DummyOperator(task_id='end')

    # Definindo o encadeamento
    start >> hello_task >> end
