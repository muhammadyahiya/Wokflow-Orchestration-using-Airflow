from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.operators.s3 import S3ToS3Operator
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator, GlueCrawlerOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    's3_to_glue_pipeline',
    default_args=default_args,
    description='A DAG to update data in S3 and use AWS Lambda, Glue, and Crawler',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Step 1: Define a dummy start task
    start = DummyOperator(task_id='start')

    # Step 2: Copy data from source S3 bucket to target S3 bucket
    copy_s3_data = S3ToS3Operator(
        task_id='copy_s3_data',
        source_bucket_name='source-bucket',
        source_bucket_key='data/*.csv',
        dest_bucket_name='target-bucket',
        dest_bucket_key='data/',
        aws_conn_id='aws_default',
    )

    # Step 3: Trigger AWS Lambda function to process data (e.g., data validation/transformation)
    lambda_function = LambdaInvokeFunctionOperator(
        task_id='invoke_lambda',
        function_name='your_lambda_function_name',
        payload={"key": "value"},  # Customize payload as required
        aws_conn_id='aws_default',
    )

    # Step 4: Run AWS Glue ETL job
    glue_job = GlueJobOperator(
        task_id='run_glue_job',
        job_name='your_glue_job_name',
        aws_conn_id='aws_default',
    )

    # Step 5: Run AWS Glue Crawler to update Data Catalog
    glue_crawler = GlueCrawlerOperator(
        task_id='run_glue_crawler',
        crawler_name='your_glue_crawler_name',
        aws_conn_id='aws_default',
    )

    # Step 6: Define a dummy end task
    end = DummyOperator(task_id='end')

    # Define task dependencies
    start >> copy_s3_data >> lambda_function >> glue_job >> glue_crawler >> end
