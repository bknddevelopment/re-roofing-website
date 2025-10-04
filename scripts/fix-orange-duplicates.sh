#!/bin/bash

# Fix duplicate "More Orange Services" sections and broken URLs in Orange-area service pages

echo "Fixing Orange-area service pages..."

# List of all Orange-area service files
FILES=(
    "pages/services/emergency-roof-repair-orange-nj.html"
    "pages/services/emergency-roof-repair-east-orange-nj.html"
    "pages/services/emergency-roof-repair-west-orange-nj.html"
    "pages/services/emergency-roof-repair-south-orange-nj.html"
    "pages/services/roof-leak-repair-orange-nj.html"
    "pages/services/roof-leak-repair-east-orange-nj.html"
    "pages/services/roof-leak-repair-west-orange-nj.html"
    "pages/services/roof-leak-repair-south-orange-nj.html"
    "pages/services/roof-repair-orange-nj.html"
    "pages/services/roof-repair-east-orange-nj.html"
    "pages/services/roof-repair-west-orange-nj.html"
    "pages/services/roof-repair-south-orange-nj.html"
    "pages/services/roof-replacement-orange-nj.html"
    "pages/services/roof-replacement-east-orange-nj.html"
    "pages/services/roof-replacement-west-orange-nj.html"
    "pages/services/roof-replacement-south-orange-nj.html"
    "pages/services/new-roof-installation-orange-nj.html"
    "pages/services/new-roof-installation-east-orange-nj.html"
    "pages/services/new-roof-installation-west-orange-nj.html"
    "pages/services/new-roof-installation-south-orange-nj.html"
    "pages/services/siding-installation-orange-nj.html"
    "pages/services/siding-installation-east-orange-nj.html"
    "pages/services/siding-installation-west-orange-nj.html"
    "pages/services/siding-installation-south-orange-nj.html"
    "pages/services/siding-repair-orange-nj.html"
    "pages/services/siding-repair-east-orange-nj.html"
    "pages/services/siding-repair-west-orange-nj.html"
    "pages/services/siding-repair-south-orange-nj.html"
    "pages/services/gutter-installation-orange-nj.html"
    "pages/services/gutter-installation-east-orange-nj.html"
    "pages/services/gutter-installation-west-orange-nj.html"
    "pages/services/gutter-installation-south-orange-nj.html"
    "pages/services/gutter-repair-cleaning-orange-nj.html"
    "pages/services/gutter-repair-cleaning-east-orange-nj.html"
    "pages/services/gutter-repair-cleaning-west-orange-nj.html"
    "pages/services/gutter-repair-cleaning-south-orange-nj.html"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."

        # Create a backup
        cp "$file" "$file.bak"

        # Remove first duplicate section (lines with href="orange-nj.html" or similar short paths)
        # Keep only the section with proper /pages/services/ paths

        # Use awk to remove the first "More...Orange Services" section
        awk '
        BEGIN { in_first_section = 0; section_count = 0 }
        /<!-- More.*Orange Services -->/ {
            section_count++
            if (section_count == 1) {
                in_first_section = 1
                next
            }
        }
        /<\/section>/ {
            if (in_first_section == 1) {
                in_first_section = 0
                next
            }
        }
        in_first_section == 0 { print }
        ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"

        # Fix privacy policy link in cookie consent
        sed -i.bak2 's|href="/privacy-policy.html"|href="/pages/core/privacy-policy.html"|g' "$file"

        # Clean up backup files
        rm -f "$file.bak" "$file.bak2"

        echo "  ✓ Fixed $file"
    else
        echo "  ✗ File not found: $file"
    fi
done

echo ""
echo "All Orange-area service pages have been fixed!"
echo "Duplicate sections removed and privacy policy links corrected."
