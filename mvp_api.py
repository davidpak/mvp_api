from flask import *
import pandas as pd

app = Flask(__name__)

basic_df = pd.read_csv("../data/mvp_basic_stats.csv")
advanced_df = pd.read_csv("../data/mvp_advanced_stats.csv")


@app.route("/getbasicstats", methods=["GET"])
def get_basic_stats():
    return basic_df.to_json(orient="records")


@app.route("/getadvancedstats", methods=["GET"])
def get_advanced_stats():
    return advanced_df.to_json(orient="records")

@app.route("/getplayerbasicstats", methods=["GET"])
def get_player_stats():
    player = request.args.get("player")
    season = request.args.get("season")
    player_stats = basic_df[(basic_df["Player"] == player) & (basic_df["Season"] == season)]
    if not player_stats.empty:
        # return with status code 200
        return player_stats.to_json(orient="records"), 200
    else:
        return {"error": f"No stats for {player} in {season} found."}
    
@app.route("/getplayeradvancedstats", methods=["GET"])
def get_player_advanced_stats():
    player = request.args.get("player")
    season = request.args.get("season")
    player_stats = advanced_df[(advanced_df["Player"] == player) & (advanced_df["Season"] == season)]
    if not player_stats.empty:
        # return with status code 200
        return player_stats.to_json(orient="records"), 200
    else:
        return {"error": f"No stats for {player} in {season} found."}

if __name__ == "__main__":
    app.run(debug=True)