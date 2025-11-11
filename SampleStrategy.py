from freqtrade.strategy.interface import IStrategy

class SampleStrategy(IStrategy):
    timeframe = '15m'
    
    # Minimal ROI designed for the strategy
    minimal_roi = {
        "0": 0.01
    }

    # Stoploss
    stoploss = -0.10

    # Trailing stop
    trailing_stop = False

    def populate_indicators(self, dataframe, metadata):
        return dataframe

    def populate_buy_trend(self, dataframe, metadata):
        dataframe.loc[
            (
                (dataframe['volume'] > 0)
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe, metadata):
        dataframe.loc[
            (
                (dataframe['volume'] > 0)
            ),
            'sell'] = 1
        return dataframe