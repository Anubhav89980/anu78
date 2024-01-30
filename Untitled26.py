#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Flask is a lightweight and flexible web framework for Python. It is designed to be simple and easy to use, allowing developers to build web applications quickly and efficiently. Some advantages of Flask include:

#Lightweight: Flask is a micro-framework, meaning it provides only the essential features to get a web application up and running. This simplicity makes it easy to learn and use.

#Flexibility: Flask allows developers to choose the components they want to use, giving them the flexibility to use any database, templating engine, or other components they prefer.

#Extensibility: Flask is easily extendable, and you can add various third-party libraries to enhance its functionality.

#Built-in Development Server: Flask comes with a built-in development server, making it easy to test and debug applications during development.

#Jinja2 Templating: Flask uses the Jinja2 templating engine, which allows for dynamic content rendering in HTML templates.

#RESTful Support: Flask supports the development of RESTful APIs, making it suitable for building both web applications and APIs.

#Active Community: Flask has a large and active community, which means there are plenty of resources, tutorials, and extensions available for developers.


# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()


# In[ ]:


#In Flask, routing refers to mapping URLs to functions. App routing defines the different URLs that your web application will respond to and the functions that will be executed when these URLs are accessed.

#We use app routes to define the behavior of our web application based on the URL requested by the client. Each route corresponds to a specific URL, and when that URL is accessed, the associated function (view function) is executed, generating the response that will be sent back to the client.

#App routing is essential because it allows developers to organize the code and define how different parts of the application respond to different URLs. It helps in creating a clear structure for the application and makes it easy to understand and maintain.


# In[ ]:


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    return render_template('company_details.html', company_name='ABC Corporation', location='India', contact_detail='999-999-9999')

if __name__ == '__main__':
    app.run()


# In[ ]:


#In Flask, the url_for() function is used for URL building. It generates a URL for the specified endpoint (view function) and can also include values for any parameters defined in the route.
#Here's an example:
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/user/<username>')
def user_profile(username):
    return f'User Profile: {username}'

@app.route('/user/<username>/posts')
def user_posts(username):
    return f'Posts by {username}'

if __name__ == '__main__':
    with app.test_request_context():
        # Demonstrating url_for() function
        print(url_for('user_profile', username='john'))
        print(url_for('user_posts', username='john'))


# In[ ]:




