# SportEvent Scout - Tournament Calendar  

## Overview

SportEvent Scout is a Django-based application providing a up-to-date calendar of sports tournaments across multiple sports and levels. The backend exposes a REST API that serves tournament data, and a simple frontend UI displays and filters tournaments.


## Features

- Supports 13 sports: Cricket, Football, Badminton, Running, Gym, Cycling, Swimming, Kabaddi, Yoga, Basketball, Chess, Table Tennis
- Covers tournament levels: Corporate, School, College/University, Club/Academy, District, State, Zonal/Regional, National, International
- REST API endpoint `/api/tournaments/` with support for filtering by sport, level, and date range
- Lightweight UI mockup (HTML + JS) for searching and filtering tournaments
- Displays tournament name, dates, level, official URL, streaming link, and summary

## Tech Stack

- Backend: Python 3, Django 4.2, Django REST Framework, django-filter
- Frontend: Plain HTML, JavaScript (Fetch API)
- Database: SQLite (default Django DB)
- Optional: django-cors-headers for enabling cross-origin requests during development


## Setup and Run Instructions

1. **Clone the repository or extract the zipped folder**
2. **Create and activate virtual environment (optional but recommended):** python -m venv venv
3. **Apply migrations:**  python manage.py migrate
4. **Create a superuser to manage tournaments (optional):** using python manage.py createsuperuser and then follow the prompts.
5. **python manage.py runserver**   
6.  **Open the frontend UI:** Open the `index.html` file in a browser (double-click or right-click > Open with).
7. **Usage:**  Use the filters and search box to find and explore tournaments. The UI fetches data dynamically from the API running locally.

