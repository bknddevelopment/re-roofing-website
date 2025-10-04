#!/usr/bin/env python3
"""
Batch page generator for Emergency & Leak Repair pages
Creates 28 HTML pages (14 towns × 2 services)
"""

import os

# Town data with coordinates
TOWNS = {
    "Newark": {"lat": "40.7357", "lon": "-74.1724"},
    "East Orange": {"lat": "40.7674", "lon": "-74.2049"},
    "Irvington": {"lat": "40.7323", "lon": "-74.2346"},
    "Bloomfield": {"lat": "40.8068", "lon": "-74.1854"},
    "West Orange": {"lat": "40.7987", "lon": "-74.2390"},
    "Montclair": {"lat": "40.8259", "lon": "-74.2090"},
    "Belleville": {"lat": "40.7937", "lon": "-74.1501"},
    "Livingston": {"lat": "40.7959", "lon": "-74.3149"},
    "Nutley": {"lat": "40.8223", "lon": "-74.1599"},
    "Maplewood": {"lat": "40.7312", "lon": "-74.2735"},
    "Millburn": {"lat": "40.7296", "lon": "-74.3043"},
    "South Orange": {"lat": "40.7490", "lon": "-74.2613"},
    "Verona": {"lat": "40.8298", "lon": "-74.2404"},
    "Cedar Grove": {"lat": "40.8534", "lon": "-74.2282"}
}

def town_to_slug(town_name):
    """Convert town name to URL slug (e.g., 'East Orange' -> 'east-orange')"""
    return town_name.lower().replace(" ", "-")

def read_template(template_path):
    """Read template file"""
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def replace_town_data(content, old_town, new_town, coords, service_type):
    """Replace town name and coordinates in template"""
    old_slug = town_to_slug(old_town)
    new_slug = town_to_slug(new_town)

    # Replace all instances of old town with new town
    result = content.replace(old_town, new_town)
    result = result.replace(old_slug, new_slug)

    # Replace coordinates
    result = result.replace('"40.7679"', f'"{coords["lat"]}"')
    result = result.replace('"-74.2326"', f'"{coords["lon"]}"')

    return result

def generate_emergency_pages():
    """Generate emergency roof repair pages for all towns"""
    template_path = "/Users/charwinvanryckdegroot/Github/re-roofing-website/emergency-roof-repair-orange-nj.html"
    template = read_template(template_path)

    files_created = []

    for town, coords in TOWNS.items():
        slug = town_to_slug(town)
        filename = f"/Users/charwinvanryckdegroot/Github/re-roofing-website/emergency-roof-repair-{slug}-nj.html"

        # Replace Orange with new town
        content = replace_town_data(template, "Orange", town, coords, "emergency")

        # Write file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        files_created.append(filename)
        print(f"✓ Created: emergency-roof-repair-{slug}-nj.html")

    return files_created

def generate_leak_pages():
    """Generate roof leak repair pages for all towns"""
    template_path = "/Users/charwinvanryckdegroot/Github/re-roofing-website/roof-leak-repair-orange-nj.html"
    template = read_template(template_path)

    files_created = []

    for town, coords in TOWNS.items():
        slug = town_to_slug(town)
        filename = f"/Users/charwinvanryckdegroot/Github/re-roofing-website/roof-leak-repair-{slug}-nj.html"

        # Replace Orange with new town
        content = replace_town_data(template, "Orange", town, coords, "leak")

        # Write file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        files_created.append(filename)
        print(f"✓ Created: roof-leak-repair-{slug}-nj.html")

    return files_created

def main():
    print("=" * 60)
    print("Generating Emergency & Leak Repair Pages")
    print("=" * 60)

    print("\n[1/2] Generating Emergency Roof Repair Pages...")
    emergency_files = generate_emergency_pages()

    print(f"\n[2/2] Generating Roof Leak Repair Pages...")
    leak_files = generate_leak_pages()

    all_files = emergency_files + leak_files

    print("\n" + "=" * 60)
    print(f"✓ Successfully created {len(all_files)} pages")
    print("=" * 60)

    # Print summary
    print("\nEmergency Roof Repair Pages (14):")
    for f in emergency_files:
        print(f"  - {os.path.basename(f)}")

    print("\nRoof Leak Repair Pages (14):")
    for f in leak_files:
        print(f"  - {os.path.basename(f)}")

if __name__ == "__main__":
    main()
