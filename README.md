# Group-13

## CampusEats

CampusEats revolutionizes how students dine near USYD. With seamless integration of Google API, we provide tailored food recommendations at your fingertips. Say goodbye to indecision and hello to culinary bliss with CampusEats!

## Table of Contents
1. [Getting Started](#2)
2. [Installation](#3)
3. [Running the App](#4)
4. [Features](#5)
5. [Directory Structure](#6)
6. [Contributors](#7)

## <a id="2">Getting Started</a>
### Prerequisites

    Before you begin, ensure you have met the following requirements:

    [Python 3.x]

## <a id="3">Installation</a>
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/CampusEats.git

    ```

2. Navigate to the project directory:
    ```python
    cd CampusEats
    ```

3. Set up a virtual environment (recommended):
    ```python
    python -m venv venv
    ```

4. Activate the virtual environment:

    ```python
        On Windows (Command Prompt):
        venv\Scripts\activate
        On macOS and Linux:
        source venv/bin/activate
    ```

5. Install project dependencies:
    ```python
    pip install -r requirements.txt
    Installation
    ```
## <a id="4">Running the App</a>
Run the following commands in steps:

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata apps/restaurants/fixtures/restaurants.json
python manage.py loaddata apps/review/fixtures/reactions_fixture.json
python manage.py runserver
```

## <a id="5">Features</a>

1. Browse Restaurants: Easily explore nearby restaurants within the vicinity of USYD campus.
2. Admin Features: Effortlessly add new restaurants to the app's database to keep information up-to-date.
3. Review System: Post and view reviews from fellow students to make informed dining decisions.
4. Commenting: Engage with the community by adding comments to existing reviews, sharing insights, and asking questions.
5. Reaction System: React to reviews and comments using emojis to express sentiments.
6. Profile Management: User-friendly profiles for both administrators and regular users to manage personal information and preferences.

## <a id="6">Directory Structure</a>
```
CampusEats/
├── campus_eats/
├── apps/
│   ├── user/
│   ├── restaurants/
    |...
├── templates/
├── static/
├── media/
├── requirements.txt
├── manage.py
```


- campus_eats/: Contains the core Django project configuration and settings.

- apps/: Houses individual Django applications (e.g., "user" and "restaurants") that encapsulate specific features and functionality of the project.

- templates/: Stores HTML template files used for rendering dynamic web pages.

- static/: Holds static files (e.g., CSS, JavaScript, images) used by the project's web pages.

- media/: Reserved for user-uploaded media files (e.g., user avatars, restaurant images) separate from static assets.

- requirements.txt: Lists project dependencies and their versions, enabling easy installation and replication of the development environment.

- manage.py: A Django management script that facilitates various project-related tasks, including running the development server, managing database migrations, and more.

## <a id="7">Contributors</a>
1. Tisha Jhabak
2. Vivian Ha
3. Olivia Smith
4. Amanda
5. Roy



