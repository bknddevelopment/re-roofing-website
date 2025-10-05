#!/bin/bash

# R&E Roofing Website Comprehensive Testing Script
# Tests all critical functionality and reports findings

BASE_URL="http://localhost:8000"
RESULTS_FILE="test-results.txt"
ERRORS_FILE="test-errors.txt"

# Color codes for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Initialize result files
> "$RESULTS_FILE"
> "$ERRORS_FILE"

echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "R&E Roofing Website - Comprehensive Test Report" | tee -a "$RESULTS_FILE"
echo "Test Date: $(date)" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "" | tee -a "$RESULTS_FILE"

# Test counter
TESTS_PASSED=0
TESTS_FAILED=0
PAGES_TESTED=0

# Function to test HTTP response
test_page() {
    local url="$1"
    local page_name="$2"

    PAGES_TESTED=$((PAGES_TESTED + 1))

    http_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

    if [ "$http_code" = "200" ]; then
        echo -e "${GREEN}✓${NC} PASS: $page_name (HTTP $http_code)" | tee -a "$RESULTS_FILE"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        echo -e "${RED}✗${NC} FAIL: $page_name (HTTP $http_code)" | tee -a "$RESULTS_FILE"
        echo "ERROR: $page_name returned HTTP $http_code" >> "$ERRORS_FILE"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

# Function to check for specific content
check_content() {
    local url="$1"
    local search_term="$2"
    local description="$3"

    if curl -s "$url" | grep -q "$search_term"; then
        echo -e "${GREEN}✓${NC} PASS: $description" | tee -a "$RESULTS_FILE"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        echo -e "${RED}✗${NC} FAIL: $description" | tee -a "$RESULTS_FILE"
        echo "ERROR: Content check failed - $description" >> "$ERRORS_FILE"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

# Function to check for broken links
check_links() {
    local url="$1"
    local page_name="$2"

    # Extract all href links
    links=$(curl -s "$url" | grep -o 'href="[^"]*"' | sed 's/href="//;s/"//' | grep -E '\.html$|^/')

    broken_count=0
    for link in $links; do
        # Skip external links and anchors
        if [[ "$link" == http* ]] || [[ "$link" == \#* ]]; then
            continue
        fi

        # Construct full URL
        if [[ "$link" == /* ]]; then
            full_url="${BASE_URL}${link}"
        else
            full_url="${BASE_URL}/${link}"
        fi

        # Test the link
        link_code=$(curl -s -o /dev/null -w "%{http_code}" "$full_url")
        if [ "$link_code" != "200" ]; then
            echo "  Broken link in $page_name: $link (HTTP $link_code)" >> "$ERRORS_FILE"
            broken_count=$((broken_count + 1))
        fi
    done

    if [ $broken_count -eq 0 ]; then
        echo -e "${GREEN}✓${NC} PASS: No broken links in $page_name" | tee -a "$RESULTS_FILE"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${YELLOW}⚠${NC} WARNING: $broken_count broken link(s) in $page_name" | tee -a "$RESULTS_FILE"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "1. HOMEPAGE TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Test homepage loads
test_page "$BASE_URL/" "Homepage"

# Test homepage content
check_content "$BASE_URL/" "R&E Roofing" "Homepage contains company name"
check_content "$BASE_URL/" "(667) 204-1609" "Homepage contains phone number"
check_content "$BASE_URL/" "contactModal" "Homepage contains contact modal"
check_content "$BASE_URL/" "mobile-menu-toggle" "Homepage contains mobile menu"
check_content "$BASE_URL/" "application/ld\+json" "Homepage contains schema markup"

# Test navigation elements
check_content "$BASE_URL/" "<nav" "Homepage has navigation"
check_content "$BASE_URL/" "footer" "Homepage has footer"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "2. CORE PAGES TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Test core pages
test_page "$BASE_URL/pages/core/about.html" "About Page"
test_page "$BASE_URL/pages/core/services.html" "Services Page"
test_page "$BASE_URL/pages/core/calculator.html" "Calculator Page"
test_page "$BASE_URL/pages/core/faq.html" "FAQ Page"
test_page "$BASE_URL/pages/core/quote.html" "Quote Page"
test_page "$BASE_URL/pages/core/reviews.html" "Reviews Page"
test_page "$BASE_URL/pages/core/blog.html" "Blog Page"
test_page "$BASE_URL/pages/core/privacy-policy.html" "Privacy Policy Page"
test_page "$BASE_URL/pages/core/terms-of-service.html" "Terms of Service Page"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "3. TOWN PAGES TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Test tier 1 town pages
test_page "$BASE_URL/pages/towns/roofing-newark-nj.html" "Newark Town Page"
test_page "$BASE_URL/pages/towns/roofing-bloomfield-nj.html" "Bloomfield Town Page"
test_page "$BASE_URL/pages/towns/roofing-montclair-nj.html" "Montclair Town Page"
test_page "$BASE_URL/pages/towns/roofing-east-orange-nj.html" "East Orange Town Page"
test_page "$BASE_URL/pages/towns/roofing-irvington-nj.html" "Irvington Town Page"

# Check town page content
check_content "$BASE_URL/pages/towns/roofing-newark-nj.html" "Newark" "Newark page contains town name"
check_content "$BASE_URL/pages/towns/roofing-newark-nj.html" "contactModal" "Newark page has contact modal"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "4. SERVICE×LOCATION PAGES TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Test service×location pages
test_page "$BASE_URL/pages/services/roof-repair-newark-nj.html" "Roof Repair Newark"
test_page "$BASE_URL/pages/services/roof-replacement-newark-nj.html" "Roof Replacement Newark"
test_page "$BASE_URL/pages/services/gutter-installation-bloomfield-nj.html" "Gutter Installation Bloomfield"
test_page "$BASE_URL/pages/services/asphalt-shingle-roofing-montclair-nj.html" "Asphalt Shingle Montclair"
test_page "$BASE_URL/pages/services/metal-roofing-east-orange-nj.html" "Metal Roofing East Orange"

# Check service page content
check_content "$BASE_URL/pages/services/roof-repair-newark-nj.html" "Roof Repair" "Service page contains service name"
check_content "$BASE_URL/pages/services/roof-repair-newark-nj.html" "Newark" "Service page contains town name"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "5. ASSET LOADING TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Test CSS and JS files load
test_page "$BASE_URL/css/styles.css" "Main CSS file"
test_page "$BASE_URL/js/main.js" "Main JS file"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "6. LINK INTEGRITY TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Test for broken links on key pages
check_links "$BASE_URL/" "Homepage"
check_links "$BASE_URL/pages/core/services.html" "Services Page"
check_links "$BASE_URL/pages/towns/roofing-newark-nj.html" "Newark Town Page"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "7. MOBILE RESPONSIVENESS CHECK" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Check for mobile meta tags and responsive elements
check_content "$BASE_URL/" "viewport" "Homepage has viewport meta tag"
check_content "$BASE_URL/" "mobile-menu-toggle" "Homepage has mobile menu toggle"
check_content "$BASE_URL/" "@media" "CSS contains media queries"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "8. SEO & SCHEMA VALIDATION" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Check for essential SEO elements
check_content "$BASE_URL/" "<title>" "Homepage has title tag"
check_content "$BASE_URL/" 'name="description"' "Homepage has meta description"
check_content "$BASE_URL/" 'rel="canonical"' "Homepage has canonical URL"
check_content "$BASE_URL/" "RoofingContractor" "Homepage has RoofingContractor schema"
check_content "$BASE_URL/" "areaServed" "Homepage schema includes areaServed"

# Check sitemap
test_page "$BASE_URL/sitemap.xml" "Sitemap XML"
test_page "$BASE_URL/robots.txt" "Robots.txt"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "TEST SUMMARY" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "" | tee -a "$RESULTS_FILE"
echo "Total Pages Tested: $PAGES_TESTED" | tee -a "$RESULTS_FILE"
echo "Total Tests Run: $((TESTS_PASSED + TESTS_FAILED))" | tee -a "$RESULTS_FILE"
echo -e "${GREEN}Tests Passed: $TESTS_PASSED${NC}" | tee -a "$RESULTS_FILE"
echo -e "${RED}Tests Failed: $TESTS_FAILED${NC}" | tee -a "$RESULTS_FILE"
echo "" | tee -a "$RESULTS_FILE"

# Calculate pass rate
TOTAL_TESTS=$((TESTS_PASSED + TESTS_FAILED))
if [ $TOTAL_TESTS -gt 0 ]; then
    PASS_RATE=$(echo "scale=1; $TESTS_PASSED * 100 / $TOTAL_TESTS" | bc)
    echo "Pass Rate: ${PASS_RATE}%" | tee -a "$RESULTS_FILE"
fi

echo "" | tee -a "$RESULTS_FILE"

# Overall status
if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${GREEN}OVERALL STATUS: ✓ ALL TESTS PASSED${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${GREEN}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    exit 0
else
    echo -e "${YELLOW}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${YELLOW}OVERALL STATUS: ⚠ SOME TESTS FAILED${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${YELLOW}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    echo "" | tee -a "$RESULTS_FILE"
    echo "Errors logged to: $ERRORS_FILE" | tee -a "$RESULTS_FILE"
    exit 1
fi
