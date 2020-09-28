CREATE TABLE pages (
	id serial PRIMARY KEY,
	page_data text NULL,
	datetime TIMESTAMP NOT NULL
);

CREATE TABLE posts (
	id serial PRIMARY KEY,
	page_id int NULL,
	"section" text null,
	page_data text NULL,
	datetime TIMESTAMP NOT NULL
);

CREATE TABLE article (
	id serial primary KEY,
	"name" text NOT NULL,
	article_data text NULL,
	url text NULL,
	datetime TIMESTAMP NULL
);
