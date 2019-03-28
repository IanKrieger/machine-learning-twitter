from textgenrnn import textgenrnn
t = textgenrnn()

file = input("Input file location: ")
num = input("How many times would you like to run the file through the model?: ")

count = int(num)

t.train_from_file(file, num_epochs=count)
