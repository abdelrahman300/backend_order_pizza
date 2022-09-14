# Table of content 
* -	simple description 
* -	how to operate locally 
* -	dependencies and how to install 
* -	app file structure 
* -	urls and action preformed over this url 

## Simple descriptuin 

App  Order pizza  build with FastAPI,Python.
FastAPI provides the backend environment for this application .
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.


## FastAPI Documentation

* https://fastapi.tiangolo.com/

## 	How to operate locally

* Follow the next steps:
   * $ git init  command creates a new Git repository
   * $ git clone the project
   * git branch <branch name>
   * git git switch < <branch name>
   know you work locally and after every excute code have to do:
    * $git add .
    * $git commit -m "name of commit "
    * $git push origin <branch name>


## Install Dependencies
  Install FastAPI
    $ pip install "fastapi[all]"
    
   ### Run the code
All the code blocks can be copied and used directly (they are actually tested Python files).

To run any of the examples, copy the code to a file main.py, and start uvicorn with:

  $ uvicorn main:app --reload
  

## APP file structure 

![drawSQL-export-2022-09-13_11_47](https://user-images.githubusercontent.com/62572088/190031820-2c1985f4-5e91-42a9-aaec-1e0a8eda32bd.png)





## URLs and action preformed over this URL

| Route | Verb(s) | Middleware | Description |
| ------------- | ------------- | ------------- | ------------- |
| create/user | POST | val:create | Create a User and return id |
| /create/order | post | val:createorder | Check the current user_phone logged in |
| /order_by_id | GET | - | check about id and return all details about this order|
| /update_order/id| PuT | ,val:id,val:update| check about id and do updates |
| /all/users | GET | - | return all users |
| /delete/{id}| Delete | val:id | check about id and return your order deleted 


 













<br>
