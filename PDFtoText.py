import os, io
import re
from google.cloud import vision
from google.cloud import storage
from google.protobuf import json_format
mime_type = 'application/pdf'


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r’<LOCATION_PATH_WHERE_GOOGLE_CREDENTIALS_STORED_LOCALLY>'
client = vision.ImageAnnotatorClient()

batch_size = 1 # One page scan

feature = vision.types.Feature(
    type=vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION)

gcs_source_uri = 'gs://<storage_name>/<output_file_name>'     #Place the PDF/TIFF file in Google storage bucket and provide the location here.
gcs_source = vision.types.GcsSource(uri=gcs_source_uri).     
input_config = vision.types.InputConfig(gcs_source=gcs_source, mime_type=mime_type)

gcs_destination_uri = 'gs://<storage_name>/<output_file_name> '    # Provide the Output file name to store the results.
gcs_destination = vision.types.GcsDestination(uri=gcs_destination_uri)
output_config = vision.types.OutputConfig(gcs_destination=gcs_destination, batch_size=batch_size)

async_request = vision.types.AsyncAnnotateFileRequest(
    features=[feature], input_config=input_config, output_config=output_config)

operation = client.async_batch_annotate_files(requests=[async_request])
print('Waiting for the operation to finish')
operation.result(timeout=180)

storage_client = storage.Client()
match = re.match(r'gs://([^/]+)/(.+)', gcs_destination_uri)
bucket_name = match.group(1)
prefix = match.group(2)

bucket = storage_client.get_bucket(bucket_name)

blob_list = list(bucket.list_blobs(prefix=prefix))
print('Output file : ')
for blob in blob_list:
    print(blob.name)

output = blob_list[0]

json_string = output.download_as_string()
response = json_format.Parse(
    json_string, vision.types.AnnotateFileResponse())

first_page_response = response.responses[0]
annotation = first_page_response.full_text_annotation

print(u'Full Text:\n{}'.format(annotation.text))
