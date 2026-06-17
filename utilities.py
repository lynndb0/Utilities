

def remove_newlines(input_query):
  """Remove newlines from string for json formatting etc.
  """

    one_line_query = " ".join(line.strip() for line in input_query.splitlines())
    return one_line_query
