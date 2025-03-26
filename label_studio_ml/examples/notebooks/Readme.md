# Label Studio Notebooks

## Label Studio Flair Project Setup Automator
The notebook [flair.ipnyb](./flair/flair.ipynb) provides an automated way to create an initial project, a connected flair backend and generating annotation predictions for all the tasks in the Label Studio project.

### Prerequisites
* Before using this notebook, be sure you have a successfully working/deployed [Label Studio UI](../../examples/README.md) and [Flair ML Backend](../flair/README.md) deployment on OpenShift.

* Review and revise values given in the ConfigMap found in this [file](./flair/flair_setup_job.yaml) 

### Build and Run the Flair Project Setup Automator
* Build and push the flair ML backend image
```shell
pwd # ensure you are in label-studio-ml-backend/label_studio_ml/examples/notebooks directory
docker build -f ./flair/Dockerfile  --platform=linux/amd64 -t quay.io/<your user>/flair-automator:0.0.0 . 
docker push quay.io/<your user>/flair-automator:0.0.0
```

* Start and run the Flair Project Setup Automator
```shell
oc delete -f ./flair/flair_setup_job.yaml
oc apply -f ./flair/flair_setup_job.yaml
```

* Ensure that the job ran successfully by examining the Job's pod logs.

* Login to the Label Studio UI and see if the project was created with the tasks and the initial annotation predictions.