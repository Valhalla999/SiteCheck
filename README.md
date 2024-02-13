# SiteCheck
# Website Status Checker

A simple Python script to check the status of a website by sending an HTTP request and examining the response code.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library

Install the `requests` library using the following command:

```bash
pip install requests
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Valhalla999/website-status-checker.git
cd website-status-checker
```

2. Run the script:

```bash
python website_status_checker.py
```

3. Enter the website URL when prompted.

4. View the status of the website.

### Example

```bash
Enter the website URL: https://www.example.com
The website https://www.example.com is up and running.
Do you want to check another website? (y/n): y
Enter the website URL: https://www.anotherexample.com
The website https://www.anotherexample.com is down. Status code: 404
Do you want to check another website? (y/n): n
Goodbye!
```

## Contributing

If you have suggestions or find issues, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License.
``