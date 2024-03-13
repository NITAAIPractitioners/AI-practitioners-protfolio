from flask import Flask, render_template

app = Flask(__name__)
students = [
{'id':1,
'project' : 'Web Scraping',
'skills' : 'urllib python, Python Requests,Selenium,Beautiful Soup'
},
{'id':2,
'project' : 'AI model for flare mointoring',
'skills' : 'Python pandas, sikitlib, matblotlib,microsoft azure,pychatgpt'} 
]

@app.route("/")
def hello_world():
  return render_template('home.html',myskills=students,
                        myname='Girls')


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=True)
