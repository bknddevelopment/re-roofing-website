const fs = require('fs');
const path = require('path');

// Find all HTML files (excluding test files)
const allFiles = fs.readdirSync('.');
const htmlFiles = allFiles.filter(file => {
    return file.endsWith('.html') &&
           !file.includes('test') &&
           file !== 'browser-test.html' &&
           file !== 'comprehensive-test-suite.html' &&
           file !== 'test-redirect.html';
});

console.log(`Found ${htmlFiles.length} HTML files to update`);

htmlFiles.forEach(file => {
    try {
        let content = fs.readFileSync(file, 'utf8');

        // Check if the file already has the mobile phone icon
        if (content.includes('mobile-phone-icon')) {
            console.log(`⏭️  Skipping ${file} - already has mobile phone icon`);
            return;
        }

        // Find the mobile menu toggle button and add the phone icon before it
        const originalToggle = `                    <!-- Mobile Menu Toggle -->
                    <button class="mobile-menu-toggle" aria-label="Toggle Menu">`;

        const newToggle = `                    <!-- Mobile Phone Icon (visible only on mobile) -->
                    <a href="tel:6672041609" class="mobile-phone-icon" aria-label="Call R&E Roofing">
                        <i class="fas fa-phone"></i>
                    </a>

                    <!-- Mobile Menu Toggle -->
                    <button class="mobile-menu-toggle" aria-label="Toggle Menu">`;

        // Replace the toggle button section
        if (content.includes(originalToggle)) {
            content = content.replace(originalToggle, newToggle);

            // Write the updated content back to the file
            fs.writeFileSync(file, content, 'utf8');
            console.log(`✅ Updated ${file}`);
        } else {
            console.log(`⚠️  Warning: Could not find mobile menu toggle in ${file}`);
        }

    } catch (error) {
        console.error(`❌ Error processing ${file}:`, error.message);
    }
});

console.log('\n✨ All files processed successfully!');
