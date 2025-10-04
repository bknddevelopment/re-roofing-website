#!/usr/bin/env python3
"""
Update sitemap.xml with Phase 3 Pages
Adds 45 new entries (3 services × 15 towns)
"""

from datetime import datetime

SERVICES = ['commercial-roofing', 'roofing-financing', 'roof-insurance-claims']
TOWNS = [
    'newark', 'east-orange', 'irvington', 'bloomfield', 'west-orange',
    'montclair', 'belleville', 'orange', 'livingston', 'nutley',
    'maplewood', 'millburn', 'south-orange', 'verona', 'cedar-grove'
]

def generate_sitemap_entries():
    """Generate sitemap entries for all Phase 3 pages"""
    today = datetime.now().strftime('%Y-%m-%d')
    entries = []

    entries.append("\n    <!-- Phase 3: Commercial & Financing Pages (45 pages) -->\n")

    service_names = {
        'commercial-roofing': 'Commercial Roofing',
        'roofing-financing': 'Roofing Financing',
        'roof-insurance-claims': 'Roof Insurance Claims'
    }

    for service in SERVICES:
        service_display = service_names[service]
        entries.append(f"    <!-- {service_display} Pages (15 towns) -->\n")

        for town in TOWNS:
            url = f"https://randeroofing.com/pages/services/{service}-{town}-nj.html"
            entry = f"""    <url>
        <loc>{url}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
"""
            entries.append(entry)

        entries.append("\n")

    return ''.join(entries)

def main():
    """Read sitemap, add Phase 3 entries, write back"""
    print("📝 Updating sitemap.xml with Phase 3 commercial & financing pages...")

    # Read existing sitemap
    with open('sitemap.xml', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find insertion point (before closing </urlset>)
    if '</urlset>' not in content:
        print("❌ Error: Invalid sitemap.xml format")
        return

    # Generate new entries
    new_entries = generate_sitemap_entries()

    # Insert before closing tag
    updated_content = content.replace('</urlset>', new_entries + '</urlset>')

    # Write updated sitemap
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"✅ Sitemap updated successfully!")
    print(f"📊 Added 45 new entries:")
    print(f"   - 15 commercial roofing pages")
    print(f"   - 15 roofing financing pages")
    print(f"   - 15 roof insurance claims pages")
    print(f"\n🌐 All entries set to:")
    print(f"   - Priority: 0.9 (high)")
    print(f"   - Change frequency: monthly")
    print(f"   - Last modified: {datetime.now().strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
