# O'Reilly Media API

The O'Reilly Media API is a simple REST API that uses python and Flask to query and add books from/to a redis database

## Prerequisites
1. Must be deployed on a kubernetes cluster
2. Server this repo is pulled to must have the kubernetes api installed
3. User must have privileges to use kubectl and deploy resources to the cluster

## Getting Started

Pull down the repository with

```sh
git pull <repo>
```
or
```sh
git clone <repo>
```
Move to the k8s directory within the repo
```sh
cd {CURRENT_DIR}/oreilly/k8s/
```
Execute the deployment to kubernetes
```sh
kubectl apply -f deployment.yml
```
Check to confirm all resources have been built and are running
```sh
kubectl get all
```

To get your API IP to use below, inspect the cluster services
```sh
kubectl get svc oreilly-nodeport 
kubectl get svc oreilly-api
```
** oreilly-nodeport will be accessible externally
** oreilly-api will be accessible from inside the cluster only
## REST API Capabilities

***********************


| Endpoint | Function |
| ------ | ------ |
| /health "GET" | Obtains responsiveness of the api - should be {'success': true} |
| /books "GET" | Grabs all books from the redis database under the key 'books' |
| /books/v1/GetField?query={field} "GET" | Grabs books under the key 'books' by field (values => \|title\|authors\|isbn\|description\| )|
| /books/v1/GetByTitle?query={title} "GET" | Grabs books under the key 'books' by title string or substring (ex: title:'My Title' values=>'my', 'my title', 'MY TITLE', 'Title') |
| /books/v1/GetByISBN?query={isbn} "GET" | Grabs books under the key 'books' by isbn string or substring (similar to ByTitle) |
| /books/v1/AddBook "POST" | Adds a book under the key 'books' - Must be in JSON format (see below for example) |

Example request for "GET" functions:
----------------------------------------------------------------------------------------------------------------------------------------------
curl http://<API URL or IP>:8000/books | python3 -m json.tool

Example JSON for AddBook:
----------------------------------------------------------------------------------------------------------------------------------------------
curl -X POST http://<API URL or IP>:8000/books/v1/AddBook -H 'Content-Type: application/json' -d '{"authors": "authors here", "description": "description here", "title": "title here", "isbn": "isbn here"}'

## Load the redis database from the O'Reilly site API
```sh
pip3 install -r db-server-script/requirements.txt
python3 db-server-script/db-builder.py
```

## Miscellaneous

Docker Image: 
tfvoncan/oreilly-repo
[Docker Image]: <https://hub.docker.com/repository/docker/tfvoncan/oreilly-repo>

