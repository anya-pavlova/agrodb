CREATE TABLE hybrid (
	id INTEGER NOT NULL,
	name TEXT NOT NULL);
	
CREATE TABLE experiment (
	id INTEGER NOT NULL,
	name TEXT NOT NULL);
	
CREATE TABLE data (
	id INTEGER NOT NULL,
	hybrid INTEGER NULL,
	experiment INTEGER NOT NULL,
	
	meancrop REAL,
	cormeancrop REAL,
	devfb REAL,
	rank REAL
	wet REAL,
	stofrep1 REAL,
	stofrep2 REAL,
	hrep1 REAL,
	hrep2 REAL,
	comments TEXT #комментария может не быть
	);