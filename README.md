# My Simple Website

This is a simple website that allows users to explore different topics, leave comments, and interact with the site.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Home Page: The main page of the website with a description of the site.
- Topics Page: A page listing different topics for users to explore.
- Topic Page: Displays a specific topic with a list of comments. Users can add their comments.
- User Authentication: Users can register, log in, and log out.
- Header: A common header section on each page with links to the home page, login/logout, registration, and topics page.
- Comments: Users can leave comments on each topic.
- Comment Management: Users can edit and delete their own comments.
- Topic Management: Users can create new topics and edit/delete their own topics.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Surfer-liner/my-simple-website.git

2. Install the required dependencies:

    ```bash
   pip install -r requirements.txt

3. Set up the database:

    ```bash
   python manage.py migrate

## Usage

1. Start the development server:

    ```bash
   python manage.py runserver

2. Access the website in your browser at:

    ```bash
    http://localhost:8000

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

## License

Massachusetts Institute of Technology License

Copyright (c) 2023 Surfer_Liner

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
2. A reference to the original repository or project page must be provided when using the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
