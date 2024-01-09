import svgwrite

def create_mini_book_svg(file_path, paper_width, paper_height, rows, cols):
    """
    Create an SVG file for a mini book layout.
    :param file_path: Path to save the SVG file.
    :param paper_width: Width of the paper in inches.
    :param paper_height: Height of the paper in inches.
    :param rows: Number of rows (horizontal folds).
    :param cols: Number of columns (vertical folds).
    """
    # Convert inches to pixels (1 inch = 96 pixels)
    width_px = paper_width * 96
    height_px = paper_height * 96
    row_height = height_px / rows
    col_width = width_px / cols

    # Create an SVG drawing
    dwg = svgwrite.Drawing(file_path, size=(width_px, height_px), profile='tiny')

    # Draw rectangles for each page section
    for row in range(rows):
        for col in range(cols):
            dwg.add(dwg.rect(insert=(col * col_width, row * row_height), size=(col_width, row_height),
                             fill='none', stroke='black', stroke_width=2))

    # Save the SVG file
    dwg.save()

# File path for the SVG
svg_file_path = 'mini_book_layout.svg'

# Create an SVG for a mini book on an 8.5 x 11 inch paper, folded to make 8 pages (2 columns, 2 rows)
create_mini_book_svg(svg_file_path, 8.5, 11, 2, 4)

svg_file_path

