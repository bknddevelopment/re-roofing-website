#!/bin/bash

# GitHub Pages Deployment Testing Script
# Tests the live R&E Roofing website at GitHub Pages

GITHUB_URL="https://bknddevelopment.github.io/re-roofing-website"
RESULTS_FILE="github-pages-test-results.txt"
ERRORS_FILE="github-pages-test-errors.txt"

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Counters
TESTS_PASSED=0
TESTS_FAILED=0
PAGES_TESTED=0

# Initialize result files
> "$RESULTS_FILE"
> "$ERRORS_FILE"

echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "GitHub Pages Deployment - Comprehensive Test Report" | tee -a "$RESULTS_FILE"
echo "Test Date: $(date)" | tee -a "$RESULTS_FILE"
echo "URL: $GITHUB_URL" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "" | tee -a "$RESULTS_FILE"

# Test page function
test_page() {
    local url="$1"
    local page_name="$2"

    PAGES_TESTED=$((PAGES_TESTED + 1))

    # Follow redirects with -L
    http_code=$(curl -s -L -o /dev/null -w "%{http_code}" "$url")

    if [ "$http_code" = "200" ]; then
        echo -e "${GREEN}✓${NC} PASS: $page_name (HTTP $http_code)" | tee -a "$RESULTS_FILE"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        echo -e "${RED}✗${NC} FAIL: $page_name (HTTP $http_code)" | tee -a "$RESULTS_FILE"
        echo "ERROR: $page_name returned HTTP $http_code - $url" >> "$ERRORS_FILE"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

# Content check function
check_content() {
    local url="$1"
    local search_term="$2"
    local description="$3"

    if curl -s -L "$url" | grep -q "$search_term"; then
        echo -e "${GREEN}✓${NC} PASS: $description" | tee -a "$RESULTS_FILE"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        echo -e "${RED}✗${NC} FAIL: $description" | tee -a "$RESULTS_FILE"
        echo "ERROR: Content check failed - $description - $url" >> "$ERRORS_FILE"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "1. HOMEPAGE TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

test_page "$GITHUB_URL/" "Homepage"
check_content "$GITHUB_URL/" "R&E Roofing" "Homepage contains company name"
check_content "$GITHUB_URL/" "(667) 204-1609" "Homepage contains phone number"
check_content "$GITHUB_URL/" "contactModal" "Homepage has contact modal"
check_content "$GITHUB_URL/" "mobile-menu-toggle" "Homepage has mobile hamburger menu"
check_content "$GITHUB_URL/" "RoofingContractor" "Homepage has RoofingContractor schema"
check_content "$GITHUB_URL/" "areaServed" "Homepage schema includes areaServed"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "2. CORE PAGES TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

test_page "$GITHUB_URL/pages/core/about.html" "About Page"
test_page "$GITHUB_URL/pages/core/services.html" "Services Page"
test_page "$GITHUB_URL/pages/core/calculator.html" "Calculator Page"
test_page "$GITHUB_URL/pages/core/faq.html" "FAQ Page"
test_page "$GITHUB_URL/pages/core/quote.html" "Quote Page"
test_page "$GITHUB_URL/pages/core/reviews.html" "Reviews Page"
test_page "$GITHUB_URL/pages/core/blog.html" "Blog Page"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "3. TOWN PAGES TESTING (Tier 1)" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

test_page "$GITHUB_URL/pages/towns/roofing-newark-nj.html" "Newark Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-east-orange-nj.html" "East Orange Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-irvington-nj.html" "Irvington Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-bloomfield-nj.html" "Bloomfield Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-west-orange-nj.html" "West Orange Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-montclair-nj.html" "Montclair Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-belleville-nj.html" "Belleville Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-livingston-nj.html" "Livingston Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-nutley-nj.html" "Nutley Town Page"
test_page "$GITHUB_URL/pages/towns/roofing-maplewood-nj.html" "Maplewood Town Page"

# Check town page has proper content
check_content "$GITHUB_URL/pages/towns/roofing-newark-nj.html" "Newark" "Newark page mentions town name"
check_content "$GITHUB_URL/pages/towns/roofing-bloomfield-nj.html" "Bloomfield" "Bloomfield page mentions town name"
check_content "$GITHUB_URL/pages/towns/roofing-montclair-nj.html" "Montclair" "Montclair page mentions town name"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "4. SERVICE×LOCATION PAGES TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

# Test various service×location combinations
test_page "$GITHUB_URL/pages/services/roof-repair-newark-nj.html" "Roof Repair - Newark"
test_page "$GITHUB_URL/pages/services/roof-replacement-newark-nj.html" "Roof Replacement - Newark"
test_page "$GITHUB_URL/pages/services/gutter-installation-bloomfield-nj.html" "Gutter Installation - Bloomfield"
test_page "$GITHUB_URL/pages/services/new-roof-installation-montclair-nj.html" "New Roof Installation - Montclair"
test_page "$GITHUB_URL/pages/services/emergency-roof-repair-east-orange-nj.html" "Emergency Roof Repair - East Orange"
test_page "$GITHUB_URL/pages/services/roof-leak-repair-irvington-nj.html" "Roof Leak Repair - Irvington"
test_page "$GITHUB_URL/pages/services/siding-installation-livingston-nj.html" "Siding Installation - Livingston"
test_page "$GITHUB_URL/pages/services/gutter-repair-cleaning-nutley-nj.html" "Gutter Repair - Nutley"

# Check service pages have proper content
check_content "$GITHUB_URL/pages/services/roof-repair-newark-nj.html" "Roof Repair" "Service page contains service name"
check_content "$GITHUB_URL/pages/services/roof-repair-newark-nj.html" "Newark" "Service page contains town name"
check_content "$GITHUB_URL/pages/services/roof-repair-newark-nj.html" "(667) 204-1609" "Service page has phone number"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "5. ASSETS & RESOURCES TESTING" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

test_page "$GITHUB_URL/css/styles.css" "Main CSS File"
test_page "$GITHUB_URL/js/main.js" "Main JavaScript File"
test_page "$GITHUB_URL/sitemap.xml" "Sitemap XML"
test_page "$GITHUB_URL/robots.txt" "Robots.txt"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "6. SEO & META TAG VALIDATION" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

check_content "$GITHUB_URL/" "<title>" "Homepage has title tag"
check_content "$GITHUB_URL/" 'name="description"' "Homepage has meta description"
check_content "$GITHUB_URL/" 'rel="canonical"' "Homepage has canonical URL"
check_content "$GITHUB_URL/" 'name="viewport"' "Homepage has viewport meta tag"
check_content "$GITHUB_URL/" 'property="og:' "Homepage has Open Graph tags"
check_content "$GITHUB_URL/" 'name="twitter:' "Homepage has Twitter Card tags"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "7. MOBILE RESPONSIVENESS INDICATORS" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

check_content "$GITHUB_URL/" "mobile-menu-toggle" "Mobile menu toggle present"
check_content "$GITHUB_URL/" "mobile-nav" "Mobile navigation present"
check_content "$GITHUB_URL/css/styles.css" "@media" "CSS contains media queries"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "8. FUNCTIONAL ELEMENTS CHECK" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"

check_content "$GITHUB_URL/" "contactModal" "Contact modal element present"
check_content "$GITHUB_URL/" "back-to-top" "Back to top button present"
check_content "$GITHUB_URL/" "live-chat" "Live chat widget present"
check_content "$GITHUB_URL/js/main.js" "calculateEstimate" "Calculator function present in JS"
check_content "$GITHUB_URL/js/main.js" "openContactModal" "Contact modal function present"

echo "" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "TEST SUMMARY" | tee -a "$RESULTS_FILE"
echo "==================================================================" | tee -a "$RESULTS_FILE"
echo "" | tee -a "$RESULTS_FILE"

# Site statistics
echo "SITE STATISTICS:" | tee -a "$RESULTS_FILE"
echo "- Core Pages: 9" | tee -a "$RESULTS_FILE"
echo "- Town Pages: 15" | tee -a "$RESULTS_FILE"
echo "- Service Pages: 255" | tee -a "$RESULTS_FILE"
echo "- Total HTML Pages: ~280" | tee -a "$RESULTS_FILE"
echo "" | tee -a "$RESULTS_FILE"

echo "TEST RESULTS:" | tee -a "$RESULTS_FILE"
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
    echo -e "${GREEN}OVERALL STATUS: ✓ ALL TESTS PASSED - SITE IS LIVE AND FUNCTIONAL${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${GREEN}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    exit 0
elif [ $TESTS_FAILED -lt 5 ]; then
    echo -e "${YELLOW}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${YELLOW}OVERALL STATUS: ⚠ MOSTLY FUNCTIONAL - MINOR ISSUES DETECTED${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${YELLOW}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    echo "" | tee -a "$RESULTS_FILE"
    echo "Errors logged to: $ERRORS_FILE" | tee -a "$RESULTS_FILE"
    exit 1
else
    echo -e "${RED}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${RED}OVERALL STATUS: ✗ MAJOR ISSUES DETECTED${NC}" | tee -a "$RESULTS_FILE"
    echo -e "${RED}==================================================================${NC}" | tee -a "$RESULTS_FILE"
    echo "" | tee -a "$RESULTS_FILE"
    echo "Errors logged to: $ERRORS_FILE" | tee -a "$RESULTS_FILE"
    exit 1
fi
