def capital_chars(string):  #Define function with string input
  return [for i in i, for char in enumerate(string), return char.index() if char.isupper()]
  
return capital_chars("HeLlO")
