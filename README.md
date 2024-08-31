# Software Architecture Assignments

**This is a work in progress for [Assignment 3](#assignment-3)**

# Book Review Web Application

This project is part of the Software Architecture course at Universidad de los Andes, under the guidance of Professor José Luis Assadi. The aim of this assignment is to develop a basic book review web application.

## Project Overview

The Book Review Web Application is designed to manage and display information related to books, authors, reviews, and sales. The application meets the following requirements:

- **Authors Management**: Allows the creation, updating, deletion, and viewing of authors, including their name, date of birth, country of origin, and a brief description.
- **Books Management**: Supports the management of books, including their name, summary, publication date, and sales data.
- **Reviews Management**: Enables users to submit reviews for books, including a score (from 1 to 5), review content, and the number of up-votes received.
- **Sales Management**: Tracks book sales by year, including the total sales figures.

## Application Features

The application provides the following views and functionalities:

- **CRUD Operations**: Full Create, Read, Update, and Delete operations for authors, books, reviews, sales.
- **Author Statistics Table**: A sortable and filterable table displaying authors, the number of books published, average review scores, and total sales.
- **Top Rated Books Table**: A table showing the top 10 highest-rated books of all time, along with their most popular highest and lowest-rated reviews.
- **Top Selling Books Table**: A table listing the top 50 best-selling books of all time, including total sales for each book, total sales for the author, and information on whether the book was among the top 5 best-selling books in the year of its publication.
- **Search Functionality**: A search window that allows users to input text and receive a paginated list of books whose descriptions contain any of the entered words.

---

## How to Run the Project

1. **Navigate to the Assignment1 directory**:
   ```bash
   cd Assignment1
   ```

2. **Start the Docker containers**:
   ```bash
   docker compose up
   ```

3. **Access the web application**: Open your browser and go to [http://localhost:8000](http://localhost:8000) to view the Bookstore app.

---

## Assignment 3
### **WIP**

For this assignment we will use:

- [Redis](https://redis.io/) for our database cache.
- Some search aplication TBD
- [HAProxy](https://www.haproxy.org/) for our Reverse Proxy

### We have to set up the following:
You must implement multiple docker compose files that account for
the following deployments:
- Application + Database
- Application + Database + Cache
- Application + Database + Search Engine
- Application + Database + Reverse Proxy
- Application + Database + Reverse Proxy + Cache + Search Engine
