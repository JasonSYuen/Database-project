Create TABLE drops(
    d_name char(32) not null,
    d_dropkey decimal(3,0) not null --could do PRIMARY KEY instead of not null to make it a primary key constraint
);

Create TABLE monster(
    m_name char(32) not null,
    m_monsterkey decimal(10,0) not null,
    m_vsfire char(32) not null,
    m_vswater char(32) not null,
    m_vsthunder char(32) not null,
    m_vsice char(32) not null,
    m_vsdragon char(32) not null,
    m_smallestsize decimal(10,0),
    m_largestsize decimal(10,0),
    m_species char(32) not null
);

Create TABLE weapon (
    
    w_name char(32) not null,
    w_weaponkey decimal(10,0) not null,
    w_weapontype char(32) not null,
    w_elementkey decimal(10,0) not null,
    w_rarity decimal(10,0) not null,
    w_damagetype char(32) not null,
    w_attack decimal(10,0) not null,
    w_elementalattack decimal(10,0) not null,
    w_affinity decimal(10,0) not null,
    w_monsterkey decimal(10,0) not null
    
);

Create Table armor(
    a_name char(32) not null,
    a_armorkey decimal(10,0) not null,
    a_monsterkey decimal(10,0) not null,	
    a_vsfire decimal(10,0) not null,	
    a_vswater decimal(10,0) not null,
    a_vsthunder decimal(10,0) not null,	
    a_vsice decimal(10,0) not null,
    a_vsdragon decimal(10,0) not null,	
    a_skill varchar(25) not null,
    a_defense decimal(10,0) not null

);

Create Table element(
    e_name char(32) not null,
    e_elementkey decimal(10,0) not null,
    e_desc varchar(25) not null,
    e_cure varchar(25) not null

);

Create Table part(
    p_name char(32) not null,
    p_partkey decimal(10,0) not null
);

Create Table biome(
    b_name char(32) not null,
    b_biomekey decimal(10,0) not null,
    b_effect varchar(25) not null,	
    b_desc varchar(25) not null

);

Create table monele(
    me_monsterkey decimal(10,0) not null,
    me_elementkey decimal(10,0) not null

);

Create table monpart(
    mp_monsterkey decimal(10,0) not null,
    mp_partkey decimal(10,0) not null,
    mp_slicing char(32) not null,
    mp_blunt char(32) not null,
    mp_ammo char(32) not null,
    mp_carvable char(32) not null
);

Create Table monbiome(
    mb_monsterkey decimal(10,0) not null,
    mb_biomekey decimal(10,0) not null
);

Create table weadrop(
    wd_weaponkey decimal(10,0) not null,
    wd_dropkey decimal(10,0) not null,
    wd_quantity decimal(10,0) not null
);

Create table armdrop(
    ad_armorkey decimal(10,0) not null,
    ad_dropkey decimal(10,0) not null,
    ad_quantity decimal(10,0) not null
);