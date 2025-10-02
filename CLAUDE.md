# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**R&E Roofing Website** - Static HTML/CSS/JS website for roofing contractor serving Essex County, NJ.

**Tech Stack:** Pure HTML5, CSS3, Vanilla JavaScript (no frameworks)
**Deployment:** GitHub Pages at `bknddevelopment.github.io/re-roofing-website`
**Business Contact:** (667) 204-1609 | info@randeroofing.com

**SEO Strategy:** 4-phase Essex County domination targeting 22 towns × 7 services = 154+ pages

---

## Core Architecture

### Site Structure Pattern
```
Static HTML Pages (154+ pages)
├── Core Pages (8): index, services, about, reviews, blog, calculator, faq, quote
├── Town Landing Pages (22): roofing-{town}-nj.html (Tier 1-3 priority)
└── Service × Location Matrix (124+): {service}-{town}-nj.html
    ├── Roof Repair (22 towns)
    ├── Roof Replacement (22 towns)
    ├── New Roof Installation (22 towns)
    ├── Siding Installation (22 towns)
    ├── Siding Repair (22 towns)
    ├── Gutter Installation (22 towns)
    └── Gutter Repair & Cleaning (22 towns)
```

### Shared Components (Must Stay Synchronized)
Every HTML page **must** include identical:
1. **Header/Navigation** - Desktop nav + mobile hamburger menu
2. **Contact Modal** - Full-screen overlay form (`#contactModal`)
3. **Footer** - Contact info, copyright, links to locations
4. **Live Chat Widget** - Floating chat button (UI only)
5. **Back to Top Button** - Floating scroll-to-top
6. **CSS/JS Links** - `css/styles.css` + `js/main.js`

**Critical:** When editing navigation, update BOTH desktop (`<nav class="main-nav">`) AND mobile (`<div class="mobile-nav">`) versions.

---

## Commands

### Development
```bash
# Serve locally (Python)
python3 -m http.server 8000
# Open: http://localhost:8000

# Serve locally (Node.js)
npx http-server -p 8000

# Validate HTML (if tidy installed)
tidy -q -e index.html
```

### Deployment
```bash
# Pre-deployment checks
./deploy.sh

# Git deployment to GitHub Pages
git add .
git commit -m "Your message"
git push origin main
```

### File Operations
```bash
# Count total HTML pages
ls -1 *.html | wc -l

# Find all service×location pages for a town
ls *-newark-nj.html

# Find all pages for a service
ls roof-repair-*.html
```

---

## SEO Architecture & Strategy

### URL Patterns (STRICT - DO NOT DEVIATE)
```
Town Pages:        /roofing-{town}-nj.html
Service Pages:     /{service}-{town}-nj.html

Examples:
  /roofing-newark-nj.html
  /roof-repair-montclair-nj.html
  /gutter-installation-bloomfield-nj.html
```

### Town Prioritization (SEO_STRATEGY.md)
**Tier 1 (High Priority):** Newark, East Orange, Irvington, Bloomfield, West Orange, Montclair, Belleville, Livingston, Nutley, Maplewood
**Tier 2:** Orange, South Orange, Millburn, Verona, Cedar Grove
**Tier 3:** Glen Ridge, Caldwell, West Caldwell, North Caldwell, Roseland, Essex Fells, Fairfield

### Required Schema Markup
Every page MUST include:
1. **RoofingContractor** schema with `areaServed` for all 22 Essex County towns
2. **Service** schema for service-specific pages
3. **FAQPage** schema for blog posts with FAQ sections
4. **BreadcrumbList** schema for navigation hierarchy

### Meta Tag Requirements
```html
<title>{Service/Location} | R&E Roofing | {CTA}</title>
<meta name="description" content="Professional {service} in {town}, NJ. Licensed & insured. 25+ years experience. Free estimates. Call (667) 204-1609.">
<link rel="canonical" href="https://reroofing.com/{page-url}">
```

### Content Differentiation Strategy
**Problem:** 154+ pages risk duplicate content penalties
**Solution:**
- Town pages: Mention specific neighborhoods, landmarks, local architecture
- Service pages: Vary intro paragraphs, highlight different benefits per town
- Use different testimonials per location
- Reference town-specific building codes/permit requirements
- Minimum 600-800 words for service pages, 1000-1500 for town pages

---

## Development Patterns

### Creating New Service × Location Pages
```bash
# 1. Copy template from existing page
cp roof-repair-newark-nj.html roof-repair-belleville-nj.html

# 2. Find/replace town name (case-sensitive)
sed -i '' 's/Newark/Belleville/g' roof-repair-belleville-nj.html

# 3. Update unique content:
#    - Meta description
#    - H1 and headers
#    - Neighborhoods list
#    - Local context paragraphs
#    - FAQ questions

# 4. Add to sitemap.xml
# 5. Test page loads and navigation works
```

### Sitemap Management
**Critical:** Every new page MUST be added to `sitemap.xml`
```xml
<url>
    <loc>https://www.reroofing.com/{page-name}.html</loc>
    <lastmod>YYYY-MM-DD</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8-0.9</priority>
</url>
```

Priority levels:
- Homepage: 1.0
- Services page: 0.9
- Service × Location pages: 0.9
- Town landing pages: 0.8
- Blog posts: 0.6-0.7
- Core pages (about, faq): 0.6-0.7

### Navigation Updates
When adding new pages to navigation:
1. Edit desktop nav in `index.html` (lines ~185-200)
2. Copy exact changes to mobile nav (lines ~220-238)
3. Replicate header to all other HTML pages
4. Test hamburger menu on mobile breakpoint (<768px)
5. Verify dropdown menus work on desktop

---

## Content Guidelines

### Phone Number & Contact Info
**Primary:** (667) 204-1609
**Email:** info@randeroofing.com
**Service Area:** All 22 Essex County towns

**Update locations:** Search/replace across all HTML files when contact info changes.

### Color Scheme
```css
/* From css/styles.css */
--primary-color: #000000;      /* Black */
--accent-color: #FF6B35;       /* Orange */
--secondary-color: #FFFFFF;    /* White */
--text-color: #333333;         /* Dark gray */
```

### Responsive Breakpoints
```css
Mobile:  < 768px
Tablet:  768px - 1024px
Desktop: > 1024px
```

### Image Requirements
- **Logo:** `images/logo.png` (header)
- **Favicon:** `images/favicon.ico`
- **Service Icons:** SVG format in `images/` (icon-roofing.svg, icon-siding.svg, icon-gutters.svg)
- **OG Images:** `images/og-image.jpg`, `images/twitter-card.jpg`

---

## SEO Implementation Phases

### Phase 1: Foundation (Weeks 1-2) ✅ COMPLETE
- Technical SEO audit
- Schema markup implementation
- Google Business Profile optimization
- Core page optimization
- Analytics setup

### Phase 2: Town Pages (Weeks 3-4) ✅ COMPLETE
- 10 Tier 1 town landing pages
- Unique 1000+ word content per town
- Internal linking structure

### Phase 3: Service × Location Matrix (Weeks 5-7) ✅ COMPLETE
- 70+ service × location pages (10 towns × 7 services)
- 600-800 word unique content
- Complete Tier 1 coverage

### Phase 4: Blog Infrastructure (Week 8) ✅ COMPLETE
- Blog listing page (`blog.html`)
- First blog post with schema
- Foundation for content marketing

### Phase 5-12: Content Marketing & Authority (ONGOING)
- 2-4 blog posts per month
- Link building and citations
- Review generation (target 50+ Google reviews)
- Social media presence

---

## Testing Checklist

Before committing new pages:
- [ ] Page loads without errors
- [ ] Navigation links work (all pages)
- [ ] Contact modal opens/closes
- [ ] Mobile menu hamburger works
- [ ] All CSS/JS files load
- [ ] Schema markup validates (Google Rich Results Test)
- [ ] No duplicate content warnings
- [ ] Meta description under 160 characters
- [ ] Title tag under 60 characters
- [ ] Canonical URL correct
- [ ] Internal links point to existing pages
- [ ] Added to sitemap.xml
- [ ] Responsive on mobile (< 768px)

---

## Common Tasks

### Adding a New Town to SEO Strategy
1. Create town landing page: `roofing-{town}-nj.html`
2. Research town demographics, neighborhoods, architecture
3. Write 1000+ unique words with local context
4. Create 7 service × location pages for that town
5. Add all 8 pages to sitemap.xml
6. Update `areaServed` schema on homepage if new town
7. Link from footer "Areas We Serve" section

### Creating Blog Posts
Location: `blog/` directory (future structure)
Current: Single blog post in `blog.html` as foundation

Requirements:
- Article schema markup
- FAQ schema for Q&A sections
- Internal links to service/location pages (3-5)
- 1500-2500 words
- 3-5 images with alt text
- Breadcrumb navigation
- Social sharing buttons

### Updating Contact Information
Files to update:
- All HTML files (header, footer, contact modal)
- Schema markup (all pages with RoofingContractor type)
- README.md
- robots.txt sitemap URL
- sitemap.xml domain

### Calculator Pricing Updates
Edit `js/main.js` → `calculateEstimate()` function:
```javascript
const materialCosts = {
    asphalt: [3, 5],
    architectural: [4, 7],
    metal: [7, 12],
    tile: [8, 15],
    slate: [15, 25]
};
```

---

## SEO Monitoring & KPIs

### Track Weekly
- Keyword rankings for top 20 keywords
- Google Business Profile insights
- Form submissions and phone calls

### Track Monthly
- Organic traffic (Google Analytics)
- Pages indexed (Google Search Console)
- Backlinks and referring domains
- Google reviews count and rating
- Conversion rate by traffic source

### Success Metrics (12-Month Goals)
- Rankings: Top 3 for "{service} {town}" in 10+ Essex County towns
- Traffic: 1,500+ organic sessions/month
- Leads: 100+ leads/month from organic search
- Authority: Domain Authority 40+
- Reviews: 200+ Google reviews

---

## Architecture Decisions

### Why Pure HTML Instead of Framework?
1. **SEO Priority:** Server-side rendering not needed; static HTML is fastest
2. **Simplicity:** No build process, easy to edit, GitHub Pages compatible
3. **Performance:** Zero JavaScript framework overhead, instant page loads
4. **Scalability:** Template-based approach handles 150+ pages efficiently

### Why Service × Location Matrix?
1. **Long-tail SEO:** Captures high-intent searches like "roof repair Newark NJ"
2. **Low competition:** Easier to rank than generic "roofing contractor NJ"
3. **Local relevance:** Matches user search intent for specific location + service
4. **Scalability:** 7 services × 22 towns = 154 high-value landing pages

### Why Duplicate Code vs. Components?
**Trade-off:** Code duplication in headers/footers across 154+ pages
**Rationale:**
- Static sites have no server-side includes
- Build process complexity not worth it for this scale
- Easy bulk updates via find/replace across files
- Performance: No client-side rendering needed

**When making header/footer changes:** Use multi-file editing or scripted find/replace.

---

## Known Constraints

1. **No Backend:** Forms submit client-side only (needs backend integration for production)
2. **No Build Process:** Manual HTML editing; no templating engine
3. **GitHub Pages:** Static hosting only; no server-side logic
4. **Domain:** Currently using GitHub Pages subdomain (production needs custom domain)
5. **Analytics:** Not yet integrated (needs Google Analytics 4 + Search Console)
6. **Blog:** Infrastructure exists but needs CMS or static site generator for scale

---

## Future Enhancements (Roadmap)

### Short-term (1-3 months)
- Complete Tier 2 and Tier 3 town pages (12 additional towns × 8 pages = 96 pages)
- Integrate contact form backend (PHP/Node.js endpoint)
- Add Google Analytics 4 and Google Tag Manager
- Launch blog with 8-16 posts
- Set up automated review requests

### Medium-term (3-6 months)
- Neighborhood-level pages for high-value areas (e.g., Ironbound-Newark, Upper Montclair)
- Before/after project gallery
- Video testimonials
- Google Maps integration
- CRM integration for lead management

### Long-term (6-12 months)
- Multi-language support (Spanish)
- Advanced blog with categories and tags
- Case studies section
- Online scheduling/booking system
- Live chat integration (currently UI-only)

---

## Reference Documents

- **SEO_STRATEGY.md** - Complete 4-phase SEO implementation plan
- **README.md** - General project documentation and setup
- **sitemap.xml** - All indexed pages (must stay updated)
- **Phase Reports** - PHASE2_COMPLETION_REPORT.md, PHASE3_COMPLETION_REPORT.md, etc.

---

## Critical Reminders

1. **Never edit just one page** - Shared components (header/footer/modal) must stay synchronized
2. **Always update sitemap.xml** when adding pages
3. **Unique content is mandatory** - Google penalizes duplicate content
4. **Test on mobile** - 60%+ traffic is mobile
5. **Schema validation** - Use Google Rich Results Test before deploying
6. **Phone number consistency** - (667) 204-1609 everywhere
7. **Town name spelling** - Match official municipality names exactly
8. **URL pattern compliance** - Never deviate from `{service}-{town}-nj.html` pattern

---

**Last Updated:** October 1, 2025
**Project Status:** Phase 4 Complete (Blog Infrastructure) | Phase 5-12 Ongoing (Content Marketing)
