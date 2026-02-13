# Python Automation Toolkit

This repository contains a collection of powerful, reusable Python scripts designed to automate repetitive tasks and simplify development workflows.

## Features

- **Web Scraper**: A robust web scraper with proxy support, retry logic, and clean data extraction.
- **PDF to Word**: Convert PDF documents into editable Word (.docx) files.
- **More to come...**

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/PETER/Python-Automation-Toolkit.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Web Scraper
```python
from web_scraper import WebScraper
scraper = WebScraper()
content = scraper.fetch("https://example.com")
```

### PDF to Word
```bash
python pdf_to_word.py input.pdf -o output.docx
```

## Contributing

Pull requests are welcome!

## License

MIT License
