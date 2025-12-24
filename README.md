# Scientist Biography Extractor 🧪📚

A command-line Python tool that extracts **scientist biographies from Wikipedia** using **BeautifulSoup** and **argparse**.  
The script fetches the scientist’s introduction and infobox details and saves them into a structured text file.

---

## 📌 Features
- CLI-based tool using `argparse`
- Scrapes Wikipedia biographies
- Extracts:
  - Scientist name
  - Introductory biography paragraphs
  - Infobox details (Born, Fields, Known for, etc.)
- Handles Wikipedia anti-scraping (403) using mobile site
- Clean, readable, and beginner-friendly code
- Saves output to a text file

---

## 📂 Project Structure

ScientistBiographyExtractor/  
│
├── scientist_biography_extractor.py   
├── output/  
│ └── [scientist_name].txt  
├── README.md


---

## ⚙️ Requirements
- Python 3.8+
- Internet connection

### Python Libraries
```bash
pip install requests beautifulsoup4 lxml
```
---

## ▶️ How It Works

   - Takes scientist name as a command-line argument

   - Builds the corresponding Wikipedia URL

   - Fetches the page using browser-like headers

   - Parses HTML using BeautifulSoup

   - Extracts biography text and infobox details

   - Saves the data in a .txt file

---

## 🚀 Usage

### Example Command

python3 scientist_biography_extractor.py "Albert Einstein" --output einstein

### Output Location

output/einstein.txt

