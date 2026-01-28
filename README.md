# Video Game Rental System (VGRS) - Procedural Programming Project

A comprehensive Python application for managing a video game rental store with customer subscription validation, automated rental processing, and inventory analytics.

## Project Overview

This is a procedural programming project that implements a video game management system. It supports store manager operations including real-time inventory searching, rental and return management, and data-driven inventory pruning. The system strictly follows assignment constraints: no Classes, no SQL, and a modular architecture.



## Architecture

### Core Modules

#### Rental & Transaction Management
- **`gameRent.py`** - Handles the checkout process for customers
  - Validates Customer IDs (4-letter format) and Game IDs.
  - Interfaces with `subscriptionManager.pyc` to enforce rental limits based on user tiers.
  - `game_rent()`: Coordinates verification, availability checks, and record updates.
  
- **`gameReturn.py`** - Manages game check-ins and customer feedback
  - Updates `Rental.txt` by replacing `NULL` return dates with the current timestamp.
  - Interfaces with `feedbackManager.pyc` to record star ratings and comments.
  - `game_return()`: Validates that a game is currently rented before allowing a return.

#### Inventory & Search
- **`gameSearch.py`** - Provides multi-criteria search functionality
  - `Title_Search()`: Filters inventory by game title.
  - `Genre_Search()`: Filters inventory by game category.
  - `Platform_Search()`: Filters inventory by console (e.g., PlayStation, Xbox).
  - Integrates a `rentable()` check to display real-time availability for every search result.

#### Analytics & Pruning
- **`InventoryPruning.py`** - Business intelligence and stock optimization
  - `create_graph()`: Uses **Matplotlib** to visualize game popularity based on user ratings.
  - `Popular_and_unpopular_Games()`: Analyzes rental frequency to identify underperforming assets.
  - Suggests games for removal based on low rental counts or poor feedback (ratings <= 2).

#### Data Layer
- **`database.py`** - Centralized file I/O utility module
  - `Read_File()`: Parses delimited text files into accessible Python lists.
  - `WriteList_File()`: Overwrites data files with updated record lists.
  - `AppendLine_File()`: Appends new transaction entries to history logs.

#### GUI
- **`menu.ipynb`** - Main manager interface using **IPyWidgets**
  - Provides a single-window Graphical User Interface.
  - Features interactive buttons and input fields for all store operations.
  - Strictly uses procedural logic to handle widget events.

## Data Files

- **`Game_Info.txt`** - Product inventory database
  - Format: `ID, Platform, Genre, Title, Publisher, Purchase Date`
- **`Rental.txt`** - Transaction and rental history log
  - Format: `Game ID, Rental Date, Return Date, Customer ID`
  - Uses `NULL` for the return date to indicate an active rental.
- **`Subscription_Info.txt`** - User account database
  - Stores registered customers and their current subscription tiers.

## Key Features

### For Store Managers
- **Advanced Search**: Instantly find games and check if they are available for rent.
- **Subscription Guard**: Automatically prevents rentals if a customer has reached their tier limit.
- **Feedback Loop**: Capture and store customer experience data during the return process.
- **Visual Analytics**: View bar charts of game performance to make informed inventory decisions.
- **Space Optimization**: Identify and "prune" unpopular games from the system.

## Design Principles

- **Modular Design** - Separation of concerns through distinct Python modules for search, rent, return, and analytics.
- **Procedural Logic** - Entirely function-based implementation with no Class type definitions.
- **Data Abstraction** - Centralized data handling in `database.py` to ensure consistent file formatting.
- **PEP 8 Compliance** - Indentation of 4 spaces and 80-character line limits for high readability.

## Technologies

- **Language**: Python 3.11
- **Visualization**: Matplotlib
- **GUI Framework**: IPyWidgets (within Jupyter)
- **Data Storage**: Text files (`.txt`)
- **Standard Libraries**: `datetime`, `sys`

## Project Structure

```text
\vgrs
├── Game_Info.txt             # Master inventory (min. 20 records)
├── Rental.txt                # Transaction history (min. 100 records)
├── Subscription_Info.txt     # Customer database
├── database.py               # File I/O utility functions
├── gameSearch.py             # Search logic
├── gameRent.py               # Rental logic
├── gameReturn.py             # Return & feedback logic
├── InventoryPruning.py       # Analytics & Matplotlib visualization
├── menu.ipynb                # Main GUI application
├── subscriptionManager.pyc   # External subscription module
└── feedbackManager.pyc       # External feedback module
```text
## Getting Started
1) Environment Setup: Ensure you have Python 3.11 installed.

Installation: Install the necessary visualization and GUI libraries:


pip install matplotlib ipywidgets
File Preparation: Ensure Game_Info.txt and Rental.txt are in the project root directory.

Launch: Open menu.ipynb in a Jupyter environment (VS Code or JupyterLab).

Operation: Run all cells to launch the GUI. Select a user and enter a 4-letter Customer ID and Game ID to process a transaction.

Future Enhancements
Database Integration: Migrate from text files to a relational database (SQLite/MySQL) for better concurrency.

User Authentication: Implement a secure login system for store managers.

Advanced Filtering: Add search functionality for publishers and purchase date ranges.

Automated Alerts: Generate notifications for games that have been rented for an excessive period.

Multi-Copy Support: Enhance logic to handle multiple physical copies of the same title more efficiently.
