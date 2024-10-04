# Flask Console Program

This is a Flask-based console program designed to manage competitions, where you can initialize a database, create competitions, add results, and view competition results. Below are the available commands and their usage details.

## Installation

Before running any commands, ensure you have all necessary dependencies installed. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

This command will install all the required dependencies from the requirements.txt file.

Available Commands
# 1. Initialize Database
Command:
```bash
flask init
```
Description: Initializes the database. Run this command to set up your database before using other commands.
Expected Output: "database initialized" after successful initialization.


# 2. Get Competitions
Command:

```bash
flask get-competitions
```
Description: Fetches and displays a list of all competitions currently stored in the database.

Expected Output:Prints the list of competitions, or "No Competitions" if there are none.

# 3. Create a Competition
Command:
```bash
flask create-competition <competition_name> <date>
```
Arguments:
competition_name (optional): Name of the competition to create. Default: 'first_competition'.
date (optional): Date of the competition in the format dd/mm/yyyy. Default: 'no-date'.
Description: Creates a new competition and adds it to the database.

Expected Output:
"Competition added successfully" on success.
"Competition already exists" if the competition already exists.
Error message if the date is invalid.

# 4. Add a Result to a Competition
Command:

```bash
flask Add_A_Result_To_Competition <competition_id> <participant> <score>
```
Arguments:
competition_id (optional): ID of the competition. Default: 1.
participant (optional): Name of the participant. Default: 'Jack Reaper'.
score (optional): Score of the participant. Default: 90.
Description: Adds a single result (participant and their score) to the specified competition.

Expected Output:
"Result added successfully" on success.
"Competition with id X does not exist" if the competition ID is invalid.

# 5. Add Results from a CSV File
Command:
```bash
flask Add_A_ResultFromFile_To_Competition <competition_id> <file_path>
```
Arguments:
competition_id (optional): ID of the competition. Default: 1.
file_path (optional): Path to the CSV file containing results. Default: 'results.csv'.
Description: Adds multiple results to a specified competition by reading them from a CSV file.

Expected Output:
"Results added successfully" on success.
"Competition with id X does not exist" if the competition ID is invalid.

# 6. Get Competition Results
Command:

```bash
flask get_competition_results <competition_id>
```
Arguments:
competition_id (optional): ID of the competition. Default: 1.
Description: Displays the results of a specific competition.

Output:
Prints the list of results for the competition.
"Competition with id X does not exist" if the competition ID is invalid.
How to Run the Program
# Install dependencies using the command:

```bash
pip install -r requirements.txt
```
# Initialize the database:

```bash
flask init
```
Use any of the commands described above to manage competitions and results.

Notes
Ensure the Flask app is properly configured and set up before running the commands.
If you encounter any issues with date formats or file paths, check the input formats and ensure the CSV file is structured correctly.
