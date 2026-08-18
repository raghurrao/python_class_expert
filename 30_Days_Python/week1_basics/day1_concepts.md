# Day 1: Setting Up VS Code & Python

Welcome to Day 1 of your 30-day journey to becoming a Python expert! Before we write code, we need a solid development environment. Today, you will install Python, install Visual Studio Code (VS Code), configure them to work together, and execute your first script.

---

## Step 1: Install Python on Windows

1. **Download Python**: Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/) and click the download button for the latest Python version (Python 3.11 or 3.12 is recommended).
2. **Run Installer**: Double-click the downloaded `.exe` installer.
3. **IMPORTANT CONFIGURATION**:
   > [!IMPORTANT]
   > At the bottom of the installer window, make sure to check the box that says **"Add python.exe to PATH"**. If you do not do this, your terminal will not recognize Python commands, and you will have to reinstall it.
4. **Choose Install Now**: Click **Install Now**.
5. **Verify Installation**:
   - Open PowerShell or Command Prompt.
   - Type the following command and press Enter:
     ```powershell
     python --version
     ```
   - It should output something like `Python 3.12.x`. If it does, Python is successfully installed!

---

## Step 2: Install Visual Studio Code (VS Code)

1. **Download VS Code**: Go to [https://code.visualstudio.com/](https://code.visualstudio.com/) and download the Windows Installer.
2. **Run Installer**: Open the downloaded installer, accept the license agreement, and click Next.
3. **Select Additional Tasks**: Keep all defaults checked. It is highly recommended to check **"Add to PATH (requires shell restart)"**.
4. **Complete Installation**: Click Install and finish.

---

## Step 3: Install the Python Extension in VS Code

VS Code is a lightweight text editor. To make it a powerful IDE for Python, we install extensions.

1. Open VS Code.
2. Open the Extensions View by clicking the Extensions icon on the Activity Bar on the left side of the window (or press `Ctrl+Shift+X`).
3. Search for **Python**.
4. Look for the extension published by **Microsoft** and click **Install**. (This installs Python linting, debugging, formatting, and intellisense).

---

## Step 4: Configure the Python Interpreter in VS Code

1. Open your workspace folder in VS Code (`File` > `Open Folder...` > select `g:\30 days Leaarning\30_Days_Python`).
2. Open the Command Palette using `Ctrl+Shift+P`.
3. Type `Python: Select Interpreter` and select it.
4. Choose the Python version you installed from the list (it should show the path to your installed `python.exe`).

---

## Step 5: How to Run Python Code

There are three main ways to run Python code in VS Code:
1. **The Play Button**: Open a `.py` file. Click the Play button in the top-right corner of the editor.
2. **Terminal (Recommended)**: Open the integrated terminal (`Ctrl+`` or `Terminal` > `New Terminal`) and run:
   ```powershell
   python filename.py
   ```
3. **Interactive Window / Jupyter**: Using standard code blocks.

---

Now, proceed to the Day 1 Assignment: [day1_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week1_basics/day1_assignment.py). Follow the instructions there to verify that your setup is working!
