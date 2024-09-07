
# Stock Portfolio System: A Comprehensive Overview

This Python script, `StockPortfolio.py`, implements a robust stock portfolio management system that allows users to buy and sell shares, view their holdings, track transactions, and analyze stock performance. The codebase effectively integrates database management, file handling, and data visualization functionalities.

---

## Table of Contents

- [Overall Structure and Interaction](#overall-structure-and-interaction)
- [Key Components and Data Structures/Algorithms](#key-components-and-data-structuresalgorithms)
- [Logic Flow Across Files](#logic-flow-across-files)
- [Inputs/Outputs Across the Codebase](#inputsoutputs-across-the-codebase)
- [Dependencies](#dependencies)

---

## Overall Structure and Interaction

The script operates within a main loop that provides users with a menu of options. The user interacts with the system by selecting actions from the menu, driving the flow of the program. The central functionality revolves around the `buy`, `sell`, `view_chart`, `show_tables`, and `show_balance` functions, each handling a specific task within the portfolio management workflow. The script heavily relies on external libraries and database connections for crucial operations. 

---

## Key Components and Data Structures/Algorithms

### Key Components:

- **Database Interaction:** The system uses `mysql.connector` for database interaction, managing user information, transaction history, and current stock holdings in separate tables for each user.
- **Data Storage & Retrieval:**  Data is stored in CSV files for stock prices and in MySQL databases for user details, holdings, and transactions. The script leverages Python's `csv` and `MySQLdb` modules for efficient data manipulation.
- **Data Visualization:** `matplotlib.pyplot` library is used to display stock price charts, enabling users to analyze historical stock trends.
- **Data Processing & Analysis:**  The system utilizes various functions to calculate purchase costs, sale returns, and other relevant financial metrics, facilitating informed decision-making.

### Data Structures:

- **Dictionaries:** Several dictionaries, including `comp_names_dict`, `comp_ids_csv`, and `comp_ids`, are used to map company codes to their names, CSV file names, and database IDs respectively. These dictionaries streamline data access and lookup operations.
- **Lists:** Lists are used to store data retrieved from databases and CSV files, providing a flexible and efficient way to manage collections of data.

### Algorithms:

- **Data Retrieval:** SQL queries are extensively used to retrieve information from the MySQL databases, ensuring efficient and structured access to data.
- **Data Parsing:** The script processes CSV files to extract stock price data, employing efficient parsing techniques for extracting relevant information.
- **Financial Calculation:** Simple mathematical algorithms are used to calculate purchase costs, sale returns, and other financial metrics based on stock prices, quantities, and user balances.
- **Chart Plotting:** The `matplotlib.pyplot` library enables the system to generate visual representations of stock price data over time, aiding in user analysis.

---

## Logic Flow Across Files

- The script begins by importing necessary libraries and defining dictionaries for data mapping.
- The user is prompted to either log in or sign up.
- For login, the username and password are validated against the `user_id_data` database.
- If a new user signs up, a new database is created for them with tables for their current shares and transaction history.
- The script then establishes a connection to the user's specific database.
- The main loop presents the user with options:
    - **Buy (B):**  The user enters the company ID, the script retrieves the latest price from the CSV file, calculates the cost, checks the user's balance, and updates the database upon successful purchase.
    - **Sell (S):** The user enters the company ID and number of shares. The script calculates the returns, updates the transaction history, removes the shares from the holdings table, and updates the balance.
    - **View Stock Chart (V):** The user enters a company ID, and the script generates a chart using `matplotlib.pyplot`.
    - **Show Company IDs (I):** The script displays a list of available company IDs and their names.
    - **Show Tables (T):** The script displays the user's current holdings and transaction history tables, optionally calculating returns for a specific company.
    - **Show Bank Balance (D):** The script displays the user's current bank balance.
    - **Exit (E):** The script closes the database connection, updates the balance, and exits the loop.

---

## Inputs/Outputs Across the Codebase

### Inputs:

- User credentials (username, password)
- Company ID for buy/sell actions
- Number of shares for buy/sell actions
- Confirmation for purchase/sale actions

### Outputs:

- Login/signup success/failure messages
- Share prices
- Total purchase cost
- Sale returns
- Bank balance
- Current share holdings and transaction history tables
- Stock price charts

---

## Dependencies

- `mysql.connector`: For MySQL database interaction.
- `matplotlib.pyplot`: For plotting charts.
- `pandas`: For data manipulation and analysis (though not directly used in the provided description).
- `csv`: For reading CSV files containing stock prices.



The script leverages these libraries to provide comprehensive functionality, including database management, data visualization, and financial calculations.  The clear separation of concerns into functions enhances code readability and maintainability, while the well-defined data structures and algorithms ensure efficient data processing and analysis.

```

