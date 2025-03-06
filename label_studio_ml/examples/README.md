# Running examples on OpenShift

## Setup a service account to run the example services and UI 
* This is a one time activity across all deployments/examples, ensure your user has cluster-admin privileges
```shell
oc login --token=<token> --server=<server-url>
oc project <your-desired-project>
oc create sa runner-sa
oc get sa
oc adm policy add-scc-to-user anyuid -z runner-sa
```

## Deploy and run the LabelStudio UI
```shell
oc delete -f deployment-ui.yaml; oc apply -f deployment-ui.yaml
# Wait for the Pod to come to running/error state (navigate to Workloads->Pods in OpenShift UI console) before running the following steps
oc get deployment
oc set sa deployment label-studio-ui runner-sa
```

## Verify the UI service is running
```shell 
oc get route
open http://<label studio ui route>
```

## Deploying Machine Learning Model Backends for use in LabelStudio to OpenShift
Please refer to individual backends ( more coming soon )
* [Flair](flair/README.md)
* [Segment Anything Model](segment_anything_model/README.md)
* [Segment Anything Model2](segment_anything_2_image/README.md)
* [Easyocr](easyocr/README.md)