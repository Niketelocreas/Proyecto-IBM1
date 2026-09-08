# Python Customer Management System

A small command-line customer management application built in Python using object-oriented programming.

## Project objective

The project implements a simple in-memory system for managing basic customer records through an interactive terminal menu.

Each customer record stores:

- Name
- Email address
- Phone number

## Features

The application supports:

- Adding customers
- Searching for a customer by name
- Deleting customers
- Listing all stored customers
- Interactive command-line navigation

## Object-oriented design

The application is organised around two main classes.

### `Cliente`

Represents an individual customer and stores their contact information.

### `SistemaClientes`

Manages the collection of customer objects and provides the operations required to add, search, remove and list records.

The `main()` function exposes these operations through an interactive command-line menu.

## Running the project

Requirements:

- Python 3.x
- No external Python packages

Run:

```bash
python gestion_clientes.py
```

## Repository contents

- `gestion_clientes.py` — main application
- `Practicas/` — supporting exercises
- Project documentation files

## Limitations

Customer data is stored only in memory and is lost when the program exits.

The project is therefore best understood as a compact demonstration of Python fundamentals and object-oriented application structure rather than a production customer-management system.

## Background

This project was originally developed as part of an IBM Python learning project.

## Project type

**Python · Object-Oriented Programming · CLI Application**
