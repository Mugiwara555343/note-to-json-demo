#!/usr/bin/env python3
"""
run_demo.py

Manually parse all .md files in the current directory to .parsed.json
"""

import sys
from pathlib import Path
from memory_parser import parse_md_file

def main():
    """Parse all .md files in the demo_entries folder"""
    current_dir = Path(__file__).parent
    
    print("🔍 Scanning for .md files...")
    md_files = []
    
    # Only scan demo_entries folder
    demo_dir = current_dir / "demo_entries"
    if demo_dir.exists():
        md_files = list(demo_dir.glob("*.md"))
    else:
        print("❌ demo_entries/ folder not found")
        return
    
    if not md_files:
        print("❌ No .md files found in current directory")
        return
    
    print(f"📝 Found {len(md_files)} .md file(s)")
    
    for md_file in md_files:
        try:
            print(f"\n🔄 Parsing: {md_file.name}")
            parsed_data = parse_md_file(md_file)
            
            # Save to .parsed.json
            output_file = md_file.with_suffix(".parsed.json")
            import json
            output_file.write_text(
                json.dumps(parsed_data, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )
            print(f"✅ Created: {output_file.name}")
            
        except Exception as e:
            print(f"❌ Error parsing {md_file.name}: {e}")
    
    print(f"\n🎉 Demo complete! Check the generated .parsed.json files.")

if __name__ == "__main__":
    main() 