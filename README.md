# django-todo-single-page-application
Django TODO Single Page App is used to Create Todo List , Edit and Marks Status from Pending to Done


# Technologies Used: 
  Python 3.6
  Django 2.0
  Mysql 5.7
  Docker 19.03.1
  Docker-Compose 1.23.2
  HTML5
  Bootstrap 4
  jQUery
  Javascript
  Ajax
  
# Other Packages  
  Django-Bootstrap-Modal-Forms 1.4.2
  Django-Widget-Tweaks 1.4.5
  MySQL-Client 1.4.4
  
  
# Steps For Running Project
  Step1 : Install docker and docker-compose
  Step2 : git clone https://github.com/abhishekbudruk007/django-todo-single-page-application.git
  Step3 : cd django-todo-single-page-application
  Step4 : sudo docker-compose build
  Step5 : sudo docker-compose up -d
  Step6 : Visit http://0.0.0.0:8000/
  
  
# Required Docker Commands

  1) Display All Docker Images 
      # sudo docker images 
  2) Display All Running Containers
      # sudo docker ps 
  3) Display All Running and Non-Running Containers
      # sudo docker ps -a
  4) Build Docker-Compose File (docker-compose.yml)
      # sudo docker-compose build
  5) Run Docker-Compose File (docker-compose.yml)
      # sudo docker-compose up
      # sudo docker-compose up -d ( daemon mode)
  6) Check Docker-Compose Running Services or Containers
      # sudo docker-compose ps 
  7) Check Logs of Docker
      # sudo docker logs [docker-name]               - Show all 
      # sudo docker logs [docker-name] --tail 100    - Show Recent 100 Lines
      Example : sudo docker logs myproject_web_1 
                sudo docker logs myproject_web_1 --tail 100
  8) Exec Inside Docker 
      # sudo docker exec -it [docker_name] bash
      Example : sudo docker exec -it myproject_web_1 bash
  
  9) Exec Inside Docker using Service Name of (docker-compose.yml )
     # sudo docker-compose exec [service-name] bash
     Example : sudo docker-compose exec web bash
  10) Exec Inside Mysql Server using Service Name of ( docker-compose.yml)
     # sudo docker-compose exec [service-name] mysql -u root -p 
     Example : sudo docker-compose exec db mysql -u root -p
     Enter root Password : Root@123mysql
     # Other User
     Example : sudo docker-compose exec db mysql -u myprojectuser -p
     Enter root Password : Root@123mysqlmyproject
  11) Remove Docker Images
     # sudo docker rmi [docker-image-id] or [docker-image-name]
     Example : sudo docker rmi myproject_web
  12) Remove Docker Containers
     # sudo docker rm [docker-container-name] or [docker-id]
     Example: sudo docker rm myproject_web_container
  13) Remove All Docker Containers Which Are Exited
     # sudo docker ps -a | grep Exited | awk '{ print $1;}' | xargs sudo docker rm -f
  14) Build Docker Image :
     # sudo docker build -t [desired-docker-name] .
     Example sudo docker build -t myproject-web .
  15) Check Docker Network :
     # sudo docker network ls 
  16) Inpsect Docker Network
     # sudo docker network inspect [network-name]
     Example : sudo docker network inspect todo_network
  
     
     
