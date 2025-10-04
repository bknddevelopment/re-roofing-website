#!/usr/bin/env python3
"""
Update all town pages with comprehensive service grid
"""

import os
import re
from pathlib import Path

# Service definitions
SERVICES = [
    {
        'id': 'emergency',
        'file': 'emergency-roof-repair',
        'icon': 'fa-exclamation-triangle',
        'title': 'Emergency Repair',
        'description': '24/7 urgent service'
    },
    {
        'id': 'leak',
        'file': 'roof-leak-repair',
        'icon': 'fa-tint',
        'title': 'Leak Detection & Repair',
        'description': 'Stop water damage fast'
    },
    {
        'id': 'repair',
        'file': 'roof-repair',
        'icon': 'fa-tools',
        'title': 'Roof Repair',
        'description': 'Expert repair services'
    },
    {
        'id': 'replacement',
        'file': 'roof-replacement',
        'icon': 'fa-sync-alt',
        'title': 'Roof Replacement',
        'description': 'Complete roof replacement'
    },
    {
        'id': 'installation',
        'file': 'new-roof-installation',
        'icon': 'fa-hammer',
        'title': 'New Installation',
        'description': 'New roof systems'
    },
    {
        'id': 'siding',
        'file': 'siding-installation',
        'icon': 'fa-layer-group',
        'title': 'Siding Installation',
        'description': 'Professional siding work'
    },
    {
        'id': 'siding-repair',
        'file': 'siding-repair',
        'icon': 'fa-wrench',
        'title': 'Siding Repair',
        'description': 'Fix damaged siding'
    },
    {
        'id': 'gutters',
        'file': 'gutter-installation',
        'icon': 'fa-water',
        'title': 'Gutter Installation',
        'description': 'Seamless gutter systems'
    }
]

def extract_town_from_filename(filename):
    """Extract town slug from filename"""
    match = re.search(r'-([\w-]+)-nj\.html$', filename)
    return match.group(1) if match else None

def format_town_name(slug):
    """Convert slug to proper town name"""
    return slug.replace('-', ' ').title()

def generate_service_grid(town_slug, town_name, current_service_file):
    """Generate HTML for service grid"""

    service_cards = []
    for service in SERVICES:
        url = f"{service['file']}-{town_slug}-nj.html"
        is_current = service['file'] in current_service_file

        card = f'''            <a href="{url}" class="service-card{' current-service' if is_current else ''}">
                <div class="service-icon">
                    <i class="fas {service['icon']}"></i>
                </div>
                <h3>{service['title']}</h3>
                <p>{service['description']}</p>
            </a>'''
        service_cards.append(card)

    # Add overview card
    overview_card = f'''            <a href="roofing-{town_slug}-nj.html" class="service-card overview-card">
                <div class="service-icon">
                    <i class="fas fa-th-large"></i>
                </div>
                <h3>All {town_name} Services</h3>
                <p>View complete service list</p>
            </a>'''
    service_cards.append(overview_card)

    grid_html = f'''
    <!-- More {town_name} Services -->
    <section class="more-services-section">
        <div class="container">
            <h2>More {town_name} Roofing Services</h2>
            <p class="section-subtitle">Explore our complete range of roofing, siding, and gutter services</p>
            <div class="services-grid-enhanced">
{chr(10).join(service_cards)}
            </div>
        </div>
    </section>'''

    return grid_html

def update_page(filepath):
    """Update a single page with new service grid"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    town_slug = extract_town_from_filename(filename)

    if not town_slug:
        return False

    town_name = format_town_name(town_slug)

    # Find and replace existing Related Services section
    # Pattern matches from <!-- Related Services --> to </section>
    pattern = r'<!-- Related Services Section -->.*?</section>'

    if not re.search(pattern, content, re.DOTALL):
        # Try alternate pattern
        pattern = r'<section class="related-services">.*?</section>'

    new_grid = generate_service_grid(town_slug, town_name, filename)

    # Replace the section
    updated_content = re.sub(pattern, new_grid.strip(), content, flags=re.DOTALL)

    # If no match found, insert before CTA section
    if updated_content == content:
        cta_pattern = r'<!-- CTA Section -->'
        updated_content = re.sub(cta_pattern, f'{new_grid}\n\n    <!-- CTA Section -->', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return True

def add_css_styles():
    """Add enhanced service grid styles to CSS"""

    css_path = 'css/styles.css'

    css_addition = '''
/* Enhanced Service Grid */
.more-services-section {
    padding: 80px 0;
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
}

.more-services-section h2 {
    text-align: center;
    font-size: 36px;
    margin-bottom: 12px;
    color: #000;
}

.section-subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 48px;
}

.services-grid-enhanced {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    max-width: 1200px;
    margin: 0 auto;
}

.services-grid-enhanced .service-card {
    background: white;
    padding: 32px 24px;
    border-radius: 16px;
    text-align: center;
    text-decoration: none;
    color: #333;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border: 2px solid transparent;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    position: relative;
    overflow: hidden;
}

.services-grid-enhanced .service-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #FF6B35, #FF3B30);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.services-grid-enhanced .service-card:hover::before {
    transform: scaleX(1);
}

.services-grid-enhanced .service-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
    border-color: #FF6B35;
}

.services-grid-enhanced .service-card.current-service {
    border-color: #FF6B35;
    background: linear-gradient(135deg, #fff5f2 0%, #ffffff 100%);
}

.services-grid-enhanced .service-card.current-service::before {
    transform: scaleX(1);
}

.service-icon {
    width: 72px;
    height: 72px;
    margin: 0 auto 20px;
    background: linear-gradient(135deg, #FF6B35 0%, #FF3B30 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
}

.services-grid-enhanced .service-card:hover .service-icon {
    transform: scale(1.1) rotate(5deg);
}

.service-icon i {
    font-size: 32px;
    color: white;
}

.services-grid-enhanced .service-card h3 {
    font-size: 20px;
    margin-bottom: 8px;
    color: #000;
}

.services-grid-enhanced .service-card p {
    font-size: 14px;
    color: #666;
    margin: 0;
}

.overview-card {
    background: linear-gradient(135deg, #000 0%, #333 100%) !important;
    color: white !important;
}

.overview-card h3,
.overview-card p {
    color: white !important;
}

.overview-card .service-icon {
    background: white !important;
}

.overview-card .service-icon i {
    color: #000 !important;
}

@media (max-width: 768px) {
    .services-grid-enhanced {
        grid-template-columns: 1fr;
        gap: 16px;
    }

    .more-services-section {
        padding: 60px 0;
    }

    .more-services-section h2 {
        font-size: 28px;
    }
}
'''

    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()

    # Check if already added
    if 'services-grid-enhanced' not in css_content:
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write(css_addition)
        return True

    return False

# Main execution
if __name__ == '__main__':
    # Get all town pages
    town_pages = list(Path('.').glob('*-*-nj.html'))

    print(f"Found {len(town_pages)} town pages")

    updated = 0
    for page in town_pages:
        if update_page(page):
            updated += 1
            print(f"Updated: {page.name}")

    print(f"\nUpdated {updated} pages")

    # Add CSS
    if add_css_styles():
        print("Added CSS styles")
    else:
        print("CSS styles already present")

    print("\n✅ Service grid update complete!")
