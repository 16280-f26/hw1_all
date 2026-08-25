import argparse
import cowsay
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_text", type=str, required=True, help="Path to the .txt file")

    args = parser.parse_args()
    input_path = args.input_text

    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' does not exist.")
        sys.exit(1)

    if not input_path.lower().endswith(".txt"):
        print("Error: Input file must have a .txt extension.")
        sys.exit(1)

    with open(input_path, "r") as f:
        content = f.read().strip()

    if not content:
        print("Warning: Input file is empty.")
        sys.exit(1)

    cowsay.cow(content)

if __name__ == "__main__":
    main()
