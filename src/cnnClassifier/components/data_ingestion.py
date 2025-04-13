import os
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Skip download step — assume ZIP already exists locally.
        """
        zip_download_dir = self.config.local_data_file
        if os.path.exists(zip_download_dir):
            logger.info(f"[INFO] Found local dataset at {zip_download_dir}, skipping download.")
        else:
            raise FileNotFoundError(f"[ERROR] Dataset not found at {zip_download_dir}. Please place it manually.")

    def extract_zip_file(self):
        """
        Extract the existing local ZIP file.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"[INFO] Extracted dataset to {unzip_path}")
