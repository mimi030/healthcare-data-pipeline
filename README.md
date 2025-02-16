# Healthcare Data Pipeline

A demonstration project showcasing ETL (Extract, Transform, Load) concepts using Apache Beam for healthcare data processing.

## Project Overview

This project demonstrates data pipeline development skills using Apache Beam, focusing on healthcare data processing. The pipeline implements common ETL operations and data transformation patterns that are typical in healthcare data processing scenarios.

## Features

- Apache Beam pipeline implementation
- Healthcare data processing and transformation
- Scalable ETL operations
- Data validation and cleaning
- Future integration with GCP Dataflow


## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd healthcare-data-pipeline-gcp

```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

3. Install required packages:
```bash
pip install -r test_beam_pipeline/requirements.txt

```

## Running the Pipeline
To run the pipeline locally:
```bash
python test_beam_pipeline/pipeline.py

```

## Future Enhancements

This project is currently in development. Future updates will include:
- Integration with Google Cloud Dataflow for scalable execution
- Additional data transformation features
- Enhanced error handling and logging
- Monitoring and alerting implementation

## Technical Stack

- Apache Beam
- Python
- (Future) Google Cloud Platform
- Cloud Storage
- Dataflow

## Technical Stack

This project is licensed under the MIT License - see the LICENSE file for details.
