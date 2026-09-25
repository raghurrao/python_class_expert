# Day 18: Running Your First Migration!

Welcome to the grand finale! Alembic is fully configured. It knows where your database is (`blog.db`) and it knows what your tables look like (`models.py`). 

Now it's time to actually generate and run a migration!

---

## Step 1: Autogenerate

**Concept:** You can tell Alembic to compare your Python classes against the actual database and automatically figure out what changed!

**🎯 Your Turn (Task 1):** 
Open your terminal and run this exact command:
```bash
python -m alembic revision --autogenerate -m "Initial migration"
```
*(You will see Alembic create a new Python script inside the `alembic/versions/` folder. This script contains the `upgrade()` and `downgrade()` instructions!)*

---

## Step 2: Upgrade

**Concept:** Generating the migration script doesn't actually change the database. To apply the script to the live database, you use the `upgrade` command.

**🎯 Your Turn (Task 2):**
In your terminal, run this exact command:
```bash
python -m alembic upgrade head
```
*(This tells Alembic to apply all migrations up to the "head", which is the latest one. Alembic will also create a new table called `alembic_version` to track which migration is currently applied).*

Run `python test_day_18.py` to verify that Alembic successfully stamped the database with your new migration version!
