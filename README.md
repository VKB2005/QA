## 🛠️ Setup and Installation

To run this project, you'll need to have **Python 3** and **Google Chrome** installed.

1.  **Clone the Repository**
    ```bash
    git clone <https://github.com/VKB2005/QA.git>
    cd QA
    ```

2.  **Create and Activate a Virtual Environment**
    This keeps the project dependencies isolated.
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  [cite_start]**Install Dependencies** 
    [cite_start]Install all the required Python packages using the `requirement.txt` file. 
    ```bash
    pip install -r requirement.txt
    ```

---
## How to Run the Tests

Make sure your virtual environment is activated. Run the tests by specifying the path to each test file:

```bash
# To run all API tests
pytest tests/api_tests.py

# To run all UI tests
pytest tests/ui_tests.py