# miRNA Targeting Tool

Interactive web application for exploring microRNA-gene targeting relationships and DNA sequence analysis.

## Getting Started

These instructions will help you deploy the web application locally.

### Prerequisites

Before running this application, you need:

* Python 3.8 or higher
* MySQL database server
* Access to miRNA targeting database
* Web browser (Chrome, Firefox, Safari)


## Usage

### Running the Application

```
$ export FLASK_APP=AJAX_and_charts.py
$ python AJAX_and_charts.py
```

Access the application at: http://localhost:5000

### Features

1. Target Score Visualization
   * Input: Gene name or miRNA identifier
   * Output: Interactive histogram of targeting scores

2. Gene Sequence Search
   * Input: DNA sequence (7-9 nucleotides, A/C/G/T only)
   * Output: Genes containing the sequence with genomic coordinates

### Example Queries

Target score histogram:
```
Input: BRCA1
Output: Distribution of 247 miRNAs targeting BRCA1
```

Sequence search:
```
Input: TATAAA
Output: 3,428 genes containing TATA box motif
```

## Deployment

### Local Development

```
$ export FLASK_ENV=development
$ python AJAX_and_charts.py
```

### Production Deployment

Using Gunicorn:
```
$ gunicorn -w 4 -b 0.0.0.0:8000 AJAX_and_charts:app
```

Using Apache with mod_wsgi:
* Configure virtual host
* Set up WSGI configuration
* Point to application directory

## Database Schema

Required tables:
* miRNA: miRNA identifiers
* gene: Gene sequences and coordinates
* targets: miRNA-gene targeting scores

## Technical Details

* Backend: Flask (Python)
* Frontend: HTML, JavaScript, jQuery
* Database: MySQL
* Visualization: Google Charts API
* Communication: AJAX asynchronous requests

## Additional Information

* Course: BF768 Biological Database Analysis
* Institution: Boston University
* Application type: Full-stack web application



<img width="1088" height="457" alt="Screenshot 2025-12-11 at 17 34 24" src="https://github.com/user-attachments/assets/2f37557c-404e-4ee7-b27b-7b57d4223ab1" />
