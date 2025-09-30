#!/usr/bin/env node

/**
 * R&E Roofing - Automated Test Runner
 * Tests all 8 pages for functionality, navigation, forms, and content
 */

const fs = require('fs');
const path = require('path');

// ANSI color codes for terminal output
const colors = {
    reset: '\x1b[0m',
    bright: '\x1b[1m',
    dim: '\x1b[2m',
    red: '\x1b[31m',
    green: '\x1b[32m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    magenta: '\x1b[35m',
    cyan: '\x1b[36m',
    white: '\x1b[37m'
};

// Test configuration
const TEST_CONFIG = {
    pages: [
        'index.html',
        'services.html',
        'calculator.html',
        'reviews.html',
        'faq.html',
        'about.html',
        'quote.html',
        'blog.html'
    ],
    baseDir: __dirname
};

// Test results storage
const testResults = {
    total: 0,
    passed: 0,
    failed: 0,
    skipped: 0,
    details: []
};

// Utility functions
function log(message, color = 'white') {
    console.log(`${colors[color]}${message}${colors.reset}`);
}

function logSection(title) {
    console.log('\n' + '='.repeat(60));
    log(title, 'cyan');
    console.log('='.repeat(60));
}

function logTest(name, status, details = '') {
    const statusSymbol = {
        'PASS': '✓',
        'FAIL': '✗',
        'SKIP': '⊘'
    }[status] || '?';

    const statusColor = {
        'PASS': 'green',
        'FAIL': 'red',
        'SKIP': 'yellow'
    }[status] || 'white';

    log(`  ${statusSymbol} ${name}`, statusColor);
    if (details) {
        log(`    ${details}`, 'dim');
    }
}

function recordTest(category, name, status, details = '') {
    testResults.total++;
    if (status === 'PASS') testResults.passed++;
    else if (status === 'FAIL') testResults.failed++;
    else if (status === 'SKIP') testResults.skipped++;

    testResults.details.push({ category, name, status, details });
    logTest(name, status, details);
}

// File system based tests
function fileExists(filePath) {
    return fs.existsSync(path.join(TEST_CONFIG.baseDir, filePath));
}

function readFile(filePath) {
    try {
        return fs.readFileSync(path.join(TEST_CONFIG.baseDir, filePath), 'utf8');
    } catch (error) {
        return null;
    }
}

// Test: All pages exist
function testPagesExist() {
    logSection('1. PAGE EXISTENCE TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const exists = fileExists(page);
        recordTest(
            'Page Existence',
            `${page} exists`,
            exists ? 'PASS' : 'FAIL',
            exists ? `File found at ${page}` : `File not found: ${page}`
        );
    });
}

// Test: Required files exist
function testRequiredFiles() {
    logSection('2. REQUIRED FILES TESTS');

    const requiredFiles = [
        { path: 'css/styles.css', name: 'Main stylesheet' },
        { path: 'js/main.js', name: 'Main JavaScript file' }
    ];

    requiredFiles.forEach(file => {
        const exists = fileExists(file.path);
        recordTest(
            'Required Files',
            `${file.name} exists`,
            exists ? 'PASS' : 'FAIL',
            exists ? `Found: ${file.path}` : `Missing: ${file.path}`
        );
    });
}

// Test: HTML structure and validity
function testHTMLStructure() {
    logSection('3. HTML STRUCTURE TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) {
            recordTest('HTML Structure', `${page} structure`, 'FAIL', 'Could not read file');
            return;
        }

        // Check for doctype
        const hasDoctype = content.trim().toLowerCase().startsWith('<!doctype html>');
        recordTest(
            'HTML Structure',
            `${page} has DOCTYPE`,
            hasDoctype ? 'PASS' : 'FAIL',
            hasDoctype ? 'Valid HTML5 DOCTYPE' : 'Missing DOCTYPE'
        );

        // Check for required meta tags
        const hasViewport = content.includes('name="viewport"');
        recordTest(
            'HTML Structure',
            `${page} has viewport meta`,
            hasViewport ? 'PASS' : 'FAIL',
            hasViewport ? 'Viewport meta tag found' : 'Missing viewport meta tag'
        );

        // Check for charset
        const hasCharset = content.includes('charset="UTF-8"') || content.includes("charset='UTF-8'");
        recordTest(
            'HTML Structure',
            `${page} has charset`,
            hasCharset ? 'PASS' : 'FAIL',
            hasCharset ? 'UTF-8 charset declared' : 'Missing charset declaration'
        );
    });
}

// Test: Navigation links
function testNavigation() {
    logSection('4. NAVIGATION TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) {
            recordTest('Navigation', `${page} navigation`, 'FAIL', 'Could not read file');
            return;
        }

        // Check for header
        const hasHeader = content.includes('class="header"');
        recordTest(
            'Navigation',
            `${page} has header`,
            hasHeader ? 'PASS' : 'FAIL',
            hasHeader ? 'Header element found' : 'Header element missing'
        );

        // Check for navigation menu
        const hasNav = content.includes('class="main-nav"') || content.includes('class="nav-menu"');
        recordTest(
            'Navigation',
            `${page} has navigation menu`,
            hasNav ? 'PASS' : 'FAIL',
            hasNav ? 'Navigation menu found' : 'Navigation menu missing'
        );

        // Check for mobile menu
        const hasMobileNav = content.includes('class="mobile-nav"') || content.includes('mobile-menu-toggle');
        recordTest(
            'Navigation',
            `${page} has mobile navigation`,
            hasMobileNav ? 'PASS' : 'FAIL',
            hasMobileNav ? 'Mobile navigation found' : 'Mobile navigation missing'
        );

        // Check nav links point to valid pages
        const navLinkPattern = /href=["'](index|services|calculator|reviews|faq|about|quote|blog)\.html["']/g;
        const navLinks = content.match(navLinkPattern) || [];
        const validLinks = navLinks.every(link => {
            const pageName = link.match(/href=["']([^"']+)["']/)[1];
            return TEST_CONFIG.pages.includes(pageName);
        });

        recordTest(
            'Navigation',
            `${page} navigation links are valid`,
            validLinks || navLinks.length === 0 ? 'PASS' : 'FAIL',
            `Found ${navLinks.length} navigation links`
        );
    });
}

// Test: Forms
function testForms() {
    logSection('5. FORM TESTS');

    // Test contact form on all pages (modal)
    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) return;

        const hasContactModal = content.includes('id="contactModal"');
        const hasContactForm = content.includes('id="contactForm"');

        recordTest(
            'Forms',
            `${page} has contact modal`,
            hasContactModal ? 'PASS' : 'FAIL',
            hasContactModal ? 'Contact modal found' : 'Contact modal missing'
        );

        if (hasContactForm) {
            // Check for required form fields
            const requiredFields = [
                { field: 'firstName', name: 'First Name' },
                { field: 'lastName', name: 'Last Name' },
                { field: 'email', name: 'Email' },
                { field: 'phone', name: 'Phone' },
                { field: 'service', name: 'Service' }
            ];

            requiredFields.forEach(({ field, name }) => {
                const hasField = content.includes(`id="${field}"`);
                recordTest(
                    'Forms',
                    `${page} contact form has ${name} field`,
                    hasField ? 'PASS' : 'FAIL',
                    hasField ? `${name} field found` : `${name} field missing`
                );
            });
        }
    });

    // Test calculator on calculator.html
    const calculatorContent = readFile('calculator.html');
    if (calculatorContent) {
        const hasCalculator = calculatorContent.includes('id="calculateBtn"');
        recordTest(
            'Forms',
            'Calculator page has calculator',
            hasCalculator ? 'PASS' : 'FAIL',
            hasCalculator ? 'Calculator found' : 'Calculator missing'
        );

        if (hasCalculator) {
            const calculatorFields = [
                { field: 'roofSize', name: 'Roof Size' },
                { field: 'roofType', name: 'Roof Type' },
                { field: 'material', name: 'Material' },
                { field: 'layers', name: 'Layers' }
            ];

            calculatorFields.forEach(({ field, name }) => {
                const hasField = calculatorContent.includes(`id="${field}"`);
                recordTest(
                    'Forms',
                    `Calculator has ${name} field`,
                    hasField ? 'PASS' : 'FAIL',
                    hasField ? `${name} field found` : `${name} field missing`
                );
            });
        }
    }
}

// Test: JavaScript functionality references
function testJavaScript() {
    logSection('6. JAVASCRIPT TESTS');

    const jsContent = readFile('js/main.js');
    if (!jsContent) {
        recordTest('JavaScript', 'Main JavaScript file', 'FAIL', 'Could not read main.js');
        return;
    }

    const jsFeatures = [
        { pattern: 'initSmoothScrolling', name: 'Smooth scrolling' },
        { pattern: 'initScrollEffects', name: 'Scroll effects' },
        { pattern: 'initMobileMenu', name: 'Mobile menu' },
        { pattern: 'initFAQ', name: 'FAQ accordion' },
        { pattern: 'initCalculator', name: 'Calculator' },
        { pattern: 'initLiveChat', name: 'Live chat' },
        { pattern: 'initBackToTop', name: 'Back to top button' },
        { pattern: 'contactForm', name: 'Form validation' }
    ];

    jsFeatures.forEach(({ pattern, name }) => {
        const hasFeature = jsContent.includes(pattern);
        recordTest(
            'JavaScript',
            `${name} initialized`,
            hasFeature ? 'PASS' : 'FAIL',
            hasFeature ? `${name} function found` : `${name} function missing`
        );
    });

    // Check for no console.log in production
    const hasConsoleLogs = jsContent.match(/console\.(log|warn|error|debug)/g);
    if (hasConsoleLogs && hasConsoleLogs.length > 1) {
        recordTest(
            'JavaScript',
            'No debug console logs',
            'FAIL',
            `Found ${hasConsoleLogs.length} console statements (should be removed for production)`
        );
    } else {
        recordTest(
            'JavaScript',
            'No debug console logs',
            'PASS',
            'Clean production code'
        );
    }
}

// Test: Content sections
function testContent() {
    logSection('7. CONTENT TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) return;

        // Check for page title
        const titleMatch = content.match(/<title>(.*?)<\/title>/);
        const hasValidTitle = titleMatch && titleMatch[1] && titleMatch[1] !== 'Document' && titleMatch[1].trim() !== '';
        recordTest(
            'Content',
            `${page} has valid title`,
            hasValidTitle ? 'PASS' : 'FAIL',
            hasValidTitle ? `Title: "${titleMatch[1]}"` : 'Invalid or missing title'
        );

        // Check for placeholder text
        const placeholders = ['Lorem ipsum', 'Placeholder', 'TODO:', 'FIXME:', 'XXX'];
        const foundPlaceholders = placeholders.filter(p => content.includes(p));
        recordTest(
            'Content',
            `${page} has no placeholder text`,
            foundPlaceholders.length === 0 ? 'PASS' : 'FAIL',
            foundPlaceholders.length > 0 ? `Found: ${foundPlaceholders.join(', ')}` : 'No placeholder text'
        );

        // Check for footer
        const hasFooter = content.includes('class="footer"');
        recordTest(
            'Content',
            `${page} has footer`,
            hasFooter ? 'PASS' : 'FAIL',
            hasFooter ? 'Footer found' : 'Footer missing'
        );
    });
}

// Test: Links and CTAs
function testLinks() {
    logSection('8. LINK & CTA TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) return;

        // Check for CTA buttons
        const hasCTA = content.includes('class="cta-button"') || content.includes('class="btn-primary"');
        recordTest(
            'Links & CTAs',
            `${page} has CTA buttons`,
            hasCTA ? 'PASS' : 'FAIL',
            hasCTA ? 'CTA buttons found' : 'No CTA buttons found'
        );

        // Check for phone number
        const hasPhone = content.includes('(862) 224-6666');
        recordTest(
            'Links & CTAs',
            `${page} displays phone number`,
            hasPhone ? 'PASS' : 'FAIL',
            hasPhone ? 'Phone number displayed' : 'Phone number missing'
        );

        // Check for email
        const hasEmail = content.includes('info@randeroofing.com');
        recordTest(
            'Links & CTAs',
            `${page} displays email`,
            hasEmail ? 'PASS' : 'FAIL',
            hasEmail ? 'Email address displayed' : 'Email address missing'
        );
    });

    // Check index.html for service cards
    const indexContent = readFile('index.html');
    if (indexContent) {
        const hasServiceCards = indexContent.includes('class="explore-card"');
        recordTest(
            'Links & CTAs',
            'Homepage has service cards',
            hasServiceCards ? 'PASS' : 'FAIL',
            hasServiceCards ? 'Service cards found' : 'Service cards missing'
        );
    }
}

// Test: Responsive design elements
function testResponsive() {
    logSection('9. RESPONSIVE DESIGN TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) return;

        // Check for mobile menu toggle
        const hasMobileToggle = content.includes('class="mobile-menu-toggle"');
        recordTest(
            'Responsive',
            `${page} has mobile menu toggle`,
            hasMobileToggle ? 'PASS' : 'FAIL',
            hasMobileToggle ? 'Mobile toggle found' : 'Mobile toggle missing'
        );

        // Check for mobile nav
        const hasMobileNav = content.includes('class="mobile-nav"');
        recordTest(
            'Responsive',
            `${page} has mobile navigation`,
            hasMobileNav ? 'PASS' : 'FAIL',
            hasMobileNav ? 'Mobile navigation found' : 'Mobile navigation missing'
        );
    });
}

// Test: SEO elements
function testSEO() {
    logSection('10. SEO TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) return;

        // Check for meta description
        const hasMetaDesc = content.includes('name="description"');
        recordTest(
            'SEO',
            `${page} has meta description`,
            hasMetaDesc ? 'PASS' : 'FAIL',
            hasMetaDesc ? 'Meta description found' : 'Meta description missing'
        );

        // Check for Open Graph tags (on key pages)
        if (page === 'index.html') {
            const hasOG = content.includes('property="og:title"');
            recordTest(
                'SEO',
                `${page} has Open Graph tags`,
                hasOG ? 'PASS' : 'FAIL',
                hasOG ? 'Open Graph tags found' : 'Open Graph tags missing'
            );
        }
    });
}

// Test: Accessibility
function testAccessibility() {
    logSection('11. ACCESSIBILITY TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) return;

        // Check for lang attribute
        const hasLang = content.includes('lang="en"');
        recordTest(
            'Accessibility',
            `${page} has lang attribute`,
            hasLang ? 'PASS' : 'FAIL',
            hasLang ? 'Language attribute set' : 'Language attribute missing'
        );

        // Check for aria-labels on interactive elements
        const hasAriaLabels = content.includes('aria-label');
        recordTest(
            'Accessibility',
            `${page} uses ARIA labels`,
            hasAriaLabels ? 'PASS' : 'FAIL',
            hasAriaLabels ? 'ARIA labels found' : 'Consider adding ARIA labels'
        );

        // Check for alt text on images (basic check)
        const imgTags = content.match(/<img[^>]+>/g) || [];
        const imgsWithoutAlt = imgTags.filter(img => !img.includes('alt='));
        recordTest(
            'Accessibility',
            `${page} images have alt text`,
            imgsWithoutAlt.length === 0 ? 'PASS' : 'FAIL',
            imgsWithoutAlt.length > 0 ? `${imgsWithoutAlt.length} images missing alt text` : 'All images have alt text'
        );
    });
}

// Test: Live chat widget
function testLiveChat() {
    logSection('12. LIVE CHAT WIDGET TESTS');

    TEST_CONFIG.pages.forEach(page => {
        const content = readFile(page);
        if (!content) return;

        const hasLiveChat = content.includes('class="live-chat"') || content.includes('id="liveChat"');
        recordTest(
            'Live Chat',
            `${page} has live chat widget`,
            hasLiveChat ? 'PASS' : 'FAIL',
            hasLiveChat ? 'Live chat widget found' : 'Live chat widget missing'
        );

        if (hasLiveChat) {
            const chatElements = [
                { pattern: 'chat-toggle', name: 'Chat toggle button' },
                { pattern: 'chat-window', name: 'Chat window' },
                { pattern: 'chatInput', name: 'Chat input field' },
                { pattern: 'chat-send', name: 'Chat send button' }
            ];

            chatElements.forEach(({ pattern, name }) => {
                const hasElement = content.includes(pattern);
                recordTest(
                    'Live Chat',
                    `${page} has ${name}`,
                    hasElement ? 'PASS' : 'FAIL',
                    hasElement ? `${name} found` : `${name} missing`
                );
            });
        }
    });
}

// Test: FAQ page specific
function testFAQPage() {
    logSection('13. FAQ PAGE SPECIFIC TESTS');

    const faqContent = readFile('faq.html');
    if (!faqContent) {
        recordTest('FAQ Page', 'FAQ page exists', 'FAIL', 'Could not read faq.html');
        return;
    }

    const hasFAQItems = faqContent.includes('class="faq-item"');
    recordTest(
        'FAQ Page',
        'FAQ page has FAQ items',
        hasFAQItems ? 'PASS' : 'FAIL',
        hasFAQItems ? 'FAQ items found' : 'FAQ items missing'
    );

    if (hasFAQItems) {
        const hasFAQQuestion = faqContent.includes('class="faq-question"');
        const hasFAQAnswer = faqContent.includes('class="faq-answer"');

        recordTest(
            'FAQ Page',
            'FAQ items have questions',
            hasFAQQuestion ? 'PASS' : 'FAIL',
            hasFAQQuestion ? 'FAQ questions found' : 'FAQ questions missing'
        );

        recordTest(
            'FAQ Page',
            'FAQ items have answers',
            hasFAQAnswer ? 'PASS' : 'FAIL',
            hasFAQAnswer ? 'FAQ answers found' : 'FAQ answers missing'
        );
    }
}

// Generate summary report
function generateSummary() {
    logSection('TEST SUMMARY');

    const passRate = testResults.total > 0
        ? ((testResults.passed / testResults.total) * 100).toFixed(1)
        : 0;

    console.log('');
    log(`  Total Tests:    ${testResults.total}`, 'white');
    log(`  Passed:         ${testResults.passed} (${passRate}%)`, 'green');
    log(`  Failed:         ${testResults.failed}`, testResults.failed > 0 ? 'red' : 'white');
    log(`  Skipped:        ${testResults.skipped}`, testResults.skipped > 0 ? 'yellow' : 'white');
    console.log('');

    if (testResults.failed === 0) {
        log('  🎉 ALL TESTS PASSED! 🎉', 'green');
    } else {
        log('  ⚠️  SOME TESTS FAILED', 'red');
        console.log('');
        log('  Failed Tests:', 'red');
        testResults.details
            .filter(t => t.status === 'FAIL')
            .forEach(test => {
                log(`    • ${test.name}`, 'red');
                if (test.details) {
                    log(`      ${test.details}`, 'dim');
                }
            });
    }

    console.log('\n' + '='.repeat(60) + '\n');
}

// Export results to JSON
function exportResults() {
    const report = {
        timestamp: new Date().toISOString(),
        summary: {
            total: testResults.total,
            passed: testResults.passed,
            failed: testResults.failed,
            skipped: testResults.skipped,
            passRate: ((testResults.passed / testResults.total) * 100).toFixed(1) + '%'
        },
        results: testResults.details
    };

    const filename = `test-results-${Date.now()}.json`;
    fs.writeFileSync(path.join(TEST_CONFIG.baseDir, filename), JSON.stringify(report, null, 2));
    log(`\nTest results exported to: ${filename}`, 'cyan');
}

// Main test runner
function runAllTests() {
    log('\n' + '█'.repeat(60), 'cyan');
    log('█' + ' '.repeat(58) + '█', 'cyan');
    log('█  R&E ROOFING - COMPREHENSIVE TEST SUITE                  █', 'cyan');
    log('█  Testing all 8 pages for functionality and quality      █', 'cyan');
    log('█' + ' '.repeat(58) + '█', 'cyan');
    log('█'.repeat(60), 'cyan');
    log(`\nStarted: ${new Date().toLocaleString()}`, 'dim');

    testPagesExist();
    testRequiredFiles();
    testHTMLStructure();
    testNavigation();
    testForms();
    testJavaScript();
    testContent();
    testLinks();
    testResponsive();
    testSEO();
    testAccessibility();
    testLiveChat();
    testFAQPage();

    generateSummary();
    exportResults();

    process.exit(testResults.failed > 0 ? 1 : 0);
}

// Run tests
runAllTests();