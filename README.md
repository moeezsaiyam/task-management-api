# Task Management API

## Overview
This is a task management API developed using Flask. It provides functionalities to create, retrieve, update, and delete tasks.

## Setup

### Prerequisites
- Python 3.x
- MySQL

### Installation
1. Clone the repository: `git clone https://github.com/moeezsaiyam/task-management-api`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix or MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up the environment variables:
   - Copy `.env.example` to `.env`
   - Update the variables in `.env`
6. Setup Postgres Database:
   - Create a database in postgres
   - Update `DATABASE_URL=postgresql://user:password@localhost/db_name` in `.env` file
   in .env file
7. Initialize the database:
   - `flask db init`
   - `flask db migrate -m "first migration"`
   - `flask db upgrade`

## Running the Application
Run the application using: `flask run`

## API Endpoints
- GET `/tasks` - Retrieve all tasks
- GET `/tasks/<id>` - Retrieve a single task
- POST `/tasks` - Create a new task
- PUT `/tasks/<id>` - Update an existing task
- DELETE `/tasks/<id>` - Delete a task

## Testing
Use Swagger(Default), Postman or any other API testing tool to test the endpoints.
