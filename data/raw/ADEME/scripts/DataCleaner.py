import pandas as pd

class DataCleaner:
    def __init__(self):
        self.df = None
    
    def load_and_clean_csv(file_path: str) -> pd.DataFrame:
        """
        Load and clean the vehicle CO2 dataset CSV file.

        Parameters:
        - file_path (str): Path to the CSV file.

        Returns:
        - pd.DataFrame: Cleaned and ready-to-use DataFrame.
        """
        # Load with appropriate encoding and separator
        df = pd.read_csv(file_path, sep=';', encoding='latin1')

        # Strip and standardize column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Convert numeric fields (e.g. consommation, CO2, puissances) to float
        numeric_cols = [
            'puiss_admin_98', 'puiss_max', 'conso_urb', 'conso_exurb', 'conso_mixte', 'co2',
            'hc', 'nox', 'hcnox', 'ptcl', 'masse_ordma_min', 'masse_ordma_max'
        ]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')

        # Optionally parse 'date_maj' if it’s a proper date column
        if 'date_maj' in df.columns:
            df['date_maj'] = pd.to_datetime(df['date_maj'], errors='coerce')

        # Drop duplicates if necessary
        df.drop_duplicates(inplace=True)

        # Return cleaned DataFrame
        return df
    
    def load_and_clean_xls(file_path: str, sheet_name: int | str = 0) -> pd.DataFrame:
        """
        Load and clean the vehicle CO2 dataset from an XLS file.

        Parameters:
        - file_path (str): Path to the XLS file.
        - sheet_name (int | str): Sheet index or name (default is 0 - first sheet).

        Returns:
        - pd.DataFrame: Cleaned and ready-to-use DataFrame.
        """
        # Load Excel sheet
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Strip and standardize column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Convert numeric fields to float (if they exist)
        numeric_cols = [
            'puiss_admin_98', 'puiss_max', 'conso_urb', 'conso_exurb', 'conso_mixte', 'co2',
            'hc', 'nox', 'hcnox', 'ptcl', 'masse_ordma_min', 'masse_ordma_max'
        ]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')

        # Parse dates if applicable
        if 'date_maj' in df.columns:
            df['date_maj'] = pd.to_datetime(df['date_maj'], errors='coerce')

        # Drop duplicates
        df.drop_duplicates(inplace=True)

        return df
    
   