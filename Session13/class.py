import os
print(os.getcwd())
fout = open('output.txt', 'a')
line1 = "How many roads must a man walk down\n"
fout.write(line1)
line2 = "Before you call him a man?\n"
fout.write(line2)
fout.write(line2)
fout.close()

print(os.path.abspath('session13(10.18)/output.text'))
print(os.path.exists('session13(10.18)/output.text'))
print(os.path.abspath('session13(10.18)/input.text'))

