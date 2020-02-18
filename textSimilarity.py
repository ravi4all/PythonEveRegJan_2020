text_1 = """
Python is a high-level programming language designed to be easy to read and simple to implement. It is open source, which means it is free to use, even for commercial applications. Python can run on Mac, Windows, and Unix systems and has also been ported to Java and .NET virtual machines.
Python is considered a scripting language, like Ruby or Perl and is often used for creating Web applications and dynamic Web content. It is also supported by a number of 2D and 3D imaging programs, enabling users to create custom plug-ins and extensions with Python. Examples of applications that support a Python API include GIMP, Inkscape, Blender, and Autodesk Maya.
Scripts written in Python (.PY files) can be parsed and run immediately. They can also be saved as a compiled programs (.PYC files), which are often used as programming modules that can be referenced by other Python programs.
"""

text_2 = """
Python is an interpreted, object-oriented programming language similar to PERL, that has gained popularity because of its clear syntax and readability. Python is said to be relatively easy to learn and portable, meaning its statements can be interpreted in a number of operating systems, including UNIX-based systems, Mac OS, MS-DOS, OS/2, and various versions of Microsoft Windows 98. Python was created by Guido van Rossum, a former resident of the Netherlands, whose favorite comedy group at the time was Monty Python's Flying Circus. The source code is freely available and open for modification and reuse. Python has a significant number of users.
A notable feature of Python is its indenting of source statements to make the code easier to read. Python offers dynamic data type, ready-made class, and interfaces to many system calls and libraries. It can be extended, using the C or C++ language.
Python can be used as the script in Microsoft's Active Server Page (ASP) technology. The scoreboard system for the Melbourne (Australia) Cricket Ground is written in Python. Z Object Publishing Environment, a popular Web application server, is also written in the Python language.
"""

# tokenization
tokens_1 = text_1.lower().split()
tokens_2 = text_2.lower().split()

# remove stopwords
stopwords = ["is","am","are","the","that","of","by","it","in","to","on","its","can","be",
             "a","or","for","also","an","as","has","and","was","with","were"]

words_1 = []
for i in range(len(tokens_1)):
    if tokens_1[i] not in stopwords:
        words_1.append(tokens_1[i])

words_2 = []
for i in range(len(tokens_2)):
    if tokens_2[i] not in stopwords:
        words_2.append(tokens_2[i])

stopwords_2 = [",",".","'s","'t",";",":"]

for i in range(len(words_1)):
    for j in range(len(stopwords_2)):
        if words_1[i].endswith(stopwords_2[j]):
            words_1[i] = words_1[i].replace(stopwords_2[j],"")

for i in range(len(words_2)):
    for j in range(len(stopwords_2)):
        if words_2[i].endswith(stopwords_2[j]):
            words_2[i] = words_2[i].replace(stopwords_2[j],"")

intersection = set(words_1).intersection(words_2)
union = set(words_1).union(words_2)
sim = len(intersection) / len(union)
print("Similar words are",intersection)
print("Similarity score is",round(sim * 100,2))