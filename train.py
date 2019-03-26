import textgenrnn
t = textgenrnn()

file = input("Input file location: ")
num = input("How many times would you like to run the file through the model?: ")

t.train_from_file(file, num_epochs=num)
