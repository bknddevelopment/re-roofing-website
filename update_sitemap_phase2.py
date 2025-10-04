#!/usr/bin/env python3
"""
Update sitemap.xml with Phase 2 Material-Specific Pages
Adds 75 new entries (5 materials × 15 towns)
"""

from datetime import datetime

MATERIALS = ['asphalt-shingle', 'metal', 'flat', 'tile', 'slate']
TOWNS = [
    'newark', 'east-orange', 'irvington', 'bloomfield', 'west-orange',
    'montclair', 'belleville', 'orange', 'livingston', 'nutley',
    'maplewood', 'millburn', 'south-orange', 'verona', 'cedar-grove'
]

def generate_sitemap_entries():
    """Generate sitemap entries for all material pages"""
    today = datetime.now().strftime('%Y-%m-%d')
    entries = []

    entries.append("\n    <!-- Phase 2: Material-Specific Roofing Pages (75 pages) -->\n")

    for material in MATERIALS:
        material_display = material.replace('-', ' ').title()
        entries.append(f"    <!-- {material_display} Roofing Pages (15 towns) -->\n")

        for town in TOWNS:
            url = f"https://randeroofing.com/{material}-roofing-{town}-nj.html"
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
    """Read sitemap, add Phase 2 entries, write back"""
    print("📝 Updating sitemap.xml with Phase 2 material-specific pages...")

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
    print(f"📊 Added 75 new entries:")
    print(f"   - 15 asphalt shingle roofing pages")
    print(f"   - 15 metal roofing pages")
    print(f"   - 15 flat roofing pages")
    print(f"   - 15 tile roofing pages")
    print(f"   - 15 slate roofing pages")
    print(f"\n🌐 All entries set to:")
    print(f"   - Priority: 0.9 (high)")
    print(f"   - Change frequency: monthly")
    print(f"   - Last modified: {datetime.now().strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
