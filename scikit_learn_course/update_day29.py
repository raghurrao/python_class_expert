import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [source]
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [s + "\n" if not s.endswith("\n") else s for s in source]
    }

def create_code_cell(source):
    if isinstance(source, str):
        source = [source]
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [s + "\n" if not s.endswith("\n") else s for s in source]
    }

day29_cells = [
    create_markdown_cell("# PHASE 5 — ADVANCED WORKFLOWS & PRODUCTION"),
    create_markdown_cell("# Day 29 — Model Production (Joblib)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain what it means to put a model into \"Production\".\n- Use `joblib` to serialize (save) a trained Scikit-learn Pipeline to your hard drive.\n- Deserialize (load) that model into a brand new Python script to make predictions.\n- Understand why saving the full Pipeline (and not just the model) is absolutely critical for production."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 5 (Pipelines)."),
    
    create_markdown_cell("## 3. Concept: The Jupyter Notebook Trap\nFor the last 28 days, every time you ran a notebook, it spent 10 seconds doing `.fit()` to train the model, and then immediately made predictions. \n\nIn the real world, you do not train a model every time a customer clicks a button on a website. Training on massive datasets can take days and cost thousands of dollars in cloud computing. \n\nInstead, you train the model **once**. You save the \"brain\" of the model to a file (like saving a Word document). Then, a web developer loads that tiny file onto a web server. When a customer clicks a button, the server just calls `.predict()` (which takes 0.001 seconds)."),
    
    create_markdown_cell("## 4. Concept: Serialization (Pickling)\nIn Python, saving an object (like a trained Scikit-learn Pipeline) to the hard drive is called **Serialization** (or \"Pickling\"). \nIt converts the mathematical arrays, the trees, and the scalers into a byte-stream and writes it to a file, usually with a `.pkl` or `.joblib` extension."),
    
    create_markdown_cell("## 5. Scikit-learn API\n```python\nimport joblib\n# Save to hard drive\njoblib.dump(trained_pipeline, 'my_model.joblib')\n\n# Load from hard drive (in a totally different script!)\nloaded_model = joblib.load('my_model.joblib')\n```"),
    
    create_markdown_cell("## 6. Simple Example: Saving a Model\nLet's train a Pipeline on some data, just like we always do, and then save it to the hard drive."),
    create_code_cell([
        "import pandas as pd",
        "import joblib",
        "import os",
        "from sklearn.datasets import make_classification",
        "from sklearn.ensemble import RandomForestClassifier",
        "from sklearn.preprocessing import StandardScaler",
        "from sklearn.pipeline import Pipeline",
        "",
        "# 1. Generate Training Data",
        "X_train, y_train = make_classification(n_samples=1000, n_features=5, random_state=42)",
        "",
        "# 2. Build and Train the Pipeline",
        "production_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('rf', RandomForestClassifier(n_estimators=50, random_state=42))",
        "])",
        "",
        "print('Training model...')",
        "production_pipe.fit(X_train, y_train)",
        "print('Training complete!')",
        "",
        "# 3. Save the Pipeline to the hard drive",
        "joblib.dump(production_pipe, 'spam_detector_v1.joblib')",
        "",
        "print(f'\\nModel saved successfully! File size: {os.path.getsize(\"spam_detector_v1.joblib\") / 1024:.1f} KB')"
    ]),
    
    create_markdown_cell("## 7. Code Walkthrough\n- We ran `.fit()` on the Pipeline.\n- The `StandardScaler` calculated the means and standard deviations of the 1,000 rows.\n- The `RandomForestClassifier` built 50 decision trees.\n- `joblib.dump()` took all of that math and saved it to a file named `spam_detector_v1.joblib`."),
    
    create_markdown_cell("## 8. Experiment: Loading the Model (Production Simulation)\nImagine this next cell is a completely different Python script running on a web server in another country. \nA user just filled out a form on a website, and the server received 1 row of data. \nThe server does NOT have the training data. It does NOT call `.fit()`. It simply loads the `.joblib` file and calls `.predict()`!"),
    create_code_cell([
        "# Assume this is a new script (e.g., app.py on a Flask/Django server)",
        "",
        "# 1. Load the model from the hard drive",
        "server_model = joblib.load('spam_detector_v1.joblib')",
        "print('Model loaded from disk successfully!')",
        "",
        "# 2. User submits 1 row of new data from the website",
        "user_input = pd.DataFrame([[0.5, -1.2, 3.4, 0.1, -0.9]])",
        "",
        "# 3. Make the prediction instantly",
        "prediction = server_model.predict(user_input)",
        "probability = server_model.predict_proba(user_input)[0][1]",
        "",
        "print(f'\\nPrediction: Class {prediction[0]}')",
        "print(f'Confidence: {probability * 100:.1f}%')"
    ]),
    create_markdown_cell("> Notice how incredibly fast that was! The server didn't have to train anything. It just executed the pre-learned math."),
    
    create_markdown_cell("## 9. Prediction Exercise\nRead the following scenario, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "# Bad Practice: Saving just the model, not the pipeline",
        "bad_scaler = StandardScaler()",
        "X_scaled = bad_scaler.fit_transform(X_train)",
        "",
        "bad_rf = RandomForestClassifier()",
        "bad_rf.fit(X_scaled, y_train)",
        "",
        "joblib.dump(bad_rf, 'bad_model.joblib')"
    ]),
    create_markdown_cell("> **Question:** The engineer above scaled the data manually, trained the Random Forest, and saved *only* the Random Forest to the hard drive. \n> When the web server loads `bad_model.joblib` and receives raw `user_input`, what will happen when it calls `predict()`?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('Error: The model will output complete garbage!')",
        "print('Why? The Random Forest was trained on SCALED data (values between -3 and 3).')",
        "print('If the user inputs a raw Salary of $85,000, the Random Forest has no idea what to do with that massive number.')",
        "print('Because the engineer didn\\'t save the Scaler, the web server has no way to scale the $85,000 down to the correct proportion.')"
    ]),
    
    create_markdown_cell("## 10. The Golden Rule of Production\n**ALWAYS SAVE THE PIPELINE.**\nIf you save the entire Pipeline to the `.joblib` file, the Pipeline remembers the `StandardScaler`. It remembers the exact Means and Standard Deviations from the training set. \nWhen the web server calls `server_model.predict(user_input)`, the Pipeline automatically routes the raw `$85,000` through the saved Scaler, transforms it to `1.2`, and then passes `1.2` to the Random Forest. It guarantees the math is perfectly identical to the training environment!"),
    
    create_markdown_cell("## 11. Coding Exercise\nLoad the model `spam_detector_v1.joblib` one more time. \nWe can actually peek inside the loaded file to prove it saved the Scaler's math.\nPrint out `server_model.named_steps['scaler'].mean_`. This will output the 5 means the scaler memorized during training!"),
    create_code_cell([
        "# YOUR CODE HERE",
        "server_model = joblib.load('spam_detector_v1.joblib')",
        "saved_means = server_model.named_steps['scaler'].mean_",
        "print('The means memorized by the saved Scaler:')",
        "print(saved_means)"
    ]),
    
    create_markdown_cell("## 12. Debugging Challenge\nA company trains a model using Scikit-learn `v1.5.0` on a Windows machine. They save it as `model.joblib`. \nThey send it to their DevOps team, who loads it onto a Linux server running Scikit-learn `v0.22.0`. The server crashes with a `ModuleNotFoundError` or `ValueError` when trying to load the file. Why?"),
    create_code_cell([
        "# Conceptual Bug",
        "print('Error: Joblib files are highly version-dependent.')",
        "print('A Pipeline saved in Scikit-learn v1.5 cannot be loaded by Scikit-learn v0.22.')",
        "print('The internal Python code for the Random Forest changed between those versions, so the byte-stream no longer makes sense to the older version.')"
    ]),
    create_markdown_cell("> **Rule:** Your Training Environment (Jupyter) and your Production Environment (Web Server) MUST use the exact same version of Scikit-learn and Python! (This is usually managed via `requirements.txt` or Docker)."),
    
    create_markdown_cell("## 13. Model Evaluation (Monitoring)\nOnce a model is in production, your job isn't over. Models suffer from **Data Drift**. \nIf you trained a house price model in 2019, and deploy it in 2024, it will massively underpredict prices because of inflation. \nYou must constantly monitor the model's predictions in production, and if they start becoming inaccurate, you must pull the newest data, retrain a new model, and save a `v2.joblib` file!"),
    
    create_markdown_cell("## 14. Real-World Example\n**Zillow Zestimate**: Zillow's data scientists train massive gradient boosting pipelines on historical housing data. They save these pipelines as `.pkl` or `.joblib` files and deploy them to cloud servers (AWS/GCP). When you open the Zillow app and look at a house, your phone sends the house's features (Beds, Baths, SqFt) to the AWS server. The server loads the `.joblib` file into RAM, runs `.predict()`, and sends the price back to your phone in milliseconds."),
    
    create_markdown_cell("## 15. Mini Project\nLet's clean up our hard drive. Use Python's built-in `os` module to delete the `spam_detector_v1.joblib` file we created earlier, just to prove we know how to manage files!"),
    create_code_cell([
        "import os",
        "",
        "file_path = 'spam_detector_v1.joblib'",
        "if os.path.exists(file_path):",
        "    os.remove(file_path)",
        "    print(f'{file_path} has been successfully deleted from the hard drive.')",
        "else:",
        "    print('File not found.')"
    ]),
    
    create_markdown_cell("## 16. Common Mistakes\n- **Not saving the Scaler**: The most catastrophic mistake a Junior Data Scientist makes. The web server must have the exact same Scaler object that was used during training. Put it in a Pipeline!\n- **Version Mismatches**: Training on Python 3.12 and deploying on Python 3.8. It will crash.\n- **Uploading massive datasets to the server**: The web server does not need `X_train.csv`. It only needs the 500KB `.joblib` file!"),
    
    create_markdown_cell("## 17. Interview Questions\n- **Beginner**: What library do we use to save a Scikit-learn model to the hard drive? (Answer: `joblib` or `pickle`).\n- **Intermediate**: Why is it critical to save a `Pipeline` instead of just the final algorithm? (Answer: Because the preprocessing steps, like `StandardScaler` or `OneHotEncoder`, contain learned math (like means or categories). If you don't save them, the production server cannot process raw user input correctly).\n- **Advanced**: What is Data Drift? (Answer: The phenomenon where a deployed model's accuracy degrades over time because the real-world data it is predicting on has fundamentally shifted away from the historical data it was trained on)."),
    
    create_markdown_cell("## 18. Knowledge Check\n- What function saves the model? (`joblib.dump()`)\n- What function loads the model? (`joblib.load()`)\n- Does `.load()` require you to run `.fit()` again? (No, the model is already trained)"),
    
    create_markdown_cell("## 19. Summary\n- **Production** means exposing your trained model to the real world (usually via a web server).\n- **Joblib** is used to save (`dump`) and load (`load`) models.\n- You must ALWAYS save the full **Pipeline** so the server remembers how to scale and encode raw user data.\n- Web servers only call `.predict()`, never `.fit()`.\n- You must ensure Python and Scikit-learn versions match between training and production environments."),
    
    create_markdown_cell("## 20. Homework\nTomorrow is Day 30, the Final Capstone! \nTake today to review Phase 4 and 5. Make sure you fully understand Pipelines, Cross-Validation, and GridSearchCV, as you will need all of them to pass the final exam!")
]

# Read existing notebook and update cells
filename = "Day_29_Model_Interpretation_and_Production.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day29_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
