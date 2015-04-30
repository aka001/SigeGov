Software Requirements and Installation guide

1. Django version 1.6.1 
	 	sudo pip install Django==1.6.10
2. Django modules
Install synaptics from this link: http://askubuntu.com/questions/131979/how-to-install-synaptic-package-manager  

	The commands to be used are:  
		1.  sudo apt-get update  
		2.  sudo apt-get upgrade  
		3.  sudo apt-get install synaptic  

	Go to synaptics manager and install:   
		1.  python-django-registration module.  
		2.  python-django-social-auth module.  
		3.  django-vote module
		4.  django-haystack module 

3. For solr-4.10.2
   curl -LO https://archive.apache.org/dist/lucene/solr/4.10.2/solr-4.10.2.tgz
   tar xvzf solr-4.10.2.tgz

4.  pip install pysolr
	pip install -e https://github.com/toastdriven/django-haystack.git
  
5. Install java version "1.7.0_75" in your system. Download and install it here - http://www.oracle.com/technetwork/java/javase/downloads/index.html
     
Database setup:

1. Assuming mysql is present in the system, If not refer  https://help.ubuntu.com/12.04/serverguide/mysql.html
2. Now go to mysql CLI, [mysql -u root -p]
   Create a database as eGov; [ create database eGov]
3.  Now change the database details in django settings.
	Go to project’s main directory
	vim test1/settings.py
	At line 70 and 71, change the username and password with mysql username(root) and password.
4.  Now setup the django tables in the database.
	python manage.py syncdb [ It will create all the tables in eGov database]
	During the process it will ask for superuser account, Enter the given details
	username: admin
	password: admin
	email: sigegovadmin@gmail.com
	You can also create superuser using 
	python manage.py createsuperuser
5. Enter project data in tables.
   python manage.py runserver [It will start a django server locally on port 8000]
6. Open 127.0.0.1:8000/sigegov/enter_data in any browser window. It will enter the value in database. [ Close the window, Ignore error page]

Running Solr backend:
Go to solr directory
cd example/
java -jar start.jar 
[It will start the solr server, move to another terminal window]

Setup indexes for solr search
1.Create a schema.xml from django haystack indexes so that solr can return the query output
	python manage.py build_solr_schema > schema.xml
2.  cp schema.xml to solr [Assuming solr is present in the home directory]
	cp schema.xml ~/solr-4.10.2/example/solr/collection1/conf/schema.xml
3.  Now run solr schema as mentioned in previous step
		* Go to solr directory 
		* cd example/
		* java -jar start.jar [It will start the solr server, move to another terminal window]
4. Now build the indexes. Go to project’s main directory.
	python manage.py rebuild_index
     
	
Running django server:
* Go to project’s main directory.
* python manage.py runserver [It will start a django server locally on port 8000]

Two servers should always run in the backend one for django and other for solr.

Home page: 127.0.0.1:8000/sigegov
Django admin page: 127.0.0.1:8000/admin