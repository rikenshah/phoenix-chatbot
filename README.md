# ChatBot - Codeshashtra Event

As part of the hackathon in our college, we developed a ChatBot that can communicate with a user via web interface and give all the required information about the event

### Problem Statement

Make a ChatBot that can give information about an event oraganized in college and can help users register for it.

### Approach

We divided the functionality into two parts, both working independently but communicating with each other.

First module is developed in Django, which basically works as an API, which communicates with frontedend module. The frontend module consists only of UI that takes the use input and sends it to the API which then after processing, generates a response and replies in JSON format.

### Technologies Used

- Django
- Python
- NLTK Library (Python Natural Language Processing Toolkit)
- Lots of plugins and packages (both frontend and backend)

### Features

- Dynamic Training
- Spoken Output
- Can be trained in according to user needs
- Stand-alone modules, API can be used in other application
- Easy to work with (Simple text file upload for training)
- Handles variations of the questions (since we use stemmed keywords)

### How to run this code

- Install `virtualenv`, `pip`, `git` and `python`, if not already done.

- Git clone the repo by using 

`git clone https://github.com/rikenshah/phoenix-chatbot.git`

- Navigate to the folder where your codes are.

`cd /where/your/codes/are/`

- Make a separate virtualenv (lets call it `phoenix`) using this command

`virtualenv phoenix`

- Activate the `virtualenv`.

`source phoenix/bin/activate`

- Install packages

`pip install -r requirements`

- Apply migrations 

`cd phoenix-chatbot/djangoModule`
`python manage.py makemigrations`
`python manage.py migrate`

- Start Server

`python manage.py runserver localhost:8080`

- Navigate to `phoenix-chatbot/Bot` and Open `Bot.html` in a web browser. 

Hurrayyy, Done.

Output - 

![output](https://raw.githubusercontent.com/rikenshah/phoenix-chatbot/master/images/1.png)
