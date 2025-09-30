"""
Extract content under '# Protocol' heading and remove MyST directive blocks.
"""

import re
import sys

def extract_protocol_section(content):
    """Extract everything under the '# Protocol' heading."""
    lines = content.split('\n')
    protocol_lines = []
    in_protocol = False
    
    for line in lines:
        # Check if we've reached the Protocol heading
        if line.strip() == '# Protocol':
            in_protocol = True
            protocol_lines.append(line)
            continue
        
        # Stop if we hit another level 1 heading
        if in_protocol and line.startswith('# ') and line.strip() != '# Protocol':
            break
        
        # Collect lines if we're in the Protocol section
        if in_protocol:
            protocol_lines.append(line)
    
    return '\n'.join(protocol_lines)

def remove_myst_directives(content):
    """Remove MyST directive blocks matching :::{} ... ::: or ::::{} ... ::::"""
    # Pattern to match both ::: and :::: style directives
    # Matches ::::{anything on this line} through closing ::::
    # or :::{anything on this line} through closing :::
    
    # First remove 4-colon directives (need to do this first to avoid conflicts)
    pattern_4 = r'::::\{[^}]*\}[^\n]*\n.*?\n::::'
    content = re.sub(pattern_4, '', content, flags=re.DOTALL)
    
    # Then remove 3-colon directives
    pattern_3 = r':::\{[^}]*\}[^\n]*\n.*?\n:::'
    content = re.sub(pattern_3, '', content, flags=re.DOTALL)
    
    # Clean up multiple consecutive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <markdown_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract Protocol section
        protocol_section = extract_protocol_section(content)
        
        if not protocol_section:
            print("Warning: No '# Protocol' heading found in the file.")
            sys.exit(1)
        
        # Remove MyST directives
        cleaned_content = remove_myst_directives(protocol_section)
        
        # Output the result
        print(cleaned_content)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()