from Invoice import Invoice

products = {}
total_amount = 0
total_amount_impure = 0
total_tax = 0;
total_tax_impure = 0;
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break
total_amount = Invoice().totalPurePrice(products)
total_tax = Invoice().totalsalesTaxforPurePrice(products)
total_amount_impure = Invoice().totalImpurePrice(products)
total_tax_impure = Invoice().totalsalesTaxforImurePrice(products)

print("Your total Impure price is: ", total_amount_impure)
print("Your total Impure price with tax is: ", total_amount_impure + total_tax_impure)
print("Your total pure price is: ", total_amount)
print("Your total pure price with tax is: ", total_amount + total_tax)


