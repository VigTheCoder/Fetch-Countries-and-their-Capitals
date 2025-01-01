# Fetch Countries Names and Abbreviations

This is a Python script that fetches and displays information about countries from the REST Countries API. It retrieves the list of all countries, displaying their common names and abbreviations.

## Features

- Sends an HTTP GET request to the REST Countries API.
- Parses the JSON response to extract country names and their two-letter abbreviations (CCA2).
- Handles errors such as failed requests or connectivity issues gracefully.

## Requirements

- Python 3.6 or later
- `requests` library

## Run the script

```bash
python fetch_usa_states.py
```
 
## Output will display a list of countries with their common names and abbreviations:
```bash
Country Name: Afghanistan
Abbreviation: AF
Country Name: Albania
Abbreviation: AL
Country Name: Algeria
Abbreviation: DZ
Country Name: Andorra
Abbreviation: AD

