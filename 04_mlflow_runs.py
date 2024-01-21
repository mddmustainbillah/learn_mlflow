import mlflow

if __name__ == "__main__":
    # Start a new mlflow run
    mlflow.start_run()

    # Machine Learning code goes here
    mlflow.log_param("learning_rate", 0.01)

    # End the mlflow run
    mlflow.end_run()