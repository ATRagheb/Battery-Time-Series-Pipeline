# Battery Time Series Pipeline

This application processes battery time series data, performs data preprocessing, and calculates hourly aggregations.

## Running Locally

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Setup

1. Create a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

## Dockerized Application

### Prerequisites

- Docker

### Running with Docker

1. Build the Docker image:

```bash
docker build -t battery-pipeline .
```

2. Run the container:

```bash
docker run -v "$(pwd)"/data:/app/data -v "$(pwd)"/outputs/output.csv:/app/outputs/output.csv battery-pipeline
```


### Output

The application will process the data and generate an `output.csv` file with the hourly aggregations.