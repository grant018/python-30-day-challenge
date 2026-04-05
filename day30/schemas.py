from pydantic import BaseModel

class BattingStatsResponse(BaseModel):
    team_abbr: str
    season: int
    name: str
    age: int
    position: str
    war: float | None
    games: int | None
    plate_appearances: int | None
    at_bats: int | None
    runs: int | None
    hits: int | None
    doubles: int | None
    triples: int | None
    homeruns: int | None
    rbi: int | None
    stolen_bases: int | None
    caught_stealing: int | None
    walks: int | None
    strikeouts: int | None
    batting_avg: float | None
    obp: float | None
    slugging: float | None
    ops: float | None
    ops_plus: float | None
    roba: float | None
    rbat: float | None
    total_bases: int | None
    gidp: int | None
    hbp: int | None
    sac_hits: int | None
    sac_flies: int | None
    intentional_walks: int | None
    positions_played: str | None
    awards: str | None

    class Config:
        from_attributes = True

class PitchingStatsResponse(BaseModel):
    team_abbr: str
    season: int
    name: str
    age: int
    position: str
    war: float | None
    wins: int | None
    losses: int | None
    win_loss_percentage: float | None
    era: float | None
    games: int | None
    games_started: int | None
    games_finished: int | None
    complete_games: int | None
    shutouts: int | None
    saves: int | None
    innings_pitched: float | None
    hits: int | None
    runs: int | None
    earned_runs: int | None
    homeruns: int | None
    walks: int | None
    intentional_walks: int | None
    strikeouts: int | None
    hbp: int | None
    balks: int | None
    wild_pitches: int | None
    batters_faced: int | None
    era_plus: int | None
    fip: float | None
    whip: float | None
    hits_per_nine: float | None
    hrs_per_nine: float | None
    walks_per_nine: float | None
    strikeouts_per_nine: float | None
    strikeouts_per_walk: float | None
    awards: str | None

    class Config:
        from_attributes = True

class GetPlayersResponse(BaseModel):
    id: int
    name: str
    batting_stats: list[BattingStatsResponse] = []
    pitching_stats: list[PitchingStatsResponse] = []

    class Config:
        from_attributes = True