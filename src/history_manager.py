import json
import os
from datetime import datetime

class HistoryManager:
    def __init__(self, filename="history_tebak_angka.json"):
        self.filename = filename
        self.history = []
        self.load_history()
        
    def load_history(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.history = json.load(file)
            except (json.JSONDecodeError, IOError):
                self.history = []
                
    def save_history(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.history, file, indent=4)
        except IOError:
            print("Gagal menyimpan history")
            
    def add_game_record(self, status, tebakan, kesempatan_terpakai):
        record = {
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": status,
            "tebakan": tebakan,
            "kesempatan_terpakai": kesempatan_terpakai,
            "total_tebakan": len(tebakan)
        }
        self.history.append(record)
        self.save_history()
        
    def get_recent_games(self, count=5):
        return self.history[-count:] if self.history else []
        
    def get_statistics(self):
        if not self.history:
            return {"total_game": 0, "menang": 0, "kalah": 0, "rata_rata_tebakan": 0}
            
        total_game = len(self.history)
        menang = sum(1 for game in self.history if game["status"] == "menang")
        kalah = total_game - menang
        rata_rata_tebakan = sum(game["total_tebakan"] for game in self.history) / total_game
        
        return {
            "total_game": total_game,
            "menang": menang,
            "kalah": kalah,
            "rata_rata_tebakan": round(rata_rata_tebakan, 2)
        }