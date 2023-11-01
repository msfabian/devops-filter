###Notes

##Despliega la app a un clúster de Minikube Kubernetes

#Editar archivo hosts (para cambiar host dns editar tambien flask-nginx-ingress.yaml)
echo "$(minikube ip) flask-app.local" | sudo tee -a /etc/hosts

#Deploy
git clone https://github.com/msfabian/devops-filter
cd devops-filter/environment
kubectl create secret generic my-secret --from-file=./db/password.txt
kubectl apply -f .

#Test
curl http://flask-app.local

##Proyecto: nginx-flask-mysql convertido y readecuado de docker-compose a Kubernetes

#framework: https://github.com/docker/awesome-compose/tree/master/nginx-flask-mysql