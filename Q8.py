from bs4 import BeautifulSoup
with open('SAMPLE.xml', 'r') as f: 
    data = f.read()
    Bs_data = BeautifulSoup(data, "xml")
    b_bookstore = Bs_data.find_all('bookstore')
    print(b_bookstore)
