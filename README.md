This code is orignial from https://github.com/senpay/3_layer_architecture_course
https://www.youtube.com/watch?v=feu38DOeTio

I modified it for standard presentation, persistance, and business layers.

How to run it:

1.	Install Visual Studio Code for running the project.
2.	Download python for VS code.
3.	Install git bash from the offical website.
4.	Check python --version
5.	Check git --version
6.	Git Clone the Repository and create a folder and open the terminal in VS code.
7.	Go to relevent path (project folder) cd .\3_layer_architecture_course\
8.	Install Python Dependencies from requirements.txt by running pip install requirment.txt in terminal.
9.	Run the main file (main.py)
10.	After running correctly  http://127.0.0.1:5000 address is displayed in the terminal as the output and  this address can be opened in a new tab.

Pip install them one by one 

click==8.1.3

colorama==0.4.6

Flask==2.2.3

itsdangerous==2.1.2

Jinja2==3.1.2

MarkupSafe==2.1.2

Werkzeug==2.2.3

To run this code, suggest you to use postman to send request.

1. create user:
http://127.0.0.1:5000/user   
{
    "user_name": "aaa",
    "first_name": "John",
    "last_name": "Doe"
}

2. get user:
http://127.0.0.1:5000/user/1

3. welcome page:
http://127.0.0.1:5000


![image](https://github.com/user-attachments/assets/291e8094-1ed6-4d61-9ca7-aa4f762eacb2)
![image](https://github.com/user-attachments/assets/79e8ea04-d953-4c81-9d11-b314ce999afe)


