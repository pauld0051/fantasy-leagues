def word_length(words, word_index):
    # Complete the function here:
    list = ''
    for word in words:
      if word.isalnum() or word.isspace():
          list += word
      elif word == "'":
          list += word
    list = list.split(' ')
    if len(list) > word_index and len(list[word_index]) > 0:
      return (list[word_index], len(list[word_index]))
    #print(len(words))
    else:
      return "Word not found."


# Sample function call:
words = "This is a ... test. This is only a test."
word_index = 5
print(word_length(words, word_index))
