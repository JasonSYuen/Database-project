import sqlite3,string
from sqlite3 import Error
class sets:
    name = ""
    header = "{:<35}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<25}"
    head = header.format(" |", "0 |", "0 |", "0 |", "0 |", "0 |", "0 |", "0")
    chest = header.format(" |", "0 |", "0 |", "0 |", "0 |", "0 |", "0 |", "0")
    arm = header.format(" |", "0 |", "0 |", "0 |", "0 |", "0 |", "0 |", "0")
    waist = header.format(" |", "0 |", "0 |", "0 |", "0 |", "0 |", "0 |", "0")
    leg = header.format(" |", "0 |", "0 |", "0 |", "0 |", "0 |", "0 |", "0")
def print_monster(rows):
    header = "{:<15} {:<11} {:<11} {:<11}{:<11}{:<11}{:<15}{:<15}{:<15}"
    print(header.format("name","vs fire","vs water","vs thunder","vs ice", "vs dragon","smallest size", "largest size","species"))
    for row in rows:
        print(header.format(row[0],row[2],row[3],row[4],row[5],row[6],row[7], row[8],row[9])) 

def print_armor(rows):
    header = "{:<30} {:<11} {:<11} {:<11}{:<11}{:<11}{:<10}{:<20}"
    print(header.format("name","vs fire","vs water","vs thunder","vs ice", "vs dragon","defense","skill(s)", ))
    for row in rows:
        print(header.format(row[0],row[3],row[4],row[5],row[6],row[7], row[9],row[8]))

def print_biome(rows):
    header = "{:<20} {:<35} {:<30}"
    print(header.format("name","effect","description"))
    for row in rows:
        print(header.format(row[0],row[2],row[3])) 

def print_element(rows):
    header = "{:<20} {:<35}"
    print(header.format("name","description"))
    for row in rows:
        print(header.format(row[0],row[2])) 

def print_weapon(rows): #note this requires rows to be  a mix of element and weapon
    header = "{:<30} {:<25} {:<15} {:<11}{:<15}{:<11}{:<20}{:<15}"
    print(header.format("name","weapon type","element","rarity","damage type", "attack ","elemental attack", "affinity"))
    for row in rows:
        print(header.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])) 


def where(orig_statment, col_name,like_blank):
    print()
    sql = orig_statment + " where " + col_name + " like \"%" + like_blank + "%\""
    return sql


def order_by(orig_statment, col_name, asc_desc):
    print()
    sql = orig_statment + " order by " + col_name + " " + asc_desc

    return sql


def choice_order(_conn,sql,possible_col1):
    up_down = ""
    count = int(0)

    print("which attribute would you like to sort by")
    for i in possible_col1:
        if i != "":
            print( str(count) + ": "+i + " : " , end="")
        count +=1


    print()
    print("enter the number") #make print statemnet better
    userchoice3 = input()
    print()
    print("ascending or descending order")
    print("0: ascending order  1: descending order")
    userchoice4 = input()
    if userchoice4 == "0":
        up_down = "asc"
    else:
        up_down = "desc"

    sql = order_by(sql,possible_col1[int(userchoice3)],up_down)
    #print(sql)
    
    cur = _conn.cursor()
    x = cur.execute(sql)
    rows = cur.fetchall()

    return rows

#def choice_where(_conn,sql,possible_col2,attr):
    print()
    count = int(0)

    print("where would you like to look for your key word")
    for i in possible_col2:
        if i != "":
            print( str(count) + ": "+i + " : " , end="")
        count +=1


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def viewtables(_conn):
    print("which table would you like to view")
    
    print("monster  : armor  : biome  : element  : weapon")
    userchoice = ""
    userchoice = input()

    sql = """select *from """ + userchoice

    if (userchoice == "monster" or userchoice == "armor" or userchoice == "biome" or userchoice == "element" or userchoice == "weapon"):
        cur = _conn.cursor()
        x = cur.execute(sql)
        rows = cur.fetchall()

        possible_col1 = ["","","","","","","","","","",""]
        possible_col2 = ["","","","","","","","","","",""]

        #header = "{:>10}"
        header = "{:<10} "
        if userchoice == "monster":
            print_monster(rows)
            possible_col1[0] = "m_smallestsize"
            possible_col1[1] = "m_largestsize"

            print()
            print("1: exit back")
            print("2: sort by attribute")
            print("3: find a monster's weakness")

            userchoice2 = input()

            if userchoice2 == "1":
                print("back to main")

            if userchoice2 == "2":
                rows = choice_order(_conn,sql,possible_col1)
                print_monster(rows)
            
            if userchoice2 == "3": 
                print("which monster?")
                userchoice7 = input()
                sql = "select m_vsfire, m_vswater, m_vsthunder, m_vsice, m_vsdragon from monster where m_name like \"%" + userchoice7 + "%\""
                #print(sql)
                cur = _conn.cursor()
                x = cur.execute(sql)
                rows = cur.fetchall()
                count = int(0)
                print(userchoice7 + " is weak to")
                for row in rows:
                    for r in row:
                        
                        #print(r, end=" ")
                        if (r == "3 star" or r == "2 star"):

                            if count == 0:
                                print("fire", end=" ")
                            if count == 1:
                                print("water", end=" ")
                            if count == 2:
                                print("thunder", end=" ")
                            if count == 3:
                                print("ice", end=" ")
                            if count == 4:
                                print("dragon", end=" ")

                        count +=1
                
                sql = "select p_name from monster join monpart on m_monsterkey = mp_monsterkey join part on p_partkey = mp_partkey where m_name like \"%" + userchoice7 + "%\""
                cur = _conn.cursor()
                x = cur.execute(sql)
                rows = cur.fetchall()
                print()
                print(userchoice7 +" has these breakable parts: ")
                for row in rows:
                    for r in row:
                        print(r, end = " ")






            #indv monst weakness + partbreak



        
        elif userchoice == "armor":
            print_armor(rows)
            possible_col1[0] = "a_vsfire"
            possible_col1[1] = "a_vswater"
            possible_col1[2] = "a_vsthunder"
            possible_col1[3] = "a_vsice"
            possible_col1[4] = "a_vsdragon"
            possible_col1[5] = "a_defense"

            possible_col2[0] = "a_skill"
            print()
            print("1: exit back")
            print("2: sort by attribute")
            print("3: find skills")

            userchoice2 = input()

            if userchoice2 == "1":
                print("back to main")

            if userchoice2 == "2":
                rows = choice_order(_conn,sql,possible_col1)
                print_armor(rows)
            
            if userchoice2 == "3":
                print("what skill are you looking for")
                print("make sure you type the name correctly or it will not print anything!")
                userchoice5 = input()
                sql = where(sql,str(possible_col2[0]),userchoice5)
                #print(sql)
                cur = _conn.cursor()
                x = cur.execute(sql)
                rows = cur.fetchall()
                print_armor(rows)


                
                

        
        elif userchoice == "biome":
            print_biome(rows)

            print()
            print("1: exit back")
            print("2: find all monsters in biome")

            userchoice2 = input()
            if userchoice2 == "1":
                print("back to main")

            if userchoice2 == "2":
                print("what biome's monsters are you looking for")
                print("make sure you type the name correctly or it will not print anything!")
                userchoice6 = input()

                
                sql = "select distinct(m_name) from biome join monbiome on b_biomekey = mb_biomekey join monster on m_monsterkey = mb_monsterkey where b_name like \"%" + userchoice6 +"%\";"
                #print(sql)
                
                cur = _conn.cursor()
                x = cur.execute(sql)
                rows = cur.fetchall()
                #print("name")
                for row in rows:
                    for r in row:
                        print(r)

        


        elif userchoice == "element":
            print_element(rows)


        elif userchoice == "weapon":
            sql = """select w_name, w_weapontype, e_name, w_rarity, w_damagetype, w_attack, w_elementalattack, w_affinity
                    from weapon  
                    join element on w_elementkey = e_elementkey"""
            
            cur = _conn.cursor()
            x = cur.execute(sql)
            rows = cur.fetchall()

            print_weapon(rows)

            possible_col1[0] = "w_rarity"
            possible_col1[1] = "w_elementalattack"
            possible_col1[2] = "w_attack"
            possible_col1[3] = "w_affinity"

            possible_col2[0] = "w_weapontype"
            possible_col2[1] = "e_name"
            possible_col2[2] = "w_damagetype"
            print()
            print("1: exit back")
            print("2: sort by attribute")
            print("3: look for specific weapon type")
            print("4: look for specific element")
            print("5: look for specific damage type")
            print("make sure you type the name correctly or it will not print anything!")
            userchoice2 = input()

            if userchoice2 == "1":
                print("back to main")

            if userchoice2 == "2":
                rows = choice_order(_conn,sql,possible_col1)
                print_weapon(rows)
            
            if userchoice2 == "3" or userchoice2 == "4" or userchoice2 == "5":
                print("what are you looking for")
                userchoice5 = input()
                sql = where(sql,str(possible_col2[int(userchoice2)-3]),userchoice5)
                #print(sql)
                cur = _conn.cursor()
                x = cur.execute(sql)
                rows = cur.fetchall()
                print_weapon(rows)




        

    else:
        print("invalid answer")


        
        


    #print(*x)

    
    #print(len(rows[0]))

    print ("\n")
        
def builds(_conn, build):
    c = _conn.cursor()
    program = True;
    while program == True:
        print("What would you like to do with your build?")
        print("1: create new build")
        print("2: see existing builds")
        print("3: select armor")
        print("4: find total defenses")
        print("5: back")
        
        try:
            userchoice = int(input())
            #adding to the build list
            if userchoice == 1:
                build.update({len(build)+1: sets()})
                print("name the build")
                n = str(input())
                build[len(build)].name = n
                
                
            if userchoice == 2:
                #table of all the builds
                for i in build:
                    print(build[i].name + ":")
                    header = "{:<35}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<25}"
                    print(header.format("name |", "vsFire |", "vsWater |", "vsThunder |", "vsIce |", "vsDragon |", "defense |", "skill"))
                    print("head: " + build[i].head)
                    print("chest: " + build[i].chest)
                    print("arm: " + build[i].arm)
                    print("waist: " + build[i].waist)
                    print("leg: " + build[i].leg + "\n")
            
            if userchoice == 3:
                #first, search for armor piece
                print("What armor do you wish to insert")
                search = str(input())
                selectPieces = """
                    SELECT a_name
                    FROM armor
                    WHERE a_name LIKE \"%""" + search + "%\""
                rows = c.execute(selectPieces)
                
                #show search results
                print("Select from the follow:")
                searches = {}
                counter = 1
                for row in rows.fetchall():
                    header = "{:<5}{:<35}"
                    print(header.format(counter, row[0]))
                    header = "{:<35}"
                    name = header.format(row[0])
                    searches.update({counter: name})
                    counter = counter + 1;
                
                #take selection
                search = int(input())
                armor = searches[search]
                selectPiece = """
                    SELECT *
                    FROM armor
                    WHERE a_name LIKE \"%""" + armor.strip() + "%\""
                rows2 = c.execute(selectPiece)
                
                #converting armor piece into a string
                piece = ""
                for row in rows2.fetchall():
                    header = "{:<35}{:<12}{:<12}{:<12}{:<12}{:<12}{:<5}{:<25}"
                    piece = header.format(str(row[0]) + "|", str(row[3]) + "|", str(row[4]) + "|", str(row[5]) + "|", str(row[6]) + "|", str(row[7]) + "|", str(row[9]) + "|", str(row[8]))
                
                #placing armor in piece
                print("What build do you want to put this armor")
                counter = 1
                for i in build:
                    print(str(counter) + ": " + build[i].name)
                    counter = counter + 1;
                setChoice = int(input())
                
                #setting armor in the right slot
                if piece.find("Helm") != -1 or piece.find("Hood") != -1 or piece.find("Headdress") != -1:
                    build[setChoice].head = piece
                if piece.find("Mail") != -1 or piece.find("Haori") != -1:
                    build[setChoice].chest = piece
                if piece.find("Vambrace") != -1 or piece.find("Kote") != -1:
                    build[setChoice].arm = piece
                if piece.find("Coil") != -1 or piece.find("Obi") != -1:
                    build[setChoice].waist = piece
                if piece.find("Greaves") != -1  or piece.find("Hakama") != -1:
                    build[setChoice].leg = piece
                
            if userchoice == 4:
                print("Choose a build:")
                counter = 1
                for i in build:
                    print(str(counter) + ": " + build[i].name)
                    counter = counter + 1;
                setChoice = int(input())
            
                #getting values
                hvalues = build[setChoice].head.split("|")
                cvalues = build[setChoice].chest.split("|")
                avalues = build[setChoice].arm.split("|")
                wvalues = build[setChoice].waist.split("|")
                lvalues = build[setChoice].leg.split("|")
                
                #total defense
                print("total defense")
                defense = 0
                defense = int(hvalues[6].strip()) + int(cvalues[6].strip()) + int(avalues[6].strip()) + int(wvalues[6].strip()) + int(lvalues[6].strip())
                print(defense)
                print()

                #elements
                print("vsFire")
                fire = 0
                fire = int(hvalues[1].strip()) + int(cvalues[1].strip()) + int(avalues[1].strip()) + int(wvalues[1].strip()) + int(lvalues[1].strip())
                print(fire)
                print()
                
                print("vsWater")
                water = 0
                water = int(hvalues[2].strip()) + int(cvalues[2].strip()) + int(avalues[2].strip()) + int(wvalues[2].strip()) + int(lvalues[2].strip())
                print(water )
                print()
                
                print("vsThunder")
                thunder = 0
                thunder = int(hvalues[3].strip()) + int(cvalues[3].strip()) + int(avalues[3].strip()) + int(wvalues[3].strip()) + int(lvalues[3].strip())
                print(thunder )
                print()
                
                print("vsIce")
                ice = 0
                ice = int(hvalues[4].strip()) + int(cvalues[4].strip()) + int(avalues[4].strip()) + int(wvalues[4].strip()) + int(lvalues[4].strip())
                print(ice )
                print()
                
                print("vsDragon")
                dragon = 0
                dragon = int(hvalues[5].strip()) + int(cvalues[5].strip()) + int(avalues[5].strip()) + int(wvalues[5].strip()) + int(lvalues[5].strip())
                print(dragon )
                print()
                
                    
            if userchoice == 5:
                program =  False
        except:
            print("Please input a valid input")


def update(_conn):
    print()
    print("what would you like to do")
    print("1: update")
    print("2: insert")
    print("3: delete")

    userchoice = input()

    if userchoice == "1":
        print ("enter the table, attribute, updated value,name coloumn, and name that you wish to update ie: monster m_smallestsize 1300 m_name Rathalos")
        try:
            table1,attribute1,value,name_col,name1 = input().split()
            sql = "update " + table1 + " set " + attribute1 + " = ? where " + name_col + " like \"%" + name1 + "%\""
            print(sql)
        
            cur = _conn.cursor()
            x = cur.execute(sql,[(int(value))])
            print("updated")
        except:
            print("update failed")
            print("")

    if userchoice == "2":
        print("1: add monster")
        print("2: add armor")
        print("3: add weapon")

        
        userchoice2 = input()

        if userchoice2 == "1":
            primary_key = primarykey(_conn,"monster")

            print("input name, primary key, vs_fire, vs_water, vs_thunder, vs_ice, vs_dragon,smallest size, largest size, species")
            print("ie: Nightshade Paolumu,9,2 star,3 star,1 star,1 star,Resistant,446,1429,Flying Wyvern ")
            try:

                userchoice3 = input().split(",")
                

                sql1 = "insert into monster Values(?,?,?,?,?,?,?,?,?,?)"
                print(sql1)

                y = userchoice3[0],int(userchoice3[1]),userchoice3[2],userchoice3[3],userchoice3[4],userchoice3[5],userchoice3[6],int(userchoice3[7]),int(userchoice3[8]),userchoice3[9]
                cur = _conn.cursor()
                x = cur.execute(sql1,y)


                print("what biomes is this monster in (enter b_biomekeys seperated by commas)")
                userchoice3 = input().split(",")
                for x in userchoice3:
                    print(x)
                    sql2 = "insert into monbiome values(?,?)"
                    print(sql2)

                    #need code to execute
                    y = int(primary_key),int(x)
                    cur = _conn.cursor()
                    x = cur.execute(sql2,y)



                print("what elements is this monster (enter e_elementkeys seperated by commas)")
                userchoice3 = input().split(",")
                for x in userchoice3:
                    sql2 = "insert into monele values(?,?)"
                    print(sql2)
                    #need code to execute
                    cur = _conn.cursor()
                    y = int(primary_key),int(x)
                    x = cur.execute(sql2,y)


                print("how many parts can be interacted with on this monster")
                userchoice3 = input()
                for i in range (0,int(userchoice3)):
                    print("enter 1 breakable part and what is the part weak to.(enter p_partkey, mp_slicing, mp_blunt, mp_ammo, mp_carvable)")
                    print("ie: 1,3 star,3 star,3 star,FALSE")
                    userchoice4 = input().split(",")
                    sql2 = "insert into monpart values (?,?,?,?,?,?)"
                    
                    
                    # need code to execute
                    cur = _conn.cursor()
                    y = int(primary_key),int(userchoice4[0]),userchoice4[1],userchoice4[2],userchoice4[3],userchoice4[4]
                    x = cur.execute(sql2,y)
            except:
                print("insert failed")
                print("")
        
        if userchoice2 == "2":
            primary_key = primarykey(_conn,"armor")

            print("input name,primary key, monster key, a_vsfire, a_vswater, a_vsthunder, a_vsuce, a_vsdragon, a_skill, a_defense ")
            print("ie: Jagras Helm Alpha,41,3,1,1,1,1,1,speed eater 2,50")

            try:
                userchoice3 = input().split(",")

                sql1 = "insert into armor Values(?,?,?,?,?,?,?,?,?,?)"
                #print(sql1)

                y = userchoice3[0],int(userchoice3[1]),int(userchoice3[2]),int(userchoice3[3]),int(userchoice3[4]),int(userchoice3[5]),int(userchoice3[6]),int(userchoice3[7]),userchoice3[8],int(userchoice3[9])
                cur = _conn.cursor()
                x = cur.execute(sql1,y)


                print("how many different drops are needed to make this armor piece")
                userchoice3 = input()
                for i in range (0,int(userchoice3)):
                    print("what drops are needed to make this armor piece (enter d_dropkey,ad_quantity seperated by commas)")
                    userchoice3 = input().split(",")
                    
                    sql2 = "insert into armdrop values(?,?,?)"
                    

                    y = int(primary_key),int(userchoice3[0]),int(userchoice3[1]),
                    cur = _conn.cursor()
                    x = cur.execute(sql2,y)
            except:
                print("insert failed")
                print("")

        if userchoice2 == "3":
            primary_key = primarykey(_conn,"weapon")
            print("input name,primary key, weapon type,element key, rarity, damage type, attack, elemental attack,affinity,monsterkey ")
            print("ie: Jagras Gunlance,16,Gunlance,9,1,slicing,100,0,.15,3")
            try:
                userchoice3 = input().split(",")

                sql1 = "insert into weapon Values(?,?,?,?,?,?,?,?,?,?)"
                #print(sql1)

                y = userchoice3[0],int(userchoice3[1]),userchoice3[2],int(userchoice3[3]),int(userchoice3[4]),userchoice3[5],int(userchoice3[6]),int(userchoice3[7]),float(userchoice3[8]),userchoice3[9]
                cur = _conn.cursor()
                x = cur.execute(sql1,y)


                print("how many different drops are needed to make this weapon ")
                userchoice3 = input()
                for i in range (0,int(userchoice3)):
                    print("what drops are needed to make this weapon piece (enter d_dropkey,wd_quantity seperated by commas)")
                    userchoice4 = input().split(",")
                    
                    sql2 = "insert into weadrop values(?,?,?)"
                    

                    y = int(primary_key),int(userchoice4[0]),int(userchoice4[1]),
                    cur = _conn.cursor()
                    x = cur.execute(sql2,y)
            except:
                print("insert failed")
                print("")

    if userchoice == "3":

        print ("enter the table, attribute, and name that you wish to delete ie: monster, m_name, Nightshade Paolumu")
        try: 
            userchoice2 = input().split(",")
            sql = "delete from ? where ? like ?"
            
            #need code to execute it
            cur = _conn.cursor()
            x = cur.execute(sql,userchoice2[0],userchoice2[1],userchoice2[2])
            print("deleted")
        except:
            print("delete failed")
            print("")


def primarykey(_conn,table):
    sql = "select count(*) from " + table
    cur = _conn.cursor()
    x = cur.execute(sql)
    rows = cur.fetchall()
    primary_key = int(rows[0][0]) + 1
    print("your primary key is: " + str(primary_key))
    return primary_key


def wishlist(_conn, build):
    c = _conn.cursor()
    print("Choose a build:")
    counter = 1
    for i in build:
        print(str(counter) + ": " + build[i].name)
        counter = counter + 1;
    setChoice = int(input())

    #getting values
    hvalues = build[setChoice].head.split("|")
    cvalues = build[setChoice].chest.split("|")
    avalues = build[setChoice].arm.split("|")
    wvalues = build[setChoice].waist.split("|")
    lvalues = build[setChoice].leg.split("|")

    hName = hvalues[0].strip()
    cName = cvalues[0].strip()
    aName = avalues[0].strip()
    wName = wvalues[0].strip()
    lName = lvalues[0].strip()
    
    query = """
        SELECT a_name, d_name, ad_quantity
        FROM armor
        JOIN armdrop ON a_armorkey = ad_armorkey
        JOIN drops ON ad_dropkey = d_dropkey
        WHERE a_name = \"""" + hName + "\" OR a_name = \"" + cName + "\" OR a_name = \"" + aName + "\" OR a_name = \"" + wName + "\" OR a_name = \"" + lName + "\""
    rows3 = c.execute(query)
    #drops = {}
    for row in rows3.fetchall():
        header = "{:<35}{:<35}{:<5}"
        inputs = header.format(row[0] + "|", row[1] + "|", row[2])
        print(inputs)
        #splits = inputs.split("|")
        #drops.update({splits[1].strip():splits[2].strip()})
    
    print("Would you like this in total?")
    print("1: Yes")
    print("2: No")
    answer = int(input())
    
    if answer == 1:
        query = """
            SELECT d_name, ad_quantity
            FROM armor
            JOIN armdrop ON a_armorkey = ad_armorkey
            JOIN drops ON ad_dropkey = d_dropkey
            WHERE a_name = \"""" + hName + "\" OR a_name = \"" + cName + "\" OR a_name = \"" + aName + "\" OR a_name = \"" + wName + "\" OR a_name = \"" + lName + "\"" + "GROUP BY d_name"
        rows4 = c.execute(query)
        for row in rows4.fetchall():
            header = "{:<35}{:<5}"
            print(header.format(row[0] + "|", row[1]))

def main():

    database = r"project.sqlite"
    #print("hello")
    # create a database connection
    conn = openConnection(database)
    with conn:
        print("hello")
        build = {}
        endprogram = False
        userchoice = 0
        while (endprogram == False):
            print("input what you would like to do")
            print("1: end program")
            print("2: view tables")
            print("3: build armor sets")
            print("4: drop list") #?
            print("5: update database")




            try:
                userchoice = int(input())
                if userchoice == 1:
                    print("ending program")
                    endprogram = True

                if userchoice == 2:
                    viewtables(conn)

                if userchoice == 3:
                    builds(conn,build)

                if userchoice == 4:
                    wishlist(conn,build)
                if userchoice == 5:
                    print("developer password ... hint: password")
                    userchoice0 = input()
                    if userchoice0 == "password":
                        update(conn)
                    
                    else:
                        print("incorrect password")
            except:
                print("Please use a valid input")


            #view tables:
            #build armor sets:

    closeConnection(conn, database)

if __name__ == '__main__':
    main()
