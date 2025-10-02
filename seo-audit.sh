#!/bin/bash

# SEO Site Health Audit Script
# R&E Roofing Website - Comprehensive SEO Audit

echo "========================================="
echo "R&E ROOFING - SEO SITE HEALTH AUDIT"
echo "========================================="
echo ""

# Count total HTML pages (exclude test files)
TOTAL_PAGES=$(ls -1 *.html 2>/dev/null | grep -v "test" | grep -v "optimized" | wc -l | tr -d ' ')
echo "Total Pages to Audit: $TOTAL_PAGES"
echo ""

# 1. META TAG ANALYSIS
echo "========================================="
echo "1. META TAG ANALYSIS"
echo "========================================="

echo ""
echo "1.1 Title Tag Analysis:"
echo "------------------------"

# Check for missing title tags
echo "Missing Title Tags:"
MISSING_TITLES=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    if ! grep -q "<title>" "$file" 2>/dev/null; then
        echo "  - $file"
        ((MISSING_TITLES++))
    fi
done
if [ $MISSING_TITLES -eq 0 ]; then
    echo "  ✓ All pages have title tags"
fi
echo ""

# Check title length (>60 characters)
echo "Title Tags Over 60 Characters:"
LONG_TITLES=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    TITLE=$(grep -o "<title>.*</title>" "$file" 2>/dev/null | sed 's/<[^>]*>//g')
    if [ -n "$TITLE" ]; then
        LENGTH=${#TITLE}
        if [ $LENGTH -gt 60 ]; then
            echo "  ⚠ $file: $LENGTH chars - $TITLE"
            ((LONG_TITLES++))
        fi
    fi
done
if [ $LONG_TITLES -eq 0 ]; then
    echo "  ✓ All title tags are under 60 characters"
fi
echo ""

# Check for duplicate titles
echo "Duplicate Title Tags:"
DUPLICATE_TITLES=$(for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    grep -o "<title>.*</title>" "$file" 2>/dev/null | sed 's/<[^>]*>//g'
done | sort | uniq -d)

if [ -z "$DUPLICATE_TITLES" ]; then
    echo "  ✓ All title tags are unique"
else
    echo "$DUPLICATE_TITLES" | while read -r title; do
        echo "  ✗ Duplicate: $title"
        for file in *.html; do
            if grep -q "<title>$title</title>" "$file" 2>/dev/null; then
                echo "    - $file"
            fi
        done
    done
fi
echo ""

echo "1.2 Meta Description Analysis:"
echo "-------------------------------"

# Check for missing meta descriptions
echo "Missing Meta Descriptions:"
MISSING_DESC=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    if ! grep -q 'meta name="description"' "$file" 2>/dev/null; then
        echo "  - $file"
        ((MISSING_DESC++))
    fi
done
if [ $MISSING_DESC -eq 0 ]; then
    echo "  ✓ All pages have meta descriptions"
fi
echo ""

# Check description length (>160 characters)
echo "Meta Descriptions Over 160 Characters:"
LONG_DESC=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    DESC=$(grep 'meta name="description"' "$file" 2>/dev/null | sed 's/.*content="\([^"]*\)".*/\1/')
    if [ -n "$DESC" ]; then
        LENGTH=${#DESC}
        if [ $LENGTH -gt 160 ]; then
            echo "  ⚠ $file: $LENGTH chars"
            ((LONG_DESC++))
        fi
    fi
done
if [ $LONG_DESC -eq 0 ]; then
    echo "  ✓ All meta descriptions are under 160 characters"
fi
echo ""

echo "1.3 Meta Keywords (Deprecated - Should Remove):"
echo "------------------------------------------------"
KEYWORDS_COUNT=$(grep -l 'meta name="keywords"' *.html 2>/dev/null | grep -v "test" | grep -v "optimized" | wc -l | tr -d ' ')
echo "  ⚠ Found $KEYWORDS_COUNT pages with meta keywords tag (deprecated, should remove)"
echo ""

# 2. CANONICAL URL ANALYSIS
echo "========================================="
echo "2. CANONICAL URL ANALYSIS"
echo "========================================="
echo ""

echo "Missing Canonical Tags:"
MISSING_CANONICAL=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    if ! grep -q 'rel="canonical"' "$file" 2>/dev/null; then
        echo "  - $file"
        ((MISSING_CANONICAL++))
    fi
done
if [ $MISSING_CANONICAL -eq 0 ]; then
    echo "  ✓ All pages have canonical tags"
fi
echo ""

echo "Canonical URL Format Issues:"
CANONICAL_ISSUES=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    CANONICAL=$(grep 'rel="canonical"' "$file" 2>/dev/null | sed 's/.*href="\([^"]*\)".*/\1/')
    if [ -n "$CANONICAL" ]; then
        # Check if starts with https://reroofing.com or https://www.reroofing.com
        if [[ ! "$CANONICAL" =~ ^https://(www\.)?reroofing\.com/ ]]; then
            echo "  ⚠ $file: $CANONICAL (should use https://reroofing.com or https://www.reroofing.com)"
            ((CANONICAL_ISSUES++))
        fi
    fi
done
if [ $CANONICAL_ISSUES -eq 0 ]; then
    echo "  ✓ All canonical URLs use correct domain format"
fi
echo ""

# 3. SCHEMA MARKUP ANALYSIS
echo "========================================="
echo "3. SCHEMA MARKUP ANALYSIS"
echo "========================================="
echo ""

echo "Schema Markup Presence:"
echo "-----------------------"

echo "RoofingContractor Schema:"
CONTRACTOR_SCHEMA=$(grep -l '"@type": "RoofingContractor"' *.html 2>/dev/null | grep -v "test" | grep -v "optimized" | wc -l | tr -d ' ')
echo "  Found on $CONTRACTOR_SCHEMA pages"

echo "Service Schema:"
SERVICE_SCHEMA=$(grep -l '"@type": "Service"' *.html 2>/dev/null | grep -v "test" | grep -v "optimized" | wc -l | tr -d ' ')
echo "  Found on $SERVICE_SCHEMA pages"

echo "BreadcrumbList Schema:"
BREADCRUMB_SCHEMA=$(grep -l '"@type": "BreadcrumbList"' *.html 2>/dev/null | grep -v "test" | grep -v "optimized" | wc -l | tr -d ' ')
echo "  Found on $BREADCRUMB_SCHEMA pages"
echo ""

# 4. OPEN GRAPH & TWITTER CARDS
echo "========================================="
echo "4. OPEN GRAPH & TWITTER CARDS"
echo "========================================="
echo ""

echo "Missing Open Graph Tags:"
MISSING_OG=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    if ! grep -q 'property="og:title"' "$file" 2>/dev/null; then
        echo "  - $file (missing og:title)"
        ((MISSING_OG++))
    fi
done
if [ $MISSING_OG -eq 0 ]; then
    echo "  ✓ All pages have Open Graph title tags"
fi
echo ""

echo "Missing Twitter Card Tags:"
MISSING_TWITTER=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    if ! grep -q 'name="twitter:card"' "$file" 2>/dev/null; then
        echo "  - $file (missing twitter:card)"
        ((MISSING_TWITTER++))
    fi
done
if [ $MISSING_TWITTER -eq 0 ]; then
    echo "  ✓ All pages have Twitter Card tags"
fi
echo ""

# 5. SITEMAP VALIDATION
echo "========================================="
echo "5. SITEMAP VALIDATION"
echo "========================================="
echo ""

if [ -f "sitemap.xml" ]; then
    SITEMAP_URLS=$(grep -c "<loc>" sitemap.xml 2>/dev/null)
    echo "URLs in sitemap.xml: $SITEMAP_URLS"

    # Check for pages not in sitemap
    echo ""
    echo "Pages NOT in sitemap.xml:"
    MISSING_FROM_SITEMAP=0
    for file in *.html; do
        if [[ "$file" == "index.html" ]] || [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
            continue
        fi
        if ! grep -q "$file" sitemap.xml 2>/dev/null; then
            echo "  - $file"
            ((MISSING_FROM_SITEMAP++))
        fi
    done
    if [ $MISSING_FROM_SITEMAP -eq 0 ]; then
        echo "  ✓ All pages are in sitemap.xml"
    fi
else
    echo "  ✗ sitemap.xml not found!"
fi
echo ""

# 6. MOBILE OPTIMIZATION
echo "========================================="
echo "6. MOBILE OPTIMIZATION"
echo "========================================="
echo ""

echo "Viewport Meta Tag:"
MISSING_VIEWPORT=0
for file in *.html; do
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"optimized"* ]]; then
        continue
    fi
    if ! grep -q 'name="viewport"' "$file" 2>/dev/null; then
        echo "  - $file"
        ((MISSING_VIEWPORT++))
    fi
done
if [ $MISSING_VIEWPORT -eq 0 ]; then
    echo "  ✓ All pages have viewport meta tag"
fi
echo ""

# 7. SUMMARY & VERDICT
echo "========================================="
echo "7. AUDIT SUMMARY & VERDICT"
echo "========================================="
echo ""

TOTAL_ERRORS=$((MISSING_TITLES + MISSING_DESC + MISSING_CANONICAL + MISSING_VIEWPORT))
TOTAL_WARNINGS=$((LONG_TITLES + LONG_DESC + KEYWORDS_COUNT + CANONICAL_ISSUES))

echo "Critical Errors (BLOCK DEPLOYMENT): $TOTAL_ERRORS"
echo "  - Missing Titles: $MISSING_TITLES"
echo "  - Missing Descriptions: $MISSING_DESC"
echo "  - Missing Canonicals: $MISSING_CANONICAL"
echo "  - Missing Viewport: $MISSING_VIEWPORT"
echo ""

echo "Warnings (Fix Before Launch): $TOTAL_WARNINGS"
echo "  - Long Titles: $LONG_TITLES"
echo "  - Long Descriptions: $LONG_DESC"
echo "  - Deprecated Keywords Tags: $KEYWORDS_COUNT"
echo "  - Canonical Format Issues: $CANONICAL_ISSUES"
echo ""

if [ $TOTAL_ERRORS -eq 0 ]; then
    if [ $TOTAL_WARNINGS -eq 0 ]; then
        echo "VERDICT: ✓ GO - Site is production ready"
    else
        echo "VERDICT: ⚠ CAUTION - Site can deploy but has $TOTAL_WARNINGS warnings to address"
    fi
else
    echo "VERDICT: ✗ NO-GO - Site has $TOTAL_ERRORS critical errors that BLOCK deployment"
fi

echo ""
echo "========================================="
echo "END OF SEO AUDIT"
echo "========================================="
