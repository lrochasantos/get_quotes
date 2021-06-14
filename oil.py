import yfinance as yf 
import yahoo_fin.stock_info as si 
import pandas as pd 
import datetime
import streamlit as st 


# getting date

today = datetime.date.today()
today_formatted = today.strftime("%d/%m/%Y")
yesterday = today - datetime.timedelta(days=1)

current_time = str(datetime.datetime.now())
current_hour = current_time[11:13]

# importing oil prices

oil_now = round(si.get_live_price('BZ=F'), 2)

oil_ticker = yf.Ticker('BZ=F')

oil_prices_1d_ago = oil_ticker.info['previousClose'] 

oil_prices_1mo = oil_ticker.history(period='1mo')
oil_prices_1mo_ago = oil_prices_1mo.iloc[0,3]

oil_prices_ytd = oil_ticker.history(period='ytd')
oil_prices_ytd_ago = oil_prices_ytd.iloc[0,3]

oil_prices_1y = oil_ticker.history(period='1y')
oil_prices_1y_ago = oil_prices_1y.iloc[0,3]


# calculating oil price variations

oil_day = round(((oil_now / oil_prices_1d_ago) -1 ) * 100, 2)

oil_1m = round(((oil_now / oil_prices_1mo_ago) - 1) * 100, 2)

oil_ytd = round(((oil_now / oil_prices_ytd_ago) - 1) * 100, 2)

oil_1y = round(((oil_now / oil_prices_1y_ago) - 1) * 100, 2)


# importing FX

fx_now = round(si.get_live_price('BRL=X'), 2)

fx_ticker = yf.Ticker('BRL=X')

fx_prices_1d_ago = fx_ticker.info['previousClose']

fx_prices_1mo = fx_ticker.history(period='1mo')
fx_prices_1mo_ago = fx_prices_1mo.iloc[0,3]

fx_prices_ytd = fx_ticker.history(period='ytd')
fx_prices_ytd_ago = fx_prices_ytd.iloc[0,3]

fx_prices_1y = fx_ticker.history(period='1y')
fx_prices_1y_ago = fx_prices_1y.iloc[0,3]


# calculating fx price variations

fx_day = round(((fx_now / fx_prices_1d_ago) -1 ) * 100, 2)

fx_1m = round(((fx_now / fx_prices_1mo_ago) - 1) * 100, 2)

fx_ytd = round(((fx_now / fx_prices_ytd_ago) - 1) * 100, 2)

fx_1y = round(((fx_now / fx_prices_1y_ago) - 1) * 100, 2)


# importing IBOV

ibov_now = round(si.get_live_price('^BVSP'), 0)

ibov_ticker = yf.Ticker('^BVSP')

ibov_prices_1d_ago = ibov_ticker.info['previousClose']

ibov_prices_1mo = ibov_ticker.history(period='1mo')
ibov_prices_1mo_ago = ibov_prices_1mo.iloc[0,3]

ibov_prices_ytd = ibov_ticker.history(period='ytd')
ibov_prices_ytd_ago = ibov_prices_ytd.iloc[0,3]

ibov_prices_1y = ibov_ticker.history(period='1y')
ibov_prices_1y_ago = ibov_prices_1y.iloc[0,3]


# calculating IBOV variations

ibov_day = round(((ibov_now / ibov_prices_1d_ago) -1 ) * 100, 2)

ibov_1m = round(((ibov_now / ibov_prices_1mo_ago) - 1) * 100, 2)

ibov_ytd = round(((ibov_now / ibov_prices_ytd_ago) - 1) * 100, 2)

ibov_1y = round(((ibov_now / ibov_prices_1y_ago) - 1) * 100, 2)


# Output 

cotacoes = 	{
			' ': ['Brent', 'Real/US$', 'Ibovespa'],
			'Cotação': [oil_now, fx_now, ibov_now],
			'Var. Dia %': [oil_day, fx_day, ibov_day],
			'Var. Mês %': [oil_1m, fx_1m, ibov_1m],
			'Var. Ano %': [oil_ytd, fx_ytd, ibov_ytd],
			'Var. 12m %': [oil_1y, fx_1y, ibov_1y]
			} 

st.write(today_formatted)
st.table(cotacoes)
st.write('Fonte: Yahoo Finance')