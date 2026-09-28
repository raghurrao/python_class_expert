# SQL 30-Day Course

Self-study course from beginner to advanced SQL using SQLite and a reusable university/business database.

## Contents

- `lessons/`: 30 guided daily lessons with examples, exercises, checks, and revision notes.
- `exercises/`: question-only SQL scripts; solutions are kept separately.
- `solutions/`: runnable answer scripts with explanatory comments.
- `database/`: schema, seed data, reset script, and initialized `university.db`.
- `assessments/`: weekly checks and final examination.
- `projects/`: university capstone and project solution.

## Setup and use

SQLite 3.25+ is recommended (window functions are used on Day 28). Install the SQLite command-line tool from sqlite.org or use DB Browser for SQLite. Open `database/university.db` in DB Browser, then use Execute SQL to run a script. With the CLI, run `sqlite3 database/university.db < exercises/day_01_exercises.sql`.

To rebuild the sample database, run `python database/reset_database.py`. This recreates the database from the SQL scripts; make a copy first if you have added data you want to keep. Open a lesson, follow its examples, attempt the linked exercise file, then consult its separately linked solution file. Run solutions against a disposable database copy when they modify data. Follow `study_plan.md` in order and complete weekly assessments.

SQLite enforces foreign keys per connection: enable with `PRAGMA foreign_keys=ON`. SQLite does not implement stored procedures or ANY/ALL operators; lessons explain equivalent patterns and limitations.
