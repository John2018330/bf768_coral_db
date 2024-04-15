-- VCF table
--    BAM_ID primary key, data type is STRING so 
--    BAM_ID refers to the relevant parts of the original ID extacted from VCF
--	  CORAL_ID SHOULD BE USED TO JOIN TO PHENOTYPIC DATA
drop table if exists vcf;

CREATE TABLE vcf (
	CORAL_ID VARCHAR(10) NOT NULL,
	BAM_ID VARCHAR(20) NOT NULL,
	CHROM VARCHAR(20),
	POS INT,
	ID VARCHAR(20),
	REF VARCHAR(10),
	ALT VARCHAR(10),
	QUAL INT,
	FILTER VARCHAR(10),
	NS INT,
	INFO_DP INT,
	AF NUMERIC (8,8),
	GT VARCHAR(10),
	FORMAT_DP INT,
	GL VARCHAR(30),
	PL VARCHAR(20),
	GP VARCHAR(30),
	PRIMARY KEY (BAM_ID, POS)
	) ENGINE=InnoDB;


load data local infile '/Users/jz/Desktop/BU/Spring 2024 BF768 Bio Databases/project/final_data/vcf.tsv' into table vcf
ignore 1 lines
(CORAL_ID, BAM_ID, CHROM, POS, ID, REF, ALT, QUAL, FILTER, NS, INFO_DP, AF, GT, FORMAT_DP, GL, PL, GP);


-- 2015 phenotypic data table
--     tagid primary key, character

drop table if exists y2015;

create table y2015 (
	tagid varchar(30) NOT NULL,
	location varchar(30),
	notes varchar(100),
	alive_status varchar(50),
	length_cm float,
	width_cm float,
	height_cm float,
	lw_div_4 float,
	lw_div_4_sq float,
	eco_volume float,
	ln_eco_volume float,
	volume_cylinder float,
	tip_number varchar(100),
	old_tag varchar(50),
	branch_diameter_1 float,
	branch_diameter_2 float,
	branch_diameter_3 float,
	average_bd float,
	PRIMARY KEY (tagid)
) engine = INNODB;


-- When loading in data, must utilize NULLIF for columns that have 
-- empty values, i.e. set cell to NULL if cell value = ''

load data local infile '/Users/jz/Documents/git_repos/bf768_coral_db/final_data/metadata_2015.tsv' INTO TABLE y2015
ignore 1 lines 
(tagid, location, @notes, alive_status, length_cm, width_cm, height_cm, lw_div_4, lw_div_4_sq, eco_volume,
@ln_eco_volume, @volume_cylinder, tip_number, @old_tag, @branch_diameter_1, @branch_diameter_2, @branch_diameter_3, average_bd)
SET
notes = NULLIF(@notes,''),
ln_eco_volume = NULLIF(@ln_eco_volume,''),
volume_cylinder = NULLIF(@volume_cylinder,''),
old_tag = NULLIF(@old_tag,''),
branch_diameter_1 = NULLIF(@branch_diameter_1,''),
branch_diameter_2 = NULLIF(@branch_diameter_2,''),
branch_diameter_3 = NULLIF(@branch_diameter_3,'');

 
-- 2016 phenotypic data table
--     tagid primary key, character

drop table if exists y2016;

create table y2016 (
	tagid varchar(30) NOT NULL,
	location varchar(30),
	notes varchar(100),
	alive_status varchar(50),
	length_cm float,
	width_cm float,
	height_cm float,
	lw_div_4 float,
	lw_div_4_sq float,
	eco_volume float,
	ln_eco_volume float,
	volume_cylinder float,
	tip_number varchar(100),
	old_tag varchar(50),
	branch_diameter_1 float,
	branch_diameter_2 float,
	branch_diameter_3 float,
	average_bd float,
	PRIMARY KEY (tagid)
) engine = INNODB;


-- When loading in data, must utilize NULLIF for columns that have 
-- empty values, i.e. set cell to NULL if cell value = ''

load data local infile '/Users/jz/Documents/git_repos/bf768_coral_db/final_data/metadata_2016.tsv' INTO TABLE y2016
ignore 1 lines 
(tagid, location, @notes, alive_status, @length_cm, @width_cm, @height_cm, @lw_div_4, @lw_div_4_sq, @eco_volume,
@ln_eco_volume, @volume_cylinder, @tip_number, @old_tag, @branch_diameter_1, @branch_diameter_2, @branch_diameter_3, @average_bd)
SET
notes = NULLIF(@notes,''),
length_cm = NULLIF(@length_cm,''),
width_cm = NULLIF(@width_cm,''),
height_cm = NULLIF(@height_cm,''),
lw_div_4 = NULLIF(@lw_div_4,''),
lw_div_4_sq = NULLIF(@lw_div_4_sq,''),
eco_volume = NULLIF(@eco_volume,''),
ln_eco_volume = NULLIF(@ln_eco_volume,''),
volume_cylinder = NULLIF(@volume_cylinder,''),
tip_number = NULLIF(@tip_number,''),
old_tag = NULLIF(@old_tag,''),
branch_diameter_1 = NULLIF(@branch_diameter_1,''),
branch_diameter_2 = NULLIF(@branch_diameter_2,''),
branch_diameter_3 = NULLIF(@branch_diameter_3,''),
average_bd = NULLIF(@average_bd,'');

-- 2017 phenotypic data table
--    tagid primary key

drop table if exists y2017;

create table y2017 (
	tagid varchar(30) NOT NULL,
	location varchar(30),
	notes varchar(100),
	alive_status varchar(50),
	length_cm float,
	width_cm float,
	height_cm float,
	lw_div_4 float,
	lw_div_4_sq float,
	eco_volume float,
	ln_eco_volume float,
	volume_cylinder float,
	tip_number varchar(100),
	old_tag varchar(50),
	PRIMARY KEY (tagid)
) engine = INNODB;

-- When loading in data, must utilize NULLIF for columns that have 
-- empty values, i.e. set cell to NULL if cell value = ''

load data local infile '/Users/jz/Documents/git_repos/bf768_coral_db/final_data/metadata_2017.tsv' into table y2017
ignore 1 lines 
(tagid, location, @notes, alive_status, @length_cm, @width_cm, @height_cm, @lw_div_4, @lw_div_4_sq, @eco_volume,
@ln_eco_volume, @volume_cylinder, @tip_number, @old_tag)
SET
notes = NULLIF(@notes,''),
length_cm = NULLIF(@length_cm,''),
width_cm = NULLIF(@width_cm,''),
height_cm = NULLIF(@height_cm,''),
lw_div_4 = NULLIF(@lw_div_4,''),
lw_div_4_sq = NULLIF(@lw_div_4_sq,''),
eco_volume = NULLIF(@eco_volume,''),
ln_eco_volume = NULLIF(@ln_eco_volume,''),
volume_cylinder = NULLIF(@volume_cylinder,''),
tip_number = NULLIF(@tip_number,''),
old_tag = NULLIF(@old_tag,'');


-- 2018 phenotypic data
--   tagid primary key

drop table if exists y2018;

create table y2018 (
	tagid varchar(30) NOT NULL,
	location varchar(30),
	notes varchar(100),
	alive_status varchar(100),
	length_cm float,
	width_cm float,
	height_cm float,
	lw_div_4 float,
	lw_div_4_sq float,
	eco_volume float,
	ln_eco_volume float,
	volume_cylinder float,
	tip_number varchar(100),
	old_tag varchar(50),
	bd_single_branches float,
	PRIMARY KEY (tagid)
) engine = INNODB;


-- When loading in data, must utilize NULLIF for columns that have 
-- empty values, i.e. set cell to NULL if cell value = ''
-- HAD TO TWEAK ORIGINAL FILE bc of duplicate keys in combined coral rows

load data local infile '/Users/jz/Documents/git_repos/bf768_coral_db/final_data/metadata_2018.tsv' into table y2018
ignore 1 lines 
(tagid, location, @notes, alive_status, @length_cm, @width_cm, @height_cm, @lw_div_4, @lw_div_4_sq, @eco_volume,
@ln_eco_volume, @volume_cylinder, @tip_number, @old_tag, @bd_single_branches)
SET
notes = NULLIF(@notes,''),
length_cm = NULLIF(@length_cm,''),
width_cm = NULLIF(@width_cm,''),
height_cm = NULLIF(@height_cm,''),
lw_div_4 = NULLIF(@lw_div_4,''),
lw_div_4_sq = NULLIF(@lw_div_4_sq,''),
eco_volume = NULLIF(@eco_volume,''),
ln_eco_volume = NULLIF(@ln_eco_volume,''),
volume_cylinder = NULLIF(@volume_cylinder,''),
tip_number = NULLIF(@tip_number,''),
old_tag = NULLIF(@old_tag,''),
bd_single_branches = NULLIF(@bd_single_branches,'');