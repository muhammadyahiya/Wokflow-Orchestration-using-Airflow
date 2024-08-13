# docker-airflow
Python based
Dynamic Tasks
Airflow has dynamic wokflows
Branching

Airflow can handle small and large amounts of work
different execution modes

Airflow has a visual dahsboard and control your tasks and workflows
monitor and troblue shoot workflows
highlighet relationship between tasks and workflows
identify bottle necks with performed metrics
Manage users and roles of your airflow instance

You can add fatures or connect airflow to other tools easily
many providers: package with functsions to interact with a toolor service (aws, Snowflake etc)
Customizable user interface
Posssibility to custom existing functions


AirFlow Components:
Web Server -it provides the user interface , you see when you se AirFlow.
              It allows to view, manage, and monitir your workflows through a web browser.
Scheduler - It is responsible for determining when tasks should run
              It ensures your task run at the right time and in the correct order.
The Meta DataBase - This data base stores information about your taska nd thier staus. It keeps                     the track of all the importtant detail saboi=ut the workflows.
The Triggerer - It is responsible for managning defeable tasks- tasks that wait for external                   events. It allows Airflow to effiecintly handle tasks taht depend on external                   factors witout blocking other processess.
Executor - It determines how your tasks will be run
           It manages the execution of the tasks, decoidng wether to run them in sequence or in            parallel and on which system.
Queue - It is a list waiting to be executed. It helps in manage the order of task execution,            especially when there are many tasks to run.
Worker - It is a processes that actually perform the tasks. They do the actual work defined in           your tasks.  
              



Core Concepts :
DAG (directed Acyclic Graph) -A DAG is a collection of all the tasks you want to run, organised in a way that reflects thier dependencies.
It helps you to define  the struture of your entire workflow, showing which tasks need to happen before others.

Operator - An opearator defines a single , ideally idempotent, task in your DAG. Opeartor allows to break down the wokflows into discrete , manageable pieces of work.

Airflow has thousands of operators


Tak/Task Instance -  A task is a specific intance of a opertaor. When an opeartor is assigned to a DAG , it becomes a task. Tasks are the actual units of work that get executed when your DAG runs.

Workflow -  A workflow is the entire process defined by the DAG, including all tasks and thier dependencies. It represnts the entire data pipeline, showing how all the pieces fit togetehr to achieve the goal.

Airflow is used batch/Scheduled data processing, it does not has a stoarge system. It used for tasks for minutues or hours. It doesnot processing large dataset. It is not used for Real time data streaming. It doesnot work for simple, linear workflows or dependencies. 

![image](https://github.com/user-attachments/assets/6df0666a-373c-4e04-8dc5-905135622265)




The Differnet Architctures -
  Single node Archtecture -- ![image](https://github.com/user-attachments/assets/9fb00137-bf3e-4366-bfdd-d353185768a8)

Multi Node Architecture- A node is a single computer or server. "Multi-Node" refers to running Airflow across multiplle  computers or servers.
![image](https://github.com/user-attachments/assets/8b9f99ec-4847-4a6c-9a20-a7b7794f7bff)

![image](https://github.com/user-attachments/assets/0e3a6193-2cdb-4974-acea-142499ff663d)


  








