def value_at_target(price, target, btc_price):
    """Value of `price` put into BTC today, if BTC reaches `target`."""
    btc_amount = price / btc_price
    return btc_amount * target
