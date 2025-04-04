# CSV to Moodle XML Converter

This project is a Python-based generator that transforms a CSV file into an XML format compatible with Moodle. It simplifies the process of importing structured data into Moodle, ensuring seamless integration.

## Features
- Converts CSV files into Moodle-compatible XML
- Supports multiple question formats (Right now: "multichoice" and "truefalse")
- Easy-to-use command-line interface
- Open-source and customizable

## Installation
### Prerequisites
Ensure you have Python installed (version 3.x recommended). You can check your Python version with:

```sh
python --version
```

### Clone the Repository
Clone this repository to your local machine:

```sh
git clone https://github.com/NoNameiqz/pygentoxml
cd pygentoxml
```

## Usage
### Running the Converter
Execute the script with:

```sh
python pygentoxml.py
```
*Chnage the csv directory in the python file*

- `input.csv`: The CSV file containing the structured data.
- `quiz.xml`: The resulting Moodle-compatible XML file.

### Example CSV Format
Ensure your CSV file follows a structured format, e.g.:

```csv
Dificulty,Question Type,Question Name,Question Text,answer,values
Easy,multichoice,Question1,What is the name of our planet?,green planet;blue planet;planet mars;planet earth,0;0;0;100
```

## Contributing
Feel free to fork this repository and submit pull requests. If you find any issues, please report them via the Issues tab.

## Contact
For questions or suggestions, open an issue or reach out at goncomelozero12@gmail.com.

