import pandas as pd
from typing import List, Dict

class DataHandler:
    @staticmethod
    def read_input(file_path: str) -> pd.DataFrame:
        """
        Read the input data from CSV file.
        """
        return pd.read_csv(file_path)
    
    @staticmethod
    def save_submission(results: List[Dict], output_path: str):
        """
        Save results to submission file.
        """
        submission_df = pd.DataFrame(results)
        submission_df.to_csv(output_path, index=False)
        print(f"Submission saved to {output_path}")