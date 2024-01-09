
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom

def create_svg(width_in_inches, height_in_inches, rows, cols):
    # Converting inches to pixels (96 pixels per inch)
    width_px = width_in_inches * 96
    height_px = height_in_inches * 96
    page_width = width_px / cols
    page_height = height_px / rows

    # Create the main SVG element
    svg = Element('svg', width=str(width_px), height=str(height_px), xmlns="http://www.w3.org/2000/svg")

    # Adding rectangles for each page
    for row in range(rows):
        for col in range(cols):
            x = col * page_width
            y = row * page_height
            attributes = {
                'x': str(x),
                'y': str(y),
                'width': str(page_width),
                'height': str(page_height),
                'fill': 'none',
                'stroke': 'black'
            }
            SubElement(svg, 'rect', attributes)

    # Format the SVG content
    rough_string = tostring(svg, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_svg = reparsed.toprettyxml(indent="  ")

    return pretty_svg

# Create an SVG for a mini book on an 8.5x11 inch paper, folded to make 8 pages (2 columns, 2 rows)
svg_content = create_svg(8.5, 11, 2, 2)

# Save the SVG content to a file
file_path = 'mini_book_gen.svg'
with open(file_path, 'w') as file:
    file.write(svg_content)

file_path


