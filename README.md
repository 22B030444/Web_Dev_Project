## Team members

| Student name          | Student ID      |
|-----------------------|-----------------|
| Suleimenova Zhasmin   | 22B030444       |
| Shapkat Ernur         | 22B030465       |
| Taubaev Azamat        | 22B030450       |

# Corporate Mail Application API Documentation

## Overview

This document provides an overview of the API endpoints and their functionalities for the Corporate Mail Application. The API is designed to facilitate communication between the front-end application and the back-end server.

## Authentication

- **Endpoint**: `/api/auth/login`
  - **Method**: POST
  - **Description**: Endpoint for user authentication. Requires providing username and password in the request body. Upon successful authentication, returns an authentication token.
  - **Parameters**:
    - `username` (string): User's username.
    - `password` (string): User's password.
  - **Response**:
    - `token` (string): Authentication token for accessing protected endpoints.

- **Endpoint**: `/api/auth/logout`
  - **Method**: POST
  - **Description**: Endpoint for user logout. Requires providing authentication token in the request headers. Logs the user out by invalidating the authentication token.

## Mail Management

- **Endpoint**: `/api/mails`
  - **Method**: GET
  - **Description**: Retrieve a list of mails for the authenticated user.
  - **Response**:
    - Array of mail objects containing mail details such as sender, recipient, subject, body, etc.

- **Endpoint**: `/api/mails/:id`
  - **Method**: GET
  - **Description**: Retrieve details of a specific mail by ID.
  - **Parameters**:
    - `id` (integer): ID of the mail to retrieve.
  - **Response**:
    - Mail object containing mail details.

- **Endpoint**: `/api/mails`
  - **Method**: POST
  - **Description**: Create a new mail.
  - **Request Body**:
    - `sender` (string): Email address of the sender.
    - `recipient` (string): Email address of the recipient.
    - `subject` (string): Subject of the mail.
    - `body` (string): Body/content of the mail.
  - **Response**:
    - Created mail object.

- **Endpoint**: `/api/mails/:id`
  - **Method**: DELETE
  - **Description**: Delete a mail by ID.
  - **Parameters**:
    - `id` (integer): ID of the mail to delete.
  - **Response**:
    - Success message indicating deletion.

## User Management

- **Endpoint**: `/api/users`
  - **Method**: GET
  - **Description**: Retrieve a list of users.
  - **Response**:
    - Array of user objects containing user details such as username, email, etc.

- **Endpoint**: `/api/users/:id`
  - **Method**: GET
  - **Description**: Retrieve details of a specific user by ID.
  - **Parameters**:
    - `id` (integer): ID of the user to retrieve.
  - **Response**:
    - User object containing user details.


