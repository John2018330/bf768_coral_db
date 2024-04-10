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
--     tagid primary, int
drop table if exists y2015;

create table y2015 (
	tagid int NOT NULL,
	location varchar(30),
	notes varchar(100),
	alive_status varchar(10),
	length float,
	width float,
	height float,
	lw_div_4 float,
	lw_div_4_sq float,
	eco_volume float,
	ln_ecovolume float,
	Volume_Cylinder float,
	tip_number int,
	old_tag int,
	Branch_Diameter_1 float,
	Branch_Diameter_2 float,
	Branch_Diameter_3 float,
	Average_BD float,
	PRIMARY KEY (tagid)
) engine = INNODB;

-- When loading in data, must utilize NULLIF for columns that have 
-- empty values, i.e. set cell to NULL if cell value = ''
load data local infile '/Users/jz/Desktop/BU/Spring 2024 BF768 Bio Databases/project/final_data/metadata_2015.csv' INTO TABLE y2015
fields terminated by ","
ignore 1 lines 
(tagid, location, @notes, alive_status, length, width, height, lw_div_4, lw_div_4_sq, eco_volume, @ln_ecovolume, @Volume_Cylinder, 
tip_number, @old_tag, @Branch_Diameter_1, @Branch_Diameter_2, @Branch_Diameter_3, Average_BD)
SET 
notes = NULLIF(@notes,''),
ln_ecovolume = NULLIF(@ln_ecovolume,''),
Volume_Cylinder = NULLIF(@Volume_Cylinder,''),
old_tag = NULLIF(@old_tag,''),
Branch_Diameter_1 = NULLIF(@Branch_Diameter_1,''),
Branch_Diameter_2 = NULLIF(@Branch_Diameter_2,''),
Branch_Diameter_3 = NULLIF(@Branch_Diameter_3,'');


