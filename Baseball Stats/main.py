from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import desc, asc
from sqlalchemy.orm import Session
from database import engine, Base
from models import Player, BattingStats, PitchingStats, Team
from schemas import GetPlayersResponse, PitchingStatsResponse, BattingStatsResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Baseball Stats API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BATTING_RATE_STATS = {"batting_avg", "obp", "slugging", "ops"}
PITCHING_RATE_STATS = {"era", "whip", "fip", "hits_per_nine", "hrs_per_nine", 
                        "walks_per_nine", "strikeouts_per_nine", "strikeouts_per_walk", "era_plus"}

@app.get("/players", response_model=list[GetPlayersResponse])
def get_players():
    with Session(engine) as session:
        all_players = session.query(Player).all()
        return all_players

@app.get("/players/search", response_model=list[GetPlayersResponse])
def search_players(name: str):
    with Session(engine) as session:
        players_found = session.query(Player).filter(Player.name.ilike(f"%{name}%")).all()
        if not players_found:
            raise HTTPException(status_code=404, detail="No players found")
        return players_found
    
@app.get("/players/{player_id}", response_model=GetPlayersResponse)
def get_player_by_id(player_id: int):
    with Session(engine) as session:
        player = session.query(Player).filter(Player.id == player_id).first()
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        return player

@app.get("/batting/leaders", response_model=list[BattingStatsResponse])
def get_batting_leaders(sort_by="", sort_order="desc", top: int = 10):
    with Session(engine) as session:
        if sort_by == "":
            raise HTTPException(status_code=404, detail="Stat category is required")
        elif sort_by in BattingStats.__table__.columns.keys():
            column = getattr(BattingStats, sort_by)
            query = session.query(BattingStats).filter(BattingStats.is_split == False)
            if sort_by in BATTING_RATE_STATS:
                query = query.filter(BattingStats.plate_appearances >= 150)
            if sort_order == "asc":
                query = query.order_by(asc(column))
            else:
                query = query.order_by(desc(column))
            batting_stats = query.limit(top).all()
            return batting_stats
        else:
            raise HTTPException(status_code=404, detail="Stat category not found")
        
@app.get("/batting", response_model=list[BattingStatsResponse])
def get_batting_stats(sort_by="", sort_order="desc"):
    with Session(engine) as session:
        if sort_by == "":
            batting_stats = session.query(BattingStats).filter(BattingStats.is_split == False).all()
            return batting_stats
        elif sort_by in BattingStats.__table__.columns.keys():
            column = getattr(BattingStats, sort_by)
            if sort_order == "asc":
                batting_stats = session.query(BattingStats).order_by(asc(column)).filter(BattingStats.is_split == False).all()
            else:
                batting_stats = session.query(BattingStats).order_by(desc(column)).filter(BattingStats.is_split == False).all()
            return batting_stats
        else:
            raise HTTPException(status_code=404, detail="Stat category not found")

@app.get("/teams/{team_abbr}/pitching", response_model=list[PitchingStatsResponse])
def get_team_pitching(team_abbr: str, sort_by: str = "", sort_order: str = "desc"):
    with Session(engine) as session:
        if sort_by == "":
            team_pitching = session.query(PitchingStats).filter(PitchingStats.team_abbr == team_abbr).all()
            return team_pitching
        elif sort_by in PitchingStats.__table__.columns.keys():
            column = getattr(PitchingStats, sort_by)
            if sort_order == "asc":
                team_pitching = session.query(PitchingStats).order_by(asc(column)).filter(PitchingStats.team_abbr == team_abbr).all()
            else:
                team_pitching = session.query(PitchingStats).order_by(desc(column)).filter(PitchingStats.team_abbr == team_abbr).all()
            return team_pitching
        else:
            raise HTTPException(status_code=404, detail="Stat category not found")
        
@app.get("/pitching/leaders", response_model=list[PitchingStatsResponse])
def get_pitching_leaders(sort_by="", sort_order="desc", top: int = 10):
    with Session(engine) as session:
        if sort_by == "":
            raise HTTPException(status_code=404, detail="Stat category is required")
        elif sort_by in PitchingStats.__table__.columns.keys():
            column = getattr(PitchingStats, sort_by)
            query = session.query(PitchingStats).filter(PitchingStats.is_split == False)
            if sort_by in PITCHING_RATE_STATS:
                query = query.filter(PitchingStats.innings_pitched >= 50)
            if sort_order == "asc":
                query = query.order_by(asc(column))
            else:
                query = query.order_by(desc(column))
            pitching_stats = query.limit(top).all()
            return pitching_stats
        else:
            raise HTTPException(status_code=404, detail="Stat category not found")
        
@app.get("/pitching", response_model=list[PitchingStatsResponse])
def get_pitching_stats(sort_by="", sort_order="desc"):
    with Session(engine) as session:
        if sort_by == "":
            pitching_stats = session.query(PitchingStats).filter(PitchingStats.is_split == False).all()
            return pitching_stats
        elif sort_by in PitchingStats.__table__.columns.keys():
            column = getattr(PitchingStats, sort_by)
            if sort_order == "asc":
                pitching_stats = session.query(PitchingStats).order_by(asc(column)).filter(PitchingStats.is_split == False).all()
            else:
                pitching_stats = session.query(PitchingStats).order_by(desc(column)).filter(PitchingStats.is_split == False).all()
            return pitching_stats
        else:
            raise HTTPException(status_code=404, detail="Stat category not found")

@app.get("/teams/{team_abbr}/batting", response_model=list[BattingStatsResponse])
def get_team_batting(team_abbr: str, sort_by: str = "", sort_order: str = "desc"):
    with Session(engine) as session:
        if sort_by == "":
            team_batting = session.query(BattingStats).filter(BattingStats.team_abbr == team_abbr).all()
            return team_batting
        elif sort_by in BattingStats.__table__.columns.keys():
            column = getattr(BattingStats, sort_by)
            if sort_order == "asc":
                team_batting = session.query(BattingStats).order_by(asc(column)).filter(BattingStats.team_abbr == team_abbr).all()
            else:
                team_batting = session.query(BattingStats).order_by(desc(column)).filter(BattingStats.team_abbr == team_abbr).all()
            return team_batting
        else:
            raise HTTPException(status_code=404, detail="Stat category not found")
        
@app.get("/teams")
def get_teams():
    with Session(engine) as session:
        teams = session.query(Team).all()
        return teams
           
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)