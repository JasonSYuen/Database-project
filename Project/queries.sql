.headers ON
.separator |

--1) basic select
select m_name
from monster
where m_species = "Flying Wyvern";

--2) build a weapon

select m_name, d_name, wd_quantity
from weapon
join weadrop on w_weaponkey = wd_weaponkey
join drops on wd_dropkey = d_dropkey
join monster on w_monsterkey = m_monsterkey
where w_name = "Flame Knife 1" ;

--3) build a full set of armor

select m_name, d_name, sum(ad_quantity)
from armor
join armdrop on a_armorkey = ad_armorkey
join drops on d_dropkey=  ad_dropkey
join monster on m_monsterkey = a_monsterkey
where a_name like 'Jagras%'
group by d_dropkey;

--4) build a mixed set of armor
select m_name, d_name, sum(ad_quantity)
from armor
join armdrop on a_armorkey = ad_armorkey
join drops on d_dropkey=  ad_dropkey
join monster on m_monsterkey = a_monsterkey
where a_name like 'Jagras Helm'
or a_name like 'Jagras Coil'
or a_name like 'Rathalos Greaves Alpha'
or a_name like 'Rathalos Vambrace Alpha'   -- Vambrace need to change to vanbraces in table
or a_name like 'Pukei Mail Alpha'
group by m_name, d_dropkey;

--5) get total armor values for a set of armor and skills
select  sum(armor.a_vsfire), sum(armor.a_vsice), sum(armor.a_vswater), sum(armor.a_vsice), sum(armor.a_vsdragon)
from armor
join monster on m_monsterkey = a_monsterkey
where a_name like 'Jagras Helm'
or a_name like 'Jagras Coil'
or a_name like 'Rathalos Greaves Alpha'
or a_name like 'Rathalos Vambrace Alpha'   -- Vambrace need to change to vanbraces in table
or a_name like 'Pukei Mail Alpha';


Select a_skill
from armor
where a_name like 'Jagras Helm'
or a_name like 'Jagras Coil'
or a_name like 'Rathalos Greaves Alpha'
or a_name like 'Rathalos Vambrace Alpha'   -- Vambrace need to change to vanbraces in table
or a_name like 'Pukei Mail Alpha';

--6)
UPDATE monster set m_smallestsize = 1400
where m_name like 'Rathalos';

UPDATE monster set m_smallestsize = 1500
where m_name like 'Rathalos';

--7)

Update weapon set w_damagetype = 'ammo'
where w_damagetype like 'blunt';

UPDATE weapon set w_damagetype = 'blunt'
where w_name like 'Cocytus+' 
or w_name like 'Glacial Bagpipe 1';

--8)
Select w_name 
from weapon 
where w_monsterkey not in 
(
Select m_monsterkey
from monster
join monbiome on m_monsterkey = mb_monsterkey
join biome on mb_biomekey = b_biomekey
where b_name like 'Ancient Forest'
or b_name like 'Rotten Vale'
)


--9)

select m_name, p_name, mp_slicing, mp_blunt, mp_ammo
from monpart
join monster on m_monsterkey = mp_monsterkey
join part on p_partkey = mp_partkey
where m_name = 'Dodogama'

Union
select m_name, p_name, mp_slicing, mp_blunt, mp_ammo
from monpart
join monster on m_monsterkey = mp_monsterkey
join part on p_partkey = mp_partkey
where m_name = 'Pukei Pukei';

--10) delete

DELETE
from armdrop
where ad_armorkey like 'ad_armorkey';

DELETE
from armor
where a_name like 'a_name';

DELETE
from biome
where b_name like 'b_name';

DELETE
from drops
where d_name like 'd_name';

DELETE
from element
where e_name like 'e_name';

Delete 
from monbiome
where mb_monsterkey like 'mb_monsterkey';

DELETE
from monele
where me_monsterkey like 'me_monsterkey';

DELETE
from monpart
where mp_monsterkey like 'p_monsterkey';

DELETE
from monster
where m_name like 'm_name';

DELETE
from part 
where p_name like 'p_name';

DELETE
from weadrop
where wd_weaponkey like 'wd_weaponkey';

DELETE
from weapon
where w_name = 'w_name';


--#1
delete from armdrop;
delete from armor;
delete from biome;
delete from drops;
delete from element;
delete from monbiome;
delete from monele;
delete from monpart;
delete from monster;
delete from part;
delete from weadrop;
delete from weapon;

--#2
INSERT INTO element
VALUES('Wind Pressure', 14, 'Monster: prevents the player from moving for a brief duration of time', 'wind resistant buffs or skills');

--#3
DROP TABLE armdrop;
DROP TABLE armor;
DROP TABLE biome;
DROP TABLE drops;
DROP TABLE element;
DROP TABLE monbiome;
DROP TABLE monele;
DROP TABLE monpart;
DROP TABLE monster;
DROP TABLE part;
DROP TABLE weadrop;
DROP TABLE weapon;

--#4
INSERT INTO monster
VALUES('Nightshade Paolumu', 9, '2 star', '3 star', '1 star', '1 star', 'Resistant', 446, 1429, 'Flying Wyvern');

INSERT INTO monbiome
VALUES(9, 1), (9, 2);

INSERT INTO monele
VALUES(9, 9);

INSERT INTO part
VALUES(ears, 12);

INSERT INTO monpart
VALUES(9,1, '3 star', '3 star', '3 star', 'FALSE'),
(9, 11, '3 star', '3 star', '2 star', 'FALSE'),
(9, 9, '2 star', '2 star', '2 star', 'FALSE'),
(9, 2, '0 star', '0 star', '0 star', 'FALSE'),
(9, 3, '0 star', '0 star', '0 star', 'FALSE');

--#5
.headers on 
.separator |

SELECT m_name AS monster, w_name AS name, w_weapontype AS weapon, e_name AS element, w_attack AS attack, w_elementalattack AS elementdamage, w_affinity AS affinity
FROM weapon
JOIN element ON w_elementkey = e_elementkey
JOIN (SELECT m_name, m_monsterkey
FROM monster
WHERE m_species LIKE 'Flying%') ON w_monsterkey = m_monsterkey
WHERE w_rarity > 2;

--#6
SELECT e_name AS element
FROM element
WHERE e_desc LIKE '%time';

--#7
SELECT m_name AS monster, p_name AS part, mp_slicing AS slicing, mp_blunt AS blunt, mp_ammo AS ammo
FROM monster
JOIN monpart ON m_monsterkey = mp_monsterkey
JOIN part ON mp_partkey = p_partkey
WHERE mp_carvable = "TRUE";

--#8
SELECT m_name AS monster, b_name AS biome
FROM monster
JOIN monbiome ON m_monsterkey = mb_monsterkey
JOIN biome ON mb_biomekey = b_biomekey
WHERE b_effect LIKE '%HEAT%';

--#9
SELECT a_name AS armor
FROM armor
WHERE a_name LIKE '%Helm%'
OR a_name LIKE '%Headdress%'
OR a_name LIKE '%Hood%';

--#10
SELECT w_name AS weapon, d_name AS drops, wd_quantity AS amount
FROM weapon
JOIN weadrop ON w_weaponkey = wd_weaponkey
JOIN drops ON wd_dropkey = d_dropkey
WHERE d_name LIKE '%+%';