#!/bin/bash

# Script to update sitemap.xml with new directory structure
# Run from project root

echo "Updating sitemap.xml with new paths..."

sed -i '' \
    -e 's|<loc>https://randeroofing.com/about\.html</loc>|<loc>https://randeroofing.com/pages/core/about.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/services\.html</loc>|<loc>https://randeroofing.com/pages/core/services.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/calculator\.html</loc>|<loc>https://randeroofing.com/pages/core/calculator.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/faq\.html</loc>|<loc>https://randeroofing.com/pages/core/faq.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/quote\.html</loc>|<loc>https://randeroofing.com/pages/core/quote.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/reviews\.html</loc>|<loc>https://randeroofing.com/pages/core/reviews.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/blog\.html</loc>|<loc>https://randeroofing.com/pages/core/blog.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/privacy-policy\.html</loc>|<loc>https://randeroofing.com/pages/core/privacy-policy.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/terms-of-service\.html</loc>|<loc>https://randeroofing.com/pages/core/terms-of-service.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/roofing-\([a-z-]*\)-nj\.html</loc>|<loc>https://randeroofing.com/pages/towns/roofing-\1-nj.html</loc>|g' \
    -e 's|<loc>https://randeroofing.com/\([a-z-]*-[a-z-]*-[a-z-]*-nj\)\.html</loc>|<loc>https://randeroofing.com/pages/services/\1.html</loc>|g' \
    sitemap.xml

# Fix any double /pages/ that might have been created
sed -i '' 's|/pages/pages/|/pages/|g' sitemap.xml

echo "Sitemap.xml updated successfully!"
