# GoogleVisionAPI
Google Vision API to detect text in files(PDF/TIFF)
PRE-REQUISITES:
1. Installation of below packages:
  Python version 3.8.3
  Pip version 20.1.1
 2. Install below python modules using 
    -- import re <-- Regular Expression Module
    -- import vision <-- Google Cloud Vision API module
    -- import storage <-- Storage Module
    -- import json or json_format <-- Json Module
  3. Create Google storage bucket and place the PDF document in the bucket.
  4. Create Service Account for the Buckets and store the credentials locally from where the script will be executed.
  
  BEFORE SCRIPT EXECUTION:
  1. Provide the PATH of GOOGLE ACCOUNT CREDENTIALS in the script PDFtoText.py.
  2. Get the URI details of the PDF object file and update the PDFtoText.py script with URI for Source.
      example, gs://PDF_Input/Invoice_Receipt.pdf
  3. The output of the script execution can be placed in the same storage bucket or can create seperate output bucket.
      example, gs://TXT_Output/Invoice_Receipt.txt
      
  EXECUTION:
  1. Setup pyhon virtual environment (penv) and execute the script 
                          or
     Go into the terminal and execute the script
        python3 PDFtoText.py
        
  RESULTS:
  1. Check the Output file in Google Output path provided.
 
