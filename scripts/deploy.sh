#!/bin/bash

# R&E Roofing Website Deployment Script
# This script helps with basic deployment tasks

echo "🏠 R&E Roofing Website Deployment Helper"
echo "========================================"

# Check if running in correct directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo "✅ Project structure verified"

# Check for required files
required_files=("index.html" "css/styles.css" "js/main.js")
missing_files=()

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -gt 0 ]; then
    echo "❌ Missing required files:"
    printf '%s\n' "${missing_files[@]}"
    exit 1
fi

echo "✅ All required files present"

# Check for images directory
if [ ! -d "images" ]; then
    echo "⚠️  Warning: images directory not found. Creating it..."
    mkdir images
    echo "📁 Created images directory"
fi

# List what images are needed
echo ""
echo "📸 Required Images Checklist:"
echo "  - logo.png (Company logo)"
echo "  - favicon.ico (Browser icon)"
echo "  - hero-roof.jpg (Hero background)"
echo "  - financing-family.jpg (Family photo)"
echo "  - team-photo.jpg (Team photo)"

# Check if images exist
image_files=("logo.png" "favicon.ico" "hero-roof.jpg" "financing-family.jpg" "team-photo.jpg")
missing_images=()

for img in "${image_files[@]}"; do
    if [ ! -f "images/$img" ]; then
        missing_images+=("$img")
    fi
done

if [ ${#missing_images[@]} -gt 0 ]; then
    echo ""
    echo "⚠️  Missing images (website will use placeholders):"
    printf '   - %s\n' "${missing_images[@]}"
else
    echo "✅ All images present"
fi

# Basic HTML validation
if command -v tidy >/dev/null 2>&1; then
    echo ""
    echo "🔍 Running HTML validation..."
    if tidy -q -e index.html; then
        echo "✅ HTML validation passed"
    else
        echo "⚠️  HTML validation warnings (check output above)"
    fi
else
    echo "ℹ️  Install 'tidy' for HTML validation"
fi

# Check file permissions
echo ""
echo "🔒 Checking file permissions..."
find . -name "*.html" -o -name "*.css" -o -name "*.js" | while read file; do
    if [ ! -r "$file" ]; then
        echo "❌ $file is not readable"
    fi
done
echo "✅ File permissions OK"

# Display deployment instructions
echo ""
echo "🚀 Deployment Instructions:"
echo "=========================="
echo "1. Upload all files to your web server"
echo "2. Ensure the document root points to this directory"
echo "3. Update contact information in index.html:"
echo "   - Phone: (555) 123-4567"
echo "   - Email: info@reroofing.com"
echo "   - Address: 123 Main Street, Your City, ST 12345"
echo "4. Add your actual images to the images/ directory"
echo "5. Update robots.txt and sitemap.xml with your domain"
echo "6. Test the website thoroughly"
echo ""
echo "🔧 Optional Optimizations:"
echo "- Minify CSS and JavaScript"
echo "- Optimize images (WebP format)"
echo "- Enable Gzip compression"
echo "- Set up SSL certificate"
echo "- Configure Google Analytics"
echo ""
echo "✨ Deployment check complete!"

# Option to open in browser for testing
read -p "🌐 Open website in browser for testing? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if command -v open >/dev/null 2>&1; then
        open index.html
    elif command -v xdg-open >/dev/null 2>&1; then
        xdg-open index.html
    else
        echo "Please open index.html in your browser manually"
    fi
fi