echo "enter the path of the wild card file:"
read -e wildcard_file
# Read the file 'urls.txt' line by line
while IFS= read -r wildcardurl; do
  # Check if the line is not empty
  if [[ -n "$wildcardurl" ]]; then
    # Run 'amass' for subwildcardurl enumeration and append the output to the file
    echo "running crt on $wildcardurl"
    curl -s "https://crt.sh/?q=:${wildcardurl#*.}&output=json" | jq -r '.[].name_value' | grep -Po '(\w+\.\w+\.\w+)$' | anew all_urls.txt

    # Check if the 'amass' command was successful
    if [[ $? -ne 0 ]]; then
      echo "Error enumerating subwildcardurls for $wildcardurl"
    fi
  else
    echo "Skipping empty line in all_urls.txt"
  fi
done < $wildcard_file
