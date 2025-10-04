#!/usr/bin/env python3
"""
Generate Phase 3: Commercial & Financing Pages
Creates 45 pages (3 service types × 15 Essex County towns)
"""

import os
from datetime import datetime

# 3 Service Types with detailed specs
SERVICES = {
    'commercial-roofing': {
        'name': 'Commercial Roofing',
        'title_suffix': 'Business & Property Solutions',
        'price_range': '$15,000 - $150,000+',
        'target_market': 'business owners, property managers, and facility directors',
        'key_benefits': [
            'Minimize business disruption with flexible scheduling',
            'TPO, EPDM, PVC, and built-up roofing systems',
            'Preventive maintenance programs reduce long-term costs',
            'Licensed & insured with commercial liability coverage',
            'Emergency repair response within 2 hours',
            'Detailed documentation for property management'
        ],
        'services': [
            'Flat roof installation (TPO, EPDM, PVC)',
            'Built-up roofing systems (BUR)',
            'Modified bitumen roofing',
            'Commercial roof repairs and leak detection',
            'Preventive maintenance contracts',
            'Emergency commercial roof repair'
        ],
        'faqs': [
            {
                'q': 'What types of commercial roofs do you install in {town}?',
                'a': 'We install all major commercial roofing systems in {town} including TPO (thermoplastic polyolefin), EPDM (rubber roofing), PVC, built-up roofing (BUR), and modified bitumen. We assess your building\'s needs, budget, and local {town} building codes to recommend the optimal system.'
            },
            {
                'q': 'Can you work around our business hours in {town}?',
                'a': 'Absolutely. We understand {town} businesses can\'t afford downtime. We offer evening, weekend, and off-hours scheduling to minimize disruption. Many {town} commercial projects are completed outside normal business hours.'
            },
            {
                'q': 'Do you offer commercial roof maintenance plans in {town}?',
                'a': 'Yes! Our preventive maintenance programs in {town} include bi-annual inspections, debris removal, drain cleaning, and minor repairs. Regular maintenance extends roof life by 30-50% and prevents costly emergency repairs.'
            },
            {
                'q': 'How long does a commercial roof last in {town}?',
                'a': 'Commercial roofing lifespan in {town} varies by system: TPO and PVC typically last 20-30 years, EPDM 15-25 years, and built-up roofing 15-20 years. Essex County\'s climate requires quality installation - we provide warranties up to 20 years.'
            },
            {
                'q': 'Can you handle large commercial properties in {town}?',
                'a': 'Yes. We\'ve completed commercial roofing projects in {town} ranging from 5,000 to 100,000+ square feet including retail centers, office buildings, warehouses, and multi-family properties. We have the crew size and equipment for any scale.'
            }
        ],
        'description_template': 'Commercial roofing in {town}, NJ. TPO, EPDM, PVC & built-up systems. Flexible scheduling. Preventive maintenance plans. Licensed & insured. 25+ years experience. Call (667) 204-1609.'
    },
    'roofing-financing': {
        'name': 'Roofing Financing',
        'title_suffix': 'Flexible Payment Options',
        'price_range': 'From $99/month',
        'target_market': 'homeowners seeking affordable payment plans',
        'key_benefits': [
            'Flexible payment plans from $99/month',
            '0% financing available (for qualified applicants)',
            'Quick approval process - same day in most cases',
            'No hidden fees or prepayment penalties',
            'All credit types considered - even poor credit',
            'Start your roof project today, pay over time'
        ],
        'services': [
            '0% interest financing (12-18 months)',
            'Extended payment plans (up to 10 years)',
            'Same-day approval process',
            'Poor credit financing options',
            'Home equity financing guidance',
            'Insurance deductible financing'
        ],
        'faqs': [
            {
                'q': 'What financing options are available in {town}?',
                'a': 'R&E Roofing offers multiple financing options for {town} homeowners: 0% interest for 12-18 months (qualified applicants), extended payment plans up to 10 years, and special programs for all credit types. Monthly payments start as low as $99.'
            },
            {
                'q': 'Can I get financing with bad credit in {town}?',
                'a': 'Yes! We work with multiple lenders who specialize in all credit situations. Many {town} homeowners with credit challenges have been approved. We focus on getting you the roof you need, regardless of past credit issues.'
            },
            {
                'q': 'How quickly can I get approved for financing in {town}?',
                'a': 'Most {town} homeowners receive same-day approval. Our simple application takes 5-10 minutes, and you\'ll typically know your approval status within hours. We can often start your roofing project within days of approval.'
            },
            {
                'q': 'Are there any hidden fees or prepayment penalties?',
                'a': 'No hidden fees, ever. Our {town} financing programs are transparent with no prepayment penalties. Pay off your loan early without penalty, and there are no origination fees or application fees to worry about.'
            },
            {
                'q': 'What is the typical monthly payment for a new roof in {town}?',
                'a': 'Monthly payments for {town} homeowners typically range from $99-$400 depending on roof size and financing term selected. A typical $8,000 roof with our 0% financing (18 months) is approximately $444/month with no interest charges.'
            }
        ],
        'description_template': 'Roofing financing in {town}, NJ. Flexible payment plans from $99/month. 0% financing available. Same-day approval. All credit types. Licensed contractor. Call (667) 204-1609.'
    },
    'roof-insurance-claims': {
        'name': 'Roof Insurance Claims',
        'title_suffix': 'Storm Damage Assistance',
        'price_range': 'Insurance Covered',
        'target_market': 'homeowners with storm damage and insurance claims',
        'key_benefits': [
            'Free insurance claim inspection and documentation',
            'Work directly with your insurance adjuster',
            'Maximize your insurance claim payout',
            'Handle all paperwork and documentation',
            'Storm damage specialists - wind, hail, ice dams',
            'We work with all major insurance companies'
        ],
        'services': [
            'Free insurance damage inspection',
            'Claim documentation and photography',
            'Insurance adjuster meeting coordination',
            'Detailed repair estimates for claims',
            'Emergency tarping and mitigation',
            'Full roof replacement if approved'
        ],
        'faqs': [
            {
                'q': 'How do roof insurance claims work in {town}?',
                'a': 'After storm damage in {town}, contact your insurance company to file a claim. We provide a free inspection, document all damage with photos and measurements, meet with your adjuster, and provide a detailed estimate. Your insurance typically covers the repair/replacement minus your deductible.'
            },
            {
                'q': 'Will you work directly with my insurance company?',
                'a': 'Yes! We work with all major insurance carriers serving {town} including State Farm, Allstate, Liberty Mutual, and others. We handle communication with adjusters, provide necessary documentation, and ensure you receive fair compensation for your {town} roof damage.'
            },
            {
                'q': 'What if my claim is denied in {town}?',
                'a': 'If your {town} insurance claim is initially denied, we help with the appeals process. We provide additional documentation, expert assessments, and work with public adjusters if needed. Many initially denied claims in {town} are successfully appealed with proper documentation.'
            },
            {
                'q': 'How long does the insurance claim process take in {town}?',
                'a': 'Most {town} insurance claims are processed within 2-4 weeks. We expedite the process by providing complete documentation upfront. Emergency repairs can often begin immediately while the full claim is being processed to prevent further damage.'
            },
            {
                'q': 'What types of storm damage are covered by insurance in {town}?',
                'a': '{town} insurance policies typically cover wind damage, hail damage, ice dam damage, and storm-related leaks. We document all damage types during our inspection to ensure your claim includes everything covered by your Essex County homeowner\'s policy.'
            }
        ],
        'description_template': 'Roof insurance claims assistance in {town}, NJ. Free damage inspection. Work with all insurers. Storm damage specialists. Maximize your claim. Licensed contractor. Call (667) 204-1609.'
    }
}

# 15 Essex County Towns (same as Phase 2)
TOWNS = {
    'newark': {
        'name': 'Newark',
        'commercial_context': 'Essex County\'s largest business district with downtown offices, retail centers, and industrial properties',
        'zip_codes': '07102, 07103, 07104, 07105',
        'geo': {'lat': '40.7357', 'lon': '-74.1724'}
    },
    'east-orange': {
        'name': 'East Orange',
        'commercial_context': 'Growing commercial corridor with retail centers and multi-family properties',
        'zip_codes': '07017, 07018, 07019',
        'geo': {'lat': '40.7673', 'lon': '-74.2049'}
    },
    'irvington': {
        'name': 'Irvington',
        'commercial_context': 'Mixed-use commercial district with retail and residential properties',
        'zip_codes': '07111',
        'geo': {'lat': '40.7323', 'lon': '-74.2346'}
    },
    'bloomfield': {
        'name': 'Bloomfield',
        'commercial_context': 'Vibrant downtown business district with shops, offices, and restaurants',
        'zip_codes': '07003',
        'geo': {'lat': '40.8068', 'lon': '-74.1854'}
    },
    'west-orange': {
        'name': 'West Orange',
        'commercial_context': 'Upscale commercial properties including shopping centers and professional offices',
        'zip_codes': '07052',
        'geo': {'lat': '40.7987', 'lon': '-74.2390'}
    },
    'montclair': {
        'name': 'Montclair',
        'commercial_context': 'Thriving downtown with boutiques, restaurants, and professional services',
        'zip_codes': '07042, 07043',
        'geo': {'lat': '40.8259', 'lon': '-74.2090'}
    },
    'belleville': {
        'name': 'Belleville',
        'commercial_context': 'Industrial and commercial corridor with warehouses and retail properties',
        'zip_codes': '07109',
        'geo': {'lat': '40.7937', 'lon': '-74.1502'}
    },
    'orange': {
        'name': 'Orange',
        'commercial_context': 'Revitalizing commercial district with mixed-use developments',
        'zip_codes': '07050, 07051',
        'geo': {'lat': '40.7679', 'lon': '-74.2326'}
    },
    'livingston': {
        'name': 'Livingston',
        'commercial_context': 'Suburban commercial centers and professional office parks',
        'zip_codes': '07039',
        'geo': {'lat': '40.7959', 'lon': '-74.3149'}
    },
    'nutley': {
        'name': 'Nutley',
        'commercial_context': 'Local businesses, retail centers, and small commercial properties',
        'zip_codes': '07110',
        'geo': {'lat': '40.8223', 'lon': '-74.1599'}
    },
    'maplewood': {
        'name': 'Maplewood',
        'commercial_context': 'Charming village business district with shops and restaurants',
        'zip_codes': '07040',
        'geo': {'lat': '40.7312', 'lon': '-74.2735'}
    },
    'millburn': {
        'name': 'Millburn',
        'commercial_context': 'Premium commercial properties including Short Hills Mall area',
        'zip_codes': '07041, 07078',
        'geo': {'lat': '40.7296', 'lon': '-74.3121'}
    },
    'south-orange': {
        'name': 'South Orange',
        'commercial_context': 'University area commercial district with mixed-use properties',
        'zip_codes': '07079',
        'geo': {'lat': '40.7490', 'lon': '-74.2615'}
    },
    'verona': {
        'name': 'Verona',
        'commercial_context': 'Small town commercial properties and local business centers',
        'zip_codes': '07044',
        'geo': {'lat': '40.8298', 'lon': '-74.2402'}
    },
    'cedar-grove': {
        'name': 'Cedar Grove',
        'commercial_context': 'Quiet suburban commercial properties and strip malls',
        'zip_codes': '07009',
        'geo': {'lat': '40.8512', 'lon': '-74.2293'}
    }
}

def generate_service_page(service_slug, service_data, town_slug, town_data):
    """Generate a complete Phase 3 service page"""

    service_name = service_data['name']
    town_name = town_data['name']

    # Replace {town} placeholders in FAQs
    faqs = []
    for faq in service_data['faqs']:
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

    # Determine service-specific content
    if service_slug == 'commercial-roofing':
        hero_subtitle = f"Serving {town_name} businesses • {service_data['price_range']} • TPO, EPDM, PVC systems"
        about_paragraph = f"R&E Roofing provides comprehensive commercial roofing services to {town_name} businesses. {town_data['commercial_context']}. Whether you manage a small retail shop or a 50,000 sq ft warehouse, we deliver professional commercial roofing with minimal business disruption."
    elif service_slug == 'roofing-financing':
        hero_subtitle = f"Affordable payment plans for {town_name} homeowners • {service_data['price_range']} • 0% financing available"
        about_paragraph = f"Don't let budget concerns delay your {town_name} roof replacement. R&E Roofing partners with leading lenders to offer flexible financing options for all credit types. From 0% interest promotions to extended payment plans, we help {town_name} homeowners get the roof they need with payments that fit their budget."
    else:  # roof-insurance-claims
        hero_subtitle = f"Storm damage specialists serving {town_name} • {service_data['price_range']} • Work with all insurers"
        about_paragraph = f"After storm damage in {town_name}, navigating insurance claims can be overwhelming. R&E Roofing specializes in working with insurance companies to ensure {town_name} homeowners receive fair compensation. We document damage, meet with adjusters, and handle all paperwork so you can focus on getting your home protected."

    # Generate HTML content
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{service_name} {town_name}, NJ | {service_data['title_suffix']} | R&E Roofing</title>

    <!-- SEO Meta Tags -->
    <meta name="description" content="{service_data['description_template'].replace('{town}', town_name)}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="R&E Roofing">

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{service_name} {town_name}, NJ | {service_data['title_suffix']} | R&E Roofing">
    <meta property="og:description" content="{service_data['description_template'].replace('{town}', town_name)}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://randeroofing.com/pages/services/{service_slug}-{town_slug}-nj.html">
    <meta property="og:image" content="https://randeroofing.com/images/og-image.jpg">
    <meta property="og:site_name" content="R&E Roofing">
    <meta property="og:locale" content="en_US">

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{service_name} {town_name}, NJ | {service_data['title_suffix']} | R&E Roofing">
    <meta name="twitter:description" content="{service_data['description_template'].replace('{town}', town_name)}">
    <meta name="twitter:image" content="https://randeroofing.com/images/twitter-card.jpg">

    <!-- Canonical URL -->
    <link rel="canonical" href="https://randeroofing.com/pages/services/{service_slug}-{town_slug}-nj.html">

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/logo.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/images/logo.png">

    <!-- Service Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "{service_name}",
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
        "description": "{service_data['description_template'].replace('{town}', town_name)}",
        "url": "https://randeroofing.com/pages/services/{service_slug}-{town_slug}-nj.html"
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
            "item": "https://randeroofing.com/pages/towns/roofing-{town_slug}-nj.html"
        }}, {{
            "@type": "ListItem",
            "position": 3,
            "name": "{service_name} in {town_name}",
            "item": "https://randeroofing.com/pages/services/{service_slug}-{town_slug}-nj.html"
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
    <link rel="stylesheet" href="../../css/styles.css">
</head>
<body>

    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="../../index.html">
                        <img src="../../images/logo.png" alt="R&E Roofing Logo">
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="../../index.html">Home</a></li>
                        <li><a href="../core/services.html">Services</a></li>
                        <li><a href="../towns/roofing-{town_slug}-nj.html">{town_name} Roofing</a></li>
                        <li><a href="../core/reviews.html">Reviews</a></li>
                        <li><a href="../core/about.html">About</a></li>
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
            <li><a href="../../index.html">Home</a></li>
            <li><a href="../core/services.html">Services</a></li>
            <li><a href="../towns/roofing-{town_slug}-nj.html">{town_name} Roofing</a></li>
            <li><a href="../core/reviews.html">Reviews</a></li>
            <li><a href="../core/about.html">About</a></li>
            <li><a href="#" onclick="openContactModal(); return false;">Get Free Estimate</a></li>
        </ul>
    </div>

    <!-- Hero Section -->
    <section class="hero" style="background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); padding: 120px 0 80px;">
        <div class="container">
            <div class="breadcrumb">
                <a href="../../index.html">Home</a> &gt;
                <a href="../towns/roofing-{town_slug}-nj.html">{town_name} Roofing</a> &gt;
                <span>{service_name}</span>
            </div>
            <h1 class="hero-title" style="color: white;">{service_name} in {town_name}, NJ</h1>
            <p class="hero-subtitle" style="color: #e0e0e0; max-width: 800px; margin: 20px auto 30px;">{hero_subtitle}</p>
            <div class="hero-cta">
                <a href="#" class="cta-button cta-primary" onclick="openContactModal(); return false;">Get Free Consultation</a>
                <a href="tel:6672041609" class="cta-button cta-secondary" style="background: white; color: #333;">Call (667) 204-1609</a>
            </div>
        </div>
    </section>

    <!-- Benefits Section -->
    <section class="benefits-section" style="padding: 80px 0; background: #f8f9fa;">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 50px;">Why Choose R&E Roofing for {service_name} in {town_name}?</h2>
            <div class="benefits-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
'''

    # Add benefits
    for benefit in service_data['key_benefits']:
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
            <h2 style="text-align: center; margin-bottom: 50px;">Our {service_name} Services in {town_name}</h2>
            <div class="services-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto;">
'''

    # Add services
    for service in service_data['services']:
        html += f'''                <div class="service-card" style="background: white; padding: 30px; border-radius: 12px; border: 2px solid #f0f0f0; transition: all 0.3s ease;">
                    <h3 style="margin-bottom: 15px; font-size: 18px; color: #333;">{service}</h3>
                    <p style="color: #666; line-height: 1.6;">Professional service for {town_name} clients</p>
                </div>
'''

    html += f'''            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about-section" style="padding: 80px 0; background: #f8f9fa;">
        <div class="container">
            <div style="max-width: 900px; margin: 0 auto;">
                <h2 style="margin-bottom: 30px;">Trusted {service_name} Provider in {town_name}</h2>
                <p style="font-size: 18px; line-height: 1.8; color: #333; margin-bottom: 20px;">
                    {about_paragraph}
                </p>
                <p style="font-size: 18px; line-height: 1.8; color: #333; margin-bottom: 20px;">
                    With over 25 years serving Essex County, R&E Roofing has become the go-to roofing contractor for {town_name} {service_data['target_market']}. We combine technical expertise with exceptional customer service, ensuring every project exceeds expectations.
                </p>
                <p style="font-size: 18px; line-height: 1.8; color: #333;">
                    Contact us today for a free consultation. We'll assess your needs, answer all questions, and provide transparent pricing with no hidden fees. Join hundreds of satisfied {town_name} customers who trust R&E Roofing for quality and reliability.
                </p>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section" style="padding: 80px 0;">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 50px;">{service_name} FAQs for {town_name}</h2>
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
            <h2 style="color: white; margin-bottom: 20px;">Ready to Get Started in {town_name}?</h2>
            <p style="font-size: 20px; margin-bottom: 30px; color: white;">Contact R&E Roofing for a free consultation and transparent pricing</p>
            <div class="cta-buttons">
                <a href="#" class="cta-button" style="background: white; color: #FF6B35; margin: 0 10px;" onclick="openContactModal(); return false;">Get Free Consultation</a>
                <a href="tel:6672041609" class="cta-button" style="background: transparent; border: 2px solid white; color: white; margin: 0 10px;">Call (667) 204-1609</a>
            </div>
        </div>
    </section>

    <!-- More Services Section -->
    <section class="more-services-section" style="padding: 80px 0; background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 50px;">More {town_name} Roofing Services</h2>
            <div class="services-grid-enhanced" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; max-width: 1200px; margin: 0 auto;">

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

                <a href="asphalt-shingle-roofing-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
                    <div class="service-icon" style="width: 72px; height: 72px; margin: 0 auto 20px; background: linear-gradient(135deg, #3498DB 0%, #2980B9 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-th-large" style="color: white; font-size: 32px;"></i>
                    </div>
                    <h3 style="font-size: 18px; margin-bottom: 12px; color: #333;">Asphalt Shingles</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">Affordable shingle roofing</p>
                </a>

                <a href="../towns/roofing-{town_slug}-nj.html" class="service-card" style="background: white; padding: 32px 24px; border-radius: 16px; text-align: center; text-decoration: none; color: inherit; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border: 2px solid transparent; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
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
            <h2>Get Your Free Consultation</h2>
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
                        <option value="{service_name} - {town_name}" selected>{service_name} - {town_name}</option>
                        <option value="Commercial Roofing">Commercial Roofing</option>
                        <option value="Roofing Financing">Roofing Financing</option>
                        <option value="Insurance Claims">Insurance Claims</option>
                        <option value="Roof Repair">Roof Repair</option>
                        <option value="Roof Replacement">Roof Replacement</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="message">Project Details</label>
                    <textarea id="message" name="message" rows="4"></textarea>
                </div>
                <button type="submit" class="cta-button">Request Free Consultation</button>
            </form>
        </div>
    </div>

    <!-- Back to Top Button -->
    <button id="backToTop" class="back-to-top">↑</button>

    <!-- Font Awesome -->
    <script src="https://kit.fontawesome.com/your-fontawesome-kit.js" crossorigin="anonymous"></script>

    <!-- Main JavaScript -->
    <script src="../../js/main.js"></script>

</body>
</html>'''

    return html

def main():
    """Generate all 45 Phase 3 service pages"""
    print("🏗️  Generating Phase 3: Commercial & Financing Pages")
    print(f"📊 Creating 3 services × 15 towns = 45 pages\n")

    # Create pages/services directory if it doesn't exist
    os.makedirs('pages/services', exist_ok=True)

    pages_created = 0

    for service_slug, service_data in SERVICES.items():
        print(f"\n🔨 Creating {service_data['name']} pages...")

        for town_slug, town_data in TOWNS.items():
            filename = f"pages/services/{service_slug}-{town_slug}-nj.html"

            # Generate page content
            html_content = generate_service_page(service_slug, service_data, town_slug, town_data)

            # Write file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)

            pages_created += 1
            print(f"  ✅ Created: {filename}")

    print(f"\n✅ Phase 3 Complete: {pages_created} pages created successfully!")
    print(f"\n📁 Files created:")
    print(f"   - {len(SERVICES)} service types (commercial, financing, insurance)")
    print(f"   - {len(TOWNS)} towns")
    print(f"   - {pages_created} total pages")
    print(f"\n🎯 Next Steps:")
    print(f"   1. Update sitemap.xml with {pages_created} new entries")
    print(f"   2. Test pages locally")
    print(f"   3. Deploy to production")

if __name__ == "__main__":
    main()
