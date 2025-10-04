# R&E Roofing Website

A professional, responsive website for R&E Roofing featuring roofing, siding, and gutter services. Optimized for SEO, performance, and user experience.

## Current Site Structure

This site is **in transition from single-page to multi-page** structure:

```
/
├── index.html              # Homepage with all sections (~32KB)
├── services.html           # Services detail page (exists)
├── index-old.html          # Backup of previous version
├── test-redirect.html      # Testing file for redirects
├── css/
│   └── styles.css          # All CSS styles (~33KB)
├── js/
│   └── main.js             # JavaScript functionality (~17KB)
├── images/                 # Image assets
│   ├── icon-siding.svg
│   ├── icon-roofing.svg
│   ├── icon-gutters.svg
│   └── (other images)
├── videos/                 # Video assets
├── deploy.sh               # Deployment script
├── .gitignore
├── robots.txt
└── sitemap.xml
```

### Navigation Structure (Multi-Page Ready)
Navigation now points to separate pages:
- `index.html` - Home
- `services.html` - Services (✅ exists)
- `about.html` - About (⚠️ needs creation)
- `reviews.html` - Reviews (⚠️ needs creation)
- `blog.html` - Blog (⚠️ needs creation)
- `calculator.html` - Calculator (⚠️ needs creation)
- `faq.html` - FAQ (⚠️ needs creation)

### Current Page Content

**index.html** (Homepage) includes these sections:
1. **Hero Section** - Video background with primary CTA
2. **Explore Services** - Three service cards (Siding, Roofing, Gutters)
3. **Why Choose Us** - Feature grid with 4 benefits
4. **Footer** - Contact info and branding
5. **Contact Modal** - Quote request form (modal overlay)
6. **Live Chat Widget** - Floating chat button

**services.html** exists (needs review for content)

**Missing pages** that navigation links to:
- `about.html` - Company info and process
- `reviews.html` - Customer testimonials
- `blog.html` - Blog/news section
- `calculator.html` - Roofing cost calculator
- `faq.html` - Frequently asked questions

## Features

### Core Functionality
- **Responsive Design**: Mobile-first with breakpoints at 480px, 768px, 1024px
- **Interactive Elements**:
  - Contact form modal
  - Live chat widget
  - Roofing cost calculator
  - FAQ accordion
  - Mobile hamburger menu
  - Back-to-top button
- **SEO Optimized**:
  - Structured data (Local Business schema)
  - Open Graph and Twitter Card meta tags
  - Semantic HTML5 markup
- **Performance**:
  - Video background with fallback
  - Lazy loading ready
  - Optimized asset loading

### Backward Compatibility
The site includes redirect logic for old anchor-based URLs:
```javascript
// Redirects old anchor URLs to new multi-page structure
#services   → services.html
#calculator → calculator.html
#reviews    → reviews.html
#faq        → faq.html
#about      → about.html
```
This ensures old bookmarks/links still work during the transition.

## Running the Site Locally

### Option 1: Simple HTTP Server (Python)
```bash
cd "/Users/charwinvanryckdegroot/Downloads/R&E Roofing"
python3 -m http.server 8000
```
Open: http://localhost:8000

### Option 2: Node.js HTTP Server
```bash
cd "/Users/charwinvanryckdegroot/Downloads/R&E Roofing"
npx http-server -p 8000
```
Open: http://localhost:8000

### Option 3: VS Code Live Server
1. Install "Live Server" extension
2. Right-click `index.html`
3. Select "Open with Live Server"

## Updating Navigation

**CRITICAL**: Navigation is duplicated in **multiple locations** and must be kept synchronized:

### 1. Desktop Navigation (index.html lines ~185-200)
```html
<nav class="main-nav">
    <ul class="nav-menu">
        <li><a href="index.html" class="nav-link">Home</a></li>
        <li class="has-dropdown">
            <a href="services.html" class="nav-link">Services <i class="fas fa-chevron-down"></i></a>
            <ul class="dropdown-menu">
                <li><a href="services.html">All Services</a></li>
                <li><a href="calculator.html">Get Quote</a></li>
                <li><a href="faq.html">FAQs</a></li>
            </ul>
        </li>
        <li><a href="about.html" class="nav-link">About</a></li>
        <li><a href="reviews.html" class="nav-link">Reviews</a></li>
        <li><a href="blog.html" class="nav-link">Blog</a></li>
    </ul>
</nav>
```

### 2. Mobile Navigation (index.html lines ~220-238)
```html
<div class="mobile-nav">
    <ul class="mobile-nav-menu">
        <li><a href="index.html" class="mobile-nav-link">Home</a></li>
        <!-- Must mirror desktop navigation -->
    </ul>
</div>
```

### 3. Other HTML Pages
Each page (`services.html`, `about.html`, etc.) will need the same navigation header.

### 4. Service Card Links
In the "Explore Services" section, update "Learn More" buttons:
```html
<a href="services.html" class="btn-learn-more">Learn More</a>
```

**To update navigation across all pages:**
1. Edit desktop navigation in index.html
2. Copy exact same changes to mobile navigation in index.html
3. Copy the entire header to all other HTML pages
4. Update service card links if needed
5. Test navigation on all pages
6. Verify mobile menu hamburger works
7. Test dropdown menus on desktop

## Shared Components

These components should be **identical across all pages**:

### Header Navigation (~lines 153-238 in index.html)
Contains:
- Logo (`R&E ROOFING`)
- Desktop navigation menu with dropdown
- Mobile hamburger toggle
- Phone number display: `(862) 224-6666`
- "Get Free Quote" CTA button
- Mobile navigation drawer (hidden by default)

**Must copy to**: Every HTML page
**Files needing this**: `index.html`, `services.html`, and all future pages

### Contact Modal (~lines 91-150 in index.html)
Full-screen modal overlay with contact form:
- Form fields: First name, Last name, Email, Phone, Service type, Address, Message
- Radio buttons for preferred contact method
- Form validation handled in `js/main.js`
- "Get My Free Quote" submit button

**Must copy to**: Every HTML page (so modal works site-wide)
**Trigger**: Any `.cta-button` or `.btn-primary` button

### Footer (~lines 617-646 in index.html)
Contains:
- Company logo and tagline
- Contact information (phone, email)
- Copyright notice: `© 2024 R&E Roofing`

**Must copy to**: Every HTML page
**Update**: Copyright year annually

### Live Chat Widget (~lines 651-674 in index.html)
Floating chat button with expandable chat window (UI-only, not connected).

**Must copy to**: Every HTML page (optional)
**Location**: Before closing `</body>` tag

### Back to Top Button (~line 677-679 in index.html)
Floating button that scrolls to page top.

**Must copy to**: Every HTML page
**Functionality**: Handled in `js/main.js`

## Customization Guide

### Update Contact Information
Search and replace in `index.html`:
- **Phone**: `(862) 224-6666`
- **Email**: `info@randeroofing.com`
- **Address**: Update in structured data (lines 37-44)

### Update Colors
Edit CSS variables in `css/styles.css`:
```css
:root {
    --primary-color: #000000;      /* Black */
    --accent-color: #FF6B35;       /* Orange */
    --secondary-color: #FFFFFF;    /* White */
    --text-color: #333333;         /* Dark gray */
}
```

### Update Services
Edit the service cards in `index.html` (lines 241-295):
```html
<div class="explore-card card-siding">
    <div class="explore-icon">
        <img src="images/icon-siding.svg" alt="...">
    </div>
    <h3>Service Name</h3>
    <p>Service description...</p>
    <a href="#" class="btn-learn-more">Learn More</a>
</div>
```

### Update Calculator Pricing
Edit pricing logic in `js/main.js` (search for "calculateEstimate" function):
```javascript
// Material costs per square foot
const materialCosts = {
    asphalt: [3, 5],
    architectural: [4, 7],
    metal: [7, 12],
    tile: [8, 15],
    slate: [15, 25]
};
```

## Adding a New Page (Completing Multi-Page Conversion)

The site navigation is already configured for multi-page structure. To add missing pages:

### Step-by-Step Process

**1. Copy the Template**
```bash
cp index.html about.html  # Example: creating about.html
```

**2. Update Page-Specific Content**
Open the new file and modify:
```html
<!-- Update title tag -->
<title>About R&E Roofing - 25+ Years of Excellence</title>

<!-- Update meta description -->
<meta name="description" content="Learn about R&E Roofing's 25+ years...">

<!-- Keep: Header, Footer, Modal, LiveChat, CSS/JS links -->
<!-- Remove: All sections except the one you need -->
<!-- Add: New page-specific content -->
```

**3. Update Canonical URL**
```html
<link rel="canonical" href="https://reroofing.com/about.html">
```

**4. Update Open Graph URLs**
```html
<meta property="og:url" content="https://reroofing.com/about.html">
```

**5. Verify Shared Components Are Present**
Every page must include:
- Header with navigation (lines 153-238 from index.html)
- Contact modal (lines 91-150)
- Footer (lines 617-646)
- Live chat widget (optional)
- Back to top button
- Links to `css/styles.css` and `js/main.js`

**6. Test the New Page**
- [ ] Opens without errors
- [ ] Navigation links work (to/from other pages)
- [ ] Contact modal opens and closes
- [ ] Mobile menu works
- [ ] All CSS styles load correctly
- [ ] JavaScript functions work (forms, calculator, etc.)

**7. Update sitemap.xml**
Add new page entry:
```xml
<url>
    <loc>https://reroofing.com/about.html</loc>
    <lastmod>2025-09-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
</url>
```

### Pages Still Needed

Based on current navigation, create these pages:

**Priority 1 (Navigation links exist)**
- `about.html` - Company info, process, team
- `reviews.html` - Customer testimonials
- `calculator.html` - Roofing cost calculator
- `faq.html` - Frequently asked questions
- `blog.html` - Blog/news listing

**Content Sources**
The old single-page version (`index-old.html`) may contain content for:
- Calculator section → `calculator.html`
- Reviews section → `reviews.html`
- FAQ section → `faq.html`
- Process section → `about.html`

**Template for New Pages**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Copy entire <head> from index.html -->
    <!-- Update title, description, canonical URL, og:url -->
</head>
<body>
    <!-- Contact Modal (lines 91-150 from index.html) -->

    <!-- Header (lines 153-238 from index.html) -->

    <!-- Your Page-Specific Content Here -->
    <section class="page-content">
        <div class="container">
            <h1>Page Title</h1>
            <!-- Your content -->
        </div>
    </section>

    <!-- Footer (lines 617-646 from index.html) -->

    <!-- Scripts and widgets -->
    <script src="js/main.js"></script>
    <!-- Live Chat Widget (optional) -->
    <!-- Back to Top Button -->
</body>
</html>
```

## File Sizes & Performance

Current file sizes:
- `index.html`: ~32KB (uncompressed)
- `css/styles.css`: ~33KB (uncompressed)
- `js/main.js`: ~17KB (uncompressed)

**Total page weight**: ~82KB (HTML/CSS/JS only)

### Performance Optimizations
- Enable Gzip compression (reduces by ~70%)
- Minify CSS/JS for production
- Optimize images (WebP format)
- Consider code splitting for multi-page version
- Use CDN for Font Awesome and Google Fonts

## Browser Support

Tested and working on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile Safari (iOS 13+)
- Chrome Mobile (Android 8+)

## Deployment

### Using Deploy Script
```bash
chmod +x deploy.sh
./deploy.sh
```

### Manual Deployment
1. Upload all files to web server via FTP/SFTP
2. Ensure file permissions are correct (644 for files, 755 for directories)
3. Test all functionality on live server
4. Configure SSL certificate
5. Point domain DNS to server

### Recommended Hosting
- Netlify (drag-and-drop deployment)
- Vercel (Git-based deployment)
- GitHub Pages (free for static sites)
- Traditional web hosting (cPanel, Plesk)

## SEO Checklist

- [x] Structured data (Local Business schema)
- [x] Open Graph meta tags
- [x] Twitter Card meta tags
- [x] Descriptive page title
- [x] Meta description
- [x] robots.txt file
- [x] sitemap.xml file
- [ ] Google Analytics tracking
- [ ] Google Search Console verification
- [ ] Bing Webmaster Tools verification

## Known Issues & Follow-ups

### Current
- Video background may not load on slow connections (fallback needed)
- Calculator results are estimates only (not connected to backend)
- Live chat is UI-only (needs integration with chat service)
- Contact form submits but doesn't send emails (needs backend)

### Future Enhancements
- Multi-page structure for better SEO
- Blog section for content marketing
- Project gallery with before/after photos
- Integration with CRM for lead management
- Email automation for quote requests
- Google Maps integration in footer
- Social media feed integration

## Form Submission

**Current Setup**: Forms are handled by JavaScript only (no backend).

**To Connect Forms**:
1. Add backend endpoint (PHP, Node.js, etc.)
2. Update form action in `js/main.js`
3. Implement email sending service
4. Add CAPTCHA for spam protection
5. Store submissions in database/CRM

Example PHP endpoint:
```php
// contact.php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);

    // Validate and sanitize
    $email = filter_var($data['email'], FILTER_SANITIZE_EMAIL);

    // Send email
    mail('info@randeroofing.com', 'New Quote Request', $message);

    echo json_encode(['success' => true]);
}
?>
```

## Support & Maintenance

### Regular Updates
- [ ] Update customer testimonials quarterly
- [ ] Check for broken links monthly
- [ ] Update pricing in calculator annually
- [ ] Refresh images and content as needed
- [ ] Monitor form submissions daily

### Technical Maintenance
- [ ] Check browser compatibility with new releases
- [ ] Update dependencies (Font Awesome, fonts)
- [ ] Monitor page speed (Google PageSpeed Insights)
- [ ] Check mobile usability (Google Mobile-Friendly Test)
- [ ] Review analytics for user behavior insights

## License

© 2024 R&E Roofing. All rights reserved.

---

**Last Updated**: September 30, 2025
**Version**: 1.0 (Single-page)