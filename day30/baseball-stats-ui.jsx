import { useState, useEffect, useCallback } from "react";

const API_BASE = "http://localhost:8000";

// Mock data for demo when API isn't running
const MOCK_BATTING = [
  { name: "Elly De La Cruz", team: "CIN", season: 2025, age: 23, position: "SS", games: 162, at_bats: 629, runs: 102, hits: 166, doubles: 31, triples: 7, homeruns: 22, rbi: 86, stolen_bases: 37, walks: 67, strikeouts: 181, batting_avg: 0.264, obp: 0.336, slugging: 0.44, ops: 0.777, war: 3.6, awards: "AS,MVP-23" },
  { name: "TJ Friedl", team: "CIN", season: 2025, age: 29, position: "CF", games: 152, at_bats: 579, runs: 82, hits: 151, doubles: 22, triples: 2, homeruns: 14, rbi: 53, stolen_bases: 12, walks: 81, strikeouts: 115, batting_avg: 0.261, obp: 0.364, slugging: 0.378, ops: 0.742, war: 2.3, awards: "" },
  { name: "Spencer Steer", team: "CIN", season: 2025, age: 27, position: "1B", games: 146, at_bats: 509, runs: 66, hits: 121, doubles: 21, triples: 2, homeruns: 21, rbi: 75, stolen_bases: 7, walks: 51, strikeouts: 129, batting_avg: 0.238, obp: 0.312, slugging: 0.411, ops: 0.723, war: 0.7, awards: "" },
  { name: "Matt McLain", team: "CIN", season: 2025, age: 25, position: "2B", games: 147, at_bats: 510, runs: 73, hits: 112, doubles: 18, triples: 0, homeruns: 15, rbi: 50, stolen_bases: 18, walks: 55, strikeouts: 167, batting_avg: 0.22, obp: 0.3, slugging: 0.343, ops: 0.643, war: 0.0, awards: "" },
  { name: "Austin Hays", team: "CIN", season: 2025, age: 29, position: "LF", games: 103, at_bats: 380, runs: 60, hits: 101, doubles: 16, triples: 5, homeruns: 15, rbi: 64, stolen_bases: 7, walks: 29, strikeouts: 107, batting_avg: 0.266, obp: 0.315, slugging: 0.453, ops: 0.768, war: 0.8, awards: "" },
  { name: "Noelvi Marté", team: "CIN", season: 2025, age: 23, position: "RF", games: 90, at_bats: 339, runs: 45, hits: 89, doubles: 17, triples: 2, homeruns: 14, rbi: 51, stolen_bases: 10, walks: 16, strikeouts: 85, batting_avg: 0.263, obp: 0.3, slugging: 0.448, ops: 0.748, war: 1.4, awards: "" },
  { name: "Gavin Lux", team: "CIN", season: 2025, age: 27, position: "DH", games: 140, at_bats: 446, runs: 49, hits: 120, doubles: 28, triples: 2, homeruns: 5, rbi: 53, stolen_bases: 1, walks: 56, strikeouts: 114, batting_avg: 0.269, obp: 0.35, slugging: 0.374, ops: 0.724, war: -0.2, awards: "" },
  { name: "Tyler Stephenson", team: "CIN", season: 2025, age: 28, position: "C", games: 88, at_bats: 299, runs: 40, hits: 69, doubles: 18, triples: 0, homeruns: 13, rbi: 50, stolen_bases: 0, walks: 37, strikeouts: 116, batting_avg: 0.231, obp: 0.316, slugging: 0.421, ops: 0.737, war: 1.3, awards: "" },
];

const MOCK_PITCHING = [
  { name: "Andrew Abbott", team: "CIN", season: 2025, age: 25, position: "SP", wins: 10, losses: 7, era: 2.87, games: 28, games_started: 28, saves: 0, innings_pitched: 165.0, strikeouts: 176, walks: 55, whip: 1.12, war: 4.1, awards: "" },
  { name: "Hunter Greene", team: "CIN", season: 2025, age: 25, position: "SP", wins: 7, losses: 4, era: 2.76, games: 19, games_started: 19, saves: 0, innings_pitched: 114.1, strikeouts: 140, walks: 33, whip: 0.99, war: 3.2, awards: "" },
  { name: "Brady Singer", team: "CIN", season: 2025, age: 28, position: "SP", wins: 14, losses: 12, era: 4.03, games: 33, games_started: 33, saves: 0, innings_pitched: 198.0, strikeouts: 155, walks: 48, whip: 1.24, war: 2.1, awards: "" },
  { name: "Nick Lodolo", team: "CIN", season: 2025, age: 27, position: "SP", wins: 9, losses: 8, era: 3.33, games: 30, games_started: 30, saves: 0, innings_pitched: 175.2, strikeouts: 168, walks: 54, whip: 1.2, war: 2.8, awards: "" },
  { name: "Nick Martinez", team: "CIN", season: 2025, age: 35, position: "SP", wins: 11, losses: 14, era: 4.45, games: 32, games_started: 32, saves: 0, innings_pitched: 186.1, strikeouts: 139, walks: 62, whip: 1.35, war: 1.0, awards: "" },
  { name: "Emilio Pagán", team: "CIN", season: 2025, age: 33, position: "RP", wins: 2, losses: 4, era: 2.88, games: 65, games_started: 0, saves: 28, innings_pitched: 62.2, strikeouts: 74, walks: 20, whip: 1.07, war: 1.5, awards: "" },
  { name: "Tony Santillan", team: "CIN", season: 2025, age: 27, position: "RP", wins: 1, losses: 5, era: 2.44, games: 62, games_started: 0, saves: 8, innings_pitched: 59.0, strikeouts: 66, walks: 25, whip: 1.15, war: 1.2, awards: "" },
  { name: "Graham Ashcraft", team: "CIN", season: 2025, age: 26, position: "SP", wins: 8, losses: 5, era: 3.99, games: 25, games_started: 18, saves: 0, innings_pitched: 119.1, strikeouts: 85, walks: 42, whip: 1.31, war: 0.8, awards: "" },
];

const MOCK_PLAYERS = MOCK_BATTING.map((b, i) => ({ id: i + 1, name: b.name, batting_stats: [b], pitching_stats: [] }));

const formatAvg = (val) => {
  if (val === null || val === undefined) return "—";
  const s = val.toFixed(3);
  return s.startsWith("0") ? s.slice(1) : s;
};

const formatEra = (val) => {
  if (val === null || val === undefined) return "—";
  return val.toFixed(2);
};

const formatNum = (val) => {
  if (val === null || val === undefined) return "—";
  return val.toString();
};

const BATTING_COLS = [
  { key: "name", label: "PLAYER", align: "left", format: (v) => v },
  { key: "position", label: "POS", align: "center", format: formatNum },
  { key: "age", label: "AGE", align: "center", format: formatNum },
  { key: "games", label: "G", align: "center", format: formatNum },
  { key: "at_bats", label: "AB", align: "center", format: formatNum },
  { key: "runs", label: "R", align: "center", format: formatNum },
  { key: "hits", label: "H", align: "center", format: formatNum },
  { key: "doubles", label: "2B", align: "center", format: formatNum },
  { key: "triples", label: "3B", align: "center", format: formatNum },
  { key: "homeruns", label: "HR", align: "center", format: formatNum },
  { key: "rbi", label: "RBI", align: "center", format: formatNum },
  { key: "stolen_bases", label: "SB", align: "center", format: formatNum },
  { key: "walks", label: "BB", align: "center", format: formatNum },
  { key: "strikeouts", label: "SO", align: "center", format: formatNum },
  { key: "batting_avg", label: "AVG", align: "center", format: formatAvg },
  { key: "obp", label: "OBP", align: "center", format: formatAvg },
  { key: "slugging", label: "SLG", align: "center", format: formatAvg },
  { key: "ops", label: "OPS", align: "center", format: formatAvg },
  { key: "war", label: "WAR", align: "center", format: (v) => v?.toFixed(1) ?? "—" },
];

const PITCHING_COLS = [
  { key: "name", label: "PLAYER", align: "left", format: (v) => v },
  { key: "position", label: "POS", align: "center", format: formatNum },
  { key: "age", label: "AGE", align: "center", format: formatNum },
  { key: "wins", label: "W", align: "center", format: formatNum },
  { key: "losses", label: "L", align: "center", format: formatNum },
  { key: "era", label: "ERA", align: "center", format: formatEra },
  { key: "games", label: "G", align: "center", format: formatNum },
  { key: "games_started", label: "GS", align: "center", format: formatNum },
  { key: "saves", label: "SV", align: "center", format: formatNum },
  { key: "innings_pitched", label: "IP", align: "center", format: (v) => v?.toFixed(1) ?? "—" },
  { key: "hits", label: "H", align: "center", format: formatNum },
  { key: "runs", label: "R", align: "center", format: formatNum },
  { key: "earned_runs", label: "ER", align: "center", format: formatNum },
  { key: "homeruns", label: "HR", align: "center", format: formatNum },
  { key: "walks", label: "BB", align: "center", format: formatNum },
  { key: "strikeouts", label: "SO", align: "center", format: formatNum },
  { key: "whip", label: "WHIP", align: "center", format: formatEra },
  { key: "war", label: "WAR", align: "center", format: (v) => v?.toFixed(1) ?? "—" },
];

const LEADER_STATS = {
  batting: [
    { key: "batting_avg", label: "Batting Average", format: formatAvg },
    { key: "homeruns", label: "Home Runs", format: formatNum },
    { key: "rbi", label: "RBI", format: formatNum },
    { key: "hits", label: "Hits", format: formatNum },
    { key: "stolen_bases", label: "Stolen Bases", format: formatNum },
    { key: "ops", label: "OPS", format: formatAvg },
    { key: "war", label: "WAR", format: (v) => v?.toFixed(1) ?? "—" },
    { key: "runs", label: "Runs", format: formatNum },
  ],
  pitching: [
    { key: "era", label: "ERA", format: formatEra, order: "asc" },
    { key: "wins", label: "Wins", format: formatNum },
    { key: "strikeouts", label: "Strikeouts", format: formatNum },
    { key: "saves", label: "Saves", format: formatNum },
    { key: "whip", label: "WHIP", format: formatEra, order: "asc" },
    { key: "war", label: "WAR", format: (v) => v?.toFixed(1) ?? "—" },
    { key: "innings_pitched", label: "Innings Pitched", format: (v) => v?.toFixed(1) ?? "—" },
    { key: "wins", label: "Win %", format: (v) => v?.toFixed(3) ?? "—" },
  ],
};

export default function BaseballStatsApp() {
  const [activeTab, setActiveTab] = useState("batting");
  const [battingData, setBattingData] = useState([]);
  const [pitchingData, setPitchingData] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState(null);
  const [selectedPlayer, setSelectedPlayer] = useState(null);
  const [sortConfig, setSortConfig] = useState({ key: "war", direction: "desc" });
  const [loading, setLoading] = useState(true);
  const [useMock, setUseMock] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [batRes, pitRes] = await Promise.all([
          fetch(`${API_BASE}/batting`),
          fetch(`${API_BASE}/pitching`),
        ]);
        if (!batRes.ok || !pitRes.ok) throw new Error("API error");
        setBattingData(await batRes.json());
        setPitchingData(await pitRes.json());
      } catch {
        setUseMock(true);
        setBattingData(MOCK_BATTING);
        setPitchingData(MOCK_PITCHING);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  const handleSort = useCallback((key) => {
    setSortConfig((prev) => ({
      key,
      direction: prev.key === key && prev.direction === "desc" ? "asc" : "desc",
    }));
  }, []);

  const sortData = useCallback(
    (data) => {
      return [...data].sort((a, b) => {
        const aVal = a[sortConfig.key];
        const bVal = b[sortConfig.key];
        if (aVal === null || aVal === undefined) return 1;
        if (bVal === null || bVal === undefined) return -1;
        if (typeof aVal === "string") {
          return sortConfig.direction === "asc" ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
        }
        return sortConfig.direction === "asc" ? aVal - bVal : bVal - aVal;
      });
    },
    [sortConfig]
  );

  const handleSearch = async () => {
    if (!searchQuery.trim()) return;
    if (useMock) {
      const results = MOCK_PLAYERS.filter((p) => p.name.toLowerCase().includes(searchQuery.toLowerCase()));
      setSearchResults(results);
      return;
    }
    try {
      const res = await fetch(`${API_BASE}/players/search?name=${encodeURIComponent(searchQuery)}`);
      if (res.ok) {
        setSearchResults(await res.json());
      } else {
        setSearchResults([]);
      }
    } catch {
      setSearchResults([]);
    }
  };

  const handlePlayerClick = async (player) => {
    if (useMock) {
      setSelectedPlayer(player);
      return;
    }
    try {
      const res = await fetch(`${API_BASE}/players/${player.id}`);
      if (res.ok) setSelectedPlayer(await res.json());
    } catch {
      setSelectedPlayer(player);
    }
  };

  const getLeaders = (data, key, order = "desc", count = 5) => {
    return [...data]
      .filter((d) => d[key] !== null && d[key] !== undefined)
      .sort((a, b) => (order === "asc" ? a[key] - b[key] : b[key] - a[key]))
      .slice(0, count);
  };

  const currentData = activeTab === "batting" ? battingData : pitchingData;
  const currentCols = activeTab === "batting" ? BATTING_COLS : PITCHING_COLS;
  const sorted = sortData(currentData);

  return (
    <div style={styles.app}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Source+Sans+3:ital,wght@0,300;0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap');
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #1a1a2e; }
        ::-webkit-scrollbar-thumb { background: #c4342d; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #e63946; }
        
        @keyframes fadeIn { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes slideIn { from { opacity: 0; transform: translateX(-20px); } to { opacity: 1; transform: translateX(0); } }
        @keyframes pulseGlow { 0%, 100% { box-shadow: 0 0 20px rgba(196, 52, 45, 0.15); } 50% { box-shadow: 0 0 30px rgba(196, 52, 45, 0.3); } }
        @keyframes barGrow { from { width: 0%; } to { width: var(--bar-width); } }
        @keyframes countUp { from { opacity: 0; } to { opacity: 1; } }
      `}</style>

      {/* HEADER */}
      <header style={styles.header}>
        <div style={styles.headerInner}>
          <div style={styles.headerLeft}>
            <div style={styles.logoMark}>
              <svg width="36" height="36" viewBox="0 0 36 36" fill="none">
                <circle cx="18" cy="18" r="16" stroke="#c4342d" strokeWidth="2.5" />
                <path d="M10 18 Q18 8 26 18 Q18 28 10 18Z" fill="#c4342d" opacity="0.9" />
                <line x1="10" y1="18" x2="26" y2="18" stroke="#0f0f1e" strokeWidth="1.5" />
                <path d="M13 14 Q18 18 13 22" stroke="#0f0f1e" strokeWidth="1" fill="none" />
                <path d="M23 14 Q18 18 23 22" stroke="#0f0f1e" strokeWidth="1" fill="none" />
              </svg>
            </div>
            <div>
              <h1 style={styles.title}>DIAMOND<span style={styles.titleAccent}>STATS</span></h1>
              <p style={styles.subtitle}>2025 CINCINNATI REDS — STATISTICAL DATABASE</p>
            </div>
          </div>
          <div style={styles.headerRight}>
            <div style={styles.recordBadge}>
              <span style={styles.recordLabel}>2025 RECORD</span>
              <span style={styles.recordValue}>83-79</span>
            </div>
            {useMock && (
              <div style={styles.mockBadge}>DEMO MODE</div>
            )}
          </div>
        </div>
        <div style={styles.headerStripe} />
      </header>

      {/* SEARCH BAR */}
      <div style={styles.searchContainer}>
        <div style={styles.searchInner}>
          <div style={styles.searchInputWrap}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#888" strokeWidth="2" style={{ flexShrink: 0 }}>
              <circle cx="11" cy="11" r="8" />
              <line x1="21" y1="21" x2="16.65" y2="16.65" />
            </svg>
            <input
              style={styles.searchInput}
              placeholder="Search players..."
              value={searchQuery}
              onChange={(e) => {
                setSearchQuery(e.target.value);
                if (!e.target.value.trim()) setSearchResults(null);
              }}
              onKeyDown={(e) => e.key === "Enter" && handleSearch()}
            />
            {searchQuery && (
              <button
                style={styles.clearBtn}
                onClick={() => { setSearchQuery(""); setSearchResults(null); }}
              >
                ×
              </button>
            )}
          </div>
          <button style={styles.searchBtn} onClick={handleSearch}>SEARCH</button>
        </div>

        {/* Search Results Dropdown */}
        {searchResults !== null && (
          <div style={styles.searchResults}>
            {searchResults.length === 0 ? (
              <div style={styles.noResults}>No players found</div>
            ) : (
              searchResults.map((p, i) => (
                <div
                  key={p.id || i}
                  style={{ ...styles.searchResult, animationDelay: `${i * 50}ms` }}
                  onClick={() => { handlePlayerClick(p); setSearchResults(null); setSearchQuery(""); }}
                >
                  <span style={styles.resultName}>{p.name}</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#c4342d" strokeWidth="2">
                    <polyline points="9 18 15 12 9 6" />
                  </svg>
                </div>
              ))
            )}
          </div>
        )}
      </div>

      {/* PLAYER DETAIL MODAL */}
      {selectedPlayer && (
        <div style={styles.modalOverlay} onClick={() => setSelectedPlayer(null)}>
          <div style={styles.modal} onClick={(e) => e.stopPropagation()}>
            <button style={styles.modalClose} onClick={() => setSelectedPlayer(null)}>×</button>
            <div style={styles.modalHeader}>
              <h2 style={styles.modalName}>{selectedPlayer.name}</h2>
              <div style={styles.modalMeta}>
                {selectedPlayer.batting_stats?.[0] && (
                  <span style={styles.modalTag}>{selectedPlayer.batting_stats[0].position}</span>
                )}
                {selectedPlayer.pitching_stats?.[0] && (
                  <span style={styles.modalTag}>{selectedPlayer.pitching_stats[0].position}</span>
                )}
              </div>
            </div>
            {selectedPlayer.batting_stats?.length > 0 && (
              <div style={styles.modalSection}>
                <h3 style={styles.modalSectionTitle}>BATTING</h3>
                <div style={styles.modalGrid}>
                  {[
                    ["AVG", formatAvg(selectedPlayer.batting_stats[0].batting_avg)],
                    ["HR", selectedPlayer.batting_stats[0].homeruns],
                    ["RBI", selectedPlayer.batting_stats[0].rbi],
                    ["R", selectedPlayer.batting_stats[0].runs],
                    ["H", selectedPlayer.batting_stats[0].hits],
                    ["SB", selectedPlayer.batting_stats[0].stolen_bases],
                    ["OBP", formatAvg(selectedPlayer.batting_stats[0].obp)],
                    ["SLG", formatAvg(selectedPlayer.batting_stats[0].slugging)],
                    ["OPS", formatAvg(selectedPlayer.batting_stats[0].ops)],
                    ["BB", selectedPlayer.batting_stats[0].walks],
                    ["SO", selectedPlayer.batting_stats[0].strikeouts],
                    ["WAR", selectedPlayer.batting_stats[0].war?.toFixed(1)],
                  ].map(([label, val]) => (
                    <div key={label} style={styles.modalStat}>
                      <div style={styles.modalStatValue}>{val ?? "—"}</div>
                      <div style={styles.modalStatLabel}>{label}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}
            {selectedPlayer.pitching_stats?.length > 0 && (
              <div style={styles.modalSection}>
                <h3 style={styles.modalSectionTitle}>PITCHING</h3>
                <div style={styles.modalGrid}>
                  {[
                    ["W", selectedPlayer.pitching_stats[0].wins],
                    ["L", selectedPlayer.pitching_stats[0].losses],
                    ["ERA", formatEra(selectedPlayer.pitching_stats[0].era)],
                    ["G", selectedPlayer.pitching_stats[0].games],
                    ["GS", selectedPlayer.pitching_stats[0].games_started],
                    ["SV", selectedPlayer.pitching_stats[0].saves],
                    ["IP", selectedPlayer.pitching_stats[0].innings_pitched?.toFixed(1)],
                    ["SO", selectedPlayer.pitching_stats[0].strikeouts],
                    ["BB", selectedPlayer.pitching_stats[0].walks],
                    ["WHIP", formatEra(selectedPlayer.pitching_stats[0].whip)],
                    ["HR", selectedPlayer.pitching_stats[0].homeruns],
                    ["WAR", selectedPlayer.pitching_stats[0].war?.toFixed(1)],
                  ].map(([label, val]) => (
                    <div key={label} style={styles.modalStat}>
                      <div style={styles.modalStatValue}>{val ?? "—"}</div>
                      <div style={styles.modalStatLabel}>{label}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* MAIN CONTENT */}
      <main style={styles.main}>
        {/* TAB NAV */}
        <div style={styles.tabBar}>
          {["batting", "pitching", "leaders"].map((tab) => (
            <button
              key={tab}
              style={{
                ...styles.tab,
                ...(activeTab === tab ? styles.tabActive : {}),
              }}
              onClick={() => setActiveTab(tab)}
            >
              {tab.toUpperCase()}
              {activeTab === tab && <div style={styles.tabIndicator} />}
            </button>
          ))}
        </div>

        {loading ? (
          <div style={styles.loading}>
            <div style={styles.loadingDiamond}>
              <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
                <path d="M24 4 L44 24 L24 44 L4 24Z" stroke="#c4342d" strokeWidth="2" fill="none">
                  <animateTransform attributeName="transform" type="rotate" values="0 24 24;360 24 24" dur="2s" repeatCount="indefinite" />
                </path>
              </svg>
            </div>
            <p style={styles.loadingText}>Loading stats...</p>
          </div>
        ) : activeTab === "leaders" ? (
          /* LEADERS VIEW */
          <div style={styles.leadersContainer}>
            <h2 style={styles.leadersTitle}>STAT LEADERS</h2>
            <div style={styles.leadersSplit}>
              <div>
                <h3 style={styles.leadersGroupTitle}>
                  <span style={styles.leadersGroupIcon}>⚾</span> BATTING
                </h3>
                <div style={styles.leadersGrid}>
                  {LEADER_STATS.batting.map((stat) => {
                    const leaders = getLeaders(battingData, stat.key, "desc", 5);
                    const maxVal = leaders[0]?.[stat.key] || 1;
                    return (
                      <div key={stat.key} style={styles.leaderCard}>
                        <div style={styles.leaderCardTitle}>{stat.label}</div>
                        {leaders.map((p, i) => (
                          <div key={i} style={styles.leaderRow}>
                            <span style={styles.leaderRank}>{i + 1}</span>
                            <span style={styles.leaderName}>{p.name}</span>
                            <div style={styles.leaderBarTrack}>
                              <div
                                style={{
                                  ...styles.leaderBar,
                                  "--bar-width": `${(p[stat.key] / maxVal) * 100}%`,
                                  width: `${(p[stat.key] / maxVal) * 100}%`,
                                  animationDelay: `${i * 100}ms`,
                                }}
                              />
                            </div>
                            <span style={styles.leaderValue}>{stat.format(p[stat.key])}</span>
                          </div>
                        ))}
                      </div>
                    );
                  })}
                </div>
              </div>
              <div>
                <h3 style={styles.leadersGroupTitle}>
                  <span style={styles.leadersGroupIcon}>🔥</span> PITCHING
                </h3>
                <div style={styles.leadersGrid}>
                  {LEADER_STATS.pitching.map((stat) => {
                    const leaders = getLeaders(pitchingData, stat.key, stat.order || "desc", 5);
                    const vals = leaders.map((p) => p[stat.key]);
                    const maxVal = Math.max(...vals) || 1;
                    return (
                      <div key={stat.key + stat.label} style={styles.leaderCard}>
                        <div style={styles.leaderCardTitle}>{stat.label}</div>
                        {leaders.map((p, i) => (
                          <div key={i} style={styles.leaderRow}>
                            <span style={styles.leaderRank}>{i + 1}</span>
                            <span style={styles.leaderName}>{p.name}</span>
                            <div style={styles.leaderBarTrack}>
                              <div
                                style={{
                                  ...styles.leaderBar,
                                  width: `${(p[stat.key] / maxVal) * 100}%`,
                                  animationDelay: `${i * 100}ms`,
                                }}
                              />
                            </div>
                            <span style={styles.leaderValue}>{stat.format(p[stat.key])}</span>
                          </div>
                        ))}
                      </div>
                    );
                  })}
                </div>
              </div>
            </div>
          </div>
        ) : (
          /* TABLE VIEW */
          <div style={styles.tableContainer}>
            <div style={styles.tableScroll}>
              <table style={styles.table}>
                <thead>
                  <tr>
                    <th style={{ ...styles.th, ...styles.thRank }}>#</th>
                    {currentCols.map((col) => (
                      <th
                        key={col.key}
                        style={{
                          ...styles.th,
                          textAlign: col.align,
                          cursor: "pointer",
                          ...(col.align === "left" ? styles.thPlayer : {}),
                        }}
                        onClick={() => handleSort(col.key)}
                      >
                        <div style={{ display: "flex", alignItems: "center", gap: "4px", justifyContent: col.align === "left" ? "flex-start" : "center" }}>
                          {col.label}
                          {sortConfig.key === col.key && (
                            <span style={styles.sortArrow}>
                              {sortConfig.direction === "desc" ? "▼" : "▲"}
                            </span>
                          )}
                        </div>
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {sorted.map((row, i) => (
                    <tr
                      key={i}
                      style={{
                        ...styles.tr,
                        animationDelay: `${i * 20}ms`,
                        background: i % 2 === 0 ? "transparent" : "rgba(255,255,255,0.02)",
                      }}
                      onMouseEnter={(e) => {
                        e.currentTarget.style.background = "rgba(196, 52, 45, 0.08)";
                      }}
                      onMouseLeave={(e) => {
                        e.currentTarget.style.background = i % 2 === 0 ? "transparent" : "rgba(255,255,255,0.02)";
                      }}
                    >
                      <td style={{ ...styles.td, ...styles.tdRank }}>{i + 1}</td>
                      {currentCols.map((col) => (
                        <td
                          key={col.key}
                          style={{
                            ...styles.td,
                            textAlign: col.align,
                            ...(col.key === "name" ? styles.tdPlayer : {}),
                            ...(col.key === "war" ? {
                              color: row[col.key] > 2 ? "#4ade80" : row[col.key] > 0 ? "#d4d4d8" : "#ef4444",
                              fontWeight: 600,
                            } : {}),
                          }}
                          onClick={col.key === "name" ? () => {
                            const mockPlayer = MOCK_PLAYERS.find(p => p.name === row.name);
                            if (mockPlayer) handlePlayerClick(mockPlayer);
                            else handlePlayerClick({ id: null, name: row.name, batting_stats: activeTab === "batting" ? [row] : [], pitching_stats: activeTab === "pitching" ? [row] : [] });
                          } : undefined}
                        >
                          {col.format(row[col.key])}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </main>

      {/* FOOTER */}
      <footer style={styles.footer}>
        <p>Data sourced from Baseball Reference — 2025 Cincinnati Reds</p>
      </footer>
    </div>
  );
}

const styles = {
  app: {
    minHeight: "100vh",
    background: "#0f0f1e",
    color: "#e4e4e7",
    fontFamily: "'Source Sans 3', sans-serif",
  },
  header: {
    background: "linear-gradient(180deg, #161628 0%, #0f0f1e 100%)",
    borderBottom: "1px solid rgba(196, 52, 45, 0.2)",
    position: "relative",
  },
  headerInner: {
    maxWidth: "1400px",
    margin: "0 auto",
    padding: "20px 24px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  headerLeft: {
    display: "flex",
    alignItems: "center",
    gap: "16px",
  },
  logoMark: {
    width: "48px",
    height: "48px",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    background: "rgba(196, 52, 45, 0.1)",
    borderRadius: "12px",
    border: "1px solid rgba(196, 52, 45, 0.2)",
  },
  title: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "28px",
    fontWeight: 700,
    letterSpacing: "2px",
    color: "#fafafa",
    lineHeight: 1,
  },
  titleAccent: {
    color: "#c4342d",
  },
  subtitle: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "11px",
    fontWeight: 300,
    letterSpacing: "3px",
    color: "#71717a",
    marginTop: "4px",
  },
  headerRight: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
  },
  recordBadge: {
    display: "flex",
    flexDirection: "column",
    alignItems: "flex-end",
    gap: "2px",
  },
  recordLabel: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "10px",
    fontWeight: 300,
    letterSpacing: "2px",
    color: "#71717a",
  },
  recordValue: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "24px",
    fontWeight: 600,
    color: "#fafafa",
    letterSpacing: "1px",
  },
  mockBadge: {
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: "10px",
    fontWeight: 500,
    color: "#f59e0b",
    background: "rgba(245, 158, 11, 0.1)",
    border: "1px solid rgba(245, 158, 11, 0.3)",
    padding: "4px 10px",
    borderRadius: "4px",
    letterSpacing: "1px",
  },
  headerStripe: {
    height: "3px",
    background: "linear-gradient(90deg, transparent 0%, #c4342d 20%, #c4342d 80%, transparent 100%)",
    opacity: 0.6,
  },
  searchContainer: {
    maxWidth: "1400px",
    margin: "0 auto",
    padding: "16px 24px 0",
    position: "relative",
  },
  searchInner: {
    display: "flex",
    gap: "8px",
  },
  searchInputWrap: {
    flex: 1,
    display: "flex",
    alignItems: "center",
    gap: "10px",
    background: "#1a1a2e",
    border: "1px solid #2a2a3e",
    borderRadius: "8px",
    padding: "0 14px",
    transition: "border-color 0.2s",
  },
  searchInput: {
    flex: 1,
    background: "transparent",
    border: "none",
    outline: "none",
    color: "#e4e4e7",
    fontFamily: "'Source Sans 3', sans-serif",
    fontSize: "15px",
    padding: "12px 0",
  },
  clearBtn: {
    background: "none",
    border: "none",
    color: "#71717a",
    fontSize: "20px",
    cursor: "pointer",
    padding: "0 4px",
    lineHeight: 1,
  },
  searchBtn: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "14px",
    fontWeight: 500,
    letterSpacing: "1.5px",
    color: "#fafafa",
    background: "#c4342d",
    border: "none",
    borderRadius: "8px",
    padding: "0 24px",
    cursor: "pointer",
    transition: "background 0.2s",
    whiteSpace: "nowrap",
  },
  searchResults: {
    position: "absolute",
    top: "100%",
    left: "24px",
    right: "24px",
    background: "#1a1a2e",
    border: "1px solid #2a2a3e",
    borderRadius: "0 0 8px 8px",
    zIndex: 100,
    maxHeight: "240px",
    overflowY: "auto",
    boxShadow: "0 12px 40px rgba(0,0,0,0.5)",
  },
  searchResult: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "12px 16px",
    cursor: "pointer",
    borderBottom: "1px solid rgba(255,255,255,0.04)",
    animation: "fadeIn 0.3s ease both",
    transition: "background 0.15s",
  },
  resultName: {
    fontWeight: 600,
    fontSize: "15px",
  },
  noResults: {
    padding: "20px 16px",
    color: "#71717a",
    textAlign: "center",
    fontSize: "14px",
  },
  main: {
    maxWidth: "1400px",
    margin: "0 auto",
    padding: "16px 24px 40px",
  },
  tabBar: {
    display: "flex",
    gap: "4px",
    marginBottom: "20px",
    borderBottom: "1px solid #2a2a3e",
    paddingBottom: "0",
  },
  tab: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "15px",
    fontWeight: 400,
    letterSpacing: "2px",
    color: "#71717a",
    background: "transparent",
    border: "none",
    padding: "12px 24px",
    cursor: "pointer",
    position: "relative",
    transition: "color 0.2s",
  },
  tabActive: {
    color: "#fafafa",
    fontWeight: 500,
  },
  tabIndicator: {
    position: "absolute",
    bottom: "-1px",
    left: "0",
    right: "0",
    height: "2px",
    background: "#c4342d",
    borderRadius: "2px 2px 0 0",
  },
  loading: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    padding: "80px 0",
    gap: "16px",
  },
  loadingDiamond: {},
  loadingText: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "14px",
    letterSpacing: "2px",
    color: "#71717a",
  },
  tableContainer: {
    animation: "fadeIn 0.4s ease",
    border: "1px solid #2a2a3e",
    borderRadius: "8px",
    overflow: "hidden",
    background: "#13132a",
  },
  tableScroll: {
    overflowX: "auto",
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
    fontSize: "14px",
  },
  th: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "12px",
    fontWeight: 500,
    letterSpacing: "1px",
    color: "#a1a1aa",
    padding: "12px 10px",
    borderBottom: "1px solid #2a2a3e",
    background: "#161628",
    position: "sticky",
    top: 0,
    whiteSpace: "nowrap",
    userSelect: "none",
  },
  thRank: {
    width: "40px",
    textAlign: "center",
  },
  thPlayer: {
    minWidth: "180px",
    position: "sticky",
    left: 0,
    zIndex: 2,
    background: "#161628",
  },
  tr: {
    animation: "fadeIn 0.3s ease both",
    transition: "background 0.15s",
  },
  td: {
    padding: "10px 10px",
    borderBottom: "1px solid rgba(255,255,255,0.04)",
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: "13px",
    whiteSpace: "nowrap",
    color: "#d4d4d8",
  },
  tdRank: {
    textAlign: "center",
    color: "#52525b",
    fontWeight: 500,
    width: "40px",
  },
  tdPlayer: {
    fontFamily: "'Source Sans 3', sans-serif",
    fontWeight: 600,
    fontSize: "14px",
    color: "#fafafa",
    cursor: "pointer",
    position: "sticky",
    left: 0,
    background: "inherit",
    zIndex: 1,
  },
  sortArrow: {
    fontSize: "9px",
    color: "#c4342d",
  },
  leadersContainer: {
    animation: "fadeIn 0.4s ease",
  },
  leadersTitle: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "24px",
    fontWeight: 600,
    letterSpacing: "3px",
    marginBottom: "24px",
    color: "#fafafa",
  },
  leadersSplit: {
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "32px",
  },
  leadersGroupTitle: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "16px",
    fontWeight: 500,
    letterSpacing: "2px",
    color: "#a1a1aa",
    marginBottom: "16px",
    display: "flex",
    alignItems: "center",
    gap: "8px",
  },
  leadersGroupIcon: {
    fontSize: "18px",
  },
  leadersGrid: {
    display: "flex",
    flexDirection: "column",
    gap: "16px",
  },
  leaderCard: {
    background: "#13132a",
    border: "1px solid #2a2a3e",
    borderRadius: "8px",
    padding: "16px",
  },
  leaderCardTitle: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "13px",
    fontWeight: 500,
    letterSpacing: "1.5px",
    color: "#c4342d",
    marginBottom: "12px",
    textTransform: "uppercase",
  },
  leaderRow: {
    display: "flex",
    alignItems: "center",
    gap: "8px",
    padding: "4px 0",
  },
  leaderRank: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "13px",
    fontWeight: 600,
    color: "#52525b",
    width: "18px",
    textAlign: "center",
    flexShrink: 0,
  },
  leaderName: {
    fontSize: "13px",
    fontWeight: 600,
    color: "#d4d4d8",
    width: "140px",
    flexShrink: 0,
    overflow: "hidden",
    textOverflow: "ellipsis",
    whiteSpace: "nowrap",
  },
  leaderBarTrack: {
    flex: 1,
    height: "6px",
    background: "rgba(255,255,255,0.05)",
    borderRadius: "3px",
    overflow: "hidden",
  },
  leaderBar: {
    height: "100%",
    background: "linear-gradient(90deg, #c4342d, #e63946)",
    borderRadius: "3px",
    animation: "barGrow 0.8s ease both",
  },
  leaderValue: {
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: "13px",
    fontWeight: 500,
    color: "#fafafa",
    width: "50px",
    textAlign: "right",
    flexShrink: 0,
  },
  modalOverlay: {
    position: "fixed",
    inset: 0,
    background: "rgba(0,0,0,0.7)",
    backdropFilter: "blur(4px)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    zIndex: 1000,
    animation: "fadeIn 0.2s ease",
  },
  modal: {
    background: "#161628",
    border: "1px solid #2a2a3e",
    borderRadius: "12px",
    padding: "32px",
    maxWidth: "560px",
    width: "90%",
    maxHeight: "80vh",
    overflowY: "auto",
    position: "relative",
    animation: "fadeIn 0.3s ease",
    boxShadow: "0 24px 80px rgba(0,0,0,0.6)",
  },
  modalClose: {
    position: "absolute",
    top: "16px",
    right: "16px",
    background: "none",
    border: "none",
    color: "#71717a",
    fontSize: "24px",
    cursor: "pointer",
    lineHeight: 1,
    padding: "4px 8px",
  },
  modalHeader: {
    marginBottom: "24px",
  },
  modalName: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "32px",
    fontWeight: 700,
    color: "#fafafa",
    letterSpacing: "1px",
  },
  modalMeta: {
    display: "flex",
    gap: "8px",
    marginTop: "8px",
  },
  modalTag: {
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: "12px",
    fontWeight: 500,
    color: "#c4342d",
    background: "rgba(196, 52, 45, 0.1)",
    border: "1px solid rgba(196, 52, 45, 0.2)",
    padding: "4px 10px",
    borderRadius: "4px",
  },
  modalSection: {
    marginBottom: "24px",
  },
  modalSectionTitle: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "14px",
    fontWeight: 500,
    letterSpacing: "2px",
    color: "#c4342d",
    marginBottom: "12px",
    paddingBottom: "8px",
    borderBottom: "1px solid rgba(196, 52, 45, 0.2)",
  },
  modalGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(4, 1fr)",
    gap: "12px",
  },
  modalStat: {
    textAlign: "center",
    padding: "10px 4px",
    background: "rgba(255,255,255,0.02)",
    borderRadius: "6px",
    border: "1px solid rgba(255,255,255,0.04)",
  },
  modalStatValue: {
    fontFamily: "'Oswald', sans-serif",
    fontSize: "22px",
    fontWeight: 600,
    color: "#fafafa",
    lineHeight: 1.2,
  },
  modalStatLabel: {
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: "10px",
    fontWeight: 500,
    color: "#71717a",
    marginTop: "4px",
    letterSpacing: "0.5px",
  },
  footer: {
    borderTop: "1px solid #2a2a3e",
    padding: "20px 24px",
    textAlign: "center",
    fontFamily: "'Source Sans 3', sans-serif",
    fontSize: "12px",
    color: "#52525b",
  },
};
