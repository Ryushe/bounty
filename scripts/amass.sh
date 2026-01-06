num=0
# Read the file 'urls.txt' line by line
while IFS= read -r domain; do
  # Check if the line is not empty
  if [[ -n "$domain" ]]; then
    # Run 'amass' for subdomain enumeration and append the output to the file
    echo "running amass on $domain"
    amass enum -d "$domain" -active -brute >> all_subdomains.txt 2>&1
    # Check if the 'amass' command was successful
    if [[ $? -ne 0 ]]; then
      echo "Error enumerating subdomains for $domain"
    fi
  else
    echo "Skipping empty line in urls.txt"
  fi
done < urls.txt  # Read from 'urls.txt'
