import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


# Define pipeline options
class DataPipelineOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        super(DataPipelineOptions, cls)._add_argparse_args(parser)
        parser.add_argument('--input_file', default='../data/raw/healthcare_dataset.csv', help='Path to the input file (in GCS)')
        parser.add_argument('--output_file', default='../data/processed/healthcare_dataset.csv', help='Path to the output file (in GCS)')


# Data Processing Function
def process_data(record):
    # Example transformation: Clean the data (e.g., removing empty rows)
    try:
        if record:
            return record.strip() # Add custom transformation logic
        return None
    except Exception as e:
        print(f"Error processing record: {e}")
        return None

def run(argv=None):
    # Set pipeline options
    # for local running
    options = PipelineOptions(
        flags=argv, runner='DirectRunner', # Specify DirectRunner for local execution
        streaming=False # Set to True if you're doing streaming
    )
    pipeline_options = options.view_as(DataPipelineOptions)

    with beam.Pipeline(options=pipeline_options) as p:
        # Read data from the raw GCS bucket (input file path)
        input_data = p | 'ReadInputData' >> beam.io.ReadFromText(pipeline_options.input_file)

        # Apply transformation
        transformed_data = (input_data 
          | 'ProcessData' >> beam.Map(process_data)
          | 'FilterNone' >> beam.Filter(lambda x: x is not None)
        )

        # Write transformed data to processed folder in GCS
        transformed_data | 'WriteData' >> beam.io.WriteToText(
            pipeline_options.output_file,
            shard_name_template='', # No sharding and prevents sharding for local testing
        )

if __name__ == '__main__':
    run()
