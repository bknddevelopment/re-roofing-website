#!/usr/bin/env python3
"""
Generate Phase 2: Material-Specific Roofing Pages
Creates 75 pages (5 materials × 15 Essex County towns)
"""

import os
from datetime import datetime

# 5 Roofing Materials with detailed specs
MATERIALS = {
    'asphalt-shingle': {
        'name': 'Asphalt Shingle',
        'title_suffix': 'Expert Installation',
        'lifespan': '15-30 years',
        'price_range': '$4,500 - $9,000',
        'best_for': 'homeowners seeking affordability and variety',
        'key_benefits': [
            'Most affordable roofing option',
            'Wide variety of colors and styles',
            '15-30 year lifespan with proper maintenance',
            'Easy to repair and replace individual shingles',
            'Proven performance in Essex County weather',
            'Quick installation (1-3 days typical)'
        ],
        'services': [
            'New asphalt shingle roof installation',
            'Architectural shingle upgrades',
            'Asphalt shingle roof replacement',
            'Storm damage repair',
            'Shingle replacement and patching',
            'Ventilation and underlayment upgrades'
        ],
        'faqs': [
            {
                'q': 'How long do asphalt shingles last in {town}?',
                'a': 'With proper installation and maintenance, asphalt shingles typically last 15-30 years in {town}, NJ. Essex County\'s weather patterns - including hot summers and cold winters - make quality installation and ventilation critical for maximizing lifespan.'
            },
            {
                'q': 'What\'s the cost of asphalt shingle roofing in {town}?',
                'a': 'Asphalt shingle roofing in {town} typically ranges from $4,500-$9,000 for an average home, depending on roof size, pitch, and shingle quality. We offer free estimates with transparent pricing and financing options.'
            },
            {
                'q': 'Can you match my current asphalt shingle color?',
                'a': 'Yes! We work with leading manufacturers offering 100+ color options. We can match your existing shingles or help you choose a new color that complements your {town} home\'s architecture.'
            },
            {
                'q': 'Do asphalt shingles work well in {town}\'s climate?',
                'a': 'Absolutely. Modern asphalt shingles are engineered for freeze-thaw cycles, high winds, and temperature extremes common in Essex County. We use wind-resistant shingles rated for {town}\'s weather conditions.'
            },
            {
                'q': 'How quickly can you install an asphalt shingle roof?',
                'a': 'Most asphalt shingle installations in {town} take 1-3 days, depending on roof complexity. We work efficiently while maintaining quality standards, and we always protect your property during the process.'
            }
        ],
        'description_template': 'Professional asphalt shingle roofing in {town}, NJ. Expert installation, repair & replacement. 25+ years experience. Wide variety of colors & styles. Licensed & insured. Free estimates. Call (667) 204-1609.'
    },
    'metal': {
        'name': 'Metal',
        'title_suffix': 'Premium Installation',
        'lifespan': '40-70 years',
        'price_range': '$12,000 - $25,000',
        'best_for': 'homeowners prioritizing longevity and energy efficiency',
        'key_benefits': [
            '40-70 year lifespan - lasts 2-3x longer than asphalt',
            'Energy efficient - reflects heat, lowers cooling costs',
            'Fire resistant and non-combustible',
            'Lightweight yet extremely durable',
            'Low maintenance and eco-friendly',
            'Modern aesthetic with variety of styles'
        ],
        'services': [
            'Standing seam metal roof installation',
            'Metal shingle and tile roofing',
            'Copper and zinc roofing systems',
            'Metal roof coating and restoration',
            'Fastener replacement and repairs',
            'Architectural metal roofing'
        ],
        'faqs': [
            {
                'q': 'How long do metal roofs last in {town}?',
                'a': 'Metal roofs in {town} typically last 40-70 years - often outlasting the building itself. With proper installation, metal roofing can withstand Essex County\'s harsh winters, summer heat, and severe storms for decades.'
            },
            {
                'q': 'Are metal roofs noisy during rain in {town}?',
                'a': 'No. Modern metal roofs with proper insulation and underlayment are actually quieter than asphalt shingles during {town}\'s rainstorms. Our installation includes sound-dampening materials for a peaceful interior.'
            },
            {
                'q': 'Will a metal roof lower my energy bills in {town}?',
                'a': 'Yes! Metal roofs reflect solar heat, reducing cooling costs by 10-25% during {town}\'s hot summers. Many {town} homeowners see ROI through energy savings within 10-15 years.'
            },
            {
                'q': 'What metal roofing styles are available for my {town} home?',
                'a': 'We offer standing seam, metal shingles, metal tiles, and corrugated panels in various colors and finishes. Our team helps {town} homeowners choose styles that complement traditional or modern architecture.'
            },
            {
                'q': 'Can you install metal roofing over my existing roof in {town}?',
                'a': 'In many {town} homes, yes - metal roofing can be installed over one layer of asphalt shingles, saving tear-off costs. We assess your roof structure to determine the best installation method.'
            }
        ],
        'description_template': 'Expert metal roofing in {town}, NJ. 40-70 year lifespan. Energy efficient & fire resistant. Standing seam, shingles & tiles. Licensed & insured. Free estimates. Call (667) 204-1609.'
    },
    'flat': {
        'name': 'Flat',
        'title_suffix': 'Commercial & Residential',
        'lifespan': '15-30 years',
        'price_range': '$8,000 - $18,000',
        'best_for': 'commercial buildings and modern residential designs',
        'key_benefits': [
            'TPO, EPDM, and PVC membrane options',
            'Ideal for commercial and modern homes',
            'Easier maintenance and equipment access',
            'Potential for rooftop gardens or solar panels',
            'Cost-effective for large surface areas',
            'Superior waterproofing technology'
        ],
        'services': [
            'TPO flat roof installation',
            'EPDM rubber roofing systems',
            'PVC membrane roofing',
            'Modified bitumen installation',
            'Flat roof leak repair',
            'Drainage system optimization'
        ],
        'faqs': [
            {
                'q': 'What type of flat roof is best for {town} commercial buildings?',
                'a': 'TPO and EPDM are most popular for {town} commercial properties. TPO offers energy efficiency and durability, while EPDM provides proven performance at lower cost. We assess your building and budget to recommend the optimal system.'
            },
            {
                'q': 'How do you prevent pooling water on flat roofs in {town}?',
                'a': 'Proper drainage is critical in {town}\'s climate. We design tapered insulation systems and install scuppers, drains, and gutters to ensure water flows off your flat roof efficiently, preventing leaks and extending roof life.'
            },
            {
                'q': 'Can I install solar panels on my {town} flat roof?',
                'a': 'Absolutely! Flat roofs in {town} are ideal for solar panel installation. We coordinate with solar installers or can integrate mounting systems during roof installation, ensuring proper waterproofing around penetrations.'
            },
            {
                'q': 'How long do flat roofs last in {town}?',
                'a': 'Flat roofing systems in {town} typically last 15-30 years depending on material and maintenance. TPO and PVC systems often reach 20-30 years, while EPDM averages 15-25 years with proper care.'
            },
            {
                'q': 'Do flat roofs require more maintenance in {town}?',
                'a': 'Flat roofs benefit from bi-annual inspections in {town} to clear debris, check drains, and inspect seams. Regular maintenance prevents small issues from becoming major leaks and maximizes your roof\'s lifespan.'
            }
        ],
        'description_template': 'Professional flat roofing in {town}, NJ. TPO, EPDM & PVC systems. Commercial & residential. Expert installation & repair. Licensed & insured. Free estimates. Call (667) 204-1609.'
    },
    'tile': {
        'name': 'Tile',
        'title_suffix': 'Mediterranean Elegance',
        'lifespan': '50-100 years',
        'price_range': '$15,000 - $30,000',
        'best_for': 'homeowners wanting Mediterranean style and exceptional longevity',
        'key_benefits': [
            '50-100 year lifespan - generational durability',
            'Mediterranean and Spanish architectural style',
            'Fire resistant (Class A rating)',
            'Energy efficient with natural ventilation',
            'Unmatched curb appeal and property value',
            'Clay and concrete tile options'
        ],
        'services': [
            'Clay tile roof installation',
            'Concrete tile roofing systems',
            'Spanish tile installation',
            'Tile roof repair and replacement',
            'Tile underlayment upgrades',
            'Custom tile color matching'
        ],
        'faqs': [
            {
                'q': 'How long do tile roofs last in {town}?',
                'a': 'Tile roofs in {town} can last 50-100 years or more - often outliving the homes they protect. Clay and concrete tiles withstand Essex County\'s freeze-thaw cycles, making them an excellent long-term investment for {town} homeowners.'
            },
            {
                'q': 'Are tile roofs too heavy for homes in {town}?',
                'a': 'Most {town} homes can support tile roofing with proper structural assessment. We evaluate your home\'s framing and can recommend reinforcement if needed. Many historic and newer {town} homes already have tile-ready structures.'
            },
            {
                'q': 'What tile roofing styles work best in {town}?',
                'a': 'Spanish barrel tiles and flat profile tiles are popular in {town}. We offer clay and concrete options in various colors. Our designers help match tiles to your home\'s architectural style, whether Mediterranean, Colonial, or contemporary.'
            },
            {
                'q': 'Can individual tiles be replaced if damaged in {town}?',
                'a': 'Yes! One advantage of tile roofing in {town} is that individual tiles damaged by storms or impacts can be easily replaced without replacing the entire roof. We stock matching tiles for quick repairs.'
            },
            {
                'q': 'Are tile roofs energy efficient for {town} homes?',
                'a': 'Very much so. Tile roofs naturally ventilate, keeping {town} homes cooler in summer. The thermal mass of tiles also provides insulation benefits, reducing energy costs year-round.'
            }
        ],
        'description_template': 'Expert tile roofing in {town}, NJ. Clay & concrete tiles. 50-100 year lifespan. Mediterranean elegance. Fire resistant. Licensed & insured. Free estimates. Call (667) 204-1609.'
    },
    'slate': {
        'name': 'Slate',
        'title_suffix': 'Luxury & Heritage',
        'lifespan': '75-200 years',
        'price_range': '$25,000 - $50,000+',
        'best_for': 'historic homes and luxury properties',
        'key_benefits': [
            '75-200 year lifespan - century-long performance',
            'Natural stone beauty and elegance',
            'Perfect for historic and luxury homes',
            'Fire resistant and non-combustible',
            'Virtually maintenance-free',
            'Unparalleled curb appeal and property value'
        ],
        'services': [
            'Vermont slate roof installation',
            'Spanish and Welsh slate systems',
            'Historic slate roof restoration',
            'Slate repair and replacement',
            'Copper flashing and detailing',
            'Slate roof inspection and maintenance'
        ],
        'faqs': [
            {
                'q': 'How long do slate roofs last in {town}?',
                'a': 'Slate roofs in {town} regularly last 75-200 years - some historic {town} homes still have their original 100+ year old slate roofs. This makes slate the most durable roofing material available, often outlasting multiple generations.'
            },
            {
                'q': 'What makes slate roofing ideal for historic {town} homes?',
                'a': 'Many of {town}\'s Victorian and historic homes were originally built with slate. We specialize in authentic restoration using period-appropriate slate colors and installation techniques that maintain your home\'s historic character and value.'
            },
            {
                'q': 'Can my {town} home support the weight of slate roofing?',
                'a': 'Historic {town} homes were often built with slate-capable framing. We perform structural assessments to verify your home can support slate. Modern {town} homes may require reinforcement, which we can design and install.'
            },
            {
                'q': 'How much does slate roofing cost in {town}?',
                'a': 'Slate roofing in {town} typically ranges from $25,000-$50,000+ depending on roof size and slate quality. While the upfront cost is higher, the 100+ year lifespan means it\'s often the most cost-effective roofing choice long-term.'
            },
            {
                'q': 'Do you offer slate roof repair in {town}?',
                'a': 'Yes! We specialize in slate roof repair and restoration for {town}\'s historic homes. Individual slates can be replaced, and we can source matching vintage or new slates to maintain your roof\'s authentic appearance.'
            }
        ],
        'description_template': 'Premium slate roofing in {town}, NJ. 75-200 year lifespan. Natural stone elegance. Historic restoration specialists. Licensed & insured. Free estimates. Call (667) 204-1609.'
    }
}

# 15 Essex County Towns with local context
TOWNS = {
    'newark': {
        'name': 'Newark',
        'neighborhoods': 'Ironbound, Forest Hill, North Ward, Downtown',
        'architecture': 'Victorian brownstones, historic brick buildings, modern high-rises',
        'local_context': 'Essex County\'s largest city with diverse architectural styles from Victorian homes in Forest Hill to modern developments downtown',
        'zip_codes': '07102, 07103, 07104, 07105',
        'geo': {'lat': '40.7357', 'lon': '-74.1724'}
    },
    'east-orange': {
        'name': 'East Orange',
        'neighborhoods': 'Ampere, Elmwood, Ashland, Greenwood',
        'architecture': 'Colonial Revival homes, Tudor-style residences, brick multi-families',
        'local_context': 'Known for historic neighborhoods with well-maintained Colonial and Tudor architecture',
        'zip_codes': '07017, 07018, 07019',
        'geo': {'lat': '40.7673', 'lon': '-74.2049'}
    },
    'irvington': {
        'name': 'Irvington',
        'neighborhoods': 'Civic Square, University Heights, Grove Street',
        'architecture': 'Victorian homes, Colonial-style houses, brick apartment buildings',
        'local_context': 'Residential community with mix of Victorian and Colonial homes near major transportation',
        'zip_codes': '07111',
        'geo': {'lat': '40.7323', 'lon': '-74.2346'}
    },
    'bloomfield': {
        'name': 'Bloomfield',
        'neighborhoods': 'Brookdale, Watsessing Park, Downtown Bloomfield',
        'architecture': 'Colonial homes, Cape Cods, Victorian-era houses',
        'local_context': 'Family-oriented suburb with beautiful Colonial and Cape Cod homes surrounding Watsessing Park',
        'zip_codes': '07003',
        'geo': {'lat': '40.8068', 'lon': '-74.1854'}
    },
    'west-orange': {
        'name': 'West Orange',
        'neighborhoods': 'Llewellyn Park, Pleasant Valley, Eagle Rock',
        'architecture': 'Luxury estates, Colonial Revivals, contemporary custom homes',
        'local_context': 'Upscale community featuring historic Llewellyn Park and stunning views from Eagle Rock',
        'zip_codes': '07052',
        'geo': {'lat': '40.7987', 'lon': '-74.2390'}
    },
    'montclair': {
        'name': 'Montclair',
        'neighborhoods': 'Upper Montclair, South End, Watchung Plaza',
        'architecture': 'Victorian mansions, Craftsman bungalows, Tudor estates',
        'local_context': 'Affluent township known for Victorian architecture, arts community, and tree-lined streets',
        'zip_codes': '07042, 07043',
        'geo': {'lat': '40.8259', 'lon': '-74.2090'}
    },
    'belleville': {
        'name': 'Belleville',
        'neighborhoods': 'Silver Lake, Joralemon Street, Franklin Avenue',
        'architecture': 'Dutch Colonial homes, brick colonials, Cape Cod-style houses',
        'local_context': 'Diverse community with mix of Colonial and Cape Cod homes near Branch Brook Park',
        'zip_codes': '07109',
        'geo': {'lat': '40.7937', 'lon': '-74.1502'}
    },
    'orange': {
        'name': 'Orange',
        'neighborhoods': 'Oakwood, East Orange Border, Valley',
        'architecture': 'Victorian homes, Colonial-style buildings, brick row houses',
        'local_context': 'Historic city with well-preserved Victorian architecture and growing revitalization',
        'zip_codes': '07050, 07051',
        'geo': {'lat': '40.7679', 'lon': '-74.2326'}
    },
    'livingston': {
        'name': 'Livingston',
        'neighborhoods': 'Riker Hill, Northland Woods, Collins Estates',
        'architecture': 'Colonial homes, split-levels, contemporary estates',
        'local_context': 'Affluent suburban township with excellent schools and spacious Colonial homes',
        'zip_codes': '07039',
        'geo': {'lat': '40.7959', 'lon': '-74.3149'}
    },
    'nutley': {
        'name': 'Nutley',
        'neighborhoods': 'Franklin, Yantacaw, Radcliffe',
        'architecture': 'Colonial homes, Cape Cods, Tudor-style residences',
        'local_context': 'Close-knit community with well-maintained Colonial and Tudor homes near NYC',
        'zip_codes': '07110',
        'geo': {'lat': '40.8223', 'lon': '-74.1599'}
    },
    'maplewood': {
        'name': 'Maplewood',
        'neighborhoods': 'Maplewood Village, Tuscan, Hilton',
        'architecture': 'Colonial Revivals, Victorian homes, Craftsman bungalows',
        'local_context': 'Charming township with walkable village, Victorian architecture, and strong community',
        'zip_codes': '07040',
        'geo': {'lat': '40.7312', 'lon': '-74.2735'}
    },
    'millburn': {
        'name': 'Millburn',
        'neighborhoods': 'Short Hills, Wyoming, Millburn Village',
        'architecture': 'Luxury estates, Colonial mansions, contemporary custom homes',
        'local_context': 'Prestigious township including Short Hills area with luxury homes and top-rated schools',
        'zip_codes': '07041, 07078',
        'geo': {'lat': '40.7296', 'lon': '-74.3121'}
    },
    'south-orange': {
        'name': 'South Orange',
        'neighborhoods': 'Seton Hall, Newstead, Montrose',
        'architecture': 'Victorian homes, Tudor estates, Colonial Revivals',
        'local_context': 'Historic village with Seton Hall University, Victorian architecture, and cultural diversity',
        'zip_codes': '07079',
        'geo': {'lat': '40.7490', 'lon': '-74.2615'}
    },
    'verona': {
        'name': 'Verona',
        'neighborhoods': 'Brookdale, Linn Drive, Pompton Avenue',
        'architecture': 'Colonial homes, split-levels, ranch-style houses',
        'local_context': 'Small, tight-knit township with excellent parks and family-friendly neighborhoods',
        'zip_codes': '07044',
        'geo': {'lat': '40.8298', 'lon': '-74.2402'}
    },
    'cedar-grove': {
        'name': 'Cedar Grove',
        'neighborhoods': 'North End, Bradford, Little Falls Road',
        'architecture': 'Colonial homes, split-levels, contemporary residences',
        'local_context': 'Quiet suburban township with spacious properties and family-oriented community',
        'zip_codes': '07009',
        'geo': {'lat': '40.8512', 'lon': '-74.2293'}
    }
}

def generate_material_page(material_slug, material_data, town_slug, town_data):
    """Generate a complete material-specific roofing page"""

    material_name = material_data['name']
    town_name = town_data['name']

    # Replace {town} placeholders in FAQs
    faqs = []
    for faq in material_data['faqs']:
        faqs.append({
            'q': faq['q'].replace('{town}', town_name),
            'a': faq['a'].replace('{town}', town_name)
        })

    # Generate FAQ schema
    faq_schema_items = []
    for i, faq in enumerate(faqs):
        faq_schema_items.append(f'''        {{
            "@type": "Question",
            "name": "{faq['q']}",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "{faq['a']}"
            }}
        }}''')

    faq_schema = ',\n'.join(faq_schema_items)

    # Generate HTML content
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{material_name} Roofing {town_name}, NJ | {material_data['title_suffix']} | R&E Roofing</title>

    <!-- SEO Meta Tags -->
    <meta name="description" content="{material_data['description_template'].replace('{town}', town_name)}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="R&E Roofing">

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{material_name} Roofing {town_name}, NJ | {material_data['title_suffix']} | R&E Roofing">
    <meta property="og:description" content="{material_data['description_template'].replace('{town}', town_name)}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://randeroofing.com/{material_slug}-roofing-{town_slug}-nj.html">
    <meta property="og:image" content="https://randeroofing.com/images/og-image.jpg">
    <meta property="og:site_name" content="R&E Roofing">
    <meta property="og:locale" content="en_US">

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{material_name} Roofing {town_name}, NJ | {material_data['title_suffix']} | R&E Roofing">
    <meta name="twitter:description" content="{material_data['description_template'].replace('{town}', town_name)}">
    <meta name="twitter:image" content="https://randeroofing.com/images/twitter-card.jpg">

    <!-- Canonical URL -->
    <link rel="canonical" href="https://randeroofing.com/{material_slug}-roofing-{town_slug}-nj.html">

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/logo.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/images/logo.png">

    <!-- Service Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "{material_name} Roofing",
        "provider": {{
            "@type": "RoofingContractor",
            "name": "R&E Roofing",
            "telephone": "(667) 204-1609",
            "email": "info@randeroofing.com",
            "areaServed": {{
                "@type": "City",
                "name": "{town_name}",
                "addressRegion": "NJ"
            }},
            "geo": {{
                "@type": "GeoCoordinates",
                "latitude": "{town_data['geo']['lat']}",
                "longitude": "{town_data['geo']['lon']}"
            }}
        }},
        "description": "Professional {material_name.lower()} roofing services in {town_name}, NJ including installation, repair, and replacement",
        "url": "https://randeroofing.com/{material_slug}-roofing-{town_slug}-nj.html"
    }}
    </script>

    <!-- Breadcrumb Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://randeroofing.com/"
        }}, {{
            "@type": "ListItem",
            "position": 2,
            "name": "{town_name} Roofing",
            "item": "https://randeroofing.com/roofing-{town_slug}-nj.html"
        }}, {{
            "@type": "ListItem",
            "position": 3,
            "name": "{material_name} Roofing in {town_name}",
            "item": "https://randeroofing.com/{material_slug}-roofing-{town_slug}-nj.html"
        }}]
    }}
    </script>

    <!-- FAQ Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{faq_schema}
        ]
    }}
    </script>

    <!-- Stylesheet -->
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>

    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="index.html">
                        <img src="images/logo.png" alt="R&E Roofing Logo">
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="roofing-{town_slug}-nj.html">{town_name} Roofing</a></li>
                        <li><a href="reviews.html">Reviews</a></li>
                        <li><a href="about.html">About</a></li>
                        <li><a href="#" class="cta-button" onclick="openContactModal(); return false;">Get Free Estimate</a></li>
                    </ul>
                </nav>
                <div class="mobile-menu-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    </header>

    <!-- Mobile Navigation -->
    <div class="mobile-nav">
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="roofing-{town_slug}-nj.html">{town_name} Roofing</a></li>
            <li><a href="reviews.html">Reviews</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="#" onclick="openContactModal(); return false;">Get Free Estimate</a></li>
        </ul>
    </div>

    <!-- Hero Section -->
    <section class="hero" style="background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); padding: 120px 0 80px;">
        <div class="container">
            <div class="breadcrumb">
                <a href="index.html">Home</a> &gt;
                <a href="roofing-{town_slug}-nj.html">{town_name} Roofing</a> &gt;
                <span>{material_name} Roofing</span>
            </div>
            <h1 class="hero-title" style="color: white;">{material_name} Roofing in {town_name}, NJ</h1>
            <p class="hero-subtitle" style="color: #e0e0e0; max-width: 700px; margin: 20px auto 30px;">{material_data['lifespan']} lifespan • {material_data['price_range']} average cost • Best for {material_data['best_for']}</p>
            <div class="hero-cta">
                <a href="#" class="cta-button cta-primary" onclick="openContactModal(); return false;">Get Free Estimate</a>
                <a href="tel:6672041609" class="cta-button cta-secondary" style="background: white; color: #333;">Call (667) 204-1609</a>
            </div>
        </div>
    </section>

    <!-- Benefits Section -->
    <section class="benefits-section" style="padding: 80px 0; background: #f8f9fa;">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 50px;">Why Choose {material_name} Roofing for Your {town_name} Home?</h2>
            <div class="benefits-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
'''

    # Add benefits
    for benefit in material_data['key_benefits']:
        html += f'''                <div class="benefit-card" style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
                    <div class="benefit-icon" style="width: 60px; height: 60px; background: linear-gradient(135deg, #FF6B35 0%, #FF3B30 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                        <i class="fas fa-check" style="color: white; font-size: 24px;"></i>
                    </div>
                    <h3 style="margin-bottom: 10px; font-size: 18px;">{benefit}</h3>
                </div>
'''

    html += f'''            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services-section" style="padding: 80px 0;">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 50px;">Our {material_name} Roofing Services in {town_name}</h2>
            <div class="services-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto;">
'''

    # Add services
    for service in material_data['services']:
        html += f'''                <div class="service-card" style="background: white; padding: 30px; border-radius: 12px; border: 2px solid #f0f0f0; transition: all 0.3s ease;">
                    <h3 style="margin-bottom: 15px; font-size: 18px; color: #333;">{service}</h3>
                    <p style="color: #666; line-height: 1.6;">Expert installation and service for {town_name} homeowners</p>
                </div>
'''

    html += f'''            </div>
        </div>
    </section>

    <!-- About Material Section -->
    <section class="about-material-section" style="padding: 80px 0; background: #f8f9fa;">
        <div class="container">
            <div style="max-width: 900px; margin: 0 auto;">
                <h2 style="margin-bottom: 30px;">Expert {material_name} Roofing Installation in {town_name}</h2>
                <p style="font-size: 18px; line-height: 1.8; color: #333; margin-bottom: 20px;">
                    R&E Roofing brings over 25 years of {material_name.lower()} roofing expertise to {town_name}, NJ. We understand the unique architectural character of {town_name}'s homes - from {town_data['architecture']} - and we're experts at selecting and installing {material_name.lower()} roofing systems that complement your home's style while providing superior protection.
                </p>
                <p style="font-size: 18px; line-height: 1.8; color: #333; margin-bottom: 20px;">
                    {town_data['local_context']}. Our team has completed hundreds of {material_name.lower()} roof installations throughout {town_data['neighborhoods']}, earning a reputation for quality craftsmanship and exceptional customer service.
                </p>
                <p style="font-size: 18px; line-height: 1.8; color: #333;">
                    Whether you're building a new home, replacing an aging roof, or upgrading to {material_name.lower()} roofing for its superior performance, we provide transparent pricing, professional installation, and industry-leading warranties. Every {material_name.lower()} roofing project in {town_name} is backed by our commitment to excellence and customer satisfaction.
                </p>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section" style="padding: 80px 0;">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 50px;">{material_name} Roofing FAQs for {town_name} Homeowners</h2>
            <div class="faq-container" style="max-width: 900px; margin: 0 auto;">
'''

    # Add FAQs
    for faq in faqs:
        html += f'''                <div class="faq-item" style="background: white; padding: 30px; margin-bottom: 20px; border-radius: 12px; border: 2px solid #f0f0f0;">
                    <h3 style="margin-bottom: 15px; font-size: 20px; color: #333;">{faq['q']}</h3>
                    <p style="color: #666; line-height: 1.8;">{faq['a']}</p>
                </div>
'''

    html += f'''            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section" style="padding: 80px 0; background: linear-gradient(135deg, #FF6B35 0%, #FF3B30 100%); color: white; text-align: center;">
        <div class="container">
            <h2 style="color: white; margin-bottom: 20px;">Ready for {material_name} Roofing in {town_name}?</h2>
            <p style="font-size: 20px; margin-bottom: 30px; color: white;">Get a free, no-obligation estimate from {town_name}'s trusted {material_name.lower()} roofing experts</p>
            <div class="cta-buttons">
                <a href="#" class="cta-button" style="background: white; color: #FF6B35; margin: 0 10px;" onclick="openContactModal(); return false;">Get Free Estimate</a>
                <a href="tel:6672041609" class="cta-button" style="background: transparent; border: 2px solid white; color: white; margin: 0 10px;">Call (667) 204-1609</a>
            </div>
        </div>
    </section>

    <!-- More Services Section -->
    <section class="more-services-section" style="padding: 80px 0; background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 50px;">More {town_name} Roofing Services</h2>
            <div class="services-grid-enhanced" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; max-width: 1200px; margin: 0 auto;">

                <a href="emergency-roof-repair-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #FF6B35 0%, #FF3B30 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-exclamation-triangle" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">Emergency Repair</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">24/7 emergency roof repair</p>
                </a>

                <a href="roof-leak-repair-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #4A90E2 0%, #357ABD 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-tint" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">Leak Detection & Repair</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">Advanced leak detection</p>
                </a>

                <a href="roof-repair-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #50C878 0%, #3BA05F 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-tools" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">Roof Repair</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">Professional roof repairs</p>
                </a>

                <a href="roof-replacement-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #9B59B6 0%, #8E44AD 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-sync-alt" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">Roof Replacement</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">Complete roof replacement</p>
                </a>

                <a href="new-roof-installation-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #F39C12 0%, #E67E22 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-hammer" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">New Installation</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">New roof installation</p>
                </a>

                <a href="siding-installation-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #3498DB 0%, #2980B9 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-th-large" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">Siding Installation</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">Expert siding installation</p>
                </a>

                <a href="gutter-installation-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #1ABC9C 0%, #16A085 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-water" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">Gutter Installation</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">Professional gutter systems</p>
                </a>

                <a href="roofing-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #34495E 0%, #2C3E50 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-home" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">All {town_name} Services</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">View all roofing services</p>
                </a>

            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>R&E Roofing</h3>
                    <p>Professional roofing, siding, and gutter services throughout Essex County, NJ.</p>
                    <p><strong>Licensed & Insured</strong></p>
                </div>
                <div class="footer-section">
                    <h3>Contact</h3>
                    <p>Phone: <a href="tel:6672041609">(667) 204-1609</a></p>
                    <p>Email: <a href="mailto:info@randeroofing.com">info@randeroofing.com</a></p>
                </div>
                <div class="footer-section">
                    <h3>Service Areas</h3>
                    <p>Serving all of Essex County, NJ including {town_name}, Newark, Montclair, West Orange, and surrounding areas.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; {datetime.now().year} R&E Roofing. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Contact Modal -->
    <div id="contactModal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <h2>Get Your Free Estimate</h2>
            <form id="contactForm" class="contact-form">
                <div class="form-group">
                    <label for="name">Name *</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone *</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
                <div class="form-group">
                    <label for="email">Email *</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="service">Service Needed *</label>
                    <select id="service" name="service" required>
                        <option value="{material_name} Roofing - {town_name}" selected>{material_name} Roofing - {town_name}</option>
                        <option value="Roof Repair">Roof Repair</option>
                        <option value="Roof Replacement">Roof Replacement</option>
                        <option value="New Roof Installation">New Roof Installation</option>
                        <option value="Emergency Repair">Emergency Repair</option>
                        <option value="Siding">Siding</option>
                        <option value="Gutters">Gutters</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="message">Project Details</label>
                    <textarea id="message" name="message" rows="4"></textarea>
                </div>
                <button type="submit" class="cta-button">Request Free Estimate</button>
            </form>
        </div>
    </div>

    <!-- Back to Top Button -->
    <button id="backToTop" class="back-to-top">↑</button>

    <!-- Font Awesome -->
    <script src="https://kit.fontawesome.com/your-fontawesome-kit.js" crossorigin="anonymous"></script>

    <!-- Main JavaScript -->
    <script src="js/main.js"></script>

</body>
</html>'''

    return html

def main():
    """Generate all 75 material-specific pages"""
    print("🏗️  Generating Phase 2: Material-Specific Roofing Pages")
    print(f"📊 Creating 5 materials × 15 towns = 75 pages\n")

    pages_created = 0

    for material_slug, material_data in MATERIALS.items():
        print(f"\n🔨 Creating {material_data['name']} Roofing pages...")

        for town_slug, town_data in TOWNS.items():
            filename = f"{material_slug}-roofing-{town_slug}-nj.html"

            # Generate page content
            html_content = generate_material_page(material_slug, material_data, town_slug, town_data)

            # Write file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)

            pages_created += 1
            print(f"  ✅ Created: {filename}")

    print(f"\n✅ Phase 2 Complete: {pages_created} pages created successfully!")
    print(f"\n📁 Files created:")
    print(f"   - {len(MATERIALS)} materials (asphalt-shingle, metal, flat, tile, slate)")
    print(f"   - {len(TOWNS)} towns")
    print(f"   - {pages_created} total pages")
    print(f"\n🎯 Next Steps:")
    print(f"   1. Update sitemap.xml with {pages_created} new entries")
    print(f"   2. Test pages locally")
    print(f"   3. Deploy to production")

if __name__ == "__main__":
    main()
