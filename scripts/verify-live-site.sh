#!/bin/bash

# Comprehensive live site verification script
# Tests that all pages load and have proper CSS/JS links

BASE_URL="https://randeroofing.com"

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║           LIVE SITE VERIFICATION TEST                        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Test core assets
echo "📦 Testing Core Assets..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

CSS_CODE=$(curl -L -s -o /dev/null -w "%{http_code}" $BASE_URL/css/styles.css)
JS_CODE=$(curl -L -s -o /dev/null -w "%{http_code}" $BASE_URL/js/main.js)

if [ "$CSS_CODE" = "200" ]; then
    echo "✓ CSS file loads: $BASE_URL/css/styles.css"
else
    echo "✗ CSS file FAILED: HTTP $CSS_CODE"
fi

if [ "$JS_CODE" = "200" ]; then
    echo "✓ JS file loads: $BASE_URL/js/main.js"
else
    echo "✗ JS file FAILED: HTTP $JS_CODE"
fi

echo ""
echo "🏠 Testing Core Pages..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Array of core pages to test
declare -a CORE_PAGES=(
    "/"
    "/pages/core/services.html"
    "/pages/core/about.html"
    "/pages/core/calculator.html"
    "/pages/core/reviews.html"
    "/pages/core/blog.html"
)

for page in "${CORE_PAGES[@]}"; do
    CODE=$(curl -L -s -o /dev/null -w "%{http_code}" $BASE_URL$page)
    if [ "$CODE" = "200" ]; then
        # Check if page has CSS link
        HAS_CSS=$(curl -L -s $BASE_URL$page | grep -c 'href="/css/styles.css"')
        if [ "$HAS_CSS" -gt "0" ]; then
            echo "✓ $page (CSS linked)"
        else
            echo "⚠ $page (loads but CSS link missing)"
        fi
    else
        echo "✗ $page (HTTP $CODE)"
    fi
done

echo ""
echo "🏘️  Testing Town Pages (sample)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

declare -a TOWN_PAGES=(
    "/pages/towns/roofing-newark-nj.html"
    "/pages/towns/roofing-montclair-nj.html"
    "/pages/towns/roofing-bloomfield-nj.html"
)

for page in "${TOWN_PAGES[@]}"; do
    CODE=$(curl -L -s -o /dev/null -w "%{http_code}" $BASE_URL$page)
    if [ "$CODE" = "200" ]; then
        HAS_CSS=$(curl -L -s $BASE_URL$page | grep -c 'href="/css/styles.css"')
        if [ "$HAS_CSS" -gt "0" ]; then
            echo "✓ $page (CSS linked)"
        else
            echo "⚠ $page (loads but CSS link missing)"
        fi
    else
        echo "✗ $page (HTTP $CODE)"
    fi
done

echo ""
echo "🔧 Testing Service×Location Pages (sample)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

declare -a SERVICE_PAGES=(
    "/pages/services/roof-repair-newark-nj.html"
    "/pages/services/roof-replacement-montclair-nj.html"
    "/pages/services/gutter-installation-bloomfield-nj.html"
    "/pages/services/siding-installation-east-orange-nj.html"
)

for page in "${SERVICE_PAGES[@]}"; do
    CODE=$(curl -L -s -o /dev/null -w "%{http_code}" $BASE_URL$page)
    if [ "$CODE" = "200" ]; then
        HAS_CSS=$(curl -L -s $BASE_URL$page | grep -c 'href="/css/styles.css"')
        if [ "$HAS_CSS" -gt "0" ]; then
            echo "✓ $page (CSS linked)"
        else
            echo "⚠ $page (loads but CSS link missing)"
        fi
    else
        echo "✗ $page (HTTP $CODE)"
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ LIVE SITE VERIFICATION COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🌐 Visit: https://randeroofing.com"
echo "📱 Test in browser to verify full styling and functionality"
echo ""
