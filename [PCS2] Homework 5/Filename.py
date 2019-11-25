import os 
def file_reader(file_name):
    path = os.path.expanduser("~/Desktop/"+ file_name)
    with open(path, "r") as file:
        s = file.read()
    return s.split("\n")
    
if __name__ == "__main__":
    input_list = file_reader("rosalind_gc.txt")
    print(input_list)    
