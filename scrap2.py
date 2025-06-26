class Main:
    def __init__(self):
        self.pyramid()

        
    def pyramid(self):
        num = 64
        index = 0
        for i in range(7):
            num += 1
            print()
            for s in range(index):
                print(" ", end='')
            for j in range(7-2*index):
                print(chr(num), end = '') 
            if i < 3:
                index +=1
            else:
                index -= 1
        print()
        print()
        
if __name__ == "__main__":
    run = Main()
