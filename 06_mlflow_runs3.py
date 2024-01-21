import mlflow

from mlflow_utils import create_mlflow_experiment, get_mlflow_experiment

if __name__ == "__main__":
    experiment = create_mlflow_experiment(
        experiment_name='testing_mlflow1',
        artifact_location='testing_mlflow1_artifacts',
        tags={'env': 'dev', 'version': '1.0.0'}
    )

# mlflow.set_experiment(experiment_name='testing_mlflow1')
    
# with mlflow.start_run(run_name='testing', experiment_id=experiment) as run:
    
experiment = get_mlflow_experiment(experiment_id=experiment)
print('Name: {}'.format(experiment.name))
with mlflow.start_run(run_name='testing', experiment_id=experiment.experiment_id) as run:

    # Machine learning code goes here
    mlflow.log_param('learning_rate', 0.01)

    # Print the info
    print('run_id: {}'.format(run.info.run_id))
    print("experiment_id: {}".format(run.info.experiment_id))
    print("status: {}".format(run.info.status))
    print('start_time: {}'.format(run.info.start_time))
    print('end_time: {}'.format(run.info.end_time))
    print('lifecycle_stage: {}'.format(run.info.lifecycle_stage))