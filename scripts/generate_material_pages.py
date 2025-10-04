#!/usr/bin/env python3
"""
Generate 75 material-specific roofing pages for Phase 2 SEO strategy.
5 materials × 15 towns = 75 pages
"""

import os
from datetime import datetime

# Configuration
TOWNS = [
    {"name": "Newark", "lat": "40.7357", "lon": "-74.1724"},
    {"name": "East Orange", "lat": "40.7673", "lon": "-74.2049"},
    {"name": "Irvington", "lat": "40.7323", "lon": "-74.2346"},
    {"name": "Bloomfield", "lat": "40.8067", "lon": "-74.1854"},
    {"name": "West Orange", "lat": "40.7987", "lon": "-74.2390"},
    {"name": "Montclair", "lat": "40.8259", "lon": "-74.2090"},
    {"name": "Belleville", "lat": "40.7937", "lon": "-74.1502"},
    {"name": "Orange", "lat": "40.7679", "lon": "-74.2326"},
    {"name": "Livingston", "lat": "40.7959", "lon": "-74.3149"},
    {"name": "Nutley", "lat": "40.8223", "lon": "-74.1599"},
    {"name": "Maplewood", "lat": "40.7312", "lon": "-74.2735"},
    {"name": "Millburn", "lat": "40.7296", "lon": "-74.3071"},
    {"name": "South Orange", "lat": "40.7490", "lon": "-74.2613"},
    {"name": "Verona", "lat": "40.8298", "lon": "-74.2401"},
    {"name": "Cedar Grove", "lat": "40.8534", "lon": "-74.2282"}
]

MATERIALS = {
    "asphalt-shingle-roofing": {
        "display_name": "Asphalt Shingle Roofing",
        "short_name": "Asphalt Shingle",
        "service_type": "Asphalt Shingle Roofing Installation",
        "description": "Professional asphalt shingle roofing in {town}, NJ. Affordable, durable roofing with 15-30 year warranties. Licensed & insured. Free estimates. Call (667) 204-1609.",
        "hero_title": "Asphalt Shingle Roofing in {town}, NJ",
        "hero_subtitle": "Expert Asphalt Shingle Installation & Replacement | Affordable & Durable Roofing Solutions",
        "intro": "<p>Asphalt shingles remain the most popular roofing choice for {town} homeowners, combining affordability, durability, and aesthetic versatility. R&E Roofing specializes in professional asphalt shingle installation, offering a wide range of styles and colors to complement your home's architecture—from {town}'s historic Victorians to modern colonial designs.</p>",
        "benefits": [
            {"icon": "dollar-sign", "title": "Cost-Effective", "desc": "Most affordable roofing option with excellent ROI"},
            {"icon": "clock", "title": "15-30 Year Lifespan", "desc": "Architectural shingles last 20-30 years"},
            {"icon": "palette", "title": "Design Versatility", "desc": "Hundreds of colors and styles available"},
            {"icon": "tools", "title": "Easy Repairs", "desc": "Individual shingles can be replaced affordably"},
            {"icon": "shield-alt", "title": "Wind Resistance", "desc": "Up to 130 mph wind rating for Essex County storms"},
            {"icon": "home", "title": "Curb Appeal", "desc": "Enhance your home's value and appearance"}
        ],
        "services": [
            {"icon": "hammer", "title": "New Installation", "desc": "Complete asphalt shingle roof installation"},
            {"icon": "sync-alt", "title": "Roof Replacement", "desc": "Replace old shingles with premium options"},
            {"icon": "tools", "title": "Shingle Repair", "desc": "Fix damaged or missing shingles"},
            {"icon": "search", "title": "Roof Inspection", "desc": "Free comprehensive roof assessment"},
            {"icon": "certificate", "title": "Warranty Service", "desc": "Manufacturer and workmanship warranties"},
            {"icon": "layer-group", "title": "Upgrade Options", "desc": "Architectural and designer shingle upgrades"}
        ],
        "faq": [
            {
                "q": "How long do asphalt shingles last in {town}, NJ?",
                "a": "Standard 3-tab asphalt shingles last 15-20 years in {town}, while architectural (dimensional) shingles last 25-30 years. Lifespan depends on factors like roof pitch, ventilation, and weather exposure. Essex County's climate requires quality installation for optimal longevity."
            },
            {
                "q": "What's the difference between 3-tab and architectural shingles?",
                "a": "3-tab shingles are flat, single-layered, and more affordable ($90-$150 per square installed). Architectural shingles are multi-layered, dimensionally textured, more durable (25-30 year lifespan), and provide superior wind resistance and curb appeal. Most {town} homeowners now choose architectural shingles for better long-term value."
            },
            {
                "q": "How much does asphalt shingle roofing cost in {town}?",
                "a": "Asphalt shingle installation in {town} typically costs $350-$550 per square (100 sq ft) for materials and labor. A typical 2,000 sq ft home costs $7,000-$11,000 for 3-tab shingles or $9,000-$15,000 for architectural shingles. Factors include roof complexity, pitch, and material grade. We provide free detailed estimates."
            },
            {
                "q": "Can you match my existing shingle color?",
                "a": "Yes! We work with leading manufacturers (GAF, Owens Corning, CertainTeed) offering hundreds of color options. We can match your existing shingles or help you choose a new color to complement your {town} home's style. We'll provide samples and digital visualization before installation."
            },
            {
                "q": "Do asphalt shingles work well in New Jersey weather?",
                "a": "Absolutely. Modern asphalt shingles are engineered for Northeast climates. They handle {town}'s hot summers, cold winters, snow loads, and summer storms. We recommend architectural shingles rated for 110-130 mph winds for maximum protection against nor'easters and severe weather common in Essex County."
            }
        ]
    },
    "metal-roofing": {
        "display_name": "Metal Roofing",
        "short_name": "Metal",
        "service_type": "Metal Roofing Installation",
        "description": "Premium metal roofing in {town}, NJ. 50+ year lifespan, energy efficient, fire resistant. Standing seam & metal shingle options. Licensed & insured. Call (667) 204-1609.",
        "hero_title": "Metal Roofing in {town}, NJ",
        "hero_subtitle": "Premium Metal Roof Installation | 50+ Year Lifespan | Energy Efficient Solutions",
        "intro": "<p>Metal roofing represents the premium choice for {town} homeowners seeking unmatched durability, energy efficiency, and modern aesthetics. With a lifespan exceeding 50 years, metal roofs outlast traditional materials while providing superior weather protection. R&E Roofing specializes in standing seam metal roofing and metal shingle systems that complement both contemporary and traditional {town} architecture.</p>",
        "benefits": [
            {"icon": "infinity", "title": "50+ Year Lifespan", "desc": "Outlasts asphalt shingles 2-3 times"},
            {"icon": "bolt", "title": "Energy Efficient", "desc": "Reflects solar heat, reduces cooling costs 10-25%"},
            {"icon": "fire", "title": "Fire Resistant", "desc": "Class A fire rating for maximum safety"},
            {"icon": "wind", "title": "Wind Resistant", "desc": "Withstands 140+ mph winds and severe storms"},
            {"icon": "snowflake", "title": "Snow Shedding", "desc": "Metal surface prevents ice dam formation"},
            {"icon": "leaf", "title": "Eco-Friendly", "desc": "100% recyclable, often contains recycled content"}
        ],
        "services": [
            {"icon": "ruler-combined", "title": "Standing Seam", "desc": "Sleek vertical panel metal roofing systems"},
            {"icon": "th-large", "title": "Metal Shingles", "desc": "Traditional look with metal durability"},
            {"icon": "sync-alt", "title": "Roof Replacement", "desc": "Replace old roofs with premium metal"},
            {"icon": "palette", "title": "Custom Colors", "desc": "Wide range of color and finish options"},
            {"icon": "tools", "title": "Metal Repair", "desc": "Expert metal roof repair and restoration"},
            {"icon": "certificate", "title": "Lifetime Warranty", "desc": "Manufacturer warranties up to 50 years"}
        ],
        "faq": [
            {
                "q": "How long does a metal roof last in {town}?",
                "a": "Metal roofs in {town} typically last 50-70 years with minimal maintenance—2-3 times longer than asphalt shingles. Premium metal roofing systems can last even longer. The durability comes from corrosion-resistant materials, superior fastening systems, and resistance to Essex County's weather extremes including heavy snow, ice, and summer heat."
            },
            {
                "q": "Is metal roofing noisy during rain or hail?",
                "a": "No! Modern metal roofing installed over solid decking with proper insulation is actually quieter than asphalt shingles during rain. The solid substrate and attic insulation dampen sound. Many {town} homeowners report they can't hear rain on their metal roofs. Professional installation is key to noise prevention."
            },
            {
                "q": "How much does metal roofing cost in {town}?",
                "a": "Metal roofing in {town} costs $700-$1,400 per square (100 sq ft) installed, depending on material type. A typical 2,000 sq ft home costs $14,000-$28,000. While more expensive upfront than asphalt, the 50+ year lifespan means lower lifetime cost. Metal roofs also increase home value and reduce insurance premiums."
            },
            {
                "q": "Will metal roofing increase my {town} home's value?",
                "a": "Yes! Metal roofing increases home value 1-6% and recoups 85-95% of installation cost at resale—higher than any other roofing material. {town} buyers value the longevity, energy efficiency, and low maintenance. Metal roofs also qualify for energy tax credits and insurance discounts."
            },
            {
                "q": "Can metal roofing handle New Jersey snow and ice?",
                "a": "Absolutely. Metal roofing excels in {town}'s winter weather. The smooth surface allows snow to slide off naturally, preventing dangerous ice dam formation. Metal roofs handle heavy snow loads better than asphalt and won't crack from freeze-thaw cycles. The interlocking panel design prevents wind-driven rain and snow infiltration."
            }
        ]
    },
    "flat-roofing": {
        "display_name": "Flat Roofing",
        "short_name": "Flat",
        "service_type": "Flat Roofing Installation",
        "description": "Commercial & residential flat roofing in {town}, NJ. TPO, EPDM, PVC membrane systems. Expert installation & repair. Licensed & insured. Call (667) 204-1609.",
        "hero_title": "Flat Roofing in {town}, NJ",
        "hero_subtitle": "Commercial & Residential Flat Roof Systems | TPO, EPDM & PVC Experts",
        "intro": "<p>Flat roofing systems are essential for {town}'s commercial buildings, modern homes, and additions requiring low-slope or flat roof solutions. R&E Roofing specializes in advanced membrane roofing systems including TPO, EPDM, and PVC that provide waterproof protection, energy efficiency, and long-term durability for {town} properties.</p>",
        "benefits": [
            {"icon": "water", "title": "Waterproof Protection", "desc": "Advanced membrane systems prevent leaks"},
            {"icon": "dollar-sign", "title": "Cost Efficient", "desc": "Lower installation costs than pitched roofs"},
            {"icon": "ruler-combined", "title": "Usable Space", "desc": "Roof deck access and HVAC equipment space"},
            {"icon": "sun", "title": "Energy Efficient", "desc": "White TPO reflects heat, reduces cooling costs"},
            {"icon": "tools", "title": "Easy Maintenance", "desc": "Simple inspection and repair access"},
            {"icon": "certificate", "title": "Long Warranties", "desc": "15-30 year manufacturer warranties available"}
        ],
        "services": [
            {"icon": "layer-group", "title": "TPO Roofing", "desc": "Heat-welded thermoplastic membrane systems"},
            {"icon": "shield-alt", "title": "EPDM Rubber", "desc": "Durable rubber membrane roofing"},
            {"icon": "droplet", "title": "PVC Membrane", "desc": "Premium chemical-resistant roofing"},
            {"icon": "compress-arrows-alt", "title": "Modified Bitumen", "desc": "Torch-down and self-adhered systems"},
            {"icon": "tint", "title": "Drainage Systems", "desc": "Proper slope and drainage solutions"},
            {"icon": "wrench", "title": "Flat Roof Repair", "desc": "Leak detection and membrane repair"}
        ],
        "faq": [
            {
                "q": "What type of flat roofing is best for {town} commercial buildings?",
                "a": "TPO (Thermoplastic Polyolefin) is the most popular choice for {town} commercial flat roofs due to its white reflective surface (energy efficiency), heat-welded seams (100% waterproof), and excellent value (15-20 year lifespan at moderate cost). EPDM rubber is best for budget-conscious projects, while PVC excels for restaurants and buildings with chemical exposure."
            },
            {
                "q": "How long do flat roofs last in {town}?",
                "a": "Properly installed flat roofing systems in {town} last 15-30 years depending on material. EPDM rubber lasts 15-25 years, TPO lasts 20-30 years, and premium PVC systems can last 30+ years. Regular maintenance and proper drainage are critical for longevity in Essex County's climate with heavy rain and snow."
            },
            {
                "q": "How much does flat roofing cost in {town}?",
                "a": "Flat roofing costs in {town} range $400-$800 per square (100 sq ft) installed. EPDM is most affordable at $400-$550/square, TPO costs $500-$700/square, and PVC is $600-$800/square. A typical 2,000 sq ft flat roof costs $8,000-$16,000. Commercial projects often include insulation, drainage improvements, and warranty upgrades."
            },
            {
                "q": "Do flat roofs leak more than pitched roofs?",
                "a": "No—when properly installed and maintained, modern flat roofing systems are highly waterproof. Heat-welded TPO and PVC seams are actually more watertight than shingle roofs. The key is proper installation with correct slope (1/4\" per foot minimum), quality drainage systems, and regular maintenance to prevent ponding water. R&E Roofing ensures leak-free flat roof installation."
            },
            {
                "q": "Can flat roofs handle {town}'s snow loads?",
                "a": "Yes. Flat roofs are engineered for {town}'s snow loads (30-40 lbs per square foot design load). The structural decking, not the membrane, supports snow weight. Proper insulation prevents ice dam formation, and we design drainage systems to handle snowmelt. Commercial flat roofs include snow load calculations in structural design."
            }
        ]
    },
    "tile-roofing": {
        "display_name": "Tile Roofing",
        "short_name": "Tile",
        "service_type": "Tile Roofing Installation",
        "description": "Premium tile roofing in {town}, NJ. Clay & concrete tile installation. Mediterranean & Spanish styles. 50-100 year lifespan. Licensed & insured. Call (667) 204-1609.",
        "hero_title": "Tile Roofing in {town}, NJ",
        "hero_subtitle": "Premium Clay & Concrete Tile Roofing | Mediterranean Elegance | 50-100 Year Lifespan",
        "intro": "<p>Tile roofing brings timeless Mediterranean elegance and unmatched durability to {town} homes. With a lifespan of 50-100 years, tile roofs are a lifetime investment that dramatically enhances curb appeal and property value. R&E Roofing specializes in clay and concrete tile installation, offering Spanish, Mediterranean, and contemporary profiles that complement {town}'s diverse architectural styles.</p>",
        "benefits": [
            {"icon": "infinity", "title": "50-100 Year Lifespan", "desc": "Clay tiles can last over a century"},
            {"icon": "fire", "title": "Fire Resistant", "desc": "Class A fire rating—non-combustible material"},
            {"icon": "home", "title": "Exceptional Curb Appeal", "desc": "Distinctive Mediterranean and Spanish aesthetics"},
            {"icon": "leaf", "title": "Eco-Friendly", "desc": "Natural materials, 100% recyclable"},
            {"icon": "shield-alt", "title": "Weather Resistant", "desc": "Withstands wind, hail, and extreme temperatures"},
            {"icon": "chart-line", "title": "Increases Home Value", "desc": "Premium roofing adds 10-15% to property value"}
        ],
        "services": [
            {"icon": "gem", "title": "Clay Tile Installation", "desc": "Authentic terracotta clay tile roofing"},
            {"icon": "cube", "title": "Concrete Tile", "desc": "Durable concrete tile in multiple colors"},
            {"icon": "palette", "title": "Custom Profiles", "desc": "Spanish S-tile, flat, and barrel profiles"},
            {"icon": "sync-alt", "title": "Tile Replacement", "desc": "Replace old or damaged tile roofs"},
            {"icon": "tools", "title": "Tile Repair", "desc": "Individual tile replacement and repairs"},
            {"icon": "hard-hat", "title": "Structural Assessment", "desc": "Roof structure evaluation for tile weight"}
        ],
        "faq": [
            {
                "q": "How long do tile roofs last in {town}?",
                "a": "Clay tile roofs in {town} can last 75-100+ years, while concrete tiles last 50-75 years. Tile is the longest-lasting roofing material available. Many European clay tile roofs are centuries old. In {town}, proper installation and occasional maintenance (replacing broken tiles) ensures your tile roof can outlast the house itself."
            },
            {
                "q": "Can my {town} home support the weight of tile roofing?",
                "a": "It depends on your home's structure. Tile roofing weighs 600-1,100 lbs per square (concrete tile) to 900-1,200 lbs per square (clay tile)—much heavier than asphalt. We provide free structural assessments to determine if your {town} home can support tile, or if structural reinforcement is needed. Many homes require roof framing upgrades before tile installation."
            },
            {
                "q": "How much does tile roofing cost in {town}?",
                "a": "Tile roofing in {town} costs $1,000-$2,500 per square installed. Concrete tiles cost $1,000-$1,500/square, while premium clay tiles cost $1,500-$2,500/square. A typical 2,000 sq ft home costs $20,000-$50,000. While expensive upfront, the 50-100 year lifespan means you'll never need another roof. Tile also adds significant resale value."
            },
            {
                "q": "Do tile roofs break easily in {town}'s weather?",
                "a": "Quality tile roofs are extremely durable. Modern tiles are rated for Class 4 hail impact and can withstand walking (when properly distributed). However, individual tiles can crack from severe hail or falling branches. The advantage is that damaged tiles can be individually replaced without replacing the entire roof—unlike asphalt shingles."
            },
            {
                "q": "What tile style works best for {town} homes?",
                "a": "Spanish S-tile suits Mediterranean and Spanish Colonial homes common in upscale {town} neighborhoods. Flat concrete tiles complement contemporary and modern homes. Barrel tiles work well with Mission-style architecture. We help match tile profile and color to your home's style. Many {town} homeowners choose terracotta or earth-tone colors for traditional appeal."
            }
        ]
    },
    "slate-roofing": {
        "display_name": "Slate Roofing",
        "short_name": "Slate",
        "service_type": "Slate Roofing Installation",
        "description": "Premium slate roofing in {town}, NJ. Natural stone slate installation & repair. 100+ year lifespan. Historic home specialists. Licensed & insured. Call (667) 204-1609.",
        "hero_title": "Slate Roofing in {town}, NJ",
        "hero_subtitle": "Premium Natural Slate Roofing | 100+ Year Lifespan | Historic Home Specialists",
        "intro": "<p>Slate roofing represents the pinnacle of roofing elegance and longevity—the premium choice for {town}'s historic estates, luxury homes, and homeowners seeking a lifetime roofing investment. Natural slate roofs can last 100-200 years, making them a true multi-generational investment. R&E Roofing specializes in authentic slate installation and restoration, preserving the architectural heritage of {town}'s most distinguished properties.</p>",
        "benefits": [
            {"icon": "infinity", "title": "100-200 Year Lifespan", "desc": "True lifetime roofing—lasts generations"},
            {"icon": "crown", "title": "Unmatched Elegance", "desc": "Natural stone beauty that improves with age"},
            {"icon": "fire", "title": "Fireproof", "desc": "Class A fire rating—natural stone is non-combustible"},
            {"icon": "leaf", "title": "100% Natural", "desc": "Eco-friendly quarried stone, no synthetic materials"},
            {"icon": "shield-alt", "title": "Weather Impervious", "desc": "Unaffected by freeze-thaw, rot, or insects"},
            {"icon": "chart-line", "title": "Maximum Property Value", "desc": "Premium roofing adds 15-20% to estate value"}
        ],
        "services": [
            {"icon": "gem", "title": "New Slate Installation", "desc": "Premium quarried slate roof systems"},
            {"icon": "history", "title": "Historic Restoration", "desc": "Preserve original slate on historic {town} homes"},
            {"icon": "tools", "title": "Slate Repair", "desc": "Individual slate replacement and repairs"},
            {"icon": "palette", "title": "Custom Patterns", "desc": "Decorative slate patterns and colors"},
            {"icon": "hard-hat", "title": "Structural Upgrades", "desc": "Roof framing reinforcement for slate weight"},
            {"icon": "search", "title": "Slate Inspection", "desc": "Comprehensive slate roof assessment"}
        ],
        "faq": [
            {
                "q": "How long do slate roofs last in {town}?",
                "a": "Quality slate roofs in {town} last 100-200 years—often outlasting the building itself. Many {town} historic homes still have their original slate roofs installed 100+ years ago. Soft slate lasts 50-125 years, while hard slate from premium quarries can exceed 200 years. Slate is the only roofing material that truly lasts multiple generations."
            },
            {
                "q": "Can my {town} home support a slate roof?",
                "a": "Slate roofing weighs 800-1,500 lbs per square—requiring robust structural support. Most {town} historic homes were originally built for slate and can support it. However, homes built for lighter materials need structural reinforcement. We provide free structural engineering assessments to determine if your {town} home can support slate or what upgrades are needed."
            },
            {
                "q": "How much does slate roofing cost in {town}?",
                "a": "Slate roofing in {town} costs $1,500-$4,000+ per square installed, making it the most expensive roofing material. A typical 2,000 sq ft home costs $30,000-$80,000+. Premium quarry slate with custom installation can exceed $100,000 for estate homes. However, the 100-200 year lifespan means it's the last roof you'll ever need—often cheaper lifetime cost than replacing asphalt every 20 years."
            },
            {
                "q": "Can damaged slate tiles be repaired?",
                "a": "Yes! Individual slate tiles can be carefully removed and replaced by experienced craftsmen without disturbing surrounding slates. R&E Roofing specializes in slate repair using traditional copper hooks and matching quarry sources. Many {town} slate roofs just need 10-20% tile replacement to extend life another 50-75 years—much more affordable than full replacement."
            },
            {
                "q": "What color slate options are available for {town} homes?",
                "a": "Natural slate comes in beautiful earth tones: gray, black, green, purple, red, and mottled blends. {town} historic homes often feature Unfading Green Vermont slate, purple Welsh slate, or classic Pennsylvania black. We can match existing slate or create custom color patterns. Each quarry produces unique colors—we help select slate that complements your {town} home's architecture and neighborhood character."
            }
        ]
    }
}

def generate_page(material_key, material_data, town):
    """Generate a single material-specific roofing page."""

    town_name = town["name"]
    town_slug = town_name.lower().replace(" ", "-")
    material_slug = material_key
    filename = f"{material_slug}-{town_slug}-nj.html"

    # Replace town placeholders in text
    def replace_town(text):
        return text.replace("{town}", town_name)

    # Build HTML content
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{material_data["display_name"]} {town_name}, NJ | Expert Installation | R&E Roofing</title>

    <!-- SEO Meta Tags -->
    <meta name="description" content="{replace_town(material_data["description"])}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="R&E Roofing">

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{material_data["display_name"]} {town_name}, NJ | Expert Installation | R&E Roofing">
    <meta property="og:description" content="{replace_town(material_data["description"])}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://randeroofing.com/{filename}">
    <meta property="og:image" content="https://randeroofing.com/images/og-image.jpg">
    <meta property="og:site_name" content="R&E Roofing">
    <meta property="og:locale" content="en_US">

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{material_data["display_name"]} {town_name}, NJ | Expert Installation | R&E Roofing">
    <meta name="twitter:description" content="{replace_town(material_data["description"])}">
    <meta name="twitter:image" content="https://randeroofing.com/images/twitter-card.jpg">

    <!-- Canonical URL -->
    <link rel="canonical" href="https://randeroofing.com/{filename}">

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/logo.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/images/logo.png">

    <!-- Service Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "{material_data["service_type"]}",
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
                "latitude": "{town["lat"]}",
                "longitude": "{town["lon"]}"
            }}
        }},
        "description": "{replace_town(material_data["description"])}",
        "url": "https://randeroofing.com/{filename}"
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
            "name": "{material_data["display_name"]} in {town_name}",
            "item": "https://randeroofing.com/{filename}"
        }}]
    }}
    </script>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght=800&family=Overpass:wght=400;900&display=swap" rel="stylesheet">

    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg==" crossorigin="anonymous">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <!-- Contact Form Modal -->
    <div id="contactModal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <h2>Request {material_data["display_name"]} Quote</h2>
            <p>Fill out the form below for a free estimate</p>
            <form id="contactForm" class="contact-form">
                <div class="form-row">
                    <div class="form-group">
                        <label for="firstName">First Name*</label>
                        <input type="text" id="firstName" name="firstName" required>
                    </div>
                    <div class="form-group">
                        <label for="lastName">Last Name*</label>
                        <input type="text" id="lastName" name="lastName" required>
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="email">Email*</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone*</label>
                        <input type="tel" id="phone" name="phone" required>
                    </div>
                </div>
                <div class="form-group">
                    <label for="service">Service Needed*</label>
                    <select id="service" name="service" required>
                        <option value="">Select a service</option>
                        <option value="{material_key}" selected>{material_data["display_name"]}</option>
                        <option value="roof-repair">Roof Repair</option>
                        <option value="roof-replacement">Roof Replacement</option>
                        <option value="roof-inspection">Roof Inspection</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="address">Property Address</label>
                    <input type="text" id="address" name="address" placeholder="{town_name}, NJ">
                </div>
                <div class="form-group">
                    <label for="message">Project Details*</label>
                    <textarea id="message" name="message" rows="4" placeholder="Tell us about your {material_data["short_name"].lower()} roofing project..." required></textarea>
                </div>
                <div class="form-group">
                    <label for="preferred-contact">Preferred Contact Method</label>
                    <div class="radio-group">
                        <label><input type="radio" name="contact-method" value="phone" checked> Phone</label>
                        <label><input type="radio" name="contact-method" value="email"> Email</label>
                        <label><input type="radio" name="contact-method" value="text"> Text</label>
                    </div>
                </div>
                <div class="form-group consent-group">
                    <input type="checkbox" id="gdprConsent" name="gdprConsent" required>
                    <label for="gdprConsent">
                        I agree to the <a href="/privacy-policy.html" target="_blank">Privacy Policy</a>
                        and consent to my data being processed for the purpose of this inquiry.
                    </label>
                </div>
                <button type="submit" class="btn-primary submit-btn">Get Free Quote</button>
                <p class="form-disclaimer">*We respect your privacy and will never share your information.</p>
            </form>
        </div>
    </div>

    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <img src="images/logo.png" alt="R&E Roofing" class="logo-img">
                </div>

                <!-- Navigation Menu -->
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

                <div class="header-right">
                    <div class="phone-number">
                        <i class="fas fa-phone"></i>
                        <span>(667) 204-1609</span>
                    </div>
                    <button class="cta-button">Get Free Quote</button>

                    <!-- Mobile Phone Icon (visible only on mobile) -->
                    <a href="tel:6672041609" class="mobile-phone-icon" aria-label="Call R&E Roofing">
                        <i class="fas fa-phone"></i>
                    </a>

                    <!-- Mobile Menu Toggle -->
                    <button class="mobile-menu-toggle" aria-label="Toggle Menu">
                        <span class="hamburger"></span>
                        <span class="hamburger"></span>
                        <span class="hamburger"></span>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Navigation -->
        <div class="mobile-nav">
            <ul class="mobile-nav-menu">
                <li><a href="index.html" class="mobile-nav-link">Home</a></li>
                <li>
                    <a href="services.html" class="mobile-nav-link has-submenu">Services <i class="fas fa-chevron-down"></i></a>
                    <ul class="mobile-submenu">
                        <li><a href="services.html">All Services</a></li>
                        <li><a href="calculator.html">Get Quote</a></li>
                        <li><a href="faq.html">FAQs</a></li>
                    </ul>
                </li>
                <li><a href="about.html" class="mobile-nav-link">About</a></li>
                <li><a href="reviews.html" class="mobile-nav-link">Reviews</a></li>
                <li><a href="blog.html" class="mobile-nav-link">Blog</a></li>
                <li class="mobile-cta">
                    <button class="cta-button mobile-quote-btn">Get Free Quote</button>
                </li>
            </ul>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-video-container">
            <video autoplay muted loop playsinline class="hero-video">
                <source src="https://youngconstructionnorthiowa.com/wp-content/uploads/2024/11/young-construction-homepage-video.mp4" type="video/mp4">
                <source src="videos/roofing-background.mp4" type="video/mp4">
            </video>
        </div>
        <div class="hero-overlay"></div>
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title">{replace_town(material_data["hero_title"])}</h1>
                <p class="hero-subtitle">{replace_town(material_data["hero_subtitle"])}</p>
                <div class="hero-buttons">
                    <a href="tel:6672041609" class="btn-primary">
                        <i class="fas fa-phone"></i>
                        Call (667) 204-1609
                    </a>
                    <button class="btn-outline-white">Get Free Quote</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Service Details Section -->
    <section class="service-details-section">
        <div class="container">
            <div class="section-header">
                <h2>{material_data["display_name"]} Services in {town_name}</h2>
                <p>Expert {material_data["short_name"].lower()} roof installation and repair</p>
            </div>

            <div class="service-details">
                {replace_town(material_data["intro"])}

                <h3>Our {material_data["display_name"]} Services:</h3>
                <div class="services-grid">'''

    # Add services grid
    for service in material_data["services"]:
        html += f'''
                    <div class="service-item">
                        <i class="fas fa-{service["icon"]}"></i>
                        <h4>{service["title"]}</h4>
                        <p>{service["desc"]}</p>
                    </div>'''

    html += '''
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us Section -->
    <section class="why-choose-us">
        <div class="container">
            <h2>Why Choose {material_short} Roofing for Your {town} Home?</h2>
            <div class="benefits-grid">'''.format(material_short=material_data["short_name"], town=town_name)

    # Add benefits grid
    for benefit in material_data["benefits"]:
        html += f'''
                <div class="benefit-item">
                    <i class="fas fa-{benefit["icon"]}"></i>
                    <h3>{benefit["title"]}</h3>
                    <p>{benefit["desc"]}</p>
                </div>'''

    html += f'''
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
        <div class="container">
            <div class="section-header">
                <h2>{material_data["display_name"]} FAQs</h2>
                <p>Common questions from {town_name} homeowners</p>
            </div>
            <div class="faq-container">'''

    # Add FAQ items
    for faq in material_data["faq"]:
        html += f'''
                <div class="faq-item">
                    <button class="faq-question">
                        <span>{replace_town(faq["q"])}</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p>{replace_town(faq["a"])}</p>
                    </div>
                </div>'''

    html += f'''
            </div>
        </div>
    </section>

    <!-- More Services Section -->
    <section class="more-services-section">
        <div class="container">
            <h2>More {town_name} Roofing Services</h2>
            <p class="section-subtitle">Explore our complete range of roofing, siding, and gutter services</p>
            <div class="services-grid-enhanced">
                <a href="roof-repair-{town_slug}-nj.html" class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-tools"></i>
                    </div>
                    <h3>Roof Repair</h3>
                    <p>Expert repair services</p>
                </a>
                <a href="roof-replacement-{town_slug}-nj.html" class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-sync-alt"></i>
                    </div>
                    <h3>Roof Replacement</h3>
                    <p>Complete roof replacement</p>
                </a>
                <a href="new-roof-installation-{town_slug}-nj.html" class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-hammer"></i>
                    </div>
                    <h3>New Installation</h3>
                    <p>New roof systems</p>
                </a>
                <a href="siding-installation-{town_slug}-nj.html" class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-layer-group"></i>
                    </div>
                    <h3>Siding Installation</h3>
                    <p>Professional siding work</p>
                </a>
                <a href="siding-repair-{town_slug}-nj.html" class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-wrench"></i>
                    </div>
                    <h3>Siding Repair</h3>
                    <p>Fix damaged siding</p>
                </a>
                <a href="gutter-installation-{town_slug}-nj.html" class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-water"></i>
                    </div>
                    <h3>Gutter Installation</h3>
                    <p>Seamless gutter systems</p>
                </a>
                <a href="gutter-repair-cleaning-{town_slug}-nj.html" class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-brush"></i>
                    </div>
                    <h3>Gutter Repair & Cleaning</h3>
                    <p>Gutter maintenance</p>
                </a>
                <a href="emergency-roof-repair-{town_slug}-nj.html" class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-exclamation-triangle"></i>
                    </div>
                    <h3>Emergency Repair</h3>
                    <p>24/7 urgent service</p>
                </a>
                <a href="roofing-{town_slug}-nj.html" class="service-card overview-card">
                    <div class="service-icon">
                        <i class="fas fa-th-large"></i>
                    </div>
                    <h3>All {town_name} Services</h3>
                    <p>View complete service list</p>
                </a>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
        <div class="container">
            <h2>Ready for {material_data["display_name"]} in {town_name}?</h2>
            <p>Get a free quote from Essex County's trusted roofing experts. Licensed, insured, and 25+ years experience.</p>
            <div class="cta-buttons">
                <a href="tel:6672041609" class="btn-primary">
                    <i class="fas fa-phone"></i>
                    Call (667) 204-1609
                </a>
                <button class="btn-outline">Request Free Quote</button>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-left">
                    <div class="footer-logo">
                        <h3>R&E ROOFING</h3>
                    </div>
                    <p>Your trusted roofing experts providing quality services for over 25 years.</p>
                    <p class="footer-license">Licensed & Insured in New Jersey</p>
                </div>

                <div class="footer-middle">
                    <div class="footer-service-areas">
                        <h4>Service Areas</h4>
                        <ul class="service-areas-list">
                            <li>Newark, NJ</li>
                            <li>East Orange, NJ</li>
                            <li>Irvington, NJ</li>
                            <li>Bloomfield, NJ</li>
                            <li>West Orange, NJ</li>
                            <li>Montclair, NJ</li>
                            <li>Belleville, NJ</li>
                            <li>Orange, NJ</li>
                            <li>Livingston, NJ</li>
                            <li>Nutley, NJ</li>
                        </ul>
                        <p class="all-essex">+ All of Essex County</p>
                    </div>
                </div>

                <div class="footer-right">
                    <div class="footer-contact">
                        <h4>Contact Info</h4>
                        <div class="contact-item">
                            <i class="fas fa-phone"></i>
                            <span>(667) 204-1609</span>
                        </div>
                        <div class="contact-item">
                            <i class="fas fa-envelope"></i>
                            <span>info@randeroofing.com</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="footer-bottom">
                <div class="footer-legal">
                    <a href="privacy-policy.html">Privacy Policy</a> |
                    <a href="terms-of-service.html">Terms of Service</a>
                </div>
                <p>&copy; 2024 R&E Roofing. All rights reserved. | Serving Essex County, NJ</p>
            </div>
        </div>
    </footer>

    <!-- JavaScript -->
    <script src="js/main.js"></script>

    <!-- Cookie Consent Banner -->
    <div id="cookieConsent" class="cookie-consent" style="display:none;">
        <p>We use cookies to improve your experience. By continuing, you accept our <a href="/privacy-policy.html">Privacy Policy</a>.</p>
        <button onclick="acceptCookies()">Accept</button>
    </div>

    <!-- Back to Top Button -->
    <button id="backToTop" class="back-to-top" aria-label="Back to top">
        <i class="fas fa-chevron-up"></i>
    </button>

</body>
</html>'''

    return filename, html


def main():
    """Generate all 75 material-specific pages."""
    output_dir = "/Users/charwinvanryckdegroot/Github/re-roofing-website"
    files_created = []

    print("Generating 75 material-specific roofing pages...")
    print("=" * 60)

    for material_key, material_data in MATERIALS.items():
        print(f"\n{material_data['display_name']}:")
        for town in TOWNS:
            filename, html = generate_page(material_key, material_data, town)
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)

            files_created.append(filename)
            print(f"  ✓ {filename}")

    print("\n" + "=" * 60)
    print(f"✅ Successfully created {len(files_created)} pages")
    print("\nFiles created:")
    for i, filename in enumerate(files_created, 1):
        print(f"{i}. {filename}")

    return len(files_created)


if __name__ == "__main__":
    total_files = main()
    print(f"\n🎉 Phase 2 Complete: {total_files} material-specific pages generated!")
