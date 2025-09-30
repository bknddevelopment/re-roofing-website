/**
 * R&E Roofing Automated Test Suite
 * Tests all functionality of the single-page site
 */

const fs = require('fs');
const path = require('path');

// Color codes for terminal output
const colors = {
    reset: '\x1b[0m',
    green: '\x1b[32m',
    red: '\x1b[31m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    cyan: '\x1b[36m'
};

class TestSuite {
    constructor() {
        this.results = {
            passed: 0,
            failed: 0,
            tests: []
        };
        this.siteRoot = __dirname;
    }

    log(message, color = colors.reset) {
        console.log(`${color}${message}${colors.reset}`);
    }

    pass(testName) {
        this.results.passed++;
        this.results.tests.push({ name: testName, status: 'PASS' });
        this.log(`✓ ${testName}`, colors.green);
    }

    fail(testName, error) {
        this.results.failed++;
        this.results.tests.push({ name: testName, status: 'FAIL', error });
        this.log(`✗ ${testName}`, colors.red);
        if (error) this.log(`  Error: ${error}`, colors.red);
    }

    // Test 1: Check if all required files exist
    testFileStructure() {
        this.log('\n=== Testing File Structure ===', colors.cyan);

        const requiredFiles = [
            'index.html',
            'js/main.js',
            'css/styles.css',
            'images/icon-roofing.svg',
            'images/icon-siding.svg',
            'images/icon-gutters.svg'
        ];

        requiredFiles.forEach(file => {
            const filePath = path.join(this.siteRoot, file);
            if (fs.existsSync(filePath)) {
                this.pass(`File exists: ${file}`);
            } else {
                this.fail(`File exists: ${file}`, `File not found: ${filePath}`);
            }
        });
    }

    // Test 2: Validate HTML structure
    testHTMLStructure() {
        this.log('\n=== Testing HTML Structure ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        // Check for essential sections
        const sections = [
            { id: 'contactModal', desc: 'Contact Modal' },
            { id: 'home', desc: 'Hero Section' },
            { id: 'services', desc: 'Services Section' },
            { id: 'calculator', desc: 'Calculator Section' },
            { id: 'reviews', desc: 'Reviews Section' },
            { id: 'faq', desc: 'FAQ Section' },
            { id: 'about', desc: 'About/Process Section' }
        ];

        sections.forEach(section => {
            if (htmlContent.includes(`id="${section.id}"`)) {
                this.pass(`Section exists: ${section.desc}`);
            } else {
                this.fail(`Section exists: ${section.desc}`, `Section with id="${section.id}" not found`);
            }
        });

        // Check for navigation
        if (htmlContent.includes('class="nav-menu"')) {
            this.pass('Desktop navigation menu exists');
        } else {
            this.fail('Desktop navigation menu exists', 'nav-menu class not found');
        }

        if (htmlContent.includes('class="mobile-nav"')) {
            this.pass('Mobile navigation menu exists');
        } else {
            this.fail('Mobile navigation menu exists', 'mobile-nav class not found');
        }
    }

    // Test 3: Validate JavaScript functionality structure
    testJavaScriptStructure() {
        this.log('\n=== Testing JavaScript Structure ===', colors.cyan);

        const jsPath = path.join(this.siteRoot, 'js/main.js');
        const jsContent = fs.readFileSync(jsPath, 'utf8');

        const functions = [
            { name: 'initSmoothScrolling', desc: 'Smooth scrolling initialization' },
            { name: 'initScrollEffects', desc: 'Scroll effects initialization' },
            { name: 'initAnimations', desc: 'Animations initialization' },
            { name: 'initMobileMenu', desc: 'Mobile menu initialization' },
            { name: 'initFAQ', desc: 'FAQ accordion initialization' },
            { name: 'initCalculator', desc: 'Calculator initialization' },
            { name: 'initLiveChat', desc: 'Live chat initialization' },
            { name: 'initBackToTop', desc: 'Back to top button initialization' }
        ];

        functions.forEach(func => {
            if (jsContent.includes(`function ${func.name}(`)) {
                this.pass(`Function exists: ${func.desc}`);
            } else {
                this.fail(`Function exists: ${func.desc}`, `Function ${func.name} not found`);
            }
        });

        // Check for DOMContentLoaded
        if (jsContent.includes("DOMContentLoaded")) {
            this.pass('DOMContentLoaded event listener exists');
        } else {
            this.fail('DOMContentLoaded event listener exists', 'DOMContentLoaded not found');
        }
    }

    // Test 4: Validate form elements
    testFormElements() {
        this.log('\n=== Testing Form Elements ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        // Contact form fields
        const formFields = [
            { id: 'firstName', desc: 'First Name field' },
            { id: 'lastName', desc: 'Last Name field' },
            { id: 'email', desc: 'Email field' },
            { id: 'phone', desc: 'Phone field' },
            { id: 'service', desc: 'Service dropdown' },
            { id: 'address', desc: 'Address field' },
            { id: 'message', desc: 'Message textarea' }
        ];

        formFields.forEach(field => {
            if (htmlContent.includes(`id="${field.id}"`)) {
                this.pass(`Contact form field exists: ${field.desc}`);
            } else {
                this.fail(`Contact form field exists: ${field.desc}`, `Field id="${field.id}" not found`);
            }
        });

        // Calculator form fields
        const calcFields = [
            { id: 'roofSize', desc: 'Roof Size input' },
            { id: 'roofType', desc: 'Roof Type dropdown' },
            { id: 'material', desc: 'Material dropdown' },
            { id: 'layers', desc: 'Layers dropdown' },
            { id: 'calculateBtn', desc: 'Calculate button' }
        ];

        calcFields.forEach(field => {
            if (htmlContent.includes(`id="${field.id}"`)) {
                this.pass(`Calculator field exists: ${field.desc}`);
            } else {
                this.fail(`Calculator field exists: ${field.desc}`, `Field id="${field.id}" not found`);
            }
        });
    }

    // Test 5: Validate navigation links
    testNavigationLinks() {
        this.log('\n=== Testing Navigation Links ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        const navLinks = [
            { href: '#home', desc: 'Home link' },
            { href: '#services', desc: 'Services link' },
            { href: '#calculator', desc: 'Calculator link' },
            { href: '#reviews', desc: 'Reviews link' },
            { href: '#faq', desc: 'FAQ link' },
            { href: '#about', desc: 'About link' }
        ];

        navLinks.forEach(link => {
            if (htmlContent.includes(`href="${link.href}"`)) {
                this.pass(`Navigation link exists: ${link.desc}`);
            } else {
                this.fail(`Navigation link exists: ${link.desc}`, `Link href="${link.href}" not found`);
            }
        });
    }

    // Test 6: Validate interactive elements
    testInteractiveElements() {
        this.log('\n=== Testing Interactive Elements ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        const elements = [
            { selector: 'close-modal', desc: 'Modal close button' },
            { selector: 'cta-button', desc: 'CTA buttons' },
            { selector: 'mobile-menu-toggle', desc: 'Mobile menu toggle' },
            { selector: 'faq-question', desc: 'FAQ questions' },
            { selector: 'chat-toggle', desc: 'Live chat toggle' },
            { selector: 'backToTop', desc: 'Back to top button' }
        ];

        elements.forEach(element => {
            if (htmlContent.includes(element.selector)) {
                this.pass(`Interactive element exists: ${element.desc}`);
            } else {
                this.fail(`Interactive element exists: ${element.desc}`, `Element "${element.selector}" not found`);
            }
        });
    }

    // Test 7: Validate CSS file structure
    testCSSStructure() {
        this.log('\n=== Testing CSS File ===', colors.cyan);

        const cssPath = path.join(this.siteRoot, 'css/styles.css');

        try {
            const cssContent = fs.readFileSync(cssPath, 'utf8');

            if (cssContent.length > 0) {
                this.pass('CSS file exists and has content');
            } else {
                this.fail('CSS file exists and has content', 'CSS file is empty');
            }

            // Check for key selectors
            const selectors = [
                '.header',
                '.hero',
                '.modal',
                '.calculator-section',
                '.faq-section',
                '.mobile-nav'
            ];

            selectors.forEach(selector => {
                if (cssContent.includes(selector)) {
                    this.pass(`CSS selector exists: ${selector}`);
                } else {
                    this.fail(`CSS selector exists: ${selector}`, `Selector ${selector} not found in CSS`);
                }
            });
        } catch (error) {
            this.fail('CSS file accessible', error.message);
        }
    }

    // Test 8: Validate calculator logic
    testCalculatorLogic() {
        this.log('\n=== Testing Calculator Logic ===', colors.cyan);

        const jsPath = path.join(this.siteRoot, 'js/main.js');
        const jsContent = fs.readFileSync(jsPath, 'utf8');

        // Check for material costs
        if (jsContent.includes('materialCosts')) {
            this.pass('Material costs object exists');
        } else {
            this.fail('Material costs object exists', 'materialCosts not found');
        }

        // Check for complexity multiplier
        if (jsContent.includes('complexityMultiplier')) {
            this.pass('Complexity multiplier exists');
        } else {
            this.fail('Complexity multiplier exists', 'complexityMultiplier not found');
        }

        // Check for calculation variables
        const calcVars = ['lowEstimate', 'highEstimate', 'roofSize', 'roofType', 'material'];
        calcVars.forEach(varName => {
            if (jsContent.includes(varName)) {
                this.pass(`Calculator variable exists: ${varName}`);
            } else {
                this.fail(`Calculator variable exists: ${varName}`, `Variable ${varName} not found`);
            }
        });

        // Check for additional services checkboxes
        const services = ['gutters', 'ventilation', 'skylights', 'chimney'];
        services.forEach(service => {
            if (jsContent.includes(`getElementById('${service}')`)) {
                this.pass(`Additional service checkbox handled: ${service}`);
            } else {
                this.fail(`Additional service checkbox handled: ${service}`, `Service ${service} not found in JS`);
            }
        });
    }

    // Test 9: Validate FAQ structure
    testFAQStructure() {
        this.log('\n=== Testing FAQ Structure ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        // Count FAQ items
        const faqCount = (htmlContent.match(/class="faq-item"/g) || []).length;

        if (faqCount >= 5) {
            this.pass(`FAQ items exist (${faqCount} found)`);
        } else {
            this.fail(`FAQ items exist`, `Only ${faqCount} FAQ items found, expected at least 5`);
        }

        // Check for FAQ structure elements
        if (htmlContent.includes('faq-question') && htmlContent.includes('faq-answer')) {
            this.pass('FAQ question/answer structure exists');
        } else {
            this.fail('FAQ question/answer structure exists', 'FAQ structure incomplete');
        }
    }

    // Test 10: Validate modal structure
    testModalStructure() {
        this.log('\n=== Testing Modal Structure ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        if (htmlContent.includes('id="contactModal"')) {
            this.pass('Contact modal exists');
        } else {
            this.fail('Contact modal exists', 'contactModal id not found');
        }

        if (htmlContent.includes('class="modal-content"')) {
            this.pass('Modal content container exists');
        } else {
            this.fail('Modal content container exists', 'modal-content class not found');
        }

        if (htmlContent.includes('class="close-modal"')) {
            this.pass('Modal close button exists');
        } else {
            this.fail('Modal close button exists', 'close-modal class not found');
        }
    }

    // Test 11: Validate live chat structure
    testLiveChatStructure() {
        this.log('\n=== Testing Live Chat Structure ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        const chatElements = [
            { selector: 'id="liveChat"', desc: 'Live chat container' },
            { selector: 'class="chat-toggle"', desc: 'Chat toggle button' },
            { selector: 'class="chat-window"', desc: 'Chat window' },
            { selector: 'class="chat-header"', desc: 'Chat header' },
            { selector: 'class="chat-body"', desc: 'Chat body' },
            { selector: 'class="chat-footer"', desc: 'Chat footer' },
            { selector: 'id="chatInput"', desc: 'Chat input field' }
        ];

        chatElements.forEach(element => {
            if (htmlContent.includes(element.selector)) {
                this.pass(`Chat element exists: ${element.desc}`);
            } else {
                this.fail(`Chat element exists: ${element.desc}`, `${element.selector} not found`);
            }
        });
    }

    // Test 12: Validate meta tags for SEO
    testSEOElements() {
        this.log('\n=== Testing SEO Elements ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        const seoElements = [
            { tag: 'meta name="description"', desc: 'Meta description' },
            { tag: 'meta name="keywords"', desc: 'Meta keywords' },
            { tag: 'meta property="og:title"', desc: 'Open Graph title' },
            { tag: 'meta property="og:description"', desc: 'Open Graph description' },
            { tag: 'meta name="twitter:card"', desc: 'Twitter card' },
            { tag: 'application/ld+json', desc: 'Structured data (JSON-LD)' }
        ];

        seoElements.forEach(element => {
            if (htmlContent.includes(element.tag)) {
                this.pass(`SEO element exists: ${element.desc}`);
            } else {
                this.fail(`SEO element exists: ${element.desc}`, `${element.tag} not found`);
            }
        });
    }

    // Test 13: Validate responsive design elements
    testResponsiveElements() {
        this.log('\n=== Testing Responsive Design Elements ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        if (htmlContent.includes('meta name="viewport"')) {
            this.pass('Viewport meta tag exists');
        } else {
            this.fail('Viewport meta tag exists', 'Viewport meta tag not found');
        }

        if (htmlContent.includes('mobile-menu-toggle')) {
            this.pass('Mobile menu toggle exists');
        } else {
            this.fail('Mobile menu toggle exists', 'Mobile menu toggle not found');
        }

        if (htmlContent.includes('mobile-nav')) {
            this.pass('Mobile navigation exists');
        } else {
            this.fail('Mobile navigation exists', 'Mobile navigation not found');
        }
    }

    // Test 14: Check for external dependencies
    testExternalDependencies() {
        this.log('\n=== Testing External Dependencies ===', colors.cyan);

        const htmlPath = path.join(this.siteRoot, 'index.html');
        const htmlContent = fs.readFileSync(htmlPath, 'utf8');

        const dependencies = [
            { url: 'fonts.googleapis.com', desc: 'Google Fonts' },
            { url: 'font-awesome', desc: 'Font Awesome icons' }
        ];

        dependencies.forEach(dep => {
            if (htmlContent.includes(dep.url)) {
                this.pass(`External dependency loaded: ${dep.desc}`);
            } else {
                this.fail(`External dependency loaded: ${dep.desc}`, `${dep.url} not found`);
            }
        });
    }

    // Run all tests
    runAllTests() {
        this.log('\n╔════════════════════════════════════════════════════════╗', colors.blue);
        this.log('║     R&E ROOFING - COMPREHENSIVE TEST SUITE           ║', colors.blue);
        this.log('╚════════════════════════════════════════════════════════╝', colors.blue);

        try {
            this.testFileStructure();
            this.testHTMLStructure();
            this.testJavaScriptStructure();
            this.testFormElements();
            this.testNavigationLinks();
            this.testInteractiveElements();
            this.testCSSStructure();
            this.testCalculatorLogic();
            this.testFAQStructure();
            this.testModalStructure();
            this.testLiveChatStructure();
            this.testSEOElements();
            this.testResponsiveElements();
            this.testExternalDependencies();
        } catch (error) {
            this.log(`\nFATAL ERROR: ${error.message}`, colors.red);
            this.log(error.stack, colors.red);
        }

        this.printSummary();
    }

    // Print test summary
    printSummary() {
        this.log('\n╔════════════════════════════════════════════════════════╗', colors.blue);
        this.log('║                    TEST SUMMARY                       ║', colors.blue);
        this.log('╚════════════════════════════════════════════════════════╝', colors.blue);

        const total = this.results.passed + this.results.failed;
        const passRate = total > 0 ? ((this.results.passed / total) * 100).toFixed(1) : 0;

        this.log(`\nTotal Tests: ${total}`);
        this.log(`Passed: ${this.results.passed}`, colors.green);
        this.log(`Failed: ${this.results.failed}`, this.results.failed > 0 ? colors.red : colors.green);
        this.log(`Pass Rate: ${passRate}%`, passRate >= 90 ? colors.green : colors.yellow);

        if (this.results.failed > 0) {
            this.log('\n--- Failed Tests ---', colors.red);
            this.results.tests
                .filter(test => test.status === 'FAIL')
                .forEach(test => {
                    this.log(`  • ${test.name}`, colors.red);
                    if (test.error) this.log(`    ${test.error}`, colors.yellow);
                });
        }

        this.log('\n═══════════════════════════════════════════════════════\n', colors.blue);

        // Exit with appropriate code
        process.exit(this.results.failed > 0 ? 1 : 0);
    }
}

// Run the test suite
const testSuite = new TestSuite();
testSuite.runAllTests();