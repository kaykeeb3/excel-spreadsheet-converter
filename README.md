# Excel Spreadsheet Converter

This project is a web application developed to convert **JSON** data into **Excel** spreadsheets automatically. Using **Flask** for the backend and **HTML**, **JavaScript**, and **TailwindCSS** for the frontend, the tool provides a simple and intuitive experience for data conversion, saving time and minimizing errors when generating Excel reports.

## Features

- **Report Generation**: Converts user-provided JSON data into custom Excel reports.
- **Automation**: Simplifies report creation from structured data, ensuring speed and accuracy in the process.
- **Intuitive and Responsive Interface**: Developed with modern technologies to ensure an optimized user experience on any device.

## Technologies Used

- **Backend**: Flask (Python framework for APIs)
- **Frontend**: HTML, TailwindCSS, JavaScript
- **Data Manipulation**: Pandas (for data processing)
- **Excel Generation**: Openpyxl (for creating and manipulating Excel files)

## Prerequisites

Before starting, you need to have the following prerequisites installed:

- **Python 3.x**
- **Pip** (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kaykeeb3/excel-spreadsheet-converter.git
   cd excel-spreadsheet-converter
   ```

2. Create and activate a virtual environment:

   For Linux/macOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   For Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. Open your browser and go to `http://localhost:5000` to use the application.

## Usage

1. Paste the **JSON** data into the provided field on the interface.
2. Click the **"Generate Report"** button.
3. The Excel file will be automatically generated and downloaded to your device.

### Example JSON Data

Here is an example of how the JSON data should be structured to generate a report:

```json
[
  {
    "ID": 1,
    "Customer Name": "Alice",
    "Customer who called on WhatsApp": "João",
    "Company Name": "Company A",
    "Customer Query": "Product X",
    "Call Time": "10:00",
    "Average Response Time": "15 minutes",
    "Date": "2024-05-20",
    "Day: .. Service of the Day": "Monday"
  },
  {
    "ID": 2,
    "Customer Name": "Bob",
    "Customer who called on WhatsApp": "Maria",
    "Company Name": "Company B",
    "Customer Query": "Service Y",
    "Call Time": "11:30",
    "Average Response Time": "20 minutes",
    "Date": "2024-05-20",
    "Day: .. Service of the Day": "Monday"
  },
  {
    "ID": 3,
    "Customer Name": "Charlie",
    "Customer who called on WhatsApp": "Pedro",
    "Company Name": "Company C",
    "Customer Query": "Product Z",
    "Call Time": "14:45",
    "Average Response Time": "10 minutes",
    "Date": "2024-05-21",
    "Day: .. Service of the Day": "Tuesday"
  }
]
```

## Future Improvements

- **Support for More Formats**: Implement support for importing and exporting other data formats (CSV, XML, etc.).
- **User Authentication**: Implement user authentication and authorization to control access to reports.
- **Data Analysis**: Add features for data analysis and visualization with charts and dynamic reports.

## Contributing

Contributions are always welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Added a new feature'`).
4. Push your branch to the remote repository (`git push origin feature/new-feature`).
5. Open a **Pull Request** with a clear description of the changes made.
