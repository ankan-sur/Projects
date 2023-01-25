    #######################################################
    #  Computer Project #9
    #
    #  open function
    #  read functions + create dict function
    #       collect company names, collect all company info and creates dictionary
    #  add prices func
    #       to add to previous dictionary rather than make a new one
    #  get max price of company func
    #  find max company price func
    #  get avg price of company func
    #  display list func  
    #
    #  main
    #   open files
    #   read files
    #   show banner
    #   input for options
    #       option cases 1,2,3,4,5,6
    #    error check
    ###########################################################


import csv
from operator import itemgetter

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    '''input:  filenames for prices and security
       returns: file pointers for both files
    '''
    while True:
        inp1 = input("\nEnter the price's filename: ")
        try:
            fp1 = open(inp1)
            break
        except FileNotFoundError:
            print("\nFile not found. Please try again.")

     #running two inputs in the same open_file, unlike others

    while True:
        inp2 = input("\nEnter the security's filename: ")
        try:
            fp2 = open(inp2)
            break
        except FileNotFoundError:
            print("\nFile not found. Please try again.")
    return fp1,fp2

def read_file(securities_fp):
    '''input: fp for securities file
       return: dictionary of company code to info from file
    '''
    set_of_names = set()
    secu_dict = {} 
    reader = csv.reader(securities_fp)
    next(reader,None)
    for line in reader:
        code = line[0]
        name = line[1]
        sector = line[3]
        subsector = line[4]
        address = line[5]
        date_add = line[6]
        set_of_names.add(name)
        comp_list = [name, sector, subsector, address, date_add, []]
        secu_dict[code] = comp_list #dictionary version of .append()
    return set_of_names, secu_dict

        
def add_prices (master_dictionary, prices_file_pointer):
    '''input: dictionary from prev func, file pointer for prices file
       return: nothing, the function edits a dictionary
    '''
    reader = csv.reader(prices_file_pointer)
    next(reader,None)
    for line in reader:
        date = line[0]
        open_info = float(line[2])
        close_info = float(line[3])
        low_info = float(line[4])
        high_info = float(line[5])
        code = line[1]
        price_lis = [date, open_info, close_info, low_info, high_info]
        if code in master_dictionary.keys():
            master_dictionary[code][5].append(price_lis)
    
def get_max_price_of_company (master_dictionary, company_symbol):
    '''input: master dict and company name to find all prices by company name
       return: tuple with max value in price and date
    '''
    empty_L = []
    if company_symbol in master_dictionary.keys():
        L = master_dictionary[company_symbol][5]
        if L != []:
            for price in L:
                date = price[0]
                max_price = float(price[4])
                price_tuple = (max_price,date)
                empty_L.append(price_tuple)
            max_val = max(empty_L) 
            return (max_val)
        else:
            return (None,None) #error checking
    else:
        return (None,None)

def find_max_company_price (master_dictionary):
    '''input: master dictionary for iteration
       return: max price along with company code 
    '''
    L = []
    for code,items in master_dictionary.items():
        if master_dictionary[code][5] == []:
            continue
        L2 = master_dictionary[code][5]
        for price in L2:
            high_price = price[4]
            price_tuple = (code,high_price)
            L.append(price_tuple)
    max_val = max(L,key=itemgetter(1)) #using itemgetter to use max()
    return max_val

def get_avg_price_of_company (master_dictionary, company_symbol):
    '''input: master dict and company name to find all prices by company name
       return: float avg value in price 
    '''
    empty_L = []
    if company_symbol in master_dictionary.keys():
        L = master_dictionary[company_symbol][5]
        if L != []:
            for price in L:
                max_price = float(price[4])
                empty_L.append(max_price)
            avg_val = (sum(empty_L))/(len(empty_L)) #avg = sum(x)/len(x)
            return round(avg_val,2)
        else:
            return 0.0
    else:
        return 0.0

def display_list (lst):  # "{:^35s}" 
    '''input: list
       return: nothing, but printing in 3s     
    '''
    iter  = len(lst)
    for i in range(0,iter,3): #fails one test bc of whitespace
        try:
            a = lst[i]
        except:
            a = ""
        try:
            b = lst[i+1]
        except:
            b = ""
        try:
            c = lst[i+2]
        except:
            c = ""
            
        print("{:^35s}{:^35s}{:^35s}".format(a,b,c))
    
def main():
    print(WELCOME)
    fp1,fp2 = open_file()
    set_of_names, master_dictionary = read_file(fp2)
    add_prices(master_dictionary,fp1)
    while True:
        print(MENU)
        op = input("\nOption: ")
        if op == "1":
            print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            list_of_names = sorted(list(set_of_names)) #converting to list
            display_list(list_of_names)
            print("\n")
        elif op == "2":
            print("\ncompanies' symbols:")
            list_of_codes = sorted(list(master_dictionary.keys())) #keys are codes for company
            display_list(list_of_codes)
            print("\n")
        elif op == "3":
            while True:
                inp = input("\nEnter company symbol for max price: ")
                if inp in master_dictionary.keys():
                    prices_tup = get_max_price_of_company(master_dictionary, inp)
                    if prices_tup != (None,None):
                        price = prices_tup[0]
                        date = prices_tup[1]
                        print("\nThe maximum stock price was ${} on the date {}/".format(round(price,2),date))
                        print()
                        break #needs a break because of a double while loop
                    else:
                        print("\nThere were no prices.")
                        break
                else:
                    print("\nError: not a company symbol. Please try again.")
                    continue
        elif op == "4":
            max_tup = find_max_company_price(master_dictionary)
            price = max_tup[1]
            comp = max_tup[0]
            print("\nThe company with the highest stock price is {} with a value of ${}".format(comp,round(price,2)))
            print()
        elif op == "5":
            while True:
                inp5 = input("\nEnter company symbol for average price: ")
                if inp5 in master_dictionary.keys():
                    avg_price = get_avg_price_of_company(master_dictionary,inp5)
                    if avg_price != 0.0:
                        print("\nThe average stock price was ${:.2f}.\n".format(avg_price))
                        break
                    else:
                        print("\nThere were no prices.")
                        break
                else:
                    print("\nError: not a company symbol. Please try again.")
        elif op == "6":
            break
        else:
            print("\nInvalid option. Please try again.")
            continue

if __name__ == "__main__": 
    main() 
