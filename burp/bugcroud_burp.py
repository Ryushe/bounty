import json
import re
import argparse

from pathlib import Path

def parse_entry(entry):
    host = entry.replace('.', '\\.').replace('*', '.*')
    return [
        {"host": f"^{host}$", "protocol": "http", "port": f"^{80}$"},
        {"host": f"^{host}$", "protocol": "https", "port": f"^{443}$"}
        ]

def build_json(domains):
    scope_entries = []
    for domain in domains:
        print(f"domain: {domain}")
        entries = parse_entry(domain)
        for entry in entries:
            # print(f"entry: {entry}")
            scope_entries.append({
                "enabled": True,
                "file": "^/.*",
                **entry
            })

    burp_json = {
        "target": {
            "scope": {
                "advanced_mode": True,
                "include": scope_entries,
                "exclude": [] # eventually exclude as well
            }
        }
    }
    return burp_json

def write_json(json_txt):
    output_file = "burp_scope.json"
    with open(output_file, "w") as f:
        json.dump(json_txt, f, indent=4)

def write_plain(txt):
    try:
        with open("burp_urls.txt", "w") as file:
            for line in txt:
                file.write(line + "\n") 
    except Exception as e:
        print(f"error: {e}")

def add_http(domain):
    return f"http://{domain}"

def add_https(domain):
    return f"https://{domain}"

def main():
    output_file = "burp_urls.txt"
    parser = argparse.ArgumentParser(description="Process a file.")

    parser.add_argument("file", nargs="?", default="urls.txt", help="Path to the input file")
    parser.add_argument("-c", "--config", action="store_true", help="Generate Burp Config")
    args = parser.parse_args()
    domain_list = []

    try:
        file_path = Path(args.file)
    except FileNotFoundError as e:
        print(f"{e}")
        exit()
    
    print(f"Processing file: {file_path}")
    with open(file_path, "r") as file:
        domains = file.read().splitlines()
    if not domains:
        exit()
    if args.config:
        print("Creating a burp config")
        burp_json = build_json(domains)
        write_json(burp_json)
        exit()
    print("Creating a url list to import")

    for domain in domains:
        domain_list.append(add_http(domain))
        domain_list.append(add_https(domain))
    
    write_plain(domain_list)

    print(f"Burp Suite scope saved to {output_file}")

if __name__ == "__main__":
    main()

