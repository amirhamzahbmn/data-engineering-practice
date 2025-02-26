from pathlib import Path
import pandas as pd
import json

def main():
    for path in Path('./data').rglob('*.json'):

        filename = path.name.split('.')[0]

        with open(path, 'r') as f:
            data = json.load(f)

        df = pd.json_normalize(data)
        df.to_csv(f'{str(path).rstrip('.json')}.csv', index=False)
        print(f'converted {filename} to .csv in {path}')


if __name__ == "__main__":
    main()
