import os 
from supabase import create_client, Client
from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

#Hämta listan med länder
@app.route("/countries", methods=["GET"])
def get_countries():
    response = supabase.table("countries").select("*").execute()
    data = response.data
    return jsonify(data), 200

@app.route("/create_country", methods=["POST"])
def create_country():
    payload = request.get_json(force=True)
    response = (
        supabase.table("countries").insert(payload).execute()
    )
    data = response.data
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True, port=5001)