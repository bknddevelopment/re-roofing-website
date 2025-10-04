#!/bin/bash

# Fix CSS and JS paths in all moved HTML files
# CSS and JS are in root-level directories, so use absolute paths

echo "Fixing asset paths in all pages..."

# Fix pages/core/ - need to go up 2 levels (../../)
for file in pages/core/*.html; do
    if [ -f "$file" ]; then
        echo "Fixing $file..."
        sed -i '' \
            -e 's|href="css/styles\.css"|href="/css/styles.css"|g' \
            -e 's|src="js/main\.js"|src="/js/main.js"|g' \
            -e 's|href="images/|href="/images/|g' \
            -e 's|src="images/|src="/images/|g' \
            "$file"
    fi
done

# Fix pages/towns/ - need to go up 2 levels (../../)
for file in pages/towns/*.html; do
    if [ -f "$file" ]; then
        echo "Fixing $file..."
        sed -i '' \
            -e 's|href="css/styles\.css"|href="/css/styles.css"|g' \
            -e 's|src="js/main\.js"|src="/js/main.js"|g' \
            -e 's|href="images/|href="/images/|g' \
            -e 's|src="images/|src="/images/|g' \
            "$file"
    fi
done

# Fix pages/services/ - need to go up 2 levels (../../)
for file in pages/services/*.html; do
    if [ -f "$file" ]; then
        echo "Fixing $file..."
        sed -i '' \
            -e 's|href="css/styles\.css"|href="/css/styles.css"|g' \
            -e 's|src="js/main\.js"|src="/js/main.js"|g' \
            -e 's|href="images/|href="/images/|g' \
            -e 's|src="images/|src="/images/|g' \
            "$file"
    fi
done

echo ""
echo "✅ Asset paths fixed in all pages!"
echo ""
echo "Changed:"
echo "  css/styles.css → /css/styles.css"
echo "  js/main.js → /js/main.js"
echo "  images/ → /images/"
echo ""
