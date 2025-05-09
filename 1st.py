from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver1 = webdriver.Firefox()
driver1.get('https://fbref.com/en/comps/9/stats/Premier-League-Stats')
soup = BeautifulSoup(driver1.page_source, 'html.parser')
driver1.quit()

driver2 = webdriver.Firefox()
driver2.get('https://fbref.com/en/comps/9/keepers/Premier-League-Stats')
soup2 = BeautifulSoup(driver2.page_source, 'html.parser')
driver2.quit()

driver3 = webdriver.Firefox()
driver3.get('https://fbref.com/en/comps/9/shooting/Premier-League-Stats')
soup3 = BeautifulSoup(driver3.page_source, 'html.parser')
driver3.quit()

driver4 = webdriver.Firefox()
driver4.get('https://fbref.com/en/comps/9/passing/Premier-League-Stats')
soup4 = BeautifulSoup(driver4.page_source, 'html.parser')
driver4.quit()

driver5 = webdriver.Firefox()
driver5.get('https://fbref.com/en/comps/9/gca/Premier-League-Stats')
soup5 = BeautifulSoup(driver5.page_source, 'html.parser')
driver5.quit()

driver6 = webdriver.Firefox()
driver6.get('https://fbref.com/en/comps/9/defense/Premier-League-Stats')
soup6 = BeautifulSoup(driver6.page_source, 'html.parser')
driver6.quit()

driver7 = webdriver.Firefox()
driver7.get('https://fbref.com/en/comps/9/possession/Premier-League-Stats')
soup7 = BeautifulSoup(driver7.page_source, 'html.parser')
driver7.quit()

driver8 = webdriver.Firefox()
driver8.get('https://fbref.com/en/comps/9/misc/Premier-League-Stats')
soup8 = BeautifulSoup(driver8.page_source, 'html.parser')
driver8.quit()

temp1 = soup.find('div', attrs = {'id' : 'all_stats_standard'})
temp2 = temp1.find_all('tr', attrs = {'data-row': True})

temp3 = soup2.find('div', attrs = {'id' : 'div_stats_keeper'})
temp4 = temp3.find_all('tr', attrs = {'data-row': True})

temp5 = soup3.find('div', attrs = {'id' : 'div_stats_shooting'})
temp6 = temp5.find_all('tr', attrs = {'data-row': True})

temp7 = soup4.find('div', attrs = {'id' : 'div_stats_passing'})
temp8 = temp7.find_all('tr', attrs = {'data-row': True})

temp9 = soup5.find('div', attrs = {'id' : 'div_stats_gca'})
temp10 = temp9.find_all('tr', attrs = {'data-row': True})

temp11 = soup6.find('div', attrs = {'id' : 'div_stats_defense'})
temp12 = temp11.find_all('tr', attrs = {'data-row': True})

temp13 = soup7.find('div', attrs = {'id' : 'div_stats_possession'})
temp14 = temp13.find_all('tr', attrs = {'data-row': True})

temp15 = soup8.find('div', attrs = {'id' : 'div_stats_misc'})
temp16 = temp15.find_all('tr', attrs = {'data-row': True})

danh = []
count = 0
for x in range(len(temp2)):
	try:
		time = temp2[x].find('td', attrs = {'data-stat' : 'minutes_90s'}).text.strip()
	except AttributeError:
		continue
	try:
		name = temp2[x].find('a').text.strip()
	except AttributeError:
		name = "0"
	try:
		nat = temp2[x].find('td', attrs = {'data-stat' : 'nationality'}).text.strip()
	except AttributeError:
		nat = "0"
	try:
		pos = temp2[x].find('td', attrs = {'data-stat' : 'position'}).text.strip()
	except AttributeError:
		pos = "0"
	if float(time) < 1:
		if pos == 'GK':
			count += 1
		continue
	try:
		squad = temp2[x].find('td', attrs = {'data-stat' : 'team'}).text.strip()
	except AttributeError:
		squad = "0"
	try:
		age = temp2[x].find('td', attrs = {'data-stat' : 'age'}).text.strip()
	except AttributeError:
		age = "0"
	try:
		mp = temp2[x].find('td', attrs = {'data-stat' : 'games'}).text.strip()
	except AttributeError:
		mp = "0"
	try:
		start = temp2[x].find('td', attrs = {'data-stat' : 'games_starts'}).text.strip()
	except AttributeError:
		start = "0"
	try:
		minute = temp2[x].find('td', attrs = {'data-stat' : 'minutes'}).text.strip()
	except AttributeError:
		minute = "0"
	try:
		goal = temp2[x].find('td', attrs = {'data-stat' : 'goals'}).text.strip()
	except AttributeError:
		goal = "0"
	try:
		assist = temp2[x].find('td', attrs = {'data-stat' : 'assists'}).text.strip()
	except AttributeError:
		assist = "0"
	try:
		yellow = temp2[x].find('td', attrs = {'data-stat' : 'cards_yellow'}).text.strip()
	except AttributeError:
		yellow = "0"
	try:
		red = temp2[x].find('td', attrs = {'data-stat' : 'cards_red'}).text.strip()
	except AttributeError:
		red = "0"
	try:
		xg = temp2[x].find('td', attrs = {'data-stat' : 'xg'}).text.strip()
	except AttributeError:
		xg = "0"
	try:
		xag = temp2[x].find('td', attrs = {'data-stat' : 'xg_assist'}).text.strip()
	except AttributeError:
		xag = "0"
	try:
		prgc = temp2[x].find('td', attrs = {'data-stat' : 'progressive_carries'}).text.strip()
	except AttributeError:
		prgc = "0"
	try:
		prgp = temp2[x].find('td', attrs = {'data-stat' : 'progressive_passes'}).text.strip()
	except AttributeError:
		prgp = "0"
	try:
		prgr = temp2[x].find('td', attrs = {'data-stat' : 'progressive_passes_received'}).text.strip()
	except AttributeError:
		prgr = "0"
	try:
		gls = temp2[x].find('td', attrs = {'data-stat' : 'goals_per90'}).text.strip()
	except AttributeError:
		gls = "0"
	try:
		ast = temp2[x].find('td', attrs = {'data-stat' : 'assists_per90'}).text.strip()
	except AttributeError:
		ast = "0"
	try:
		xg1 = temp2[x].find('td', attrs = {'data-stat' : 'xg_per90'}).text.strip()
	except AttributeError:
		xg1 = "0"
	try:
		xag1 = temp2[x].find('td', attrs = {'data-stat' : 'xg_assist_per90'}).text.strip()
	except AttributeError:
		xag1 = "0"
	if pos == 'GK' :
		try:
			ga90 = temp4[count].find('td', attrs = {'data-stat' : 'gk_goals_against_per90'}).text.strip()
		except AttributeError:
			ga90 = "0"
		try:
			save = temp4[count].find('td', attrs = {'data-stat' : 'gk_save_pct'}).text.strip()
		except AttributeError:
			save = "0"
		try:
			cs = temp4[count].find('td', attrs = {'data-stat' : 'gk_clean_sheets_pct'}).text.strip()
		except AttributeError:
			cs = '0'
		try:
			pen = temp4[count].find('td', attrs = {'data-stat' : 'gk_pens_save_pct'}).text.strip()
		except AttributeError:
			pen = '0'
		count += 1
	try:
		sot = temp6[x].find('td', attrs = {'data-stat' : 'shots_on_target_pct'}).text.strip()
	except AttributeError:
		sot = '0'
	try:
		sotper = temp6[x].find('td', attrs = {'data-stat' : 'shots_on_target_per90'}).text.strip()
	except AttributeError:
		sotper = "0"
	try:
		gsh = temp6[x].find('td', attrs = {'data-stat' : 'goals_per_shot'}).text.strip()
	except AttributeError:
		gsh = '0'
	try:
		dist = temp6[x].find('td', attrs = {'data-stat' : 'average_shot_distance'}).text.strip()
	except AttributeError:
		dist = '0'

	try:
		cmp = temp8[x].find('td', attrs = {'data-stat' : 'passes_completed'}).text.strip()
	except AttributeError:
		cmp = "0"
	try:
		paper = temp8[x].find('td', attrs = {'data-stat' : 'passes_pct'}).text.strip()
	except AttributeError:
		paper = '0'
	try:
		prodist = temp8[x].find('td', attrs = {'data-stat' : 'passes_progressive_distance'}).text.strip()
	except AttributeError:
		prodist = "0"
	try:
		short = temp8[x].find('td', attrs = {'data-stat' : 'passes_pct_short'}).text.strip()
	except AttributeError:
		short = "0"
	try:
		medium = temp8[x].find('td', attrs = {'data-stat' : 'passes_pct_medium'}).text.strip()
	except AttributeError:
		medium = '0'
	try:
		long = temp8[x].find('td', attrs = {'data-stat' : 'passes_pct_long'}).text.strip()
	except AttributeError:
		long = '0'
	try:
		kp = temp8[x].find('td', attrs = {'data-stat' : 'assisted_shots'}).text.strip()
	except AttributeError:
		kp = "0"
	try:
		oth = temp8[x].find('td', attrs = {'data-stat' : 'passes_into_final_third'}).text.strip()
	except AttributeError:
		oth = "0"
	try:
		ppa = temp8[x].find('td', attrs = {'data-stat' : 'passes_into_penalty_area'}).text.strip()
	except AttributeError:
		ppa = "0"
	try:
		crspa = temp8[x].find('td', attrs = {'data-stat' : 'crosses_into_penalty_area'}).text.strip()
	except AttributeError:
		crspa = "0"
	try:
		propass = temp8[x].find('td', attrs = {'data-stat' : 'progressive_passses'}).text.strip()
	except AttributeError:
		propass = "0"
	try:
		sca = temp10[x].find('td', attrs = {'data-stat' : 'sca'}).text.strip()
	except AttributeError:
		sca = '0'
	try:
		sca90 = temp10[x].find('td', attrs = {'data-stat' : 'sca_per90'}).text.strip()
	except AttributeError:
		sca90 = '0'
	try:
		goca = temp10[x].find('td', attrs = {'data-stat' : 'gca'}).text.strip()
	except AttributeError:
		goca = "0"
	try:
		goca90 = temp10[x].find('td', attrs = {'data-stat' : 'gca_per90'}).text.strip()
	except AttributeError:
		goca90 = '0'
	try:
		tkl = temp12[x].find('td', attrs = {'data-stat' : 'tackles'}).text.strip()
	except AttributeError:
		tkl = '0'
	try:
		tklw = temp12[x].find('td', attrs = {'data-stat' : 'tackles_won'}).text.strip()
	except AttributeError:
		tklw = '0'
	try:
		att = temp12[x].find('td', attrs = {'data-stat' : 'challenges'}).text.strip()
	except AttributeError:
		att = '0'
	try:
		loss = temp12[x].find('td', attrs = {'data-stat' : 'challenges_lost'}).text.strip()
	except AttributeError:
		loss = '0'
	try:
		block = temp12[x].find('td', attrs = {'data-stat' : 'blocks'}).text.strip()
	except AttributeError:
		block = '0'
	try:
		sh = temp12[x].find('td', attrs = {'data-stat' : 'blocked_shots'}).text.strip()
	except AttributeError:
		sh = '0'
	try:
		pas = temp12[x].find('td', attrs = {'data-stat' : 'blocked_passes'}).text.strip()
	except AttributeError:
		pas = '0'
	try:
		inter = temp12[x].find('td', attrs = {'data-stat' : 'interceptions'}).text.strip()
	except AttributeError:
		inter = '0'

	try:
		touch = temp14[x].find('td', attrs = {'data-stat' : 'touches'}).text.strip()
	except AttributeError:
		touch = '0'
	try:
		defpen = temp14[x].find('td', attrs = {'data-stat' : 'touches_def_pen_area'}).text.strip()
	except AttributeError:
		defpen = '0'
	try:
		def3rd = temp14[x].find('td', attrs = {'data-stat' : 'touches_def_3rd'}).text.strip()
	except AttributeError:
		def3rd = '0'
	try:
		mid3rd = temp14[x].find('td', attrs = {'data-stat' : 'touches_mid_3rd'}).text.strip()
	except AttributeError:
		mid3rd = '0'
	try:
		att3rd = temp14[x].find('td', attrs = {'data-stat' : 'touches_att_3rd'}).text.strip()
	except AttributeError:
		att3rd = '0'
	try:
		attpen = temp14[x].find('td', attrs = {'data-stat' : 'touches_att_pen_area'}).text.strip()
	except AttributeError:
		attpen = '0'
	try:
		atton = temp14[x].find('td', attrs = {'data-stat' : 'take_ons'}).text.strip()
	except AttributeError:
		atton = '0'
	try:
		succ = temp14[x].find('td', attrs = {'data-stat' : 'take_ons_won_pct'}).text.strip()
	except AttributeError:
		succ = '0'
	try:
		tkld = temp14[x].find('td', attrs = {'data-stat' : 'take_ons_tackled_pct'}).text.strip()
	except AttributeError:
		tkld = '0'
	try:
		carries = temp14[x].find('td', attrs = {'data-stat' : 'carries'}).text.strip()
	except AttributeError:
		carries = '0'
	try:
		prodistan = temp14[x].find('td', attrs = {'data-stat' : 'carries_progressive_distance'}).text.strip()
	except AttributeError:
		prodistan = '0'
	try:
		progc = temp14[x].find('td', attrs = {'data-stat' : 'progressive_carries'}).text.strip()
	except AttributeError:
		progc = '0'
	try:
		onth = temp14[x].find('td', attrs = {'data-stat' : 'carries_into_final_third'}).text.strip()
	except AttributeError:
		onth = '0'
	try:
		cpa = temp14[x].find('td', attrs = {'data-stat' : 'carries_into_penalty_area'}).text.strip()
	except AttributeError:
		cpa = '0'
	try:
		mis = temp14[x].find('td', attrs = {'data-stat' : 'miscontrols'}).text.strip()
	except AttributeError:
		mis = '0'
	try:
		dis = temp14[x].find('td', attrs = {'data-stat' : 'dispossessed'}).text.strip()
	except AttributeError:
		dis = '0'
	try:
		rec = temp14[x].find('td', attrs = {'data-stat' : 'passes_received'}).text.strip()
	except AttributeError:
		rec = '0'
	try:
		prgre = temp14[x].find('td', attrs = {'data-stat' : 'progressive_passes_received'}).text.strip()
	except AttributeError:
		prgre = '0'


	try:
		fls = temp16[x].find('td', attrs = {'data-stat' : 'fouls'}).text.strip()
	except AttributeError:
		fls = '0'
	try:
		fld = temp16[x].find('td', attrs = {'data-stat' : 'fouled'}).text.strip()
	except AttributeError:
		fld = '0'
	try:
		off = temp16[x].find('td', attrs = {'data-stat' : 'offsides'}).text.strip()
	except AttributeError:
		off = '0'
	try:
		crs = temp16[x].find('td', attrs = {'data-stat' : 'crosses'}).text.strip()
	except AttributeError:
		crs = '0'
	try:
		recov = temp16[x].find('td', attrs = {'data-stat' : 'ball_recoveries'}).text.strip()
	except AttributeError:
		recov = '0'
	try:
		win = temp16[x].find('td', attrs = {'data-stat' : 'aerials_won'}).text.strip()
	except AttributeError:
		win = '0'
	try:
		lost = temp16[x].find('td', attrs = {'data-stat' : 'aerials_lost'}).text.strip()
	except AttributeError:
		lost = '0'
	try:
		won = temp16[x].find('td', attrs = {'data-stat' : 'aerials_won_pct'}).text.strip()
	except AttributeError:
		won = '0'
	quoc = nat.split()
	play = {
	"Name": name,
	"Nationality": quoc[1],
	"Position": pos,
	"Team": squad,
	"Age": age,
	"Games": mp,
	"Games_Starts": start,
	"Minutes": minute,
	"Goals": goal,
	"Assists": assist,
	"Yellow_Cards": yellow,
	"Red_Cards": red,
	"xG": xg,
	"xAG": xag,
	"Progressive_Carries": prgc,
	"Progressive_Passes": prgp,
	"Progressive_Passes_Received": prgr,
	"Goals_per90": gls,
	"Assists_per90": ast,
	"xG_per90": xg1,
	"xAG_per90": xag1,
	"GA90": ga90 if pos == 'GK' else '0',
	"Save_Pct": save if pos == 'GK' else '0',
	"CS_Pct": cs if pos == 'GK' else '0',
	"Pen_Save_Pct": pen if pos == 'GK' else '0',
	"Shots_on_Target_Pct": sot,
	"Shots_on_Target_per90": sotper,
	"Goals_per_Shot": gsh,
	"Avg_Shot_Distance": dist,
	"Passes_Completed": cmp,
	"Passes_Pct": paper,
	"Passes_Prog_Distance": prodist,
	"Passes_Short_Pct": short,
	"Passes_Medium_Pct": medium,
	"Passes_Long_Pct": long,
	"Key_Passes": kp,
	"Passes_Final_Third": oth,
	"Passes_Pen_Area": ppa,
	"Crosses_Pen_Area": crspa,
	"Progressive_Passes": propass,
	"SCA": sca,
	"SCA_per90": sca90,
	"GCA": goca,
	"GCA_per90": goca90,
	"Tackles": tkl,
	"Tackles_Won": tklw,
	"Challenges": att,
	"Challenges_Lost": loss,
	"Blocks": block,
	"Blocked_Shots": sh,
	"Blocked_Passes": pas,
	"Interceptions": inter,
	"Touches": touch,
	"Touches_Def_Pen_Area": defpen,
	"Touches_Def_3rd": def3rd,
	"Touches_Mid_3rd": mid3rd,
	"Touches_Att_3rd": att3rd,
	"Touches_Att_Pen_Area": attpen,
	"Take_Ons": atton,
	"Take_Ons_Won_Pct": succ,
	"Take_Ons_Tackled_Pct": tkld,
	"Carries": carries,
	"Carries_Prog_Distance": prodistan,
	"Carries_Prog": progc,
	"Carries_Final_Third": onth,
	"Carries_Pen_Area": cpa,
	"Miscontrols": mis,
	"Dispossessed": dis,
	"Passes_Received": rec,
	"Prog_Passes_Received": prgre,
	"Fouls": fls,
	"Fouled": fld,
	"Offsides": off,
	"Crosses": crs,
	"Ball_Recoveries": recov,
	"Aerials_Won": win,
	"Aerials_Lost": lost,
	"Aerials_Won_Pct": won
	}
	danh.append(play)
df = pd.DataFrame(danh)
df.to_csv('Stats.csv', index=False)