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

day11_cells = [
    create_markdown_cell("# PHASE 2 — REGRESSION"),
    create_markdown_cell("# Day 11 — Polynomial Regression"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Identify when a dataset has a non-linear relationship.\n- Use `PolynomialFeatures` to engineer new, curved features.\n- Combine `PolynomialFeatures` and `LinearRegression` inside a Pipeline to perform Polynomial Regression.\n- Understand the mathematical expansion of polynomial terms."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 8 (Linear Regression).\n- Day 5 (Pipelines)."),
    
    create_markdown_cell("## 3. Concept\nStandard Linear Regression draws a straight line. But what if the data curves? (e.g., Disease spread grows exponentially, not linearly. Car fuel efficiency improves at certain speeds and then rapidly drops off).\n\nIf you fit a straight line to curved data, you will **Underfit** (High Bias). \n\n**Polynomial Regression** is a clever trick. We don't actually change the Linear Regression algorithm. Instead, we change the *data* by mathematically squaring or cubing the existing features before feeding them to the algorithm."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nLinear models are fast and interpretable. By using Polynomial Features, we can force a simple, fast Linear Model to learn highly complex, curved patterns, giving us the best of both worlds (speed and complexity)."),
    
    create_markdown_cell("## 5. Intuition\nImagine you only have one feature: $x_1$ (Width of a square pool). You want to predict the Volume of water it holds. \nA linear model tries to learn: $Volume = \\beta_0 + \\beta_1(Width)$. This will fail because Volume scales by the cube of Width! \nIf we mathematically engineer a new column $x_2 = Width^3$, we can feed that to the linear model. Now the linear model can perfectly \"draw a straight line\" through the cubed data."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nStandard Linear Regression equation:\n$$ \\hat{y} = \\beta_0 + \\beta_1x_1 $$\n\nPolynomial expansion of degree 2 creates a new feature $x_1^2$:\n$$ \\hat{y} = \\beta_0 + \\beta_1x_1 + \\beta_2x_1^2 $$\n\nNotice that the equation is still **linear with respect to the coefficients ($\\beta$)**. We are just multiplying a coefficient by a different number. Therefore, standard OLS math still solves this perfectly!"),
    
    create_markdown_cell("## 7. Scikit-learn API\nWe use `PolynomialFeatures` from `sklearn.preprocessing`. It acts exactly like a Scaler or Imputer (it has a `.fit_transform()` method).\n\n```python\nfrom sklearn.preprocessing import PolynomialFeatures\npoly = PolynomialFeatures(degree=2, include_bias=False)\nX_poly = poly.fit_transform(X)\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate data that curves like a parabola ($y = ax^2 + bx + c$) and see how a straight line fails, but a polynomial pipeline succeeds."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.linear_model import LinearRegression",
        "from sklearn.preprocessing import PolynomialFeatures",
        "from sklearn.pipeline import Pipeline",
        "from sklearn.metrics import mean_squared_error",
        "",
        "# 1. Generate curved data",
        "np.random.seed(42)",
        "X = 6 * np.random.rand(100, 1) - 3 # Values between -3 and 3",
        "y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1) # y = 0.5x^2 + x + 2 + noise",
        "",
        "# 2. Train Standard Linear Regression (Straight Line)",
        "lin_reg = LinearRegression()",
        "lin_reg.fit(X, y)",
        "",
        "# 3. Train Polynomial Pipeline (Curved Line)",
        "poly_pipe = Pipeline([",
        "    ('poly', PolynomialFeatures(degree=2, include_bias=False)),",
        "    ('model', LinearRegression())",
        "])",
        "poly_pipe.fit(X, y)",
        "",
        "print('Linear RMSE:', np.sqrt(mean_squared_error(y, lin_reg.predict(X))))",
        "print('Poly RMSE:  ', np.sqrt(mean_squared_error(y, poly_pipe.predict(X))))"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We explicitly generated data using the math formula $y = 0.5x^2 + 1x + 2$.\n- The standard `LinearRegression` failed because it tried to push a straight line through a U-shape.\n- The `PolynomialFeatures(degree=2)` took our $X$ column, and silently created a second column containing $X^2$.\n- The `LinearRegression` inside the pipeline then assigned a coefficient to $X$ and a coefficient to $X^2$, allowing it to perfectly match the curve."),
    
    create_markdown_cell("## 10. Experiment\nLet's visualize the difference between the models."),
    create_code_cell([
        "X_plot = np.linspace(-3, 3, 100).reshape(100, 1)",
        "",
        "plt.scatter(X, y, color='blue', alpha=0.5, label='Actual Data')",
        "plt.plot(X_plot, lin_reg.predict(X_plot), color='red', linestyle='--', linewidth=2, label='Linear Model (Underfit)')",
        "plt.plot(X_plot, poly_pipe.predict(X_plot), color='green', linewidth=3, label='Polynomial Model (Degree 2)')",
        "plt.xlabel('X')",
        "plt.ylabel('y')",
        "plt.legend()",
        "plt.show()"
    ]),
    create_markdown_cell("> As you can see, the green line perfectly captures the underlying mathematical function."),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "poly_features = PolynomialFeatures(degree=3, include_bias=False)",
        "X_dummy = np.array([[2.0], [3.0]])",
        "X_dummy_poly = poly_features.fit_transform(X_dummy)"
    ]),
    create_markdown_cell("> **Question:** What exactly will `X_dummy_poly` look like? How many columns will it have, and what will the numbers be for the first row?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print(X_dummy_poly)",
        "print('\\nWhy? Degree 3 creates x^1, x^2, and x^3. For the first row (2.0), that is 2^1=2, 2^2=4, 2^3=8.')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nWhat happens if the degree is too high? \nBuild a pipeline with `degree=50`. Fit it on `X` and `y`. Plot its predictions over `X_plot` (just like Section 10). What happens at the edges of the graph?"),
    create_code_cell([
        "# YOUR CODE HERE",
        "crazy_pipe = Pipeline([",
        "    ('poly', PolynomialFeatures(degree=50, include_bias=False)),",
        "    ('scaler', StandardScaler()), # Need scaling for extreme exponents!",
        "    ('model', LinearRegression())",
        "])",
        "crazy_pipe.fit(X, y)",
        "",
        "plt.scatter(X, y, color='blue', alpha=0.5)",
        "plt.plot(X_plot, crazy_pipe.predict(X_plot), color='red', linewidth=2)",
        "plt.ylim(0, 10)",
        "plt.title('Degree 50 Polynomial (Massive Overfitting)')",
        "plt.show()",
        "print('Notice how the red line wiggles wildly to hit every point. This is classic Overfitting!')"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nA data scientist tried to apply polynomial features to a dataset with 5 features, but their computer ran out of RAM and crashed. Why?"),
    create_code_cell([
        "# Buggy conceptual code",
        "try:",
        "    X_big = np.random.rand(100, 10)",
        "    # THE DANGER IS HERE:",
        "    # poly_big = PolynomialFeatures(degree=5)",
        "    # X_big_poly = poly_big.fit_transform(X_big)",
        "    print('Error: Combinatorial Explosion!')",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** `PolynomialFeatures` doesn't just square individual columns. It calculates all combinations! If you have $a, b, c$, degree 2 creates $a^2, b^2, c^2, ab, ac, bc$. \n> If you have 10 features and degree 5, it generates **3,003 columns**. This causes a combinatorial explosion that crashes computers. **Rule:** Rarely use a degree > 3 on datasets with multiple features."),
    
    create_markdown_cell("## 14. Model Evaluation\nIf degree 1 underfits, and degree 50 overfits, how do we choose the right degree? \nWe must use cross-validation (which we will cover in Phase 4). You loop over degrees 1 through 10, check the Test RMSE, and pick the degree that has the lowest error on unseen data."),
    
    create_markdown_cell("## 15. Real-World Example\nIn chemical manufacturing, the yield of a reaction often depends on the *interaction* between Temperature and Pressure. \nA standard Linear Regression model treats them entirely independently. By using `PolynomialFeatures(degree=2)`, Scikit-learn automatically creates a new column `Temperature * Pressure` (called an interaction term). The linear model can assign a coefficient to this interaction term, allowing it to mathematically model how the two variables affect each other!"),
    
    create_markdown_cell("## 16. Mini Project\nProve that `PolynomialFeatures` generates interaction terms. Create a tiny dataset with 2 features (`a` and `b`). Apply `PolynomialFeatures(degree=2)`. Look at the `.get_feature_names_out()` method."),
    create_code_cell([
        "import pandas as pd",
        "tiny_X = pd.DataFrame({'Temp': [10, 20], 'Pressure': [5, 10]})",
        "",
        "poly2 = PolynomialFeatures(degree=2, include_bias=False)",
        "tiny_poly = poly2.fit_transform(tiny_X)",
        "",
        "print('Original Features: Temp, Pressure')",
        "print('Generated Features:', poly2.get_feature_names_out())",
        "print('\\nNotice the Temp Pressure interaction term!')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Forgetting to Scale**: $X^{10}$ creates astronomically large numbers. You **must** put a `StandardScaler` *after* the `PolynomialFeatures` but *before* the model, or the model's math will overflow.\n- **Exploding RAM**: Using degree=4 on a dataset with 50 features.\n- **Overfitting**: Forcing a high-degree polynomial on a small dataset."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: How does Polynomial Regression differ from Linear Regression?\n- **Intermediate**: Does Polynomial Regression use a different underlying algorithm than Linear Regression?\n- **Advanced**: Explain what an \"interaction term\" is and how `PolynomialFeatures` generates it."),
    
    create_markdown_cell("## 19. Knowledge Check\n- What method shows you the mathematical names of the generated columns? (`.get_feature_names_out()`)\n- If you have features A and B, what are all the columns generated by degree 2? ($A, B, A^2, B^2, AB$)"),
    
    create_markdown_cell("## 20. Summary\n- **Polynomial Regression** solves non-linear problems using linear models.\n- It works by expanding the dataset with squared/cubed/interaction terms.\n- Use `PolynomialFeatures` inside a `Pipeline`.\n- Beware of combinatorial explosion and overfitting with high degrees."),
    
    create_markdown_cell("## 21. Homework\nLoad a dataset with a known non-linear curve (like Sine wave data). Build a pipeline with `PolynomialFeatures(degree=3)` and `Ridge`. Plot the line of best fit.")
]

# Read existing notebook and update cells
filename = "Day_11_Polynomial_Regression.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day11_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
