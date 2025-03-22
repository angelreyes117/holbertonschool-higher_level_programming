Task 0: Basics of HTTP/HTTPS

Objective
Understand the foundational principles of HTTP and HTTPS, including data transfer, methods, status codes, and the differences between secure and non-secure versions.

Explanation
HTTP (Hypertext Transfer Protocol) is the protocol used for transferring data over the web. It operates in a request-response model where a client (e.g., a browser) sends a request to a server, which responds with the requested data.

HTTPS (HTTP Secure) is HTTP with an added layer of security using SSL/TLS encryption, ensuring data is encrypted during transit, protecting it from eavesdropping and tampering.

Differences Between HTTP and HTTPS
Security: HTTP transmits data in plain text, making it vulnerable to interception. HTTPS encrypts data, ensuring confidentiality and integrity.

Port: HTTP uses port 80 by default, while HTTPS uses port 443.

Use Case: HTTP is suitable for non-sensitive data (e.g., public web pages), whereas HTTPS is essential for sensitive data (e.g., login credentials, financial transactions).

Structure of an HTTP Request and Response
Request:
Method: Specifies the action (e.g., GET, POST).

Path: The resource URL (e.g., /posts).

Headers: Metadata (e.g., Content-Type: application/json).

Body: Data sent to the server (optional, used in POST/PUT).

Response:
Status Code: Indicates the result (e.g., 200 OK).

Headers: Metadata (e.g., Content-Length).

Body: Data returned (e.g., HTML, JSON).

Common HTTP Methods
GET: Retrieves data from the server.
Use Case: Fetching a webpage or API data (e.g., list of posts).

POST: Sends data to the server to create a resource.
Use Case: Submitting a form or creating a new post.

PUT: Updates an existing resource on the server.
Use Case: Editing a user profile.

DELETE: Removes a resource from the server.
Use Case: Deleting a post.

Common HTTP Status Codes
200 OK: Request succeeded.
Scenario: Successfully retrieved a webpage.

201 Created: Resource successfully created.
Scenario: A new post was added via POST.

400 Bad Request: Invalid request syntax or parameters.
Scenario: Missing required fields in a form submission.

404 Not Found: Resource not available.
Scenario: Requesting a non-existent page.

500 Internal Server Error: Server encountered an unexpected issue.
Scenario: Database connection failure during a request.

Expected Output
HTTP vs. HTTPS Summary: HTTP is an unencrypted protocol for web data transfer, while HTTPS adds SSL/TLS encryption for security, used in sensitive applications.

HTTP Structure: Requests include method, path, headers, and optional body; responses include status code, headers, and body.

Methods and Status Codes: As listed above.


