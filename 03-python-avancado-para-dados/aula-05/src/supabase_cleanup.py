import os
import time
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BUCKET = "measurement"
MEASUREMENTS_PATH = "data/measurements.txt"
EXPIRY_PATH = "data/.measurements_expiry"


def supabase_cleanup():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    try:
        response = supabase.storage.from_(BUCKET).download(EXPIRY_PATH)
        expiry_timestamp = float(response.decode('utf-8').strip())

        if time.time() >= expiry_timestamp:
            supabase.storage.from_(BUCKET).remove([MEASUREMENTS_PATH, EXPIRY_PATH])
            print("measurements.txt expirado e removido do Supabase Storage.")
        else:
            horas = (expiry_timestamp - time.time()) / 3600
            print(f"Arquivo ainda valido. Expira em {horas:.1f} horas.")

    except Exception as e:
        print(f"Nenhum arquivo de expiracao encontrado: {e}")


if __name__ == "__main__":
    supabase_cleanup()
