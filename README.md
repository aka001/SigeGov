Install Django from this link https://www.digitalocean.com/community/tutorials/installing-django-on-ubuntu-12-04--4  

The commands to be used are:  
1.  sudo apt-get install python-imaging python-pythonmagick python-markdown python-textile python-docutils  
2.  sudo apt-get install python-django  
3.  django-admin -> To check whether django is correctly installed or not.  

Install synaptics from this link: http://askubuntu.com/questions/131979/how-to-install-synaptic-package-manager  

The commands to be used are:  
1.  sudo apt-get update  
2.  sudo apt-get upgrade  
3.  sudo apt-get install synaptic  

Go to synaptics manager and install:   
1.  python-django-registration module.  
2.  python-django-social-auth module.  

Connect to Mysql database: 
1. Create a mysql db egov [ create database egov ] 
2. Change the password in test1/settings.py with your mysql password [mysql -u root -p] 
3. Run python manage.py syncdb [Only once to create the tables in db] 
4. Done. 

Version: Django 1.6.1 [sudo pip install Django==1.6.10] 

That's all :)  
