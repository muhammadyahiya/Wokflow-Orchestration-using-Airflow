# Airflow Single-Node Setup Guide

## Introduction

Apache Airflow is a powerful platform to programmatically author, schedule, and monitor workflows. It is designed to handle both small and large workflows and comes with a rich set of features, including dynamic task generation, branching, and a visual dashboard for monitoring.

This guide will walk you through setting up a single-node Airflow instance, demonstrating core concepts and components, and providing example configurations.

## Table of Contents

- [Core Concepts](#core-concepts)
- [Components](#components)
- [Setup Instructions](#setup-instructions)
- [Example Workflows](#example-workflows)
- [Customizing Airflow](#customizing-airflow)
- [Architecture](#architecture)
- [Limitations](#limitations)
- [Additional Resources](#additional-resources)

## Core Concepts

- **DAG (Directed Acyclic Graph):** A DAG is a collection of all tasks you want to run, organized to reflect their dependencies. It defines the workflow structure.
- **Operator:** An operator defines a single task in your DAG. Operators help break down workflows into discrete, manageable pieces.
- **Task/Task Instance:** A task is a specific instance of an operator. It represents the actual work to be executed.
- **Workflow:** The entire process defined by the DAG, including all tasks and their dependencies.

## Components

- **Web Server:** Provides the user interface for viewing, managing, and monitoring workflows.
- **Scheduler:** Determines when tasks should run and ensures they execute in the correct order.
- **Meta Database:** Stores information about tasks and their statuses.
- **Triggerer:** Manages deferrable tasks that wait for external events.
- **Executor:** Manages task execution, deciding whether tasks run sequentially or in parallel.
- **Queue:** Manages the order of task execution.
- **Worker:** Processes that perform the actual work defined in tasks.

## Setup Instructions

1. **Install Airflow:**

   ```bash
   pip install apache-airflow
   ```

2. **Initialize the Database:**

   ```bash
   airflow db init
   ```

3. **Start the Web Server:**

   ```bash
   airflow webserver --port 8080
   ```

4. **Start the Scheduler:**

   ```bash
   airflow scheduler
   ```

5. **Access the Web Interface:**

   Open your web browser and navigate to [http://localhost:8080](http://localhost:8080) to access the Airflow dashboard.

## Example Workflows

### Dynamic Tasks and Branching

```python
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.branch import BranchPythonOperator
from datetime import datetime

def choose_branch(**kwargs):
    return 'branch_a' if datetime.now().second % 2 == 0 else 'branch_b'

with DAG(dag_id='dynamic_branching_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    
    start = DummyOperator(task_id='start')
    
    branch = BranchPythonOperator(
        task_id='branch_task',
        python_callable=choose_branch,
        provide_context=True
    )
    
    end_a = DummyOperator(task_id='end_a')
    end_b = DummyOperator(task_id='end_b')
    
    start >> branch
    branch >> [end_a, end_b]
```

## Customizing Airflow

- **Custom Operators:** Extend functionality by creating custom operators.
- **Plugins:** Add new features or integrate with other tools using plugins.
- **User Interface:** Customize the UI by modifying existing functions or using Airflow's built-in features.

## Architecture

### Single-Node Architecture

![Single Node Architecture](path_to_single_node_architecture_image)

### Multi-Node Architecture

![Multi Node Architecture](path_to_multi_node_architecture_image)

## Limitations

- Airflow is not a storage system; it handles scheduling and monitoring of tasks.
- It is not suitable for real-time data streaming or very large datasets.
- Airflow is ideal for batch/scheduled data processing and may not be the best fit for simple, linear workflows.

## Additional Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Airflow Operators Documentation](https://airflow.apache.org/docs/apache-airflow-providers/)
- [Airflow GitHub Repository](https://github.com/apache/airflow)
