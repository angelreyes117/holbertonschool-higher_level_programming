Task 1: Consume Data from an API Using curl

Objective
Learn to use curl to interact with APIs, fetch data, inspect headers, and make POST requests.

Explanation
curl is a command-line tool for transferring data with URLs, ideal for testing APIs.

JSONPlaceholder is a public API for testing (e.g., https://jsonplaceholder.typicode.com/posts).

Steps
Install curl: Typically pre-installed on Linux/Mac; on Windows, use WSL or download it.

Check Version: curl --version confirms installation.

Fetch Data: curl https://jsonplaceholder.typicode.com/posts retrieves a JSON array of posts.

Fetch Headers: curl -I https://jsonplaceholder.typicode.com/posts shows only headers.

POST Request: curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts simulates creating a post.

Expected Output
Version: curl 7.68.0 (x86_64-pc-linux-gnu) ...

GET Posts: [{"userId": 1, "id": 1, "title": "sunt aut facere...", "body": "quia et..."}, ...]

Headers: HTTP/1.1 200 OK ... Content-Type: application/json; charset=utf-8 ...

POST Response: {"title": "foo", "body": "bar", "userId": 1, "id": 101}


