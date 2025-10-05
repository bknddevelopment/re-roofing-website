#!/bin/bash

# Fix broken town cross-links in all town pages

for file in pages/towns/roofing-*.html; do
    # Extract town name from filename
    town=$(basename "$file" .html | sed 's/roofing-//')

    # Fix area links - add /pages/towns/ prefix
    sed -i '' \
        -e "s|href=\"newark-nj\.html\"|href=\"/pages/towns/roofing-newark-nj.html\"|g" \
        -e "s|href=\"orange-nj\.html\"|href=\"/pages/towns/roofing-east-orange-nj.html\"|g" \
        -e "s|href=\"irvington-nj\.html\"|href=\"/pages/towns/roofing-irvington-nj.html\"|g" \
        -e "s|href=\"bloomfield-nj\.html\"|href=\"/pages/towns/roofing-bloomfield-nj.html\"|g" \
        -e "s|href=\"montclair-nj\.html\"|href=\"/pages/towns/roofing-montclair-nj.html\"|g" \
        -e "s|href=\"belleville-nj\.html\"|href=\"/pages/towns/roofing-belleville-nj.html\"|g" \
        -e "s|href=\"livingston-nj\.html\"|href=\"/pages/towns/roofing-livingston-nj.html\"|g" \
        -e "s|href=\"nutley-nj\.html\"|href=\"/pages/towns/roofing-nutley-nj.html\"|g" \
        -e "s|href=\"maplewood-nj\.html\"|href=\"/pages/towns/roofing-maplewood-nj.html\"|g" \
        -e "s|href=\"verona-nj\.html\"|href=\"/pages/towns/roofing-verona-nj.html\"|g" \
        -e "s|href=\"millburn-nj\.html\"|href=\"/pages/towns/roofing-millburn-nj.html\"|g" \
        -e "s|href=\"cedar-grove-nj\.html\"|href=\"/pages/towns/roofing-cedar-grove-nj.html\"|g" \
        -e "s|href=\"west-orange-nj\.html\"|href=\"/pages/towns/roofing-west-orange-nj.html\"|g" \
        -e "s|href=\"south-orange-nj\.html\"|href=\"/pages/towns/roofing-south-orange-nj.html\"|g" \
        -e "s|href=\"east-orange-nj\.html\"|href=\"/pages/towns/roofing-east-orange-nj.html\"|g" \
        "$file"
done

echo "Town cross-links fixed!"
