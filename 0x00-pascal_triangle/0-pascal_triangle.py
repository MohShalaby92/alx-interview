def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    
    Args:
        n (int): The number of rows to generate
        
    Returns:
        list: A list of lists containing the values of Pascal's triangle
    """
    # Handle the base case
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate each subsequent row
    for i in range(1, n):
        # Previous row
        prev_row = triangle[i-1]
        
        # Start new row with 1
        current_row = [1]
        
        # Calculate middle values based on the previous row
        for j in range(1, i):
            current_row.append(prev_row[j-1] + prev_row[j])
            
        # End new row with 1
        current_row.append(1)
        
        # Add the new row to the triangle
        triangle.append(current_row)
    
    return triangle
