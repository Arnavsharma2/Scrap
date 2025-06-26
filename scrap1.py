class Main:
    def __init__(self):
        self.pyramid()

        
    def pyramid(self):
        for i in range(10):
            num = 64
            print()
            for s in range (10, i, -1):
                print(" ", end='')
            for j in range(i*2-1):
                if j <= (i*2-1)//2:
                   num += 1
                else:
                   num-=1 
                print(chr(num), end = '') 
        print()
        print()
        
if __name__ == "__main__":
    run = Main()
