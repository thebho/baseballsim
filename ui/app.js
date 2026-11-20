/**
 * Baseball Player Generator UI
 * Manages player list and interactions
 */

class PlayerManager {
    constructor() {
        this.players = [];
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadPlayersFromStorage();
        this.render();
    }

    setupEventListeners() {
        document.getElementById('addPlayerBtn').addEventListener('click', () => this.addRandomPlayer());
        document.getElementById('clearAllBtn').addEventListener('click', () => this.clearAll());
    }

    addRandomPlayer() {
        // Generate random player data
        const playerType = Math.random() > 0.5 ? 'pitcher' : 'batter';
        const player = this.generateRandomPlayer(playerType);
        this.players.push(player);
        this.savePlayersToStorage();
        this.render();
    }

    generateRandomPlayer(type) {
        const firstNames = [
            "James", "Robert", "Michael", "William", "David",
            "Richard", "Joseph", "Thomas", "Charles", "Christopher",
            "Daniel", "Matthew", "Anthony", "Mark", "Donald",
            "Steven", "Paul", "Andrew", "Joshua", "Kenneth",
            "Kevin", "Brian", "George", "Edward", "Ronald",
            "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob",
            "Gary", "Nicholas", "Eric", "Jonathan", "Stephen",
            "Larry", "Justin", "Scott", "Brandon", "Benjamin",
            "Samuel", "Frank", "Gregory", "Alexander", "Raymond",
            "Patrick", "Jack", "Dennis", "Jerry", "Tyler",
            "Aaron", "Jose", "Adam", "Henry", "Douglas"
        ];

        const lastNames = [
            "Smith", "Johnson", "Williams", "Brown", "Jones",
            "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
            "Thomas", "Taylor", "Moore", "Jackson", "Martin",
            "Lee", "Perez", "Thompson", "White", "Harris",
            "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
            "Walker", "Young", "Allen", "King", "Wright",
            "Scott", "Torres", "Peterson", "Phillips", "Campbell",
            "Parker", "Evans", "Edwards", "Collins", "Reeves",
            "Stewart", "Morris", "Morales", "Murphy", "Cook",
            "Rogers", "Gutierrez", "Ortiz", "Morgan", "Peterson"
        ];

        const teams = [
            "River Cats", "Iron Wolves", "Coastal Kings", "Desert Hawks",
            "Northside Thunder", "Bay Breakers", "Summit Eagles", "Lakewood Aces"
        ];

        const batterPositions = ["C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH"];
        const pitcherPositions = ["SP", "RP"];

        const firstName = firstNames[Math.floor(Math.random() * firstNames.length)];
        const lastName = lastNames[Math.floor(Math.random() * lastNames.length)];
        const age = Math.floor(Math.random() * 23) + 18; // 18-40
        const height = this.generateHeight();
        const weight = Math.floor(Math.random() * 111) + 150; // 150-260
        const throwingHand = Math.random() > 0.5 ? "Right" : "Left";
        const battingHand = Math.random() > 0.5 ? "Right" : "Left";
        const team = teams[Math.floor(Math.random() * teams.length)];
        const jerseyNumber = Math.floor(Math.random() * 99) + 1;
        const experience = Math.floor(Math.random() * 21); // 0-20

        const basePlayer = {
            firstName,
            lastName,
            age,
            height,
            weight,
            throwingHand,
            battingHand,
            team,
            jerseyNumber,
            experience,
            type
        };

        if (type === 'pitcher') {
            return {
                ...basePlayer,
                position: pitcherPositions[Math.floor(Math.random() * pitcherPositions.length)],
                stamina: Math.floor(Math.random() * 70) + 30,
                accuracy: Math.floor(Math.random() * 70) + 30,
                velocity: Math.floor(Math.random() * 70) + 30,
                pitch_variety: Math.floor(Math.random() * 70) + 30,
                wins: Math.floor(Math.random() * 301),
                losses: Math.floor(Math.random() * 201),
                era: (Math.random() * 5 + 1).toFixed(2)
            };
        } else {
            return {
                ...basePlayer,
                position: batterPositions[Math.floor(Math.random() * batterPositions.length)],
                power: Math.floor(Math.random() * 70) + 30,
                speed: Math.floor(Math.random() * 70) + 30,
                plate_discipline: Math.floor(Math.random() * 70) + 30,
                home_runs: Math.floor(Math.random() * 501),
                hits: Math.floor(Math.random() * 3001),
                strikeouts: Math.floor(Math.random() * 2001),
                batting_average: (Math.random() * 0.25 + 0.15).toFixed(3)
            };
        }
    }

    generateHeight() {
        // Generate height between 5'8" and 6'5"
        const totalInches = Math.floor(Math.random() * 10) + 68; // 68-77 inches
        const feet = Math.floor(totalInches / 12);
        const inches = totalInches % 12;
        return `${feet}'${inches}"`;
    }

    removePlayer(index) {
        this.players.splice(index, 1);
        this.savePlayersToStorage();
        this.render();
    }

    clearAll() {
        if (confirm('Are you sure you want to clear all players?')) {
            this.players = [];
            this.savePlayersToStorage();
            this.render();
        }
    }

    savePlayersToStorage() {
        localStorage.setItem('baseballPlayers', JSON.stringify(this.players));
    }

    loadPlayersFromStorage() {
        const stored = localStorage.getItem('baseballPlayers');
        if (stored) {
            this.players = JSON.parse(stored);
        }
    }

    render() {
        this.updateStats();
        this.renderPlayersList();
    }

    updateStats() {
        const total = this.players.length;
        const pitchers = this.players.filter(p => p.type === 'pitcher').length;
        const batters = this.players.filter(p => p.type === 'batter').length;

        document.getElementById('totalCount').textContent = total;
        document.getElementById('pitcherCount').textContent = pitchers;
        document.getElementById('batterCount').textContent = batters;
    }

    renderPlayersList() {
        const container = document.getElementById('playersList');

        if (this.players.length === 0) {
            container.innerHTML = '<p class="empty-message">No players yet. Click "Add Random Player" to get started!</p>';
            return;
        }

        container.innerHTML = this.players.map((player, index) => this.createPlayerCard(player, index)).join('');

        // Add event listeners to remove buttons
        document.querySelectorAll('.btn-remove').forEach((btn, index) => {
            btn.addEventListener('click', () => this.removePlayer(index));
        });
    }

    createPlayerCard(player, index) {
        const isPitcher = player.type === 'pitcher';
        const typeLabel = isPitcher ? 'Pitcher' : 'Batter';
        const typeClass = isPitcher ? 'pitcher' : 'batter';

        let statsHtml = '';
        if (isPitcher) {
            statsHtml = `
                <div class="stat-row">
                    <span class="stat-name">Stamina:</span>
                    <span class="stat-val">${player.stamina}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Accuracy:</span>
                    <span class="stat-val">${player.accuracy}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Velocity:</span>
                    <span class="stat-val">${player.velocity}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Pitch Variety:</span>
                    <span class="stat-val">${player.pitch_variety}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Wins/Losses:</span>
                    <span class="stat-val">${player.wins}/${player.losses}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">ERA:</span>
                    <span class="stat-val">${player.era}</span>
                </div>
            `;
        } else {
            statsHtml = `
                <div class="stat-row">
                    <span class="stat-name">Power:</span>
                    <span class="stat-val">${player.power}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Speed:</span>
                    <span class="stat-val">${player.speed}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Plate Discipline:</span>
                    <span class="stat-val">${player.plate_discipline}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Home Runs:</span>
                    <span class="stat-val">${player.home_runs}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Hits:</span>
                    <span class="stat-val">${player.hits}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-name">Batting Avg:</span>
                    <span class="stat-val">${player.batting_average}</span>
                </div>
            `;
        }

        return `
            <div class="player-card ${typeClass}">
                <span class="player-type ${typeClass}">${typeLabel}</span>
                <div class="player-name">#${player.jerseyNumber} ${player.firstName} ${player.lastName}</div>
                <div class="player-info">
                    <div class="player-info-row">
                        <span class="player-info-label">Position:</span>
                        <span>${player.position}</span>
                    </div>
                    <div class="player-info-row">
                        <span class="player-info-label">Team:</span>
                        <span>${player.team}</span>
                    </div>
                    <div class="player-info-row">
                        <span class="player-info-label">Age:</span>
                        <span>${player.age}</span>
                    </div>
                    <div class="player-info-row">
                        <span class="player-info-label">Height/Weight:</span>
                        <span>${player.height} / ${player.weight} lbs</span>
                    </div>
                    <div class="player-info-row">
                        <span class="player-info-label">Throws/Bats:</span>
                        <span>${player.throwingHand}/${player.battingHand}</span>
                    </div>
                </div>
                <div class="player-stats">
                    ${statsHtml}
                </div>
                <div class="player-actions">
                    <button class="btn btn-remove">Remove</button>
                </div>
            </div>
        `;
    }
}

// Initialize the app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new PlayerManager();
});
