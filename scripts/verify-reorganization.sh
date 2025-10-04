#!/bin/bash

# Verification script for directory reorganization
# Run from project root

echo "======================================"
echo "Directory Reorganization Verification"
echo "======================================"
echo ""

# Check directory structure exists
echo "1. Verifying directory structure..."
if [ -d "pages/core" ] && [ -d "pages/towns" ] && [ -d "pages/services" ] && [ -d "docs" ] && [ -d "scripts" ]; then
    echo "   ✓ All directories created successfully"
else
    echo "   ✗ Missing directories!"
    exit 1
fi
echo ""

# Count files in each directory
echo "2. File counts:"
CORE_COUNT=$(ls -1 pages/core/*.html 2>/dev/null | wc -l | tr -d ' ')
TOWNS_COUNT=$(ls -1 pages/towns/*.html 2>/dev/null | wc -l | tr -d ' ')
SERVICES_COUNT=$(ls -1 pages/services/*.html 2>/dev/null | wc -l | tr -d ' ')
DOCS_COUNT=$(ls -1 docs/*.md 2>/dev/null | wc -l | tr -d ' ')
SCRIPTS_COUNT=$(ls -1 scripts/* 2>/dev/null | wc -l | tr -d ' ')

echo "   Core pages:    $CORE_COUNT files"
echo "   Town pages:    $TOWNS_COUNT files"
echo "   Service pages: $SERVICES_COUNT files"
echo "   Documentation: $DOCS_COUNT files"
echo "   Scripts:       $SCRIPTS_COUNT files"
echo "   Total HTML:    $((CORE_COUNT + TOWNS_COUNT + SERVICES_COUNT + 1)) pages (+ index.html)"
echo ""

# Check root directory is clean
echo "3. Checking root directory..."
HTML_IN_ROOT=$(ls -1 *.html 2>/dev/null | grep -v "index.html\|google.*\.html\|index-optimized.html" | wc -l | tr -d ' ')
if [ "$HTML_IN_ROOT" -eq "0" ]; then
    echo "   ✓ Root directory clean (only essential files)"
else
    echo "   ⚠ Found $HTML_IN_ROOT unexpected HTML files in root"
fi
echo ""

# Verify sitemap paths updated
echo "4. Verifying sitemap.xml..."
SITEMAP_PAGES=$(grep -c "pages/" sitemap.xml)
if [ "$SITEMAP_PAGES" -gt "200" ]; then
    echo "   ✓ Sitemap updated with /pages/ paths ($SITEMAP_PAGES entries)"
else
    echo "   ✗ Sitemap may not be fully updated"
fi
echo ""

# Check for broken links (sample)
echo "5. Sample link verification..."
if grep -q 'href="/pages/core/services.html"' index.html; then
    echo "   ✓ Index.html links updated"
else
    echo "   ✗ Index.html links may be incorrect"
fi

if grep -q 'href="/pages/towns/roofing-newark-nj.html"' index.html; then
    echo "   ✓ Town page links updated"
else
    echo "   ✗ Town page links may be incorrect"
fi
echo ""

# Check CLAUDE.md exists
echo "6. Documentation check..."
if [ -f "CLAUDE.md" ] && [ -f "docs/CLAUDE.md" ]; then
    echo "   ✓ CLAUDE.md exists in root and docs/"
else
    echo "   ⚠ CLAUDE.md missing from root or docs/"
fi
echo ""

echo "======================================"
echo "Verification Summary"
echo "======================================"
echo "Total pages reorganized: $((CORE_COUNT + TOWNS_COUNT + SERVICES_COUNT + 1))"
echo "Documentation archived: $DOCS_COUNT files"
echo "Scripts organized: $SCRIPTS_COUNT files"
echo ""
echo "New structure:"
echo "  /index.html"
echo "  /pages/core/ ($CORE_COUNT files)"
echo "  /pages/towns/ ($TOWNS_COUNT files)"
echo "  /pages/services/ ($SERVICES_COUNT files)"
echo "  /docs/ ($DOCS_COUNT files)"
echo "  /scripts/ ($SCRIPTS_COUNT files)"
echo ""
echo "Next steps:"
echo "1. Test site locally: python3 -m http.server 8000"
echo "2. Verify navigation works on all pages"
echo "3. Test mobile responsiveness"
echo "4. Deploy to GitHub Pages"
echo ""
