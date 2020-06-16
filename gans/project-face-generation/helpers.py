import os
import requests
from tqdm import tqdm
from glob import glob
import zipfile

def download_dataset(dataset, base_url, folder_to_extract=None):
    '''
    will download a dataset from provided url to the folder to extract if set
    
    Parameters:
    -----------
    dataset: string, name of dataset along with extension
    base_url: string, url from where extracting information
    folder_to_extract: string, optional. If not set it will be build from the name of the dataset
    '''
    if not folder_to_extract:
        try:
            folder_to_extract, _ = os.path.splitext(dataset)
            print(folder_to_extract)
            os.mkdir(folder_to_extract)
        except FileExistsError:
            print("Directory {} already exist, so skipping creation".format(folder_to_extract))
    
    full_url = os.path.join(base_url, dataset)
    folder_extract = os.path.join(folder_to_extract,dataset)
    
    if not os.path.exists(folder_extract):
        print("Downloading: {} and saving to: {}".format(dataset, folder_to_extract))
    
        response = requests.get(full_url, stream=True)
        with tqdm.wrapattr(open(folder_extract, "wb"), "write", miniters=1,
                           total=int(response.headers.get('content-length', 0)),
                           desc=folder_extract) as fout:
            for chunk in response.iter_content(chunk_size=4096):
                fout.write(chunk)
    else:
        print("Dataset: {} already present in folder: {}".format(dataset, folder_to_extract))

def extract_dataset(dataset, extract_dir=None):
    ''' will extract the dataset on the fullpath 
      to the extract_dir defined if not then default to BASE_PATH
      Args:
        extract_dir (str): path to extract the zip file
        filename (str): zip filename
    '''
    
    if not extract_dir:
        extract_dir, _ = os.path.splitext(dataset)

    file_zip = os.path.join(extract_dir,dataset)
    print(file_zip)
    zip_ref = zipfile.ZipFile(file_zip, 'r')
    zip_ref.extractall("./")
    zip_ref.close()