def welcome():
  #Prints a welcome message and giving brief instructions about the quiz.
  print("Welcome to the Project2 WORD COUNTER!")
  print("\nLet's begin!\n")


def word_count(text):
  """
  Counts the number of words in the given text.
  Args:
      text (str): The input text.
  Returns:
      int: The word count.
  """
  words = text.split()
  return len(words)


def countletters(string):
  #Counts the number of letters in the input string and returns the count.
  letters_count = sum(c.isalpha() for c in string)
  return letters_count


def main():
  # User-friendly interface
  welcome()
  user_input = input("Enter a sentence or paragraph: ")

  # Error handling for empty input
  if not user_input.strip():
    print("Error: Empty input. Please provide some text.")
    return

  # Word counting logic
  count = word_count(user_input)
  print(f"\nThe word count is: {count}")

  # Letter counting logic
  letter_count = countletters(user_input)
  print(f"The letter count is: {letter_count}")


if __name__ == "__main__":
  main()
