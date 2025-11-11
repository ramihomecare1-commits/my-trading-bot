FROM freqtradeorg/freqtrade:stable

# Copy configuration
COPY config.json /freqtrade/config.json
USER root
RUN mkdir -p /freqtrade/user_data/strategies
COPY *.py /freqtrade/user_data/strategies/
USER ftuser

# Start the bot
CMD ["trade", "--config", "/freqtrade/config.json"]
