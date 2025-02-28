def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def coinExchange(amount, coins):
    print(f"Amount: {amount}")
    result = {}
    num = 0
    for coin in coins.keys():
        if amount >= coin:
            exchange = min(amount // coin, coins[coin])
            result[coin] = exchange
            num += exchange
            amount -= exchange * coin
        else:
            result[coin] = 0
    if amount > 0:
        print(f"Coins are not enough.")
    else:
        print(f"Coin exchange result:")
        for coin, count in result.items():
            print(f"  {coin} baht = {count} coins")
        print(f"Number of coins: {num}")

def main():
    import json
    amount = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(amount, data)

main()