#import difflib
#import SequenceMatcher
import hashlib
"""
1- Import module
2- Declare a function with 2 arguments which is for file.
3- Declare two objects for hashlib.sha1()
4- Open files
5- Read the file by breaking the line into smaller chunks
6- Now return both file such as h1.hexdigest() which is of 160 bits.
7- Use hash_file() function to store the hash of a file.
8- Compare and generate appropriate message
"""

path0 = "pdf-sample_0.pdf"
path1 = "pdf-sample_2.pdf"

def reading(hash, filetoread: str):
    #4 Open files
    with open(filetoread, 'rb') as file: 
        chunk = 0
        # 5 Read the file by breaking the line into smaller chunks
        while chunk != b'':
            chunk = file.read(1024)
            hash.update(chunk)

#2 Declare a function with 2 arguments which is for file.
def readfiles(file1: str, file2: str):
    #3 Declare two objects for hashlib.sha1()
    hash1 = hashlib.sha1()
    hash2 = hashlib.sha1()

    reading(hash1, file1)
    reading(hash2, file2)
    # 6 Now return both file such as h1.hexdigest() which is of 160 bits.
    return hash1.hexdigest(), hash2.hexdigest()

read1, read2 = readfiles(path0, path1)
if read1 == read2:
    print("Both files are the same")
else:
    print("Both files are different")