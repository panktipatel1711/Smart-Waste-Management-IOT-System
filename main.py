#!/usr/bin/env python3
import os
import random
import datetime
import pandas as pd

BIN_TOTAL_HEIGHT_CM = 50.0
CSV_FILE_PATH = "./data/waste_log.csv"

# Ensure directories exist
os.makedirs("./data", exist_ok=True)

class SmartBinDataEngine:
    def __init__(self, height_cm):
        self.height = height_cm
        
        # Check historical values to maintain smooth progression
        if os.path.exists(CSV_FILE_PATH) and os.stat(CSV_FILE_PATH).st_size > 0:
            try:
                df = pd.read_csv(CSV_FILE_PATH)
                last_pct = df.iloc[-1]['Fill_Percentage']
                self.current_waste_level = (last_pct / 100.0) * self.height
            except:
                self.current_waste_level = 5.0
        else:
            self.current_waste_level = 5.0
        
    def execute_telemetry_cycle(self):
        # Auto-reset logic if the bin gets too full
        if self.current_waste_level >= (self.height * 0.90):
            print("\n\033[94m[MUNICIPAL ACTION] Bin emptied! Resetting node level...\033[0m")
            self.current_waste_level = random.uniform(2.0, 5.0)
        else:
            # Add a random chunk of waste for this single run
            growth = random.uniform(4.0, 8.0) 
            self.current_waste_level = min(self.current_waste_level + growth, self.height - 1.5)
            
        measured_distance = self.height - self.current_waste_level
        fill_pct = (self.current_waste_level / self.height) * 100.0
        
        if fill_pct >= 80.0:
            status, alert_bit = "CRITICAL_FULL", 1
        elif fill_pct >= 50.0:
            status, alert_bit = "WARNING_HALF", 0
        else:
            status, alert_bit = "SYSTEM_OK_EMPTY", 0
            
        return round(measured_distance, 2), round(fill_pct, 2), status, alert_bit

if __name__ == "__main__":
    engine = SmartBinDataEngine(BIN_TOTAL_HEIGHT_CM)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dist, pct, stat, alert = engine.execute_telemetry_cycle()
    
    new_data = {
        "Timestamp": [timestamp], 
        "Distance_CM": [dist], 
        "Fill_Percentage": [pct], 
        "Status_Code": [stat], 
        "Alert_Status": [alert]
    }
    df_new = pd.DataFrame(new_data)
    
    # Save safely to the shared database
    if not os.path.exists(CSV_FILE_PATH) or os.stat(CSV_FILE_PATH).st_size == 0:
        df_new.to_csv(CSV_FILE_PATH, index=False)
    else:
        df_new.to_csv(CSV_FILE_PATH, mode='a', header=False, index=False)
        
    print(f"\033[92m[+] Telemetry Stream Synchronized Successfully!\033[0m")
    print(f"    Time: {timestamp} | Fill: {pct}% | Headroom: {dist}cm | State: {stat}\n")