# Sandbox for pybo
M1 Mac에서 '점프 투 장고'의 Pybo를 실행해 볼 수 있는 실습 환경을 제공한다.

## Install Docker

## Ubuntu 환경에서 실행
'점프 투 장고'의 4장에서는 AWS Lightsail에서 Ubuntu를 이용하여 서비스하는 내용을 다루고 있다. 이 환경에서 코드를 실행하기 위해서는 docker 환경을 추가로 구축해야 한다.
```bash
$ docker-compose up -d
$ docker exec -it pybo_django_1 bash
# python manage.py runserver 0:8000
```

## Install docker-compose
```bash
$ sudo apt install docker-compose 
```

## Add the current user to the "docker group"
```bash
$ sudo usermod -aG docker ${USER}
```

## Change the base image for amd64
Change the base image of docker image. Change the first line of Dockerfile;
```diff
-From arm64v8/ubuntu:22.04
+From ubuntu:22.04
```
Change the service port of the container;
```diff
     ports:
-      - "8000:8000"
+      - "80:8000"
```
