import MetaTrader5 as mt5

# MetaTrader5'i başlat
if not mt5.initialize():
    print("MetaTrader5 başlatılamadı")
    quit()

# Piyasa fiyatlarını al
symbol = "USDTRY"
rates = mt5.symbol_info_tick(symbol)

if rates:
    print(f"{symbol} güncel fiyat bilgileri: {rates}")
else:
    print(f"{symbol} için bilgi alınamadı.")

# MetaTrader5'i kapat
mt5.shutdown()



