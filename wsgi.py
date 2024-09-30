import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from datetime import datetime

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import (initialize, create_competition, add_competition_result,get_competitions, add_competition_results_from_csv, get_competition_results )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''
@app.cli.command("get-competitions",help ="Gets all the competitions")
def showCompetitions():
    competitions = get_competitions()
    if not competitions:
        print("No Competitions")
        return
    print(competitions)

@app.cli.command("create-competition",help="Creates a competition and adds it to the database")
@click.argument('competition_name',default='first_competition')
@click.argument('date',default='no-date')
def createCompetion(competition_name,date):
    date_object = datetime.now()
    try:
        # Attempt to convert the invalid date string to a datetime object
        date_object = datetime.strptime(date, "%d/%m/%Y")
    except ValueError as e:
        # Catch the ValueError and print a message
        print(f"Error: {e}")
    competition = create_competition(competition_name,date_object)
    if not competition:
        print(f"{competition_name} already exists")
        return
    
    print(f"Competition added successfully")


@app.cli.command("Add_A_Result_To_Competition",help="Adds one result to a competition")
@click.argument('competition_id',default=1)
@click.argument('participant',default='Jack Reaper')
@click.argument('score',default = 90)
def addOneResult(competition_id,participant,score):
    competition = add_competition_result(competition_id,participant,score)
    if not competition:
        print(f"Competition with id {competition_id} does not exist")
        return
    print('Result added successfully')


@app.cli.command("Add_A_ResultFromFile_To_Competition",help="Adds  results to a competition using a file")
@click.argument('competition_id',default=1)
@click.argument('file_path',default='results.csv')
def addResults(competition_id,file_path):
    competition = add_competition_results_from_csv(competition_id,file_path)
    if not competition:
        print(f"Competition with id {competition_id} does not exist")
        return
    print('Results added successfully')

@app.cli.command("get_competition_results",help="Show the results of a competition")
@click.argument('competition_id',default=1)
def showCompetitionResults(competition_id):
    results = get_competition_results(competition_id)
    if not results:
        print(f"Competition with id {competition_id} does not exist")
        return
    for result in results:
        print(result)