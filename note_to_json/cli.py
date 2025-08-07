#!/usr/bin/env python3
"""
note_to_json.cli

Command-line interface for the note-to-json parser.
"""

import argparse
import json
import sys
from pathlib import Path
from .parser import parse_file


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Convert markdown files to structured JSON",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  note2json input.md                    # Parse to input.parsed.json
  note2json input.md -o output.json    # Parse to custom output file
  note2json *.md                       # Parse multiple files
        """
    )
    
    parser.add_argument(
        "input_file",
        nargs="+",
        help="Markdown file(s) to parse"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: input.parsed.json)"
    )
    
    args = parser.parse_args()
    
    # Process each input file
    for input_path_str in args.input_file:
        input_path = Path(input_path_str)
        
        if not input_path.exists():
            print(f"Error: File not found: {input_path}", file=sys.stderr)
            continue
            
        if not input_path.suffix.lower() == ".md":
            print(f"Warning: File doesn't have .md extension: {input_path}", file=sys.stderr)
        
        try:
            # Parse the file
            parsed_data = parse_file(input_path)
            
            # Determine output path
            if args.output:
                if len(args.input_file) > 1:
                    print(f"Error: --output can only be used with a single input file", file=sys.stderr)
                    sys.exit(1)
                output_path = Path(args.output)
            else:
                output_path = input_path.with_suffix(".parsed.json")
            
            # Write output
            output_path.write_text(
                json.dumps(parsed_data, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )
            
            print(f"✅ Parsed: {input_path.name} → {output_path.name}")
            
        except Exception as e:
            print(f"❌ Error parsing {input_path.name}: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
