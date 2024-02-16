from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'Joshua Mutua',
    'retries': 5,
    'retry_delay':timedelta(minutes=2)
}
with DAG(
        dag_id='our_first_dag_v2',
        default_args=default_args,
        description = 'This is my first dag',
        start_date=datetime(2024,2,16),
        schedule_interval ='@daily'

) as dag:
    task1 = BashOperator (
        task_id ='first_task',
        bash_command="echo hello world, this is my first task"
    )
    task2 = BashOperator (
        task_id = 'second_task',
        bash_command = "echo Hey, I am task2 and i will be running after task 1"
    )
    task3 = BashOperator(
        task_id ='third_dag',
        bash_command = "echo I am task 3, i will run after task 2"
    )
task1.set_downstream(task2)
task1.set_downstream(task3)
