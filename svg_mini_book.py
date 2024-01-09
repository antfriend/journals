import drawsvg as draw

# Create a new SVG drawing
d = draw.Drawing(612, 792, origin='center')

# Define the page size and margins
page_width = 612
page_height = 792
margin = 10

# Define the page layout (8 pages per side)
page_rows = 2
page_cols = 4
page_x = page_width / page_cols
page_y = page_height / page_rows

# Loop through each page and add a rectangle and a text element
for i in range(page_rows):
    for j in range(page_cols):
        # Calculate the page coordinates and rotation angle
        x = (j - page_cols / 2 + 0.5) * page_x
        y = (i - page_rows / 2 + 0.5) * page_y
        angle = 90 if j < page_cols / 2 else -90
        
        # Create a rectangle element with a black stroke and a white fill
        rect = draw.Rectangle(x - page_x / 2 + margin, y - page_y / 2 + margin, page_x - 2 * margin, page_y - 2 * margin, fill='white', stroke='black')
        draw.elements.Rectangle.transform
        # Transform the rectangle element by rotating it around its center
        rect.transform.rotate(angle, x, y)
        
        # Append the rectangle element to the drawing
        d.append(rect)
        
        # Calculate the page number
        page_num = i * page_cols + j + 1
        
        # Create a text element with the page number and a blue fill
        text = draw.Text(f'Page {page_num}', 36, x, y, fill='blue', text_anchor='middle', dominant_baseline='middle')
        
        # Transform the text element by rotating it around its center
        text.transform.rotate(angle, x, y)
        
        # Append the text element to the drawing
        d.append(text)

# Save the SVG document as a file
d.save_svg('mini_book.svg')
print('SVG file saved successfully.')

for i in range(1, 13):
    print(i)