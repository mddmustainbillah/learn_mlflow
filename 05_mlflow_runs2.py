import mlflow

if __name__ == "__main__":
    # with mlflow.start_run(run_name="mlflow_runs"): # if i write the code this way then no need to write end_run
    #     mlflow.log_param("learning_rate", 0.01)

    with mlflow.start_run(run_name='mlflow_runs') as run:
        # Machine Learning code goes here
        mlflow.log_param("learning_rate", 0.01)
        print('Run ID')
        print(run.info.run_id)
        print(run.info)