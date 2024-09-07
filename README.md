
# Stock Portfolio Management System

## Table of Contents

- [Summary](#summary)
- [Overall Structure and Interaction](#overall-structure-and-interaction)
- [Key Components and Data Structures/Algorithms](#key-components-and-data-structuresalgorithms)
- [Logic Flow Across Files](#logic-flow-across-files)
- [Inputs/Outputs Across the Codebase](#inputsoutputs-across-the-codebase)
- [Dependencies](#dependencies)
- [Key Highlights](#key-highlights)
- [Further Development](#further-development)

## Summary

This codebase implements a rudimentary stock portfolio management system, providing users with functionality to buy, sell, view their portfolio, track bank balance, and visualize stock prices. The system relies on a MySQL database for user authentication and storage of portfolio data. 

## Overall Structure and Interaction

The code follows a clear, modular design. It primarily operates within a main loop driven by user input. The loop presents options for buying, selling, viewing portfolio, checking balance, and exiting. Each option triggers the execution of specific functions, which interact with the database, CSV files, and other libraries to perform the desired operations. 

## Key Components and Data Structures/Algorithms

- **Database Interaction:** The code leverages the `mysql.connector` library to interact with a MySQL database. It utilizes SQL queries for user authentication, creation of user-specific databases, data insertion, update, and retrieval.
- **Data Structures:**
    - **Dictionaries:** Used to store mappings between company names, IDs, and CSV file names, facilitating efficient lookup.
    - **Lists:** Used for storing and manipulating data fetched from the database.
- **Algorithms:**
    - **Buy/Sell Logic:** Involves calculating total cost/returns based on share price, checking available funds, and updating database tables accordingly.
    - **Returns Calculation:** Calculates returns based on current and original share prices, leveraging simple arithmetic calculations.
    - **Graph Plotting:** Utilizes `matplotlib.pyplot` for visualizing stock prices, leveraging plotting functionalities for data visualization.

## Logic Flow Across Files

The code primarily operates within the `Stock Portfolio.py` file. The logic flow can be summarized as follows:

1. **Initialization:** The script begins by importing required libraries, defining dictionaries, and establishing a connection to the MySQL database. 
2. **User Authentication:** The code prompts for user login or signup. Login checks credentials against the database, while signup creates a new database for the user with tables for current shares and transaction history.
3. **Main Loop:** The loop repeatedly presents user options and executes corresponding functions based on input.
    - **Buy Shares:** Fetches share price, calculates total cost, updates balances, and records the purchase in the database.
    - **Sell Shares:** Calculates returns, updates the transaction history, removes sold shares from the portfolio, and updates balances.
    - **View Portfolio:** Retrieves and displays data from the 'CURRENT_SHARES' and 'TRANSACTION_HISTORY' tables, including optional returns calculation for specific companies.
    - **View Balance:** Displays the current DMAT balance.
    - **Exit:** Closes the database connection, updates balances, and exits the program.
4. **Function Calls:** Each option triggers appropriate functions for specific tasks, such as `buy_shares()`, `sell_shares()`, `view_tables()`, and `view_balance()`.

## Inputs/Outputs Across the Codebase

- **Inputs:**
    - **User Authentication:** Username, password, bank details (LOGIN_ID, PIN)
    - **Portfolio Management:** Company ID, quantity of shares (buy/sell), options (B, I, S, V, T, D, E)
- **Outputs:**
    - **User Authentication:** Success/error messages
    - **Portfolio Management:** Success/error messages, company IDs, stock chart, portfolio table data, bank balance, returns

## Dependencies

- **Database:** MySQL (requires `mysql.connector` library)
- **Visualization:** Matplotlib (`matplotlib.pyplot`)
- **Data Handling:** pandas (`pandas`)
- **CSV Reading:** csv (`csv`) 

## Key Highlights

- The code demonstrates a basic implementation of a stock portfolio management system. 
- It relies on a database to store user data and portfolio information, ensuring persistent storage and data integrity.
- The code utilizes functions for modularity, encapsulating specific functionalities, and enhancing code readability.
- It incorporates visualization features to display stock prices using matplotlib, providing users with visual insights.
- The code integrates data handling with pandas for reading CSV files and manipulating data.

## Further Development

- Enhance user interface with more user-friendly input methods and output formatting.
- Implement more sophisticated stock data fetching and analysis capabilities.
- Integrate real-time price updates to enhance accuracy and provide up-to-date information.
- Add more features like setting watchlists, tracking historical performance, and generating reports.
- Implement robust error handling and security measures to ensure data integrity and user safety.


