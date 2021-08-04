#! usr/bin/env python3
import xmltodict
import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("xml_path", type=str, help="path to xml file")
parser.add_argument(
    "csv_folder_path",
    type=str,
    nargs="?",
    help="path to folder where csv should be stored, default is current dir",
)

args = parser.parse_args()

if args.csv_folder_path:
    csv_path = os.path.join(args.csv_folder_path, "xml_export.csv")
else:
    csv_path = "xml_export.csv"


with open(args.xml_path, "rb") as f:
    xml_dict = xmltodict.parse(f)


def flatten(d: dict):
    """recursive func to flatten a dict with nested dicts and lists"""

    def get_items(d: dict, key_prefix=False):
        for key, val in d.items():
            if isinstance(val, dict):
                if key_prefix:
                    key = key_prefix + "." + key
                get_items(val, key)
            elif isinstance(val, list):
                for i, el in enumerate(val):
                    if key_prefix:
                        key = key_prefix + "." + key
                    get_items(el, key + str(i))
            else:
                if key_prefix:
                    key = key_prefix + "." + key
                flattened_dict[key] = val

    flattened_dict = {}
    get_items(d)

    return flattened_dict


def main():
    statements = []

    # level required for each row - i.e. each row is everything between <Statement></Statement>
    parsed_statements = xml_dict["Billing_Statements"]["Statement"]

    if isinstance(parsed_statements, dict):
        # when there's only one statement in xml
        statements = [flatten(parsed_statements)]
    else:
        for statement in parsed_statements:
            statements.append(flatten(statement))

    df = pd.DataFrame(statements)
    df.to_csv(csv_path, index=False)


if __name__ == "__main__":
    main()
