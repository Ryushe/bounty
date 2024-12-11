while IFS= read -r url; do
    zap-cli context add $url --context program_scope
done < "urls.txt"
