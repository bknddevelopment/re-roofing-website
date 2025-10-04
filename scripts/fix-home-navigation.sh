#!/bin/bash

# Fix home navigation links across all pages
# Changes relative "index.html" to absolute "/index.html"

echo "Fixing home navigation links..."

# Find all HTML files in pages directory and fix the home link
find pages -name "*.html" -type f | while read file; do
    # Replace href="index.html" with href="/index.html"
    sed -i '' 's|href="index\.html"|href="/index.html"|g' "$file"
done

echo "✅ Fixed home navigation links in $(find pages -name "*.html" -type f | wc -l) files"

# Verify the fix
echo ""
echo "Verification:"
echo "Files still with relative links: $(grep -r 'href="index\.html"' pages/ --include="*.html" | wc -l)"
echo "Files with correct absolute links: $(grep -r 'href="/index\.html"' pages/ --include="*.html" | wc -l)"
