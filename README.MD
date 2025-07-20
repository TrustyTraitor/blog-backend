# Blog Backend
This is the API and database ORM that powers my blog for my personal sites 
([Portfolio](https://michaelgain.net) and [Dev site](https://trustytraitor.dev)).

It is built in 
[Python 3.13](https://www.python.org/downloads/) 
using [FastAPI](https://fastapi.tiangolo.com/), 
[SQLAlchemy 2.0](https://www.sqlalchemy.org/),
and [SQLite](https://sqlite.org/index.html).

## How to install and run
Clone the repo and then, in the `blog-backend` directory run: 
1. `python -m venv venv && source ./venv/bin/activate`
   - Deactivate the virtual environment using the `deactivate` command.
2. `pip install -e .` (SQLite is also required but not installed with pip)
    - The `-e` argument allows for the python packages to be editable. If this is not needed, `-e` can be removed.

Then run the server using uvicorn: `uvicorn main:app --host 0.0.0.0` add `--reload` for automatic reloads.

## Using the Project
A `blog.db` will be automatically generated in the top `blog-backend` directory (assuming you have SQLite installed).

## Features
This project is still a WIP. Features are incomplete or missing. A list of planned features and their status are below.
- [ ] Database requirements
  - [ ] Posts
  - [ ] Users
  - [ ] Comments
- [ ] API Completion
  - [ ] Basic features
    - [ ] Retrieve Posts
    - [ ] Create Posts
      - Creating posts is only available to the blog owner (me in this case). This will, initially, 
            be done using environment variables to store a secure key.
      - [ ] Delete posts
    - [ ] Add rate limiting
  - [ ] Advanced features
    - [ ] Filter posts
    - [ ] Create user account
      - [ ] Delete user account
    - [ ] Create Comments
      - [ ] Delete comments
    - [ ] User authentication
    - [ ] User permissions
      - Permissions are controlled solely by the site owner.
      - [ ] Create comments
      - [ ] Create posts
        - This will allow users that are not the site owner, but are approved, to create posts.
- [ ] Configuration
  - [ ] Create configuration system