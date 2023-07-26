# APPIDADE

## `Dockerfile`

```dockerfile
FROM nginx:mainline-alpine
LABEL "vendor"="klv"
LABEL version="v1.0"
LABEL description="Aplicação de cálculo de idade com JavaScript"
LABEL maintainer="rfabriciors@gmail.com"

COPY www/ /usr/share/nginx/html

EXPOSE 80
```


### deployment-appidadeklv.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: appidadeklv
  name: appidadeklv
spec:
  replicas: 2
  selector:
    matchLabels:
      app: appidadeklv
  strategy: {}
  template:
    metadata:
      labels:
        app: appidadeklv
    spec:
      containers:
      - image: rfabricio/appidadeklv:latest
        name: appidadeklv
        ports:
        - containerPort: 80
        livenessProbe:
          httpGet:
            path: /health.txt
            port: 80
          initialDelaySeconds: 3
          periodSeconds: 2
          timeoutSeconds: 1
          successThreshold: 1
          failureThreshold: 2
        rednessProbe:
          httpGet:
            path: /ready.txt
            port: 80
          initialDelaySeconds: 3
          periodSeconds: 2
          timeoutSeconds: 1
          successThreshold: 1
          failureThreshold: 2
        resources: {}
status: {}
```

*o arquivo heath.txt serve como referência para o recurso livenessProbe*

### service-appidadeklv.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    app: appidadeklv
  name: appidadeklv
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: appidadeklv
  type: NodePort
status:
  loadBalancer: {}
  ```

## Disparando o deployment

```bash
kubectl apply -f deployment-appidadeklv.yaml
```

## Expondo o serviço

```bash
kubectl apply -f deployment-appidadeklv.yaml
```

O serviço é verificado através do recurso *livenessProbe*

```yaml
        livenessProbe:
          httpGet:
            path: /health.txt
            port: 80
```

O *livenessProbe* pode ser verificado através da descrição do pod:

```bash
kubectl describe pod <pod_name>
.
.
.
Liveness:       http-get http://:80/health.txt delay=0s timeout=1s period=10s #success=1 #failure=3
```
