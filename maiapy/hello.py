def hello(name):
  """hello function
  
  This function takes a string input then returns a sentence with that string inserted in the correct spot.
  
  Parameters
  ----------
  name : str
    This string parameter should be someone's name. The parameter is used to fill in the blank in the output sentence.

  Returns
  -------
  str
    The function returns an output sentence using the input name provided.
  
  Examples
  --------
  >>> To insert your name into the sentence run hello("yourname".
  """
  print("Hello ", name, "! Welcome to my first Python package!", sep = "")
