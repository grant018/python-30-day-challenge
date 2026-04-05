import requests, time
from bs4 import BeautifulSoup
from models import Player, BattingStats, PitchingStats, Team
from database import engine, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

year = "2025"
DIVISIONS = {
    "CIN": "NL Central", "CHC": "NL Central", "MIL": "NL Central", "PIT": "NL Central", "STL": "NL Central",
    "ATL": "NL East", "MIA": "NL East", "NYM": "NL East", "PHI": "NL East", "WSN": "NL East",
    "ARI": "NL West", "COL": "NL West", "LAD": "NL West", "SDP": "NL West", "SFG": "NL West",
    "CLE": "AL Central", "CHW": "AL Central", "DET": "AL Central", "KCR": "AL Central", "MIN": "AL Central",
    "BAL": "AL East", "BOS": "AL East", "NYY": "AL East", "TBR": "AL East", "TOR": "AL East",
    "HOU": "AL West", "LAA": "AL West", "ATH": "AL West", "SEA": "AL West", "TEX": "AL West",
}
traded_players = []
errors = []

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def create_player_object(row: list, session):
    name = row[0].strip("#*")
    player = session.query(Player).filter(Player.name == name).first()
    if not player:
        player = Player(name=name)
        session.add(player)
        session.flush()
    return player

def get_or_create_team(session, team_abbr):
    team = session.query(Team).filter(Team.name == team_abbr).first()
    if not team:
        team = Team(name=team_abbr, division=DIVISIONS[team_abbr])
        session.add(team)
        session.flush()
    return team

# Build batting stats from TEAM page column order (index 0 = player name)
def create_batting_stats_object(row):
    return BattingStats(
        team_abbr=team_name,
        season=to_int(year),
        name=row[0].strip("#*"),
        age=to_int(row[1]),
        position=row[2],
        war=to_float(row[3]),
        games=to_int(row[4]),
        plate_appearances=to_int(row[5]),
        at_bats=to_int(row[6]),
        runs=to_int(row[7]),
        hits=to_int(row[8]),
        doubles=to_int(row[9]),
        triples=to_int(row[10]),
        homeruns=to_int(row[11]),
        rbi=to_int(row[12]),
        stolen_bases=to_int(row[13]),
        caught_stealing=to_int(row[14]),
        walks=to_int(row[15]),
        strikeouts=to_int(row[16]),
        batting_avg=to_float(row[17]),
        obp=to_float(row[18]),
        slugging=to_float(row[19]),
        ops=to_float(row[20]),
        ops_plus=to_float(row[21]),
        roba=to_float(row[22]),
        rbat=to_float(row[23]),
        total_bases=to_int(row[24]),
        gidp=to_int(row[25]),
        hbp=to_int(row[26]),
        sac_hits=to_int(row[27]),
        sac_flies=to_int(row[28]),
        intentional_walks=to_int(row[29]),
        positions_played=row[30],
        awards=row[31],
    )

# Build pitching stats from TEAM page column order (index 0 = player name)
def create_pitching_stats_object(row):
    return PitchingStats(
        team_abbr=team_name,
        season=to_int(year),
        name=row[0].strip("#*"),
        age=to_int(row[1]),
        position=row[2],
        war=to_float(row[3]),
        wins=to_int(row[4]),
        losses=to_int(row[5]),
        win_loss_percentage=to_float(row[6]),
        era=to_float(row[7]),
        games=to_int(row[8]),
        games_started=to_int(row[9]),
        games_finished=to_int(row[10]),
        complete_games=to_int(row[11]),
        shutouts=to_int(row[12]),
        saves=to_int(row[13]),
        innings_pitched=to_float(row[14]),
        hits=to_int(row[15]),
        runs=to_int(row[16]),
        earned_runs=to_int(row[17]),
        homeruns=to_int(row[18]),
        walks=to_int(row[19]),
        intentional_walks=to_int(row[20]),
        strikeouts=to_int(row[21]),
        hbp=to_int(row[22]),
        balks=to_int(row[23]),
        wild_pitches=to_int(row[24]),
        batters_faced=to_int(row[25]),
        era_plus=to_int(row[26]),
        fip=to_float(row[27]),
        whip=to_float(row[28]),
        hits_per_nine=to_float(row[29]),
        hrs_per_nine=to_float(row[30]),
        walks_per_nine=to_float(row[31]),
        strikeouts_per_nine=to_float(row[32]),
        strikeouts_per_walk=to_float(row[33]),
        awards=row[34],
    )

# Build batting stats from PLAYER page column order (index 0 = age, 1 = team, 2 = league)
def create_batting_stats_from_player_page(cell_text, player_name, position, t_abbr, is_split):
    return BattingStats(
        team_abbr=t_abbr,
        season=int(year),
        name=player_name,
        age=to_int(cell_text[0]),
        position=position,
        war=to_float(cell_text[3]),
        games=to_int(cell_text[4]),
        plate_appearances=to_int(cell_text[5]),
        at_bats=to_int(cell_text[6]),
        runs=to_int(cell_text[7]),
        hits=to_int(cell_text[8]),
        doubles=to_int(cell_text[9]),
        triples=to_int(cell_text[10]),
        homeruns=to_int(cell_text[11]),
        rbi=to_int(cell_text[12]),
        stolen_bases=to_int(cell_text[13]),
        caught_stealing=to_int(cell_text[14]),
        walks=to_int(cell_text[15]),
        strikeouts=to_int(cell_text[16]),
        batting_avg=to_float(cell_text[17]),
        obp=to_float(cell_text[18]),
        slugging=to_float(cell_text[19]),
        ops=to_float(cell_text[20]),
        ops_plus=to_float(cell_text[21]),
        roba=to_float(cell_text[22]),
        rbat=to_float(cell_text[23]),
        total_bases=to_int(cell_text[24]),
        gidp=to_int(cell_text[25]),
        hbp=to_int(cell_text[26]),
        sac_hits=to_int(cell_text[27]),
        sac_flies=to_int(cell_text[28]),
        intentional_walks=to_int(cell_text[29]),
        positions_played=cell_text[30],
        awards=cell_text[31],
        is_split=is_split,
    )

# Build pitching stats from PLAYER page column order (index 0 = age, 1 = team, 2 = league)
def create_pitching_stats_from_player_page(cell_text, player_name, position, t_abbr, is_split):
    return PitchingStats(
        team_abbr=t_abbr,
        season=int(year),
        name=player_name,
        age=to_int(cell_text[0]),
        position=position,
        war=to_float(cell_text[3]),
        wins=to_int(cell_text[4]),
        losses=to_int(cell_text[5]),
        win_loss_percentage=to_float(cell_text[6]),
        era=to_float(cell_text[7]),
        games=to_int(cell_text[8]),
        games_started=to_int(cell_text[9]),
        games_finished=to_int(cell_text[10]),
        complete_games=to_int(cell_text[11]),
        shutouts=to_int(cell_text[12]),
        saves=to_int(cell_text[13]),
        innings_pitched=to_float(cell_text[14]),
        hits=to_int(cell_text[15]),
        runs=to_int(cell_text[16]),
        earned_runs=to_int(cell_text[17]),
        homeruns=to_int(cell_text[18]),
        walks=to_int(cell_text[19]),
        intentional_walks=to_int(cell_text[20]),
        strikeouts=to_int(cell_text[21]),
        hbp=to_int(cell_text[22]),
        balks=to_int(cell_text[23]),
        wild_pitches=to_int(cell_text[24]),
        batters_faced=to_int(cell_text[25]),
        era_plus=to_int(cell_text[26]),
        fip=to_float(cell_text[27]),
        whip=to_float(cell_text[28]),
        hits_per_nine=to_float(cell_text[29]),
        hrs_per_nine=to_float(cell_text[30]),
        walks_per_nine=to_float(cell_text[31]),
        strikeouts_per_nine=to_float(cell_text[32]),
        strikeouts_per_walk=to_float(cell_text[33]),
        awards=cell_text[34],
        is_split=is_split,
    )

# Batting Stats
def get_batting_stats():
    batting_table = soup.find("table", id="players_standard_batting")
    body = batting_table.find("tbody")
    data_rows = body.find_all("tr")
    with Session(engine) as session:
        team = get_or_create_team(session, team_name)
        for row in data_rows:
            cells = row.find_all("td")
            cell_text = [cell.text for cell in cells]
            if cell_text != []:
                player = create_player_object(cell_text, session)
                 # If hitter is existing on another team add to traded_players
                existing = session.query(BattingStats).filter(
                    BattingStats.player_id == player.id,
                    BattingStats.season == int(year)
                ).first()
                if existing:
                    name_link = cells[0].find("a")
                    if name_link:
                        player_url = name_link.get("href")
                        position = cell_text[2]
                        entry = {"url": player_url, "position": position}
                        if player_url not in [p["url"] for p in traded_players]:
                            traded_players.append(entry)
                else:
                    player_batting = create_batting_stats_object(cell_text)
                    player_batting.team_id = team.id
                    player.batting_stats.append(player_batting)
        session.commit()

# Pitching Stats
def get_pitching_stats():
    pitching_table = soup.find("table", id="players_standard_pitching")
    body = pitching_table.find("tbody")
    data_rows = body.find_all("tr")
    with Session(engine) as session:
        team = get_or_create_team(session, team_name)
        for row in data_rows:
            cells = row.find_all("td")
            cell_text = [cell.text for cell in cells]
            if cell_text != []:
                player = create_player_object(cell_text, session)
                # If pitcher is existing on another team add to traded_players
                existing = session.query(PitchingStats).filter(
                    PitchingStats.player_id == player.id,
                    PitchingStats.season == int(year)
                ).first()
                if existing:
                    name_link = cells[0].find("a")
                    if name_link:
                        player_url = name_link.get("href")
                        position = cell_text[2]
                        entry = {"url": player_url, "position": position}
                        if player_url not in [p["url"] for p in traded_players]:
                            traded_players.append(entry)
                else:
                    player_pitching = create_pitching_stats_object(cell_text)
                    player_pitching.team_id = team.id
                    player.pitching_stats.append(player_pitching)
        session.commit()

# Deal with player splits across multiple teams
def scrape_traded_player(player_info: str, session):
    full_url = "https://www.baseball-reference.com" + player_info["url"]
    position = player_info["position"]
    response = requests.get(full_url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    # Get player name from page
    name_tag = soup.find("h1").find("span")
    player_name = name_tag.text.strip()
    
    player = session.query(Player).filter(Player.name == player_name).first()
    if not player:
        return

    # Delete existing full-season entry
    session.query(BattingStats).filter(
        BattingStats.player_id == player.id,
        BattingStats.season == int(year)
    ).delete()
    session.query(PitchingStats).filter(
        PitchingStats.player_id == player.id,
        PitchingStats.season == int(year)
    ).delete()

    # Scrape split stats
    batting_table = soup.find("table", id="players_standard_batting")
    pitching_table = soup.find("table", id="players_standard_pitching")
    if batting_table:
        body = batting_table.find("tbody")
        for row in body.find_all("tr"):
            th = row.find("th")
            cells = row.find_all("td")
            if th and year in th.text and cells:
                cell_text = [c.text for c in cells]
                t_abbr = cell_text[1]
                try:
                    if "TM" in t_abbr:
                        batting_stats = create_batting_stats_from_player_page(
                            cell_text, player_name, position, t_abbr, is_split=False
                        )
                        batting_stats.team_id = None
                        player.batting_stats.append(batting_stats)
                    else:
                        team = get_or_create_team(session, t_abbr)
                        # Build batting stats with the individual page column order
                        batting_stats = create_batting_stats_from_player_page(
                                cell_text, player_name, position, t_abbr, is_split=True
                            )
                        batting_stats.team_id = team.id
                        player.batting_stats.append(batting_stats)
                except IndexError:
                    errors.append(player_name)
                    print(f"    WARNING: Skipping row for {player_name} - unexpected column count ({len(cell_text)})")
    if pitching_table:
        body = pitching_table.find("tbody")
        for row in body.find_all("tr"):
            th = row.find("th")
            cells = row.find_all("td")
            if th and year in th.text and cells:
                cell_text = [c.text for c in cells]
                t_abbr = cell_text[1]
                try:
                    if "TM" in t_abbr:
                        pitching_stats = create_pitching_stats_from_player_page(
                            cell_text, player_name, position, t_abbr, is_split=False
                        )
                        pitching_stats.team_id = None
                        player.pitching_stats.append(pitching_stats)
                    else:
                        team = get_or_create_team(session, t_abbr)
                        # Build pitching stats with the individual page column order
                        pitching_stats = create_pitching_stats_from_player_page(
                            cell_text, player_name, position, t_abbr, is_split=True
                        )
                        pitching_stats.team_id = team.id
                        player.pitching_stats.append(pitching_stats)
                except IndexError:
                    errors.append(player_name)
                    print(f"    WARNING: Skipping row for {player_name} - unexpected column count ({len(cell_text)})")
    session.flush()

for team in DIVISIONS.keys():
    team_name = team
    print(f"\nScraping {team_name}...")
    url = f"https://www.baseball-reference.com/teams/{team_name}/{year}.shtml"
    response = requests.get(url)
    response.encoding = "utf-8"
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table")
        # Stat Tables
        for i, table in enumerate(tables):
            print(f"Table {i}: {table.get('id', 'no id')}")
        get_batting_stats()
        get_pitching_stats()
        print(f"{team_name} scrape completed...")
        time.sleep(10)
print(f"\nFound {len(traded_players)} traded players. Scraping split stats...")
with Session(engine) as session:
    for player_info in traded_players:
        print(f"  Scraping {player_info['url']}...")
        scrape_traded_player(player_info, session)
        session.commit()
        time.sleep(5)
if errors != []:
    for error_players in errors:
        print(f"ERROR\n{error_players}")
else:
    print("No errors!")