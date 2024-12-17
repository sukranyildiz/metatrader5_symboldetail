import MetaTrader5 as mt5
import pandas as pd
import matplotlib.pyplot as plt

# MetaTrader 5 terminaline bağlan
if not mt5.initialize():
    print("MetaTrader 5 başlatılamadı.")
    quit()

# Belirli bir sembol için fiyatları çekmek
symbol = "EURUSD"

# Fiyat verilerini al
rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 100)

# Veri kontrolü
if rates is None or len(rates) == 0:
    print(f"{symbol} için fiyat bilgisi alınamadı.")
    mt5.shutdown()
    quit()

# Verileri DataFrame'e dönüştür
df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')  # Zamanı okunabilir hale getir
df.set_index('time', inplace=True)

# Grafiği çiz
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['ask'], label="Ask Fiyatı", linestyle='--')
plt.plot(df.index, df['bid'], label="Bid Fiyatı", linestyle='-')
plt.title(f"{symbol} Ask ve Bid Fiyatları")
plt.xlabel("Zaman")
plt.ylabel("Fiyat")
plt.legend()
plt.grid()
plt.show()

# MetaTrader 5 bağlantısını kapat
mt5.shutdown()
