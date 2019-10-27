class productIdNotFound(Exception):
    pass

productDict = {}

def productDetail(productID):
    global productDict
    if productID in productDict.keys():
        print('Product ID : {0}\nProduct Name : {1}'.format(productID,productDict[productID]))
    else:
        raise productIdNotFound

while True:
    prodId = input('Enter the product ID : ')
    prodName = input('Enter the product name : ')
    if not prodId:
        break
    else:
        productDict[prodId] = prodName

choice = 'y'       
while(choice.lower()=='y'):
    searchProd = input('\n\nSearch Product Detail : ')
    productDetail(searchProd)
    choice = input('Do you want to continue? (y/n) : ')
