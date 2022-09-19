class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    output = 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'
    return output

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2*self.width) + (2*self.height)

  def get_diagonal(self):
    return ((self.width**2) + (self.height**2))**0.5

  def get_picture(self):
    """
      Returns a string that represents the shape using lines of "*".
      The number of lines should be equal to the height and the
      number of "*" in each line should be equal to the width. There
      should be a new line (\n) at the end of each line. If the
      width or height is larger than 50, this should return the
      string: "Too big for picture.".
    """
    if( (self.width > 50) or (self.height > 50) ):
      return 'Too big for picture.'

    output = ''
    i = 0
    while i < self.height:
      j = 0
      while j < self.width:
        output += '*'
        j += 1
      output += '\n'
      i += 1

    return output


  def get_amount_inside(self, square):
    output = 0
    if((square.width > self.width) or (square.height > self.height)):
      output = 0
    else:
      max_width = self.width
      max_height = self.height
      count_width = int(self.width/square.width)
      count_height = int(self.height/square.height)

      output = count_width*count_height

    return output
    

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    output = 'Square(side='+str(self.width)+')'
    return output

  def set_side(self, side):
    self.width = side
    self.height = side

