"""
The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding.
Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.
"""
with open('../Data/portfolio.csv', 'r') as csv:
	total_cost = 0
	header = next(csv)
	for row in csv:
		num_shares = float(row.split(',')[1])
		stock_price =  float(row.split(',')[2])
		total_cost += num_shares * stock_price
	print(total_cost)
