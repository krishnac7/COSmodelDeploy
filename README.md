
IBM Cloud CLI, Version 0.5.0 or later
IBM Cloud Container Service plug-in
Kubernetes CLI, Version 1.10.8 or later

ibmcloud login
ibmcloud plugin install container-service -r Bluemix
ibmcloud cs cluster-create --name <name-of-cluster>
ibmcloud cs cluster-config <name-of-cluster>

kubectl get pods
kubectl get services
kubectl get deployments

kubectl apply -f kubernetes-deployment.yaml

ibmcloud cs workers <name-of-cluster>

kubectl exec -it redis-master-q9zg7 redis-cli