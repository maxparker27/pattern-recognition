

t = input()

try:

    def sort_letters(string_to_test):

        even_vals = []
        odd_vals = []

        for count, i in enumerate(string_to_test):
            
            if count % 2 == 0:
                even_vals.append(i)
            else: 
                odd_vals.append(i)
                
        even_vals = ["".join(i for i in even_vals)]
        odd_vals = ["".join(i for i in odd_vals)]

        for even, odd in zip(even_vals, odd_vals):
            print(even + " " + odd)

    counter = 0

    while True:
        if counter == t:
            break
        inp = str(input())
        sort_letters(inp)
        counter += 1

except EOFError as e:
    
    pass
    
    
            
