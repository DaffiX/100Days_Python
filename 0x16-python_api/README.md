## APIs - SWAPI

The Star Wars API (SWAPI) is a public API that provides information about various aspects of the Star Wars universe, like characters, films, starships, and more.

### Requirements
+ Install Requests 
```bash
pip install requests
```
+ Import the Module
```
import requests 
```
### Creating a Python Virtual Environment
A Python virtual environment is a self-contained project directory that contains specific versions of Python and the Python modules required for the given project. This is useful for isolating one application from others on the same system by managing each one’s dependencies separately. In this step, you’ll set up a Python virtual environment from which you’ll run your Flask application.

Start by installing the python3-venv package, which will install the venv module:
```sudo apt install python3-venv```

Next, make a parent directory for your Flask project:
```mkdir ~/myproject```

Move into the directory after you create it:
```cd ~/myproject```
Create a virtual environment to store your Flask project’s Python requirements by typing

```python3.10 -m venv myprojectenv```
This will install a local copy of Python and pip into a directory called myprojectenv within your project directory.

Before installing applications within the virtual environment, you need to activate it. Do so by typing:
```source myprojectenv/bin/activate```
Your prompt will change to indicate that you are now operating within the virtual environment. It will look something like this: (myprojectenv)user@host:~/myproject$.

### Settingup Simple App
While your application might be more complex, in this example you’ll create your Flask app in a single file, called myproject.py. Open myproject.py using nano or your favorite text editor:
```nano ~/myproject/myproject.py```

The Application code:
```bash
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
```

then allo UFW
```bash 
sudo ufw allow 5000
```

Now test the app:
```bash 
python myproject.py
```

### INSTALL FLASK - ubuntu 22.04 LTS
First, install wheel with the local instance of pip to ensure that your packages will install even if they are missing wheel archives:
```bash
pip install wheel
```

- Next, install Flask and uWSGI:
```pip install uwsgi flask```