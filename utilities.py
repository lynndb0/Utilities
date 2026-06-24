import urllib.parse

def remove_newlines(input_query):
  """Remove newlines from string for json formatting etc.
  """

    one_line_query = " ".join(line.strip() for line in input_query.splitlines())
    return one_line_query

def encode_url(url):
  """Encode url
  """

return urllib.parse.quote(url)

return u

def decode_url(url):
  """Decode url  
  """

return urllib.parse.unquote(url)
