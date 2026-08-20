from alpaca.trading.client import TradingClient # Allows us to connect to our account, used everytime

from alpaca.data import StockHistoricalDataClient, StockTradesRequest # Allows us to get historical data, for getting data
from datetime import datetime # Both used to get start and end times for historical data
from zoneinfo import ZoneInfo 

from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest # Used to create a market order or limit order 
from alpaca.trading.enums import OrderSide, TimeInForce # Orderside is used for 

from alpaca.trading.requests import GetOrdersRequest 
from alpaca.trading.enums import QueryOrderStatus # And OrderSide techincally

from alpaca.data.live import StockDataStream, CryptoDataStream # Used to stream data in real time, for stocks and crypto

# trading_client = TradingClient("API_KEY_HERE", "API_SECRET_HERE", paper=True)

# Checkpoint 1: These are used to check andf make sure your alpaca account is connected properly.
# print(trading_client.get_account().account_number) 
# print(trading_client.get_account().buying_power)


# Checkpoint 2: Collecting Trading Data and to see what trades were made in a time interval 
# data_client = StockHistoricalDataClient("API_KEY_HERE", "API_SECRET_HERE")
# eastern = ZoneInfo("US/Eastern")   
# request_params = StockTradesRequest(
#     symbol_or_symbols="AAPL",
#     start=datetime(2026, 7, 9, 9, 30, tzinfo=eastern),
#     end=datetime(2026,7, 9, 9, 45, tzinfo=eastern)
# )
# trades = data_client.get_stock_trades(request_params)
# print(trades)
# for trade in trades.data["AAPL"]:
#     print(trade)
#     break 

# Checkpoint 3: Market Order Request, no limit to what to buy or sell just buy or sell at the current market price.
# market_order_data = MarketOrderRequest(
#     symbol = "SPY"',
#     qty = 1,
#     side = OrderSide.BUY,
#     time_in_force = TimeInForce.DAY
# )
# market_order = trading_client.submit_order(market_order_data)
# print(market_order)

# Checkpoint 4: Creating a limit order, this is where you can set a limit to what you want to buy or sell at.
# limit_order_data = LimitOrderRequest(
#     symbol = "SPY",
#     qty = 1,
#     side = OrderSide.BUY,
#     time_in_force = TimeInForce.DAY,
#     limit_price = 750.00
# )

# limit_order = trading_client.submit_order(limit_order_data)
# print(limit_order)

# Checkpoint 5: Used to cancel orders and get all the open orders that are currently in your account
# request_params = GetOrderRequest(
#     status = QueryOrderStatus.OPEN, # Unessary but can be used to filter orders by status, in this case we are looking for open orders
#     side = OrderSide.BUY, # Also unessary 
# )

# orders = trading_client.get_orders(request_params)
# print(orders) # This will print all the open buy orders that are currently in your account.

# for order in orders:
#     print(order.id) # This will print all the open orders you have by id 

# for order in orders:
#     trading_client.cancel_order_by_id(order.id) 

# Checkpoint 6: Getting your current positions in your account
# positions = trading_client.get_all_positions()
# print(positions)

# for position in positions: 
#     print (position.symbol, position.current_price)

# Checkpoint 7: Closing all your current positions in one go 
# trading_client.close_all_positions(True) 

# Checkpoint 8: Streaming Data in Realtime 
# stream = StockDataStream("API_KEY_HERE", "API_SECRET_HERE")

# async def handle_trade(data):
#     print(data)

# stream.subscribe_trades(handle_trade, "AAPL") 
# stream.run()
