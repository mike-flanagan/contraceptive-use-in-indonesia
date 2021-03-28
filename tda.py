# Import the client
from keys import consumer_key
from td.client import TDClient

# Create a new session, credentials path is required.
TDSession = TDClient(
    client_id= consumer_key,
    redirect_uri='https://github.com/eggrollofchaos',
    credentials_path='cred/td_state.json'
)

# Login to the session
TDSession.login()

# Grab real-time quotes for 'MSFT' (Microsoft)
msft_quotes = TDSession.get_quotes(instruments=['MSFT'])

# Grab real-time quotes for 'AMZN' (Amazon) and 'SQ' (Square)
multiple_quotes = TDSession.get_quotes(instruments=['AMZN','SQ'])
