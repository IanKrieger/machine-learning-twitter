import textgenrnn

weight_file=input("Input location of generated weights file: ")
results=input("How many things do you want generated?: ")
creativity=input("How creative do you want the results (.1 for boring - 1.+ for non-sensical output): ")

t = textgenrnn(weight_file)
t.generate(results, temperature=creativity)