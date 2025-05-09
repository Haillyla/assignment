import csv
import statistics
import pandas as pd
import matplotlib.pyplot as plt
class PlayerStats:
    def __init__(self, name, quoc, pos, squad, age, mp, start, minute, goal, assist,
                 yellow, red, xg, xag, prgc, prgp, prgr, gls, ast, xg1, xag1,
                 ga90, save, cs, pen, sot, sotper, gsh, dist, cmp, paper,
                 prodist, short, medium, long, kp, oth, ppa, crspa,
                 sca, sca90, goca, goca90, tkl, tklw, att, loss, block,
                 sh, pas, inter, touch, defpen, def3rd, mid3rd, att3rd,
                 attpen, atton, succ, tkld, carries, prodistan, progc,
                 onth, cpa, mis, dis, rec, prgre, fls, fld, off, crs,
                 recov, win, lost, won):
        self.Name = name
        self.Nationality = quoc
        self.Position = pos
        self.Squad = squad
        self.Age = age
        self.Games = mp
        self.Games_Starts = start
        self.Minutes = minute
        self.Goals = goal
        self.Assists = assist
        self.Yellow_Cards = yellow
        self.Red_Cards = red
        self.xG = xg
        self.xAG = xag
        self.Progressive_Carries = prgc
        self.Progressive_Passes = prgp
        self.Progressive_Passes_Received = prgr
        self.Goals_per90 = gls
        self.Assists_per90 = ast
        self.xG_per90 = xg1
        self.xAG_per90 = xag1
        self.GA90 = ga90 
        self.Save_Pct = save
        self.CS_Pct = cs 
        self.Pen_Save_Pct = pen if len(pen) > 0 else '0'
        self.Shots_on_Target_Pct = sot if len(sot) > 0 else '0'
        self.Shots_on_Target_per90 = sotper
        self.Goals_per_Shot = gsh if len(gsh) > 0 else '0'
        self.Avg_Shot_Distance = dist if len(dist) > 0 else '0'
        self.Passes_Completed = cmp
        self.Passes_Pct = paper
        self.Passes_Prog_Distance = prodist
        self.Passes_Short_Pct = short
        self.Passes_Medium_Pct = medium
        self.Passes_Long_Pct = long if len(long) > 0 else '0'
        self.Key_Passes = kp
        self.Passes_Final_Third = oth
        self.Passes_Pen_Area = ppa
        self.Crosses_Pen_Area = crspa
        self.SCA = sca
        self.SCA_per90 = sca90
        self.GCA = goca
        self.GCA_per90 = goca90
        self.Tackles = tkl
        self.Tackles_Won = tklw
        self.Challenges = att
        self.Challenges_Lost = loss
        self.Blocks = block
        self.Blocked_Shots = sh
        self.Blocked_Passes = pas
        self.Interceptions = inter
        self.Touches = touch
        self.Touches_Def_Pen_Area = defpen
        self.Touches_Def_3rd = def3rd
        self.Touches_Mid_3rd = mid3rd
        self.Touches_Att_3rd = att3rd
        self.Touches_Att_Pen_Area = attpen
        self.Take_Ons = atton if len(atton) > 0 else '0'
        self.Take_Ons_Won_Pct = succ if len(succ) > 0 else '0'
        self.Take_Ons_Tackled_Pct = tkld if len(tkld) > 0 else '0'
        self.Carries = carries
        self.Carries_Prog_Distance = prodistan
        self.Carries_Prog = progc
        self.Carries_Final_Third = onth
        self.Carries_Pen_Area = cpa
        self.Miscontrols = mis
        self.Dispossessed = dis
        self.Passes_Received = rec
        self.Prog_Passes_Received = prgre
        self.Fouls = fls
        self.Fouled = fld
        self.Offsides = off
        self.Crosses = crs
        self.Ball_Recoveries = recov
        self.Aerials_Won = win
        self.Aerials_Lost = lost
        self.Aerials_Won_Pct = won if len(won) > 0 else '0'
a = []
ghiban = []
scoreCre = []
goalCre = []
tack = []
attat = []
blo = []
with open('Stats.csv', mode ='r', encoding = 'utf-8-sig') as file:
    csvFile = csv.reader(file)
    trg = 0
    for lines in csvFile:
        if trg == 0:
            trg += 1
            continue
        a.append(PlayerStats(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11], lines[12], lines[13], lines[14], lines[15], lines[16], lines[17], lines[18], lines[19], lines[20], lines[21], lines[22], lines[23], lines[24], lines[25], lines[26], lines[27], lines[28], lines[29], lines[30], lines[31], lines[32], lines[33], lines[34], lines[35], lines[36], lines[37], lines[38], lines[39], lines[40], lines[41], lines[42], lines[43], lines[44], lines[45], lines[46], lines[47], lines[48], lines[49], lines[50], lines[51], lines[52], lines[53], lines[54], lines[55], lines[56], lines[57], lines[58], lines[59], lines[60], lines[61], lines[62], lines[63], lines[64], lines[65], lines[66], lines[67], lines[68], lines[69], lines[70], lines[71], lines[72], lines[73], lines[74], lines[75], lines[76]))
        ghiban.append(float(lines[8]))
        scoreCre.append(float(lines[39]))
        goalCre.append(float(lines[41]))
        tack.append(float(lines[43]))
        attat.append(float(lines[45]))
        blo.append(float(lines[47]))
f = open('top_3.txt', 'x')
a.sort(key = lambda x: -float(x.Goals))
with open('top_3.txt', 'a') as s:
    s.write('Highest Games: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Games_Starts))
with open('top_3.txt', 'a') as s:
    s.write('Highest goal: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Assists))
with open('top_3.txt', 'a') as s:
    s.write('Highest yellow card: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Red_Cards))
with open('top_3.txt', 'a') as s:
    s.write('Highest read card: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.xG))
with open('top_3.txt', 'a') as s:
    s.write('Highest expected goal: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.xAG))
with open('top_3.txt', 'a') as s:
    s.write('Highest expected assist goal: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Progressive_Carries))
with open('top_3.txt', 'a') as s:
    s.write('Highest progressive carries: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Progressive_Passes))
with open('top_3.txt', 'a') as s:
    s.write('Highest progressive passes: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Progressive_Passes_Received))
with open('top_3.txt', 'a') as s:
    s.write('Highest progressive passes received: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Goals_per90))
with open('top_3.txt', 'a') as s:
    s.write('Highest goal per 90: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Assists_per90))
with open('top_3.txt', 'a') as s:
    s.write('Highest assist per 90: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.xG_per90))
with open('top_3.txt', 'a') as s:
    s.write('Highest expect goal per 90: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.xAG_per90))
with open('top_3.txt', 'a') as s:
    s.write('Highest expect assist per 90: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Save_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest save percentage: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.CS_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest CS: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Pen_Save_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest penalty save percentage: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Shots_on_Target_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest shot on target percentage: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Shots_on_Target_per90))
with open('top_3.txt', 'a') as s:
    s.write('Highest shot on target per 90: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Goals_per_Shot))
with open('top_3.txt', 'a') as s:
    s.write('Highest goals per shot: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Avg_Shot_Distance))
with open('top_3.txt', 'a') as s:
    s.write('Highest avarnge shot distant: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Passes_Completed))
with open('top_3.txt', 'a') as s:
    s.write('Highest passes completed: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Passes_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest passes percentage: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Passes_Short_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest short passes: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Passes_Medium_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest medium passes: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Passes_Long_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest long passes: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Key_Passes))
with open('top_3.txt', 'a') as s:
    s.write('Highest key passes: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Passes_Final_Third))
with open('top_3.txt', 'a') as s:
    s.write('Highest passes final third: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Passes_Pen_Area))
with open('top_3.txt', 'a') as s:
    s.write('Highest passes pen area: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Crosses_Pen_Area))
with open('top_3.txt', 'a') as s:
    s.write('Highest crosses pen area: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.SCA))
with open('top_3.txt', 'a') as s:
    s.write('Highest SCA: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.SCA_per90))
with open('top_3.txt', 'a') as s:
    s.write('Highest SCA per 90: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Tackles))
with open('top_3.txt', 'a') as s:
    s.write('Highest tackles: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Tackles_Won))
with open('top_3.txt', 'a') as s:
    s.write('Highest tackles won: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Challenges))
with open('top_3.txt', 'a') as s:
    s.write('Highest challenges: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Challenges_Lost))
with open('top_3.txt', 'a') as s:
    s.write('Highest challenges lost: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Blocks))
with open('top_3.txt', 'a') as s:
    s.write('Highest blocks: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Blocked_Shots))
with open('top_3.txt', 'a') as s:
    s.write('Highest block shots: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Blocked_Passes))
with open('top_3.txt', 'a') as s:
    s.write('Highest block passes: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Interceptions))
with open('top_3.txt', 'a') as s:
    s.write('Highest interceptions: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Touches))
with open('top_3.txt', 'a') as s:
    s.write('Highest touches: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Touches_Def_Pen_Area))
with open('top_3.txt', 'a') as s:
    s.write('Highest touches def pen area: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Touches_Def_3rd))
with open('top_3.txt', 'a') as s:
    s.write('Highest touches def 3rd: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Touches_Mid_3rd))
with open('top_3.txt', 'a') as s:
    s.write('Highest touches mid 3rd: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Touches_Att_3rd))
with open('top_3.txt', 'a') as s:
    s.write('Highest touches att 3rd: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Touches_Att_Pen_Area))
with open('top_3.txt', 'a') as s:
    s.write('Highest touches att pen area: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Take_Ons))
with open('top_3.txt', 'a') as s:
    s.write('Highest take ons: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Take_Ons_Won_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest take ons won percentage: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Take_Ons_Tackled_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest take ons tackles percentage: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Carries))
with open('top_3.txt', 'a') as s:
    s.write('Highest carries: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Carries_Prog))
with open('top_3.txt', 'a') as s:
    s.write('Highest carries progress: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Carries_Final_Third))
with open('top_3.txt', 'a') as s:
    s.write('Highest carries final third: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Carries_Pen_Area))
with open('top_3.txt', 'a') as s:
    s.write('Highest carries pen area: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Miscontrols))
with open('top_3.txt', 'a') as s:
    s.write('Highest miscontrols: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Dispossessed))
with open('top_3.txt', 'a') as s:
    s.write('Highest dispossessed: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Passes_Received))
with open('top_3.txt', 'a') as s:
    s.write('Highest passes received: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Prog_Passes_Received))
with open('top_3.txt', 'a') as s:
    s.write('Highest Progress passes received: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Fouls))
with open('top_3.txt', 'a') as s:
    s.write('Highest fouls: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Fouled))
with open('top_3.txt', 'a') as s:
    s.write('Highest fouled: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Offsides))
with open('top_3.txt', 'a') as s:
    s.write('Highest offsides: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Crosses))
with open('top_3.txt', 'a') as s:
    s.write('Highest crosses: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Ball_Recoveries))
with open('top_3.txt', 'a') as s:
    s.write('Highest ball recoveries: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Aerials_Won))
with open('top_3.txt', 'a') as s:
    s.write('Highest aerial won: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Aerials_Lost))
with open('top_3.txt', 'a') as s:
    s.write('Highest aerial lost: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))
a.sort(key = lambda x: -float(x.Aerials_Won_Pct))
with open('top_3.txt', 'a') as s:
    s.write('Highest aerial won percentage: {}, {}, {}\n'.format(a[0].Name, a[1].Name, a[2].Name))

df = pd.read_csv("Stats.csv")

numeric_cols = df.select_dtypes(include='number').columns.tolist()

overall_stats = df[numeric_cols].agg(['mean', 'median', 'std'])
overall_stats['Team'] = 'Overall'
overall_stats = overall_stats.set_index('Team')

if 'Team' in df.columns:
    team_stats = df.groupby('Team')[numeric_cols].agg(['mean', 'median', 'std'])

    team_stats.columns = ['_'.join(col).strip() for col in team_stats.columns.values]
    team_stats.reset_index(inplace=True)

    overall_stats_flat = overall_stats.reset_index()

    final_df = pd.concat([overall_stats_flat, team_stats], ignore_index=True)
else:
    final_df = overall_stats.reset_index()

final_df.to_csv("Team_Stats_Summary.csv", index=False)

plt.hist(ghiban)
plt.show()
plt.hist(scoreCre)
plt.show()
plt.hist(goalCre)
plt.show()
plt.hist(tack)
plt.show()
plt.hist(attat)
plt.show()
plt.hist(blo)
plt.show()
