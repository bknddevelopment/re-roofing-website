#!/bin/bash

# Script to update all internal HTML links after reorganization
# Run from project root

echo "Updating paths in all HTML files..."

# Function to update paths in a file
update_file() {
    local file="$1"

    # Update core page links (from any location)
    sed -i '' \
        -e 's|href="about\.html"|href="/pages/core/about.html"|g' \
        -e 's|href="services\.html"|href="/pages/core/services.html"|g' \
        -e 's|href="calculator\.html"|href="/pages/core/calculator.html"|g' \
        -e 's|href="faq\.html"|href="/pages/core/faq.html"|g' \
        -e 's|href="quote\.html"|href="/pages/core/quote.html"|g' \
        -e 's|href="reviews\.html"|href="/pages/core/reviews.html"|g' \
        -e 's|href="blog\.html"|href="/pages/core/blog.html"|g' \
        -e 's|href="privacy-policy\.html"|href="/pages/core/privacy-policy.html"|g' \
        -e 's|href="terms-of-service\.html"|href="/pages/core/terms-of-service.html"|g' \
        "$file"

    # Update town landing pages (roofing-{town}-nj.html)
    sed -i '' \
        -e 's|href="roofing-\([a-z-]*\)-nj\.html"|href="/pages/towns/roofing-\1-nj.html"|g' \
        "$file"

    # Update service×location pages (pattern: {service}-{town}-nj.html)
    # This regex captures any word-dash-word-nj.html that's not "roofing-"
    sed -i '' \
        -e 's|href="\([a-z-]*-[a-z-]*-[a-z-]*-nj\)\.html"|href="/pages/services/\1.html"|g' \
        "$file"

    # Fix any double /pages/ that might have been created
    sed -i '' \
        -e 's|/pages/pages/|/pages/|g' \
        "$file"

    # Update index.html references to stay as root
    sed -i '' \
        -e 's|href="/pages/core/index\.html"|href="/index.html"|g' \
        -e 's|href="/pages/services/index\.html"|href="/index.html"|g' \
        -e 's|href="/pages/towns/index\.html"|href="/index.html"|g' \
        "$file"
}

# Update index.html in root
if [ -f "index.html" ]; then
    echo "Updating index.html..."
    update_file "index.html"
fi

# Update all pages in pages/core/
for file in pages/core/*.html; do
    if [ -f "$file" ]; then
        echo "Updating $file..."
        update_file "$file"
    fi
done

# Update all pages in pages/towns/
for file in pages/towns/*.html; do
    if [ -f "$file" ]; then
        echo "Updating $file..."
        update_file "$file"
    fi
done

# Update all pages in pages/services/
for file in pages/services/*.html; do
    if [ -f "$file" ]; then
        echo "Updating $file..."
        update_file "$file"
    fi
done

echo "Path updates complete!"
echo ""
echo "Next steps:"
echo "1. Update sitemap.xml with new paths"
echo "2. Test site locally"
echo "3. Verify all links work"
